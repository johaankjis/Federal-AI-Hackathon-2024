import os
import re
from lxml import etree

def parse_xml(file_path):
    # Parse the XML file
    tree = etree.parse(file_path)
    root = tree.getroot()
    return root

def sanitize_value(value):
    # Ensure the value is properly escaped for SQL Server
    if value is None:
        return "NULL"
    value = value.replace("'", "''")
    return f"N'{value}'"

def generate_create_table_sql():
    # Generate CREATE TABLE SQL statement for SQL Server
    create_table_sql = '''
    IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='award' and xtype='U')
    BEGIN
        CREATE TABLE award (
            AwardTitle NVARCHAR(MAX),
            AGENCY NVARCHAR(MAX),
            AwardEffectiveDate NVARCHAR(255),
            AwardExpirationDate NVARCHAR(255),
            AwardTotalIntnAmount FLOAT,
            AwardAmount FLOAT,
            AwardInstrumentValue NVARCHAR(255),
            OrgCode NVARCHAR(255),
            OrgDirectorateAbbreviation NVARCHAR(255),
            OrgDirectorateLongName NVARCHAR(255),
            OrgDivisionAbbreviation NVARCHAR(255),
            OrgDivisionLongName NVARCHAR(255),
            ProgramOfficerName NVARCHAR(255),
            ProgramOfficerEmail NVARCHAR(255),
            ProgramOfficerPhone NVARCHAR(255),
            AbstractNarration NVARCHAR(MAX),
            MinAmdLetterDate NVARCHAR(255),
            MaxAmdLetterDate NVARCHAR(255),
            TRAN_TYPE NVARCHAR(255),
            CFDA_NUM NVARCHAR(255),
            NSF_PAR_USE_FLAG NVARCHAR(255),
            FUND_AGCY_CODE NVARCHAR(255),
            AWDG_AGCY_CODE NVARCHAR(255),
            AwardID NVARCHAR(255),
            InvestigatorFirstName NVARCHAR(255),
            InvestigatorLastName NVARCHAR(255),
            InvestigatorMidInit NVARCHAR(255),
            InvestigatorFullName NVARCHAR(255),
            InvestigatorEmail NVARCHAR(255),
            InvestigatorNSF_ID NVARCHAR(255),
            InvestigatorStartDate NVARCHAR(255),
            InvestigatorRoleCode NVARCHAR(255),
            InstName NVARCHAR(255),
            InstCityName NVARCHAR(255),
            InstZipCode NVARCHAR(255),
            InstPhoneNumber NVARCHAR(255),
            InstStreetAddress NVARCHAR(255),
            InstCountryName NVARCHAR(255),
            InstStateName NVARCHAR(255),
            InstStateCode NVARCHAR(255),
            InstCongressDistrict NVARCHAR(255),
            InstOrgUEINum NVARCHAR(255),
            InstOrgLglBusName NVARCHAR(255),
            PerfInstName NVARCHAR(255),
            PerfInstCityName NVARCHAR(255),
            PerfInstStateCode NVARCHAR(255),
            PerfInstZipCode NVARCHAR(255),
            PerfInstStreetAddress NVARCHAR(255),
            PerfInstCountryCode NVARCHAR(255),
            PerfInstCountryName NVARCHAR(255),
            PerfInstStateName NVARCHAR(255),
            PerfInstCongressDistrict NVARCHAR(255),
            ProgramElementCode NVARCHAR(255),
            ProgramElementText NVARCHAR(255),
            FundCode NVARCHAR(255),
            FundName NVARCHAR(255),
            FundSymbolID NVARCHAR(255),
            FundObligation NVARCHAR(255)
        );
    END;

    IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='winners' and xtype='U')
    BEGIN
        CREATE TABLE winners (
            InvestigatorFullName NVARCHAR(255) PRIMARY KEY,
            Wins INT
        );
    END;
    '''
    return create_table_sql

