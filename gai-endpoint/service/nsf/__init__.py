import requests
from pydantic import BaseModel, Field


class NSFAwardsAPI:
    def __init__(self, format='xml'):
        self.base_url = f"http://api.nsf.gov/services/v1/awards.{format}"
        self.format = format
        self.params = {}

    def set_search_params(self, **kwargs):
        self.params.update(kwargs)

    def search_awards(self):
        response = requests.get(self.base_url, params=self.params)
        return response.text if self.format == 'xml' else response.json()

    def get_award_by_id(self, award_id):
        url = f"{self.base_url}/{award_id}.{self.format}"
        response = requests.get(url)
        return response.text if self.format == 'xml' else response.json()

    def get_project_outcomes(self, award_id):
        url = f"{self.base_url}/{award_id}/projectoutcomes.{self.format}"
        response = requests.get(url)
        return response.text if self.format == 'xml' else response.json()


class NSFAwardsAPISearchParams(BaseModel):
    keyword: str = Field(None, description="Free text search across all the available awards data")
    rpp: int = Field(None, ge=1, le=25,
                     description="Value in the range of 1 to 25. Default Value is set to 25 & it's the upper limit as well.")
    offset: int = Field(None, ge=1,
                        description="Enter the record offset (always starts with 1). Used with results per page to fetch large data sets in chunks.")
    callback: str = Field(None, description="Provide the name of the callback function (ex. processJson)")
    printFields: str = Field(None,
                             description="Comma separated output print field names required in the output (ex. awardeeName,id,pdPIName).")
    id: str = Field(None,
                    description="An award unique identifier to retrieve the information (ex. 1336650). Required if ProjectOutcomes is requested.")
    agency: str = Field(None, description="Agency Name (NSF, NASA)")
    awardeeCity: str = Field(None, description="Awardee city name (ex. Arlington)")
    awardeeCountryCode: str = Field(None, description="Awardee country code (ex. US)")
    awardeeDistrictCode: str = Field(None, description="Awardee congressional district code (ex. VA01,NY22)")
    awardeeName: str = Field(None, description='Name of the entity receiving award (ex, "university+of+south+florida")')
    awardeeStateCode: str = Field(None, description="Abbreviation of the awardee state (ex. VA)")
    awardeeZipCode: str = Field(None,
                                description="9 digit awardee zip code with the pattern of 5 digit + 4 (ex. 231730001)")
    cfdaNumber: str = Field(None,
                            description="Catalog of Federal Domestic Assistance (CFDA) number (ex. 43.001, 47.050)")
    coPDPI: str = Field(None, description="Co- Principal Investigator Name (ex. Christopher)")
    dateStart: str = Field(None,
                           description="Start date for award date to search. Format is mm/dd/yyyy (ex.12/31/2012)")
    dateEnd: str = Field(None, description="End date for award date to search. Format is mm/dd/yyyy (ex.12/31/2012)")
    startDateStart: str = Field(None,
                                description="Start date for award start date to search. Format is mm/dd/yyyy (ex.12/31/2012)")
    startDateEnd: str = Field(None,
                              description="End date for award start date to search. Format is mm/dd/yyyy (ex.12/31/2012)")
    expDateStart: str = Field(None,
                              description="Start date for award expiration date to search. Format is mm/dd/yyyy (ex.12/31/2012)")
    expDateEnd: str = Field(None,
                            description="End date for award expiration date to search. Format is mm/dd/yyyy (ex.12/31/2012)")
    estimatedTotalAmtFrom: str = Field(None,
                                       description="Estimated total from amount. Values GREATER than the specified amount (ex. 50000).")
    estimatedTotalAmtTo: str = Field(None,
                                     description="Estimated total to amount. Values LESS than the specified amount (ex. 500000).")
    fundsObligatedAmtFrom: str = Field(None,
                                       description="Funds obligated from amount. Values GREATER than the specified amount (ex. 50000).")
    fundsObligatedAmtTo: str = Field(None,
                                     description="Funds obligated to amount. Values LESS than the specified amount (ex. 500000).")
    ueiNumber: str = Field(None, description="Unique Identifier of Entity (ex. F2VSMAKDH8Z7)")
    fundProgramName: str = Field(None, description='Fund Program Name (ex. "ANTARCTIC+COORDINATION")')
    parentUeiNumber: str = Field(None, description="Unique Identifier of Parent Entity (ex. JBG7T7RXQ2B7)")
    pdPIName: str = Field(None, description='Project Director/Principal Investigator Name (ex. "SUMNET+STARFIELD")')
    perfCity: str = Field(None, description="Performance City Name (ex. Arlington)")
    perfCountryCode: str = Field(None, description="Performance Country Code (ex. US)")
    perfDistrictCode: str = Field(None, description="Performance congressional district code (ex. VA01,NY22)")
    perfLocation: str = Field(None, description='Performance location name (ex. "university+of+south+florida")')
    perfStateCode: str = Field(None, description="Performance State Code (ex. VA)")
    perfZipCode: str = Field(None,
                             description="9 digit performance zip code with the pattern of 5 digit + 4 (ex. 231730001)")
    poName: str = Field(None, description='Program Officer Name (ex. "Hamos+Rick")')
    primaryProgram: str = Field(None,
                                description="Comma separated numbers that include FUND_SYMB_ID to return FUND Code + FUND Name (ex. 040106, 040107)")
    transType: str = Field(None,
                           description="Transaction Type (ex. BOA/Task Order, Continuing Grant, Contract, Standard Grant)")
