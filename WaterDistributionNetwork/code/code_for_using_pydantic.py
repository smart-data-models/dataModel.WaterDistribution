from __future__ import annotations

from enum import Enum
from typing import List, Optional, Union

from pydantic import AnyUrl, AwareDatetime, BaseModel, Field, RootModel, constr


class Address(BaseModel):
    addressCountry: Optional[str] = Field(
        None, description='The country. For example, Spain'
    )
    addressLocality: Optional[str] = Field(
        None,
        description='The locality in which the street address is, and which is in the region',
    )
    addressRegion: Optional[str] = Field(
        None,
        description='The region in which the locality is, and which is in the country',
    )
    district: Optional[str] = Field(
        None,
        description='A district is a type of administrative division that, in some countries, is managed by the local government',
    )
    postOfficeBoxNumber: Optional[str] = Field(
        None,
        description='The post office box number for PO box addresses. For example, 03578',
    )
    postalCode: Optional[str] = Field(
        None, description='The postal code. For example, 24004'
    )
    streetAddress: Optional[str] = Field(None, description='The street address')
    streetNr: Optional[str] = Field(
        None, description='Number identifying a specific property on a public street'
    )


class ClTSA(BaseModel):
    avgOverTime: Optional[float] = Field(
        None,
        description='Describes the average value of a time-series data over a specified duration in past. The duration is specified using another parameter in the value descriptor object related to this value',
    )
    instValue: Optional[float] = Field(
        None,
        description='Describes the instantaneous value (associated with the current timestamp) of a time varying quantity',
    )
    maxOverTime: Optional[float] = Field(
        None,
        description='Describes the maximum value of a time-series data over a specified duration in past. The duration is specified using another parameter in the value descriptor object related to this value',
    )
    minOverTime: Optional[float] = Field(
        None,
        description='Describes the minimum value of a time-series data over a specified duration in past. The duration is specified using another parameter in the value descriptor object related to this value',
    )


class DeviceModel(BaseModel):
    brandName: Optional[str] = Field(
        None,
        description='Name of the brand associated with an entity, e.g., sensor, device etc',
    )
    manufacturerName: Optional[str] = Field(
        None,
        description='Name of the manufacturer associated with an entity, e.g., sensor, device etc',
    )
    modelName: Optional[str] = Field(
        None,
        description='Name of a specific model associated with an entity, e.g., sensor, device etc',
    )
    modelURL: Optional[str] = Field(
        None,
        description='URL providing further information of a specific model associated with an entity, e.g., sensor, device etc',
    )


class DeviceInfo(BaseModel):
    deviceBatteryStatus: Optional[str] = Field(
        None,
        description='Gives the Battery charging status of the reporting device(Connected, Disconnected)',
    )
    deviceID: Optional[str] = Field(
        None,
        description='Device ID of the physical sensor/ measurement station corresponding to this observation',
    )
    deviceModel: Optional[DeviceModel] = Field(
        None,
        description='Describes the information of the device, sensor or system in consideration',
    )
    deviceName: Optional[str] = Field(
        None,
        description='Device Name or Station name of the sensor device/station corresponding to this observation',
    )
    deviceSimNumber: Optional[str] = Field(
        None,
        description='Gives the sim number of the device in the waste management vehicle',
    )
    measurand: Optional[str] = Field(
        None, description='Property/properties sensed/observed/measured by the device'
    )
    rfID: Optional[str] = Field(None, description='Gives the ID of the RFID reader')


class Type(Enum):
    Point = 'Point'


