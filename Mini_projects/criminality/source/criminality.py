import pandas as pd
import cbsodata as cbs

agg = ['GM', 'BU', 'WK'][2]
year = [2016, 2017, 2018][2]
lang = ['ND','EN'][1]
add_geo = True

def get_database(agg_level, year, language, add_geo):
    
    # Dowloading data
    print('Downloading crime data...')
    crimes_code = get_table_code('crimes', year)
    crimes_db = pd.DataFrame(cbs.get_data(crimes_code))
    print('... Crime data done')

    print('Downloading socio economic data...')
    socio_economics_code = get_table_code('socio_economics', year)
    socio_economics_db = pd.DataFrame(cbs.get_data(socio_economics_code))
    print('... Socio economic data done')
    
    # Merging data
    print('Aggregating and mixing data...')
    crimes = agg_data_frame(crimes_db, agg_level)
    socio_economics = agg_data_frame(socio_economics_db, agg_level)
    socio_economics = socio_economics.drop(columns = ['ID', 'WijkenEnBuurten', 'Gemeentenaam_1', 'SoortRegio_2', 'IndelingswijzigingWijkenEnBuurten_4', 'AantalInwoners_5'])
    #crimes = crimes.drop(columns = [''])
    #socio_economics = socio_economics.drop(columns = [''])
    df = pd.merge(crimes, socio_economics, how = 'left', on = 'Codering_3')
    print('... aggregating and mixing done')

    # Adding geographical component
    if add_geo:
        import geopandas as gpd
        geo = gpd.read_file(f'source/{agg_level}.shp')
        geo = geo.rename(columns = {f'{agg_level.lower()}_code': 'Codering_3'})
        geo = geo.drop(columns = [f'{agg_level.lower()}_naam'])
        gdf = gpd.GeoDataFrame(pd.merge(df, geo, how = 'left', on = 'Codering_3'))

    # Translation
    if language == 'EN':
        df = translate_columns(df)
        if add_geo:
            gdf = translate_columns(gdf)
    
    if add_geo:
        return gdf
    else:
        return df

