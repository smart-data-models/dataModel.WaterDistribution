<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
实体：配水网络  
=======<!-- /10-Header -->  
<!-- 15-License -->  
[开放许可](https://github.com/smart-data-models//dataModel.WaterDistribution/blob/master/WaterDistributionNetwork/LICENSE.md)  
[文件自动生成](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
全局描述：**一个城市供水网络的数据模型。  
版本： 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## 属性列表  

<sup><sub>[*] 如果属性中没有类型，是因为它可能有多个类型或不同的格式/模式</sub></sup>。  
- `address[object]`: 邮寄地址  . Model: [https://schema.org/address](https://schema.org/address)- `alternateName[string]`: 该项目的替代名称  - `areaServed[string]`: 提供服务或提供物品的地理区域  . Model: [https://schema.org/Text](https://schema.org/Text)- `clTSA[object]`: 属性。模型：'https://schema.org/Text'。水中的氯化物浓度。  . Model: [https://schema.org/Text](https://schema.org/Text)- `compensatedTDS[number]`: 属性。模型:'https://schema.org/Number'。水中的 TDS（总溶解固体）值，带温度补偿。  . Model: [https://schema.org/Number](https://schema.org/Number)- `dataProvider[string]`: 标识统一数据实体提供者的字符序列。  - `dateCreated[string]`: 实体创建时间戳。这通常由存储平台分配。  - `dateModified[string]`: 实体最后一次修改的时间戳。这通常由存储平台分配。  - `description[string]`: 项目描述  - `deviceInfo[object]`: 属性。型号：'https://schema.org/Text'。与观测数据相关的设备信息。  . Model: [https://schema.org/Text](https://schema.org/Text)- `flowrate[number]`: 属性。模型:'https://schema.org/Number'。与该观测值相对应的储水箱进出水量。  . Model: [https://schema.org/Number](https://schema.org/Number)- `id[*]`: 实体的唯一标识符  - `location[*]`: 项目的 Geojson 引用。它可以是点、线条字符串、多边形、多点、多线条字符串或多多边形  - `name[string]`: 该项目的名称。  - `observationDateTime[string]`: 属性。模型：'https://schema.org/Text'。最后报告的观测时间。  . Model: [https://schema.org/Text](https://schema.org/Text)- `owner[array]`: 包含一个 JSON 编码字符序列的列表，其中引用了所有者的唯一 Ids  - `pHTSA[object]`: 属性。模型：'https://schema.org/Text'。水中的酸度或碱度。  . Model: [https://schema.org/Text](https://schema.org/Text)- `seeAlso[*]`: 指向有关该项目的其他资源的 uri 列表  - `source[string]`: 以 URL 形式给出实体数据原始来源的字符串。建议使用源提供者的完全合格域名或源对象的 URL。  - `tankBreadth[number]`: 属性。模型:'https://schema.org/Number'。立方体储水箱的宽度。  . Model: [https://schema.org/Number](https://schema.org/Number)- `tankCapacity[number]`: 属性。模型:'https://schema.org/Number'。该观测值对应的储水箱可容纳的最大水量。  . Model: [https://schema.org/Number](https://schema.org/Number)- `tankDepth[number]`: 属性。模型:'https://schema.org/Number'。与该观测值相对应的储水箱深度。  . Model: [https://schema.org/Number](https://schema.org/Number)- `tankDiameter[number]`: 属性。型号：'https://schema.org/Number'。圆柱形或球形储水罐的直径。  . Model: [https://schema.org/Number](https://schema.org/Number)- `tankLength[number]`: 属性。模型:'https://schema.org/Number'。立方体储水罐的长度。  . Model: [https://schema.org/Number](https://schema.org/Number)- `tankName[string]`: 属性。Model:'https://schema.org/Text'。与该观测值相对应的储水箱名称。  . Model: [https://schema.org/Text](https://schema.org/Text)- `tankShape[string]`: 属性。模型:'https://schema.org/Text'。与该观测值相对应的储水箱的物理形状。ENUM：[圆柱形、圆锥形、长方体、球形］  . Model: [https://schema.org/Text](https://schema.org/Text)- `totalML[number]`: 属性。模型：'https://schema.org/Number'。该观测值对应的储水箱总排水量。  . Model: [https://schema.org/Number](https://schema.org/Number)- `turbidityTSA[object]`: 属性。模型：'https://schema.org/Text'。当光线穿过水面照射时，对水中物质散射光量的测量。  . Model: [https://schema.org/Text](https://schema.org/Text)- `uncompensatedTDS[number]`: 属性。模型:'https://schema.org/Number'。水中的 TDS（总溶解固体）值，不含温度补偿。  . Model: [https://schema.org/Number](https://schema.org/Number)- `waterFlow[number]`: 属性。Model:'https://schema.org/Number'。与该观测值相对应的储水箱中流出的水流或水流。  . Model: [https://schema.org/Number](https://schema.org/Number)- `waterLevel[number]`: 属性。Model:'https://schema.org/Number'。与该观测值相对应的储水箱中的当前水位。  . Model: [https://schema.org/Number](https://schema.org/Number)- `waterPressure[number]`: 属性。模型:'https://schema.org/Number'。与该观测值相对应的储水箱水流压力。  . Model: [https://schema.org/Number](https://schema.org/Number)- `waterTemperature[number]`: 属性。Model:'https://schema.org/Number'。与该观测值相对应的储水箱中的水温。  . Model: [https://schema.org/Number](https://schema.org/Number)<!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
所需属性  
- `id`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## 属性的数据模型描述  
按字母顺序排列（点击查看详情）  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
WaterDistributionNetwork:    
  description: A Data Model for water supply network in a city.    
  properties:    
    address:    
      description: The mailing address    
      properties:    
        addressCountry:    
          description: 'Property. The country. For example, Spain. Model:''https://schema.org/addressCountry'''    
          type: string    
        addressLocality:    
          description: 'Property. The locality in which the street address is, and which is in the region. Model:''https://schema.org/addressLocality'''    
          type: string    
        addressRegion:    
          description: 'Property. The region in which the locality is, and which is in the country. Model:''https://schema.org/addressRegion'''    
          type: string    
        district:    
          description: 'A district is a type of administrative division that, in some countries, is managed by the local government.'    
          type: string    
        postOfficeBoxNumber:    
          description: 'Property. The post office box number for PO box addresses. For example, 03578. Model:''https://schema.org/postOfficeBoxNumber'''    
          type: string    
        postalCode:    
          description: 'Property. The postal code. For example, 24004. Model:''https://schema.org/https://schema.org/postalCode'''    
          type: string    
        streetAddress:    
          description: 'Property. The street address. Model:''https://schema.org/streetAddress'''    
          type: string    
        streetNr:    
          description: Number identifying a specific property on a public street.    
          type: string    
      type: object    
      x-ngsi:    
        model: https://schema.org/address    
        type: Property    
    alternateName:    
      description: An alternative name for this item    
      type: string    
      x-ngsi:    
        type: Property    
    areaServed:    
      description: The geographic area where a service or offered item is provided    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    clTSA:    
      description: 'Property. Model:''https://schema.org/Text''. Concentration of chlorides in the water.'    
      properties:    
        avgOverTime:    
          description: 'Property. Model:''https://schema.org/Text''. Describes the average value of a time-series data over a specified duration in past. The duration is specified using another parameter in the value descriptor object related to this value'    
          type: number    
        instValue:    
          description: 'Property. Model:''https://schema.org/Text''. Describes the instantaneous value (associated with the current timestamp) of a time varying quantity.'    
          type: number    
        maxOverTime:    
          description: 'Property. Model:''https://schema.org/Text''. Describes the maximum value of a time-series data over a specified duration in past. The duration is specified using another parameter in the value descriptor object related to this value'    
          type: number    
        minOverTime:    
          description: 'Property. Model:''https://schema.org/Text''. Describes the minimum value of a time-series data over a specified duration in past. The duration is specified using another parameter in the value descriptor object related to this value'    
          type: number    
      type: object    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    compensatedTDS:    
      description: 'Property. Model:''https://schema.org/Number''. The value of TDS (Total Dissolved Solids) level in the water with temperature compensation.'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    dataProvider:    
      description: A sequence of characters identifying the provider of the harmonised data entity.    
      type: string    
      x-ngsi:    
        type: Property    
    dateCreated:    
      description: Entity creation timestamp. This will usually be allocated by the storage platform.    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    dateModified:    
      description: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    description:    
      description: A description of this item    
      type: string    
      x-ngsi:    
        type: Property    
    deviceInfo:    
      description: 'Property. Model:''https://schema.org/Text''. Information about the device associated with the observations.'    
      properties:    
        deviceBatteryStatus:    
          description: 'Property. Model:''https://schema.org/Text''. Gives the Battery charging status of the reporting device(Connected, Disconnected).'    
          type: string    
        deviceID:    
          description: 'Property. Model:''https://schema.org/Text''. Device ID of the physical sensor/ measurement station corresponding to this observation.'    
          type: string    
        deviceModel:    
          description: 'Property. Model:''https://schema.org/Text''. Describes the information of the device, sensor or system in consideration.'    
          properties:    
            brandName:    
              description: 'Property. Model:''https://schema.org/Text''. Name of the brand associated with an entity, e.g., sensor, device etc.'    
              type: string    
            manufacturerName:    
              description: 'Property. Model:''https://schema.org/Text''. Name of the manufacturer associated with an entity, e.g., sensor, device etc.'    
              type: string    
            modelName:    
              description: 'Property. Model:''https://schema.org/Text''. Name of a specific model associated with an entity, e.g., sensor, device etc.'    
              type: string    
            modelURL:    
              description: 'Property. Model:''https://schema.org/Text''. URL providing further information of a specific model associated with an entity, e.g., sensor, device etc.'    
              type: string    
          type: object    
        deviceName:    
          description: 'Property. Model:''https://schema.org/Text''. Device Name or Station name of the sensor device/station corresponding to this observation.'    
          type: string    
        deviceSimNumber:    
          description: 'Property. Model:''https://schema.org/Text''. Gives the sim number of the device in the waste management vehicle.'    
          type: string    
        measurand:    
          description: 'Property. Model:''https://schema.org/Text''. Property/properties sensed/observed/measured by the device.'    
          type: string    
        rfID:    
          description: 'Property. Model:''https://schema.org/Text''. Gives the ID of the RFID reader.'    
          type: string    
      type: object    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    flowrate:    
      description: 'Property. Model:''https://schema.org/Number''. Volume of water flowing in/out of the water storage tank corresponding to this observation.'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    id:    
      anyOf: &waterdistributionnetwork_-_properties_-_owner_-_items_-_anyof    
        - description: Property. Identifier format of any NGSI entity    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: Property. Identifier format of any NGSI entity    
          format: uri    
          type: string    
      description: Unique identifier of the entity    
      x-ngsi:    
        type: Property    
    location:    
      description: 'Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'    
      oneOf:    
        - description: GeoProperty. Geojson reference to the item. Point    
          properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                type: number    
              minItems: 2    
              type: array    
            type:    
              enum:    
                - Point    
              type: string    
          required:    
            - type    
            - coordinates    
          title: GeoJSON Point    
          type: object    
        - description: GeoProperty. Geojson reference to the item. LineString    
          properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  type: number    
                minItems: 2    
                type: array    
              minItems: 2    
              type: array    
            type:    
              enum:    
                - LineString    
              type: string    
          required:    
            - type    
            - coordinates    
          title: GeoJSON LineString    
          type: object    
        - description: GeoProperty. Geojson reference to the item. Polygon    
          properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  items:    
                    type: number    
                  minItems: 2    
                  type: array    
                minItems: 4    
                type: array    
              type: array    
            type:    
              enum:    
                - Polygon    
              type: string    
          required:    
            - type    
            - coordinates    
          title: GeoJSON Polygon    
          type: object    
        - description: GeoProperty. Geojson reference to the item. MultiPoint    
          properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  type: number    
                minItems: 2    
                type: array    
              type: array    
            type:    
              enum:    
                - MultiPoint    
              type: string    
          required:    
            - type    
            - coordinates    
          title: GeoJSON MultiPoint    
          type: object    
        - description: GeoProperty. Geojson reference to the item. MultiLineString    
          properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  items:    
                    type: number    
                  minItems: 2    
                  type: array    
                minItems: 2    
                type: array    
              type: array    
            type:    
              enum:    
                - MultiLineString    
              type: string    
          required:    
            - type    
            - coordinates    
          title: GeoJSON MultiLineString    
          type: object    
        - description: GeoProperty. Geojson reference to the item. MultiLineString    
          properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  items:    
                    items:    
                      type: number    
                    minItems: 2    
                    type: array    
                  minItems: 4    
                  type: array    
                type: array    
              type: array    
            type:    
              enum:    
                - MultiPolygon    
              type: string    
          required:    
            - type    
            - coordinates    
          title: GeoJSON MultiPolygon    
          type: object    
      x-ngsi:    
        type: GeoProperty    
    name:    
      description: The name of this item.    
      type: string    
      x-ngsi:    
        type: Property    
    observationDateTime:    
      description: 'Property. Model:''https://schema.org/Text''. Last reported time of observation.'    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    owner:    
      description: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)    
      items:    
        anyOf: *waterdistributionnetwork_-_properties_-_owner_-_items_-_anyof    
        description: Property. Unique identifier of the entity    
      type: array    
      x-ngsi:    
        type: Property    
    pHTSA:    
      description: 'Property. Model:''https://schema.org/Text''. Acidity level or basicity level obsevered in the water.'    
      properties:    
        avgOverTime:    
          description: 'Property. Model:''https://schema.org/Text''. Describes the average value of a time-series data over a specified duration in past. The duration is specified using another parameter in the value descriptor object related to this value'    
          type: number    
        instValue:    
          description: 'Property. Model:''https://schema.org/Text''. Describes the instantaneous value (associated with the current timestamp) of a time varying quantity.'    
          type: number    
        maxOverTime:    
          description: 'Property. Model:''https://schema.org/Text''. Describes the maximum value of a time-series data over a specified duration in past. The duration is specified using another parameter in the value descriptor object related to this value'    
          type: number    
        minOverTime:    
          description: 'Property. Model:''https://schema.org/Text''. Describes the minimum value of a time-series data over a specified duration in past. The duration is specified using another parameter in the value descriptor object related to this value'    
          type: number    
      type: object    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    seeAlso:    
      description: list of uri pointing to additional resources about the item    
      oneOf:    
        - items:    
            format: uri    
            type: string    
          minItems: 1    
          type: array    
        - format: uri    
          type: string    
      x-ngsi:    
        type: Property    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: string    
      x-ngsi:    
        type: Property    
    tankBreadth:    
      description: 'Property. Model:''https://schema.org/Number''. Breadth of the Cuboid shaped water storage tank.'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tankCapacity:    
      description: 'Property. Model:''https://schema.org/Number''. Maximum amount of water the water storage tank corresponding to this observation can hold.'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tankDepth:    
      description: 'Property. Model:''https://schema.org/Number''. Depth of the water storage tank corresponding to this observation.'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tankDiameter:    
      description: 'Property. Model:''https://schema.org/Number''. Diameter of Cylindrical or Spherical water storage tanks.'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tankLength:    
      description: 'Property. Model:''https://schema.org/Number''. Length of the Cuboid shaped water storage tank.'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tankName:    
      description: 'Property. Model:''https://schema.org/Text''. Name of the water storage tank corresponding to this observation.'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    tankShape:    
      description: 'Property. Model:''https://schema.org/Text''. Physical shape of the water storage tank corresponding to this observation. ENUM: [Cylindrical, Conical, Cuboid, Spherical]'    
      enum:    
        - Cylindrical    
        - Conical    
        - Cuboid    
        - Spherical    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    totalML:    
      description: 'Property. Model:''https://schema.org/Number''. Total MLDs of water discharged from the water storage tank corresponding to this observation.'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    turbidityTSA:    
      description: 'Property. Model:''https://schema.org/Text''. Measurement of the amount of light that is scattered by material in the water when a light is shined through the water.'    
      properties:    
        avgOverTime:    
          description: 'Property. Model:''https://schema.org/Text''. Describes the average value of a time-series data over a specified duration in past. The duration is specified using another parameter in the value descriptor object related to this value'    
          type: number    
        instValue:    
          description: 'Property. Model:''https://schema.org/Text''. Describes the instantaneous value (associated with the current timestamp) of a time varying quantity.'    
          type: number    
        maxOverTime:    
          description: 'Property. Model:''https://schema.org/Text''. Describes the maximum value of a time-series data over a specified duration in past. The duration is specified using another parameter in the value descriptor object related to this value'    
          type: number    
        minOverTime:    
          description: 'Property. Model:''https://schema.org/Text''. Describes the minimum value of a time-series data over a specified duration in past. The duration is specified using another parameter in the value descriptor object related to this value'    
          type: number    
      type: object    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    uncompensatedTDS:    
      description: 'Property. Model:''https://schema.org/Number''. The value of TDS (Total Dissolved Solids) level in the water without temperature compensation.'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    waterFlow:    
      description: 'Property. Model:''https://schema.org/Number''. Flow or current of water flowing from the water storage tank corresponding to this observation.'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    waterLevel:    
      description: 'Property. Model:''https://schema.org/Number''. Current water level in the water storage tank corresponding to this observation.'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    waterPressure:    
      description: 'Property. Model:''https://schema.org/Number''. Pressure of water flowing from the water storage tank corresponding to this observation.'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    waterTemperature:    
      description: 'Property. Model:''https://schema.org/Number''. Water temperature in the water storage tank corresponding to this observation.'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
  required:    
    - id    
    - type    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.WaterDistribution/blob/master/WaterDistributionNetwork/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/SmartWater/WaterDistributionNetwork/schema.json    
  x-model-tags: ""    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## 有效载荷示例  
#### WaterDistributionNetwork NGSI-v2 key-values 示例  
下面是一个以 JSON-LD 格式作为键值的 WaterDistributionNetwork 示例。当使用 `options=keyValues` 时，它与 NGSI-v2 兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
	"id": "uri:ngsi-ld:WaterDistributionNetwork:0001",  
	"type": "WaterDistributionNetwork",  
	"tankDiameter": 10,  
	"totalML": 250,  
	"tankCapacity": 500,  
	"waterFlow": 14,  
	"tankBreadth": 50,  
	"tankDepth": 200,  
	"flowrate": 70,  
	"tankLength": 300,  
	"waterTemperature": 20,  
	"waterPressure": 5,  
	"turbidityTSA": {  
		"avgOverTime": 14,  
		"maxOverTime": 23,  
		"instValue": 34,  
		"minOverTime": 12  
	},  
	"clTSA": {  
		"avgOverTime": 6,  
		"maxOverTime": 20,  
		"instValue": 12,  
		"minOverTime": 23  
	},  
	"pHTSA": {  
		"avgOverTime": 6,  
		"maxOverTime": 8,  
		"instValue": 7,  
		"minOverTime": 6  
	},  
	"deviceInfo": {  
		"rfID": "345438",  
		"deviceBatteryStatus": "Connected",  
		"deviceName": " Device 4",  
		"deviceID": "234",  
		"measurand": "2",  
		"deviceSimNumber": "9883829934",  
		"deviceModel": {  
			"brandName": "Trumen Technologies Private Limited",  
			"manufacturerName": "Trumen Technologies Private Limited",  
			"modelName": "Model 4",  
			"modelURL": "https://trumen.in/"  
		}  
	},  
	"waterLevel": 57,  
	"tankName": "Tank 16",  
	"tankShape": "Cylindrical",  
	"observationDateTime": "2021-03-11T15:51:02+05:30",  
	"compensatedTDS":25,  
	"uncompensatedTDS":27  
}  
```  
</details>  
#### WaterDistributionNetwork NGSI-v2 归一化示例  
下面是一个规范化 JSON-LD 格式的 WaterDistributionNetwork 示例。在不使用选项的情况下，它与 NGSI-v2 兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "uri:ngsi-ld:WaterDistributionNetwork:0001",  
  "type": "WaterDistributionNetwork",  
  "tankDiameter": {  
    "type": "number",  
    "value": 10  
  },  
  "totalML": {  
    "type": "number",  
    "value": 250  
  },  
  "tankCapacity": {  
    "type": "number",  
    "value": 500  
  },  
  "waterFlow": {  
    "type": "number",  
    "value": 14  
  },  
  "tankBreadth": {  
    "type": "number",  
    "value": 50  
  },  
  "tankDepth": {  
    "type": "number",  
    "value": 200  
  },  
  "flowrate": {  
    "type": "number",  
    "value": 70  
  },  
  "tankLength": {  
    "type": "number",  
    "value": 300  
  },  
  "waterTemperature": {  
    "type": "number",  
    "value": 20  
  },  
  "waterPressure": {  
    "type": "number",  
    "value": 5  
  },  
  "turbidityTSA": {  
    "type": "StructuredValue",  
    "value": {  
      "avgOverTime": 14,  
      "maxOverTime": 23,  
      "instValue": 34,  
      "minOverTime": 12  
    }  
  },  
  "clTSA": {  
    "type": "StructuredValue",  
    "value": {  
      "avgOverTime": 6,  
      "maxOverTime": 20,  
      "instValue": 12,  
      "minOverTime": 23  
    }  
  },  
  "pHTSA": {  
    "type": "StructuredValue",  
    "value": {  
      "avgOverTime": 6,  
      "maxOverTime": 8,  
      "instValue": 7,  
      "minOverTime": 6  
    }  
  },  
  "deviceInfo": {  
    "type": "StructuredValue",  
    "value": {  
      "rfID": "345438",  
      "deviceBatteryStatus": "Connected",  
      "deviceName": " Device 4",  
      "deviceID": "234",  
      "measurand": "2",  
      "deviceSimNumber": "9883829934",  
      "deviceModel": {  
        "brandName": "Trumen Technologies Private Limited",  
        "manufacturerName": "Trumen Technologies Private Limited",  
        "modelName": "Model 4",  
        "modelURL": "https://trumen.in/"  
      }  
    }  
  },  
  "waterLevel": {  
    "type": "number",  
    "value": 57  
  },  
  "tankName": {  
    "type": "Text",  
    "value": "Tank 16"  
  },  
  "tankShape": {  
    "type": "Text",  
    "value": "Cylindrical"  
  },  
  "observationDateTime": {  
    "type": "Date-Time",  
    "value": "2021-03-11T15:51:02+05:30"  
  },  
  "compensatedTDS": {  
    "type": "number",  
    "value": 25  
  },  
  "uncompensatedTDS": {  
    "type": "number",  
    "value": 27  
  }  
}  
```  
</details>  
#### WaterDistributionNetwork NGSI-LD key-values 示例  
下面是一个以 JSON-LD 格式作为键值的 WaterDistributionNetwork 示例。当使用 `options=keyValues` 时，它与 NGSI-LD 兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
	"id": "uri:ngsi-ld:WaterDistributionNetwork:0001",  
	"@context": "iudx:WaterDistributionNetwork",  
	"type": "WaterDistributionNetwork",  
	"tankDiameter": 10,  
	"totalML": 250,  
	"tankCapacity": 500,  
	"waterFlow": 14,  
	"tankBreadth": 50,  
	"tankDepth": 200,  
	"flowrate": 70,  
	"tankLength": 300,  
	"waterTemperature": 20,  
	"waterPressure": 5,  
	"turbidityTSA": {  
		"avgOverTime": 14,  
		"maxOverTime": 23,  
		"instValue": 34,  
		"minOverTime": 12  
	},  
	"clTSA": {  
		"avgOverTime": 6,  
		"maxOverTime": 20,  
		"instValue": 12,  
		"minOverTime": 23  
	},  
	"pHTSA": {  
		"avgOverTime": 6,  
		"maxOverTime": 8,  
		"instValue": 7,  
		"minOverTime": 6  
	},  
	"deviceInfo": {  
		"rfID": "345438",  
		"deviceBatteryStatus": "Connected",  
		"deviceName": " Device 4",  
		"deviceID": "234",  
		"measurand": "2",  
		"deviceSimNumber": "9883829934",  
		"deviceModel": {  
			"brandName": "Trumen Technologies Private Limited",  
			"manufacturerName": "Trumen Technologies Private Limited",  
			"modelName": "Model 4",  
			"modelURL": "https://trumen.in/"  
		}  
	},  
	"waterLevel": 57,  
	"tankName": "Tank 16",  
	"tankShape": "Cylindrical",  
	"observationDateTime": "2021-03-11T15:51:02+05:30",  
	"compensatedTDS":25,  
	"uncompensatedTDS":27  
}  
```  
</details>  
#### WaterDistributionNetwork NGSI-LD 归一化示例  
下面是一个规范化 JSON-LD 格式的 WaterDistributionNetwork 示例。当不使用选项时，它与 NGSI-LD 兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "uri:ngsi-ld:WaterDistributionNetwork:0001",  
  "type": "WaterDistributionNetwork",  
  "tankDiameter": {  
    "type": "Property",  
    "value": 10  
  },  
  "totalML": {  
    "type": "Property",  
    "value": 250  
  },  
  "tankCapacity": {  
    "type": "Property",  
    "value": 500  
  },  
  "waterFlow": {  
    "type": "Property",  
    "value": 14  
  },  
  "tankBreadth": {  
    "type": "Property",  
    "value": 50  
  },  
  "tankDepth": {  
    "type": "Property",  
    "value": 200  
  },  
  "flowrate": {  
    "type": "Property",  
    "value": 70  
  },  
  "tankLength": {  
    "type": "Property",  
    "value": 300  
  },  
  "waterTemperature": {  
    "type": "Property",  
    "value": 20  
  },  
  "waterPressure": {  
    "type": "Property",  
    "value": 5  
  },  
  "turbidityTSA": {  
    "type": "Property",  
    "value": {  
      "avgOverTime": 14,  
      "maxOverTime": 23,  
      "instValue": 34,  
      "minOverTime": 12  
    }  
  },  
  "clTSA": {  
    "type": "Property",  
    "value": {  
      "avgOverTime": 6,  
      "maxOverTime": 20,  
      "instValue": 12,  
      "minOverTime": 23  
    }  
  },  
  "pHTSA": {  
    "type": "Property",  
    "value": {  
      "avgOverTime": 6,  
      "maxOverTime": 8,  
      "instValue": 7,  
      "minOverTime": 6  
    }  
  },  
  "deviceInfo": {  
    "type": "Property",  
    "value": {  
      "rfID": "345438",  
      "deviceBatteryStatus": "Connected",  
      "deviceName": " Device 4",  
      "deviceID": "234",  
      "measurand": "2",  
      "deviceSimProperty": "9883829934",  
      "deviceModel": {  
        "brandName": "Trumen Technologies Private Limited",  
        "manufacturerName": "Trumen Technologies Private Limited",  
        "modelName": "Model 4",  
        "modelURL": "https://trumen.in/"  
      }  
    }  
  },  
  "waterLevel": {  
    "type": "Property",  
    "value": 57  
  },  
  "tankName": {  
    "type": "Property",  
    "value": "Tank 16"  
  },  
  "tankShape": {  
    "type": "Property",  
    "value": "Cylindrical"  
  },  
  "observationDateTime": {  
    "type": "Property",  
    "value": {  
      "@type": "Date-Time",  
      "@value": "2021-03-11T15:51:02+05:30"  
    }  
  },  
  "compensatedTDS": {  
    "type": "Property",  
    "value": 25  
  },  
  "uncompensatedTDS": {  
    "type": "Property",  
    "value": 27  
  }  
}  
```  
</details><!-- /80-Examples -->  
<!-- 90-FooterNotes -->  
<!-- /90-FooterNotes -->  
<!-- 95-Units -->  
请参阅 [FAQ 10](https://smartdatamodels.org/index.php/faqs/)，获取如何处理幅度单位的答案。  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