class Location(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[float] = Field(..., min_length=2)
    type: Type


class Coordinate(RootModel[List[float]]):
    root: List[float]


class Type1(Enum):
    LineString = 'LineString'


class Location1(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[Coordinate] = Field(..., min_length=2)
    type: Type1


class Type2(Enum):
    Polygon = 'Polygon'


class Location2(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[List[Coordinate]]
    type: Type2


class Type3(Enum):
    MultiPoint = 'MultiPoint'


class Location3(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[List[float]]
    type: Type3


class Type4(Enum):
    MultiLineString = 'MultiLineString'


class Location4(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[List[Coordinate]]
    type: Type4


class Type5(Enum):
    MultiPolygon = 'MultiPolygon'


class Location5(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[List[List[Coordinate]]]
    type: Type5


class PHTSA(BaseModel):
    avgOverTime: Optional[float] = Field(
        None,
        description='Describes the average value of a time-series data over a specified duration in past. The duration is specified using another parameter in the value descriptor object related to this value',
    )
    instValue: Optional[float] = Field(
        None,
        description='Describes the instantaneous value (associated with the current timestamp) of a time varying quantity',
    )
    maxOverTime: Optional[float] = Field(
        None,
        description='Describes the maximum value of a time-series data over a specified duration in past. The duration is specified using another parameter in the value descriptor object related to this value',
    )
    minOverTime: Optional[float] = Field(
        None,
        description='Describes the minimum value of a time-series data over a specified duration in past. The duration is specified using another parameter in the value descriptor object related to this value',
    )


class TankShape(Enum):
    Cylindrical = 'Cylindrical'
    Conical = 'Conical'
    Cuboid = 'Cuboid'
    Spherical = 'Spherical'


class TurbidityTSA(BaseModel):
    avgOverTime: Optional[float] = Field(
        None,
        description='Describes the average value of a time-series data over a specified duration in past. The duration is specified using another parameter in the value descriptor object related to this value',
    )
    instValue: Optional[float] = Field(
        None,
        description='Describes the instantaneous value (associated with the current timestamp) of a time varying quantity',
    )
    maxOverTime: Optional[float] = Field(
        None,
        description='Describes the maximum value of a time-series data over a specified duration in past. The duration is specified using another parameter in the value descriptor object related to this value',
    )
    minOverTime: Optional[float] = Field(
        None,
        description='Describes the minimum value of a time-series data over a specified duration in past. The duration is specified using another parameter in the value descriptor object related to this value',
    )


class Type6(Enum):
    WaterDistributionNetwork = 'WaterDistributionNetwork'


class WaterDistributionNetwork(BaseModel):
    address: Optional[Address] = Field(None, description='The mailing address')
    alternateName: Optional[str] = Field(
        None, description='An alternative name for this item'
    )
    areaServed: Optional[str] = Field(
        None,
        description='The geographic area where a service or offered item is provided',
    )
    clTSA: Optional[ClTSA] = Field(
        None, description='Concentration of chlorides in the water'
    )
    compensatedTDS: Optional[float] = Field(
        None,
        description='The value of TDS (Total Dissolved Solids) level in the water with temperature compensation',
    )
    dataProvider: Optional[str] = Field(
        None,
        description='A sequence of characters identifying the provider of the harmonised data entity',
    )
    dateCreated: Optional[AwareDatetime] = Field(
        None,
        description='Entity creation timestamp. This will usually be allocated by the storage platform',
    )
    dateModified: Optional[AwareDatetime] = Field(
        None,
        description='Timestamp of the last modification of the entity. This will usually be allocated by the storage platform',
    )
    description: Optional[str] = Field(None, description='A description of this item')
    deviceInfo: Optional[DeviceInfo] = Field(
        None,
        description='Information about the device associated with the observations',
    )
    flowrate: Optional[float] = Field(
        None,
        description='Volume of water flowing in/out of the water storage tank corresponding to this observation',
    )
    id: Optional[
        Union[
            constr(
                pattern=r'^[\\w\\-\\.\\{\\}\\$\\+\\*\\[\\]`|~^@!, :\\\\]+$',
                min_length=1,
                max_length=256,
            ),
            AnyUrl,
        ]
    ] = Field(None, description='Unique identifier of the entity')
    location: Optional[
        Union[Location, Location1, Location2, Location3, Location4, Location5]
    ] = Field(
        None,
        description='Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon',
    )
    name: Optional[str] = Field(None, description='The name of this item')
    observationDateTime: Optional[AwareDatetime] = Field(
        None, description='Last reported time of observation'
    )
    owner: Optional[
        List[
            Union[
                constr(
                    pattern=r'^[\\w\\-\\.\\{\\}\\$\\+\\*\\[\\]`|~^@!,:\\\\]+$',
                    min_length=1,
                    max_length=256,
                ),
                AnyUrl,
            ]
        ]
    ] = Field(
        None,
        description='A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)',
    )
    pHTSA: Optional[PHTSA] = Field(
        None, description='Acidity level or basicity level observed in the water'
    )
    seeAlso: Optional[Union[List[AnyUrl], AnyUrl]] = Field(
        None, description='list of uri pointing to additional resources about the item'
    )
    source: Optional[str] = Field(
        None,
        description='A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object',
    )
    tankBreadth: Optional[float] = Field(
        None, description='Breadth of the Cuboid shaped water storage tank'
    )
    tankCapacity: Optional[float] = Field(
        None,
        description='Maximum amount of water the water storage tank corresponding to this observation can hold',
    )
    tankDepth: Optional[float] = Field(
        None,
        description='Depth of the water storage tank corresponding to this observation',
    )
    tankDiameter: Optional[float] = Field(
        None, description='Diameter of Cylindrical or Spherical water storage tanks'
    )
    tankLength: Optional[float] = Field(
        None, description='Length of the Cuboid shaped water storage tank'
    )
    tankName: Optional[str] = Field(
        None,
        description='Name of the water storage tank corresponding to this observation',
    )
    tankShape: Optional[TankShape] = Field(
        None,
        description='Physical shape of the water storage tank corresponding to this observation. ENUM: [Cylindrical, Conical, Cuboid, Spherical]',
    )
    totalML: Optional[float] = Field(
        None,
        description='Total MLDs of water discharged from the water storage tank corresponding to this observation',
    )
    turbidityTSA: Optional[TurbidityTSA] = Field(
        None,
        description='Measurement of the amount of light that is scattered by material in the water when a light is shined through the water',
    )
    type: Optional[Type6] = Field(
        None, description='NGSI Entity type. It has to be WaterDistributionNetwork'
    )
    uncompensatedTDS: Optional[float] = Field(
        None,
        description='The value of TDS (Total Dissolved Solids) level in the water without temperature compensation',
    )
    waterFlow: Optional[float] = Field(
        None,
        description='Flow or current of water flowing from the water storage tank corresponding to this observation',
    )
    waterLevel: Optional[float] = Field(
        None,
        description='Current water level in the water storage tank corresponding to this observation',
    )
    waterPressure: Optional[float] = Field(
        None,
        description='Pressure of water flowing from the water storage tank corresponding to this observation',
    )
    waterTemperature: Optional[float] = Field(
        None,
        description='Water temperature in the water storage tank corresponding to this observation',
    )