cols =  {'ID': 'ID',
         'WijkenEnBuurten': 'DistrictsAndNeighborhoods',
         'Gemeentenaam_1': 'Gemeentaam_1',
         'SoortRegio_2': 'TypeRegion_2',
         'Codering_3': 'Coding_3',
         'Indelingswijziging_4': 'Classificationchange_4',
         'AantalInwoners_5': 'NumberofResidents_5',
         'TotaalVermogenVernielingEnGeweld_6': 'TotalPowerForgementAndViolence_6',
         'TotaalVermogensmisdrijven_7': 'TotalPower Crimes_7',
         'TotaalDiefstal_8': 'TotalTheft_8',
         'Fietsendiefstal_9': 'Bicycle Theft_9',
         'DiefstalOverigeVervoermiddelen_10': 'TheftOtherVehicles_10',
         'DiefstalUitVanafVervoermiddelen_11': 'TheftFromFromMeans of Transport_11',
         'ZakkenrollerijStraatroofEnBeroving_12': 'PickpocketingStreet robbery_12',
         'TotaalDiefstalUitWoningSchuurED_13': 'TotalTheftFromHomeShed_13',
         'DiefstalUitNietResidentieleGebouwen_14': 'TheftFromNon-ResidentialBuildings_14',
         'OverigeDiefstalInbraak_15': 'OtherTheftBurglary_15',
         'OverigeVermogensmisdrijven_16': 'OtherTheftFromVehicles_16',
         'TotaalVernielingTegenOpenbareOrde_17': 'TotalVegetationFromPublicOrde_17',
         'TotaalVernieling_18': 'TotalVegetation_18',
         'VernielingAanAuto_19': 'DestructionOfAutomo_19',
         'OverigeVernieling_20': 'OtherVegetation_20',
         'OverigeVernielingTegenOpenbareOrde_21': 'OtherVegetationToPublicOrde_21',
         'TotaalGeweldsEnSeksueleMisdrijven_22': 'TotalViolenceAndSexualCrimes_22',
         'Mishandeling_23': 'Assault_23',
         'BedreigingEnStalking_24': 'ThreatEnStalking_24',
         'OverigeGeweldsEnSeksueleMisdrijven_25': 'OtherViolenceAndSexualCrimes_25',
         'TotaalVermogenVernielingEnGeweld_26': 'TotalPowerForgementAndViolence_26',
         'TotaalVermogensmisdrijven_27': 'TotalPower Crimes_27',
         'TotaalDiefstalUitWoningSchuurED_28': 'TotalTheftFromHomeShedED_28',
         'VernielingMisdrijfTegenOpenbareOrde_29': 'DestructionMisdemeanorTowardPublicOrde_29',
         'GeweldsEnSeksueleMisdrijven_30': 'ViolenceAndSexualCrimes_30',
         'Mannen_6': 'Men_6',
         'Vrouwen_7': 'Women_7',
         'k_0Tot15Jaar_8': 'k_0To15Years_8',
         'k_15Tot25Jaar_9': 'k_15To25Year_9',
         'k_25Tot45Jaar_10': 'k_25Tot45Year_10',
         'k_45Tot65Jaar_11': 'k_45Tot65Year_11',
         'k_65JaarOfOuder_12': 'k_65YearOrder_12',
         'Ongehuwd_13': 'Unmarried_13',
         'Gehuwd_14': 'Married_14',
         'Gescheiden_15': 'Divorced_15',
         'Verweduwd_16': 'Betrothed_16',
         'WestersTotaal_17': 'WesternTotal_17',
         'NietWestersTotaal_18': 'Non-Western_18',
         'Marokko_19': 'Morocco_19',
         'NederlandseAntillenEnAruba_20': 'NetherlandsAntillesAruba_20',
         'Suriname_21': 'Suriname_21',
         'Turkije_22': 'Turkey_22',
         'OverigNietWesters_23': 'OtherNonWestern_23',
         'GeboorteTotaal_24': 'BirthTotal_24',
         'GeboorteRelatief_25': 'BirthRelative_25',
         'SterfteTotaal_26': 'MortalityTotal_26',
         'SterfteRelatief_27': 'MortalityRelative_27',
         'HuishoudensTotaal_28': 'HouseholdTotal_28',
         'Eenpersoonshuishoudens_29': 'SinglePerson Households_29',
         'HuishoudensZonderKinderen_30': 'HouseholdsWithoutChildren_30',
         'HuishoudensMetKinderen_31': 'HouseholdsWithChildren_31',
         'GemiddeldeHuishoudensgrootte_32': 'Average Household Size_32',
         'Bevolkingsdichtheid_33': 'Population density_33',
         'Woningvoorraad_34': 'Housing stock_34',
         'GemiddeldeWoningwaarde_35': 'AverageHousingValue_35',
         'PercentageEengezinswoning_36': 'PercentageFamily Housing_36',
         'PercentageMeergezinswoning_37': 'PercentageFamily Housing_37',
         'PercentageBewoond_38': 'PercentageOccupied_38',
         'PercentageOnbewoond_39': 'PercentageUnoccupied_39',
         'Koopwoningen_40': 'Owner-Occupied_40',
         'HuurwoningenTotaal_41': 'Rental PropertiesTotal_41',
         'InBezitWoningcorporatie_42': 'InResidenceHousingCorporation_42',
         'InBezitOverigeVerhuurders_43': 'InAccessOtherLessees_43',
         'EigendomOnbekend_44': 'OwnershipUnknown_44',
         'BouwjaarVoor2000_45': 'BouwjaarVoor2000_45',
         'BouwjaarVanaf2000_46': 'BouwjaarVanaf2000_46',
         'GemiddeldElektriciteitsverbruikTotaal_47': 'AverageElectricity ConsumptionTotal_47',
         'Appartement_48': 'Apartment_48',
         'Tussenwoning_49': 'Mezzanine_49',
         'Hoekwoning_50': 'Corner house_50',
         'TweeOnderEenKapWoning_51': 'Two-Family House_51',
         'VrijstaandeWoning_52': 'DetachedHome_52',
         'Huurwoning_53': 'Rental_53',
         'EigenWoning_54': 'Owner-occupied_54',
         'GemiddeldAardgasverbruikTotaal_55': 'GemiddeldeAardgasconsumptionTotal_55',
         'Appartement_56': 'Apartment_56',
         'Tussenwoning_57': 'Mezzanine_57',
         'Hoekwoning_58': 'Corner house_58',
         'TweeOnderEenKapWoning_59': 'Two-Familyhouse_59',
         'VrijstaandeWoning_60': 'DetachedHome_60',
         'Huurwoning_61': 'Rental_61',
         'EigenWoning_62': 'Owner_occupied_62',
         'PercentageWoningenMetStadsverwarming_63': 'PercentageofDwellingsWithCityHeating_63',
         'Nettoarbeidsparticipatie_64': 'Net Employment_64',
         'PercentageWerknemers_65': 'PercentageEmployed_65',
         'PercentageZelfstandigen_66': 'PercentageSelf-employed_66',
         'AantalInkomensontvangers_67': 'NumberofIncomeReceivers_67',
         'GemiddeldInkomenPerInkomensontvanger_68': 'AverageIncomePerIncomeReceiver_68',
         'GemiddeldInkomenPerInwoner_69': 'AverageIncomePerInhabitant_69',
         'k_40PersonenMetLaagsteInkomen_70': 'k_40PeopleWithLowestIncome_70',
         'k_20PersonenMetHoogsteInkomen_71': 'k_20PeopleWithHighestIncome_71',
         'GemGestandaardiseerdInkomenVanHuish_72': 'AverageStandardizedIncomeFromHome_72',
         'k_40HuishoudensMetLaagsteInkomen_73': 'k_40HouseholdsWithLowestIncome_73',
         'k_20HuishoudensMetHoogsteInkomen_74': 'k_20HouseholdsWithHighestIncome_74',
         'HuishoudensMetEenLaagInkomen_75': 'HouseholdsWithLowestIncome_75',
         'HuishOnderOfRondSociaalMinimum_76': 'HouseholdUnderOfRoundSocialMinimum_76',
         'HuishoudensTot110VanSociaalMinimum_77': 'HouseholdsToo110FromSocialMinimum_77',
         'HuishoudensTot120VanSociaalMinimum_78': 'HouseholdsTot120FromSocialMinimum_78',
         'MediaanVermogenVanParticuliereHuish_79': 'MedianPowerOfPrivateHouse_79',
         'PersonenPerSoortUitkeringBijstand_80': 'PersonsPerTypeofbenefitBenefit_80',
         'PersonenPerSoortUitkeringAO_81': 'PersonsPerSortYouStatusAO_81',
         'PersonenPerSoortUitkeringWW_82': 'PersonsPerSortSofUsebenefitWW_82',
         'PersonenPerSoortUitkeringAOW_83': 'PersonsPerSortSofFundingAOW_83',
         'JongerenMetJeugdzorgInNatura_84': 'YouthWithYouthCareInNatura_84',
         'PercentageJongerenMetJeugdzorg_85': 'PercentageofYoungPeopleWithYouthCare_85',
         'WmoClienten_86': 'WmoClients_86',
         'WmoClientenRelatief_87': 'WmoClientsRelative_87',
         'TotaalDiefstalUitWoningSchuurED_88': 'TotalTheftFromHomeShedED_88',
         'VernielingMisdrijfTegenOpenbareOrde_89': 'DestructionMisdemeanorTowardPublicOrde_89',
         'GeweldsEnSeksueleMisdrijven_90': 'ViolenceAndSexualCrimes_90',
         'BedrijfsvestigingenTotaal_91': 'Business establishmentsTotal_91',
         'ALandbouwBosbouwEnVisserij_92': 'ALagricultureForestryAndFisheries_92',
         'BFNijverheidEnEnergie_93': 'BFIndustryEnergy_93',
         'GIHandelEnHoreca_94': 'GITradeAndHospitality_94',
         'HJVervoerInformatieEnCommunicatie_95': 'HJTransportationInformationEnCommunication_95',
         'KLFinancieleDienstenOnroerendGoed_96': 'KLFinancialServicesReal Estate_96',
         'MNZakelijkeDienstverlening_97': 'MNBusinessServices_97',
         'RUCultuurRecreatieOverigeDiensten_98': 'RUCultureRecreationOtherServices_98',
         'PersonenautoSTotaal_99': 'PassengerCarTotal_99',
         'PersonenautoSBrandstofBenzine_100': 'PassengerCarFuelBenzine_100',
         'PersonenautoSOverigeBrandstof_101': 'PassengerCarsOverallFuel_101',
         'PersonenautoSPerHuishouden_102': 'PassengerCarSPerHousehold_102',
         'PersonenautoSNaarOppervlakte_103': 'PassengerCarSArea_103',
         'Motorfietsen_104': 'Motorcycles_104',
         'AfstandTotHuisartsenpraktijk_105': 'DistanceToHousehold_105',
         'AfstandTotGroteSupermarkt_106': 'DistanceToBigSupermarket_106',
         'AfstandTotKinderdagverblijf_107': 'DistanceToKindergarten_107',
         'AfstandTotSchool_108': 'DistanceToSchool_108',
         'ScholenBinnen3Km_109': 'SchoolsWithin3Km_109',
         'OppervlakteTotaal_110': 'AreaTotal_110',
         'OppervlakteLand_111': 'SurfaceLand_111',
         'OppervlakteWater_112': 'SurfaceWater_112',
         'MeestVoorkomendePostcode_113': 'MostFrequentPostcode_113',
         'Dekkingspercentage_114': 'CoverageRate_114',
         'MateVanStedelijkheid_115': 'DegreeOfUrbanity_115',
         'Omgevingsadressendichtheid_116': 'EnvironmentalAddressDensity_116'}


def translate_columns(df):
    global cols
    df = df.rename(columns = cols)
    return df

# Method to get table code based on year and type
def get_table_code(table, year):
    if table == 'crimes':
        title = 'Geregistr. misdrijven; buurten'
    elif table ==  'socio_economics':
        title = 'Kerncijfers wijken en buurten'

    # Getting all available tables
    toc = pd.DataFrame(cbs.get_table_list())
    toc['check'] = toc['ShortTitle'].apply(lambda x: _isinit(f'{title} {year}', x))
    return toc.loc[toc['check'] == 1]['Identifier'].iloc[0]


# Method that resturns only codes for the aggregation selected
def agg_data_frame(df, agg):
    df['Codering_3'] = df['Codering_3'].apply(lambda x: x.strip())
    df['agg'] = df['Codering_3'].apply(lambda x: _is_agg(agg, x))
    df = df.loc[df['agg'] == 1]
    df = df.drop(columns = 'agg')
    return df

# Method identify code type fro aggregation
def _is_agg(agg, code):
    if code[0:2] == agg:
        return 1
    else:
        return 0

# Method to check if a piece of text appears in a title
def _isinit(text, title):
    if text in title:
        return 1
    else:
        return 0