def generate_insert_sql():
    # Generate INSERT INTO SQL statement for SQL Server
    insert_sql = '''
    INSERT INTO award (
        AwardTitle, AGENCY, AwardEffectiveDate, AwardExpirationDate, AwardTotalIntnAmount, AwardAmount,
        AwardInstrumentValue, OrgCode, OrgDirectorateAbbreviation, OrgDirectorateLongName, OrgDivisionAbbreviation,
        OrgDivisionLongName, ProgramOfficerName, ProgramOfficerEmail, ProgramOfficerPhone, AbstractNarration,
        MinAmdLetterDate, MaxAmdLetterDate, TRAN_TYPE, CFDA_NUM, NSF_PAR_USE_FLAG, FUND_AGCY_CODE, AWDG_AGCY_CODE,
        AwardID, InvestigatorFirstName, InvestigatorLastName, InvestigatorMidInit, InvestigatorFullName, InvestigatorEmail,
        InvestigatorNSF_ID, InvestigatorStartDate, InvestigatorRoleCode, InstName, InstCityName, InstZipCode, InstPhoneNumber,
        InstStreetAddress, InstCountryName, InstStateName, InstStateCode, InstCongressDistrict, InstOrgUEINum, InstOrgLglBusName,
        PerfInstName, PerfInstCityName, PerfInstStateCode, PerfInstZipCode, PerfInstStreetAddress, PerfInstCountryCode,
        PerfInstCountryName, PerfInstStateName, PerfInstCongressDistrict, ProgramElementCode, ProgramElementText,
        FundCode, FundName, FundSymbolID, FundObligation
    ) VALUES ({AwardTitle}, {AGENCY}, {AwardEffectiveDate}, {AwardExpirationDate}, {AwardTotalIntnAmount}, {AwardAmount}, 
              {AwardInstrumentValue}, {OrgCode}, {OrgDirectorateAbbreviation}, {OrgDirectorateLongName}, {OrgDivisionAbbreviation}, 
              {OrgDivisionLongName}, {ProgramOfficerName}, {ProgramOfficerEmail}, {ProgramOfficerPhone}, {AbstractNarration}, 
              {MinAmdLetterDate}, {MaxAmdLetterDate}, {TRAN_TYPE}, {CFDA_NUM}, {NSF_PAR_USE_FLAG}, {FUND_AGCY_CODE}, {AWDG_AGCY_CODE}, 
              {AwardID}, {InvestigatorFirstName}, {InvestigatorLastName}, {InvestigatorMidInit}, {InvestigatorFullName}, {InvestigatorEmail}, 
              {InvestigatorNSF_ID}, {InvestigatorStartDate}, {InvestigatorRoleCode}, {InstName}, {InstCityName}, {InstZipCode}, {InstPhoneNumber}, 
              {InstStreetAddress}, {InstCountryName}, {InstStateName}, {InstStateCode}, {InstCongressDistrict}, {InstOrgUEINum}, {InstOrgLglBusName}, 
              {PerfInstName}, {PerfInstCityName}, {PerfInstStateCode}, {PerfInstZipCode}, {PerfInstStreetAddress}, {PerfInstCountryCode}, 
              {PerfInstCountryName}, {PerfInstStateName}, {PerfInstCongressDistrict}, {ProgramElementCode}, {ProgramElementText}, 
              {FundCode}, {FundName}, {FundSymbolID}, {FundObligation});
    IF NOT EXISTS (SELECT * FROM winners WHERE InvestigatorFullName = {InvestigatorFullName})
    BEGIN
        INSERT INTO winners (InvestigatorFullName, Wins) VALUES ({InvestigatorFullName}, 0);
    END
    ELSE
    BEGIN
        UPDATE winners SET Wins = Wins + 1 WHERE InvestigatorFullName = {InvestigatorFullName};
    END;
    '''
    return insert_sql

def extract_data(element):
    # Extract data from XML element and its children
    data = {
        "AwardTitle": sanitize_value(element.findtext("AwardTitle", default="").strip()),
        "AGENCY": sanitize_value(element.findtext("AGENCY", default="").strip()),
        "AwardEffectiveDate": sanitize_value(element.findtext("AwardEffectiveDate", default="").strip()),
        "AwardExpirationDate": sanitize_value(element.findtext("AwardExpirationDate", default="").strip()),
        "AwardTotalIntnAmount": element.findtext("AwardTotalIntnAmount", default="").strip() or 'NULL',
        "AwardAmount": element.findtext("AwardAmount", default="").strip() or 'NULL',
        "AwardInstrumentValue": sanitize_value(element.findtext("AwardInstrument/Value", default="").strip()),
        "OrgCode": sanitize_value(element.findtext("Organization/Code", default="").strip()),
        "OrgDirectorateAbbreviation": sanitize_value(element.findtext("Organization/Directorate/Abbreviation", default="").strip()),
        "OrgDirectorateLongName": sanitize_value(element.findtext("Organization/Directorate/LongName", default="").strip()),
        "OrgDivisionAbbreviation": sanitize_value(element.findtext("Organization/Division/Abbreviation", default="").strip()),
        "OrgDivisionLongName": sanitize_value(element.findtext("Organization/Division/LongName", default="").strip()),
        "ProgramOfficerName": sanitize_value(element.findtext("ProgramOfficer/SignBlockName", default="").strip()),
        "ProgramOfficerEmail": sanitize_value(element.findtext("ProgramOfficer/PO_EMAI", default="").strip()),
        "ProgramOfficerPhone": sanitize_value(element.findtext("ProgramOfficer/PO_PHON", default="").strip()),
        "AbstractNarration": sanitize_value(element.findtext("AbstractNarration", default="").strip()),
        "MinAmdLetterDate": sanitize_value(element.findtext("MinAmdLetterDate", default="").strip()),
        "MaxAmdLetterDate": sanitize_value(element.findtext("MaxAmdLetterDate", default="").strip()),
        "TRAN_TYPE": sanitize_value(element.findtext("TRAN_TYPE", default="").strip()),
        "CFDA_NUM": sanitize_value(element.findtext("CFDA_NUM", default="").strip()),
        "NSF_PAR_USE_FLAG": sanitize_value(element.findtext("NSF_PAR_USE_FLAG", default="").strip()),
        "FUND_AGCY_CODE": sanitize_value(element.findtext("FUND_AGCY_CODE", default="").strip()),
        "AWDG_AGCY_CODE": sanitize_value(element.findtext("AWDG_AGCY_CODE", default="").strip()),
        "AwardID": sanitize_value(element.findtext("AwardID", default="").strip()),
        "InvestigatorFirstName": sanitize_value(element.findtext("Investigator/FirstName", default="").strip()),
        "InvestigatorLastName": sanitize_value(element.findtext("Investigator/LastName", default="").strip()),
        "InvestigatorMidInit": sanitize_value(element.findtext("Investigator/PI_MID_INIT", default="").strip()),
        "InvestigatorFullName": sanitize_value(element.findtext("Investigator/PI_FULL_NAME", default="").strip()),
        "InvestigatorEmail": sanitize_value(element.findtext("Investigator/EmailAddress", default="").strip()),
        "InvestigatorNSF_ID": sanitize_value(element.findtext("Investigator/NSF_ID", default="").strip()),
        "InvestigatorStartDate": sanitize_value(element.findtext("Investigator/StartDate", default="").strip()),
        "InvestigatorRoleCode": sanitize_value(element.findtext("Investigator/RoleCode", default="").strip()),
        "InstName": sanitize_value(element.findtext("Institution/Name", default="").strip()),
        "InstCityName": sanitize_value(element.findtext("Institution/CityName", default="").strip()),
        "InstZipCode": sanitize_value(element.findtext("Institution/ZipCode", default="").strip()),
        "InstPhoneNumber": sanitize_value(element.findtext("Institution/PhoneNumber", default="").strip()),
        "InstStreetAddress": sanitize_value(element.findtext("Institution/StreetAddress", default="").strip()),
        "InstCountryName": sanitize_value(element.findtext("Institution/CountryName", default="").strip()),
        "InstStateName": sanitize_value(element.findtext("Institution/StateName", default="").strip()),
        "InstStateCode": sanitize_value(element.findtext("Institution/StateCode", default="").strip()),
        "InstCongressDistrict": sanitize_value(element.findtext("Institution/CONGRESSDISTRICT", default="").strip()),
        "InstOrgUEINum": sanitize_value(element.findtext("Institution/ORG_UEI_NUM", default="").strip()),
        "InstOrgLglBusName": sanitize_value(element.findtext("Institution/ORG_LGL_BUS_NAME", default="").strip()),
        "PerfInstName": sanitize_value(element.findtext("Performance_Institution/Name", default="").strip()),
        "PerfInstCityName": sanitize_value(element.findtext("Performance_Institution/CityName", default="").strip()),
        "PerfInstStateCode": sanitize_value(element.findtext("Performance_Institution/StateCode", default="").strip()),
        "PerfInstZipCode": sanitize_value(element.findtext("Performance_Institution/ZipCode", default="").strip()),
        "PerfInstStreetAddress": sanitize_value(element.findtext("Performance_Institution/StreetAddress", default="").strip()),
        "PerfInstCountryCode": sanitize_value(element.findtext("Performance_Institution/CountryCode", default="").strip()),
        "PerfInstCountryName": sanitize_value(element.findtext("Performance_Institution/CountryName", default="").strip()),
        "PerfInstStateName": sanitize_value(element.findtext("Performance_Institution/StateName", default="").strip()),
        "PerfInstCongressDistrict": sanitize_value(element.findtext("Performance_Institution/CONGRESSDISTRICT", default="").strip()),
        "ProgramElementCode": sanitize_value(element.findtext("ProgramElement/Code", default="").strip()),
        "ProgramElementText": sanitize_value(element.findtext("ProgramElement/Text", default="").strip()),
        "FundCode": sanitize_value(element.findtext("Fund/Code", default="").strip()),
        "FundName": sanitize_value(element.findtext("Fund/Name", default="").strip()),
        "FundSymbolID": sanitize_value(element.findtext("Fund/FUND_SYMB_ID", default="").strip()),
        "FundObligation": sanitize_value(element.findtext("FUND_OBLG", default="").strip())
    }
    return data

def generate_sql_queries(root, insert_sql):
    # Generate SQL queries for the database
    queries = []
    for element in root.findall("Award"):
        data = extract_data(element)
        query = insert_sql.format(**data)
        queries.append(query)
    return queries

def main(xml_folder, output_file):
    # Main function to convert XML to SQL queries
    create_table_sql = generate_create_table_sql()
    insert_sql = generate_insert_sql()

    # Collect all SQL queries
    all_queries = [create_table_sql]

    # Process all XML files in the specified folder
    for filename in os.listdir(xml_folder):
        if filename.endswith(".xml"):
            xml_file = os.path.join(xml_folder, filename)
            root = parse_xml(xml_file)
            queries = generate_sql_queries(root, insert_sql)
            all_queries.extend(queries)

    # Save all SQL queries to a .txt file with UTF-8 encoding
    with open(output_file, "w", encoding="utf-8") as file:
        for query in all_queries:
            file.write(query + "\n")

    print(f"All SQL queries have been saved to {output_file}.")

if __name__ == "__main__":
    xml_folder = "input/"  # Path to your folder containing XML files
    output_file = "queries.txt"  # Path to the output .txt file
    main(xml_folder, output_file)
