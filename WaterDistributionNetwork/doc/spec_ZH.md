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
- `address[object]`: 邮寄地址  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: 国家。例如，西班牙  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)    
	- `addressLocality[string]`: 街道地址所在的地点，以及该地点所在的区域  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)    
	- `addressRegion[string]`: 地点所在的地区，以及该地区位于哪个国家  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)    
	- `district[string]`: 地区是一种行政区划，在一些国家由地方政府管理      
	- `postOfficeBoxNumber[string]`: 用于邮政信箱地址的邮政信箱号码。例如：03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)    
	- `postalCode[string]`: 邮政编码。例如：24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)    
	- `streetAddress[string]`: 街道地址  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)    
- `alternateName[string]`: 该项目的替代名称  - `areaServed[string]`: 提供服务或提供物品的地理区域  . Model: [https://schema.org/Text](https://schema.org/Text)- `clTSA[object]`: 水中的氯化物浓度  	- `avgOverTime[number]`: 描述时间序列数据在过去指定时间内的平均值。持续时间通过值描述符对象中与该值相关的另一个参数来指定  . Model: [https://schema.org/Number](https://schema.org/Number)    
	- `instValue[number]`: 描述时间变化量的瞬时值（与当前时间戳相关联  . Model: [https://schema.org/Number](https://schema.org/Number)    
	- `maxOverTime[number]`: 描述时间序列数据在过去指定时间内的最大值。持续时间通过值描述符对象中与该值相关的另一个参数来指定  . Model: [https://schema.org/Number](https://schema.org/Number)    
- `compensatedTDS[number]`: 温度补偿后的水中 TDS（总溶解固体）值  . Model: [https://schema.org/Number](https://schema.org/Number)- `dataProvider[string]`: 标识统一数据实体提供者的字符序列  - `dateCreated[date-time]`: 实体创建时间戳。通常由存储平台分配  - `dateModified[date-time]`: 实体最后一次修改的时间戳。通常由存储平台分配  - `description[string]`: 项目描述  - `deviceInfo[object]`: 与观测结果相关的设备信息  	- `deviceBatteryStatus[string]`: 显示报告设备的电池充电状态（连接、断开）  . Model: [https://schema.org/Text](https://schema.org/Text)    
	- `deviceID[string]`: 与该观测值相对应的物理传感器/测量站的设备 ID  . Model: [https://schema.org/Text](https://schema.org/Text)    
	- `deviceModel[object]`: 描述有关设备、传感器或系统的信息      
	- `deviceName[string]`: 该观测点对应的传感设备/站的设备名称或站名  . Model: [https://schema.org/Text](https://schema.org/Text)    
	- `deviceSimNumber[string]`: 提供废物管理车上设备的模拟号码  . Model: [https://schema.org/Text](https://schema.org/Text)    
	- `measurand[string]`: 设备感知/观测/测量的属性  . Model: [https://schema.org/Text](https://schema.org/Text)    
- `flowrate[number]`: 与该观测结果相对应的储水箱进出水量  . Model: [https://schema.org/Number](https://schema.org/Number)- `id[*]`: 实体的唯一标识符  - `location[*]`: 项目的 Geojson 引用。它可以是点、线条字符串、多边形、多点、多线条字符串或多多边形  - `name[string]`: 该项目的名称  - `observationDateTime[date-time]`: 最后报告的观察时间  . Model: [https://schema.org/Date-Time](https://schema.org/Date-Time)- `owner[array]`: 包含一个 JSON 编码字符序列的列表，其中引用了所有者的唯一 Ids  - `pHTSA[object]`: 观测到的水酸度或碱性水平  	- `avgOverTime[number]`: 描述时间序列数据在过去指定时间内的平均值。持续时间通过值描述符对象中与该值相关的另一个参数来指定  . Model: [https://schema.org/Number](https://schema.org/Number)    
	- `instValue[number]`: 描述时间变化量的瞬时值（与当前时间戳相关联  . Model: [https://schema.org/Number](https://schema.org/Number)    
	- `maxOverTime[number]`: 描述时间序列数据在过去指定时间内的最大值。持续时间通过值描述符对象中与该值相关的另一个参数来指定  . Model: [https://schema.org/Number](https://schema.org/Number)    
- `seeAlso[*]`: 指向有关该项目的其他资源的 uri 列表  - `source[string]`: 以 URL 形式给出实体数据原始来源的字符串。建议使用源提供者的完全合格域名或源对象的 URL  - `tankBreadth[number]`: 立方体储水箱的宽度  . Model: [https://schema.org/Number](https://schema.org/Number)- `tankCapacity[number]`: 该观测值对应的储水箱可容纳的最大水量  . Model: [https://schema.org/Number](https://schema.org/Number)- `tankDepth[number]`: 与该观测值相对应的储水箱深度  . Model: [https://schema.org/Number](https://schema.org/Number)- `tankDiameter[number]`: 圆柱形或球形储水罐直径  . Model: [https://schema.org/Number](https://schema.org/Number)- `tankLength[number]`: 立方体储水箱的长度  . Model: [https://schema.org/Number](https://schema.org/Number)- `tankName[string]`: 该观测点对应的储水箱名称  . Model: [https://schema.org/Text](https://schema.org/Text)- `tankShape[string]`: 与该观测值相对应的储水箱的物理形状。ENUM：[圆柱形、圆锥形、长方体、球形］  . Model: [https://schema.org/Text](https://schema.org/Text)- `totalML[number]`: 从储水罐中排出的与该观测结果相对应的水的总公升数  . Model: [https://schema.org/Number](https://schema.org/Number)- `turbidityTSA[object]`: 当光线穿过水面时，测量水中物质散射的光量  	- `avgOverTime[number]`: 描述时间序列数据在过去指定时间内的平均值。持续时间通过值描述符对象中与该值相关的另一个参数来指定  . Model: [https://schema.org/Number](https://schema.org/Number)    
	- `instValue[number]`: 描述时间变化量的瞬时值（与当前时间戳相关联  . Model: [https://schema.org/Number](https://schema.org/Number)    
	- `maxOverTime[number]`: 描述时间序列数据在过去指定时间内的最大值。持续时间通过值描述符对象中与该值相关的另一个参数来指定  . Model: [https://schema.org/Number](https://schema.org/Number)    
- `uncompensatedTDS[number]`: 不含温度补偿的水中 TDS（总溶解固体）值  . Model: [https://schema.org/Number](https://schema.org/Number)- `waterFlow[number]`: 从储水罐中流出的水流或水流与该观测结果相对应  . Model: [https://schema.org/Number](https://schema.org/Number)- `waterLevel[number]`: 该观测点对应的储水箱当前水位  . Model: [https://schema.org/Number](https://schema.org/Number)- `waterPressure[number]`: 从储水罐流出的水的压力与该观测值相对应  . Model: [https://schema.org/Number](https://schema.org/Number)- `waterTemperature[number]`: 与此观测结果相对应的储水箱中的水温  . Model: [https://schema.org/Number](https://schema.org/Number)<!-- /30-PropertiesList -->    
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
          description: 'The country. For example, Spain'      
          type: string      
          x-ngsi:      
            model: https://schema.org/addressCountry      
            type: Property      
        addressLocality:      
          description: 'The locality in which the street address is, and which is in the region'      
          type: string      
          x-ngsi:      
            model: https://schema.org/addressLocality      
            type: Property      
        addressRegion:      
          description: 'The region in which the locality is, and which is in the country'      
          type: string      
          x-ngsi:      
            model: https://schema.org/addressRegion      
            type: Property      
        district:      
          description: 'A district is a type of administrative division that, in some countries, is managed by the local government'      
          type: string      
          x-ngsi:      
            type: Property      
        postOfficeBoxNumber:      
          description: 'The post office box number for PO box addresses. For example, 03578'      
          type: string      
          x-ngsi:      
            model: https://schema.org/postOfficeBoxNumber      
            type: Property      
        postalCode:      
          description: 'The postal code. For example, 24004'      
          type: string      
          x-ngsi:      
            model: https://schema.org/https://schema.org/postalCode      
            type: Property      
        streetAddress:      
          description: The street address      
          type: string      
          x-ngsi:      
            model: https://schema.org/streetAddress      
            type: Property      
        streetNr:      
          description: Number identifying a specific property on a public street      
          type: string      
          x-ngsi:      
            type: Property      
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
      description: Concentration of chlorides in the water      
      properties:      
        avgOverTime:      
          description: Describes the average value of a time-series data over a specified duration in past. The duration is specified using another parameter in the value descriptor object related to this value      
          type: number      
          x-ngsi:      
            model: https://schema.org/Number      
            type: Property      
        instValue:      
          description: Describes the instantaneous value (associated with the current timestamp) of a time varying quantity      
          type: number      
          x-ngsi:      
            model: https://schema.org/Number      
            type: Property      
        maxOverTime:      
          description: Describes the maximum value of a time-series data over a specified duration in past. The duration is specified using another parameter in the value descriptor object related to this value      
          type: number      
          x-ngsi:      
            model: https://schema.org/Number      
            type: Property      
        minOverTime:      
          description: Describes the minimum value of a time-series data over a specified duration in past. The duration is specified using another parameter in the value descriptor object related to this value      
          type: number      
          x-ngsi:      
            model: https://schema.org/Number      
            type: Property      
      type: object      
      x-ngsi:      
        type: Property      
    compensatedTDS:      
      description: The value of TDS (Total Dissolved Solids) level in the water with temperature compensation      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
        type: Property      
    dataProvider:      
      description: A sequence of characters identifying the provider of the harmonised data entity      
      type: string      
      x-ngsi:      
        type: Property      
    dateCreated:      
      description: Entity creation timestamp. This will usually be allocated by the storage platform      
      format: date-time      
      type: string      
      x-ngsi:      
        type: Property      
    dateModified:      
      description: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform      
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
      description: Information about the device associated with the observations      
      properties:      
        deviceBatteryStatus:      
          description: 'Gives the Battery charging status of the reporting device(Connected, Disconnected)'      
          type: string      
          x-ngsi:      
            model: https://schema.org/Text      
            type: Property      
        deviceID:      
          description: Device ID of the physical sensor/ measurement station corresponding to this observation      
          type: string      
          x-ngsi:      
            model: https://schema.org/Text      
            type: Property      
        deviceModel:      
          description: 'Describes the information of the device, sensor or system in consideration'      
          properties:      
            brandName:      
              description: 'Name of the brand associated with an entity, e.g., sensor, device etc'      
              type: string      
              x-ngsi:      
                model: https://schema.org/Text      
                type: Property      
            manufacturerName:      
              description: 'Name of the manufacturer associated with an entity, e.g., sensor, device etc'      
              type: string      
              x-ngsi:      
                model: https://schema.org/Text      
                type: Property      
            modelName:      
              description: 'Name of a specific model associated with an entity, e.g., sensor, device etc'      
              type: string      
              x-ngsi:      
                model: https://schema.org/Text      
                type: Property      
            modelURL:      
              description: 'URL providing further information of a specific model associated with an entity, e.g., sensor, device etc'      
              type: string      
              x-ngsi:      
                model: https://schema.org/Text      
                type: Property      
          type: object      
          x-ngsi:      
            type: Property      
        deviceName:      
          description: Device Name or Station name of the sensor device/station corresponding to this observation      
          type: string      
          x-ngsi:      
            model: https://schema.org/Text      
            type: Property      
        deviceSimNumber:      
          description: Gives the sim number of the device in the waste management vehicle      
          type: string      
          x-ngsi:      
            model: https://schema.org/Text      
            type: Property      
        measurand:      
          description: Property/properties sensed/observed/measured by the device      
          type: string      
          x-ngsi:      
            model: https://schema.org/Text      
            type: Property      
        rfID:      
          description: Gives the ID of the RFID reader      
          type: string      
          x-ngsi:      
            model: https://schema.org/Text      
            type: Property      
      type: object      
      x-ngsi:      
        type: Property      
    flowrate:      
      description: Volume of water flowing in/out of the water storage tank corresponding to this observation      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
        type: Property      
    id:      
      anyOf:      
        - description: Identifier format of any NGSI entity      
          maxLength: 256      
          minLength: 1      
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$      
          type: string      
          x-ngsi:      
            type: Property      
        - description: Identifier format of any NGSI entity      
          format: uri      
          type: string      
          x-ngsi:      
            type: Property      
      description: Unique identifier of the entity      
      x-ngsi:      
        type: Property      
    location:      
      description: 'Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'      
      oneOf:      
        - description: Geojson reference to the item. Point      
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
          x-ngsi:      
            type: GeoProperty      
        - description: Geojson reference to the item. LineString      
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
          x-ngsi:      
            type: GeoProperty      
        - description: Geojson reference to the item. Polygon      
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
          x-ngsi:      
            type: GeoProperty      
        - description: Geojson reference to the item. MultiPoint      
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
          x-ngsi:      
            type: GeoProperty      
        - description: Geojson reference to the item. MultiLineString      
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
          x-ngsi:      
            type: GeoProperty      
        - description: Geojson reference to the item. MultiLineString      
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
      x-ngsi:      
        type: GeoProperty      
    name:      
      description: The name of this item      
      type: string      
      x-ngsi:      
        type: Property      
    observationDateTime:      
      description: Last reported time of observation      
      format: date-time      
      type: string      
      x-ngsi:      
        model: https://schema.org/Date-Time      
        type: Property      
    owner:      
      description: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)      
      items:      
        anyOf:      
          - description: Identifier format of any NGSI entity      
            maxLength: 256      
            minLength: 1      
            pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$      
            type: string      
            x-ngsi:      
              type: Property      
          - description: Identifier format of any NGSI entity      
            format: uri      
            type: string      
            x-ngsi:      
              type: Property      
        description: Unique identifier of the entity      
        x-ngsi:      
          type: Property      
      type: array      
      x-ngsi:      
        type: Property      
    pHTSA:      
      description: Acidity level or basicity level observed in the water      
      properties:      
        avgOverTime:      
          description: Describes the average value of a time-series data over a specified duration in past. The duration is specified using another parameter in the value descriptor object related to this value      
          type: number      
          x-ngsi:      
            model: https://schema.org/Number      
            type: Property      
        instValue:      
          description: Describes the instantaneous value (associated with the current timestamp) of a time varying quantity      
          type: number      
          x-ngsi:      
            model: https://schema.org/Number      
            type: Property      
        maxOverTime:      
          description: Describes the maximum value of a time-series data over a specified duration in past. The duration is specified using another parameter in the value descriptor object related to this value      
          type: number      
          x-ngsi:      
            model: https://schema.org/Number      
            type: Property      
        minOverTime:      
          description: Describes the minimum value of a time-series data over a specified duration in past. The duration is specified using another parameter in the value descriptor object related to this value      
          type: number      
          x-ngsi:      
            model: https://schema.org/Number      
            type: Property      
      type: object      
      x-ngsi:      
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
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object'      
      type: string      
      x-ngsi:      
        type: Property      
    tankBreadth:      
      description: Breadth of the Cuboid shaped water storage tank      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
        type: Property      
    tankCapacity:      
      description: Maximum amount of water the water storage tank corresponding to this observation can hold      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
        type: Property      
    tankDepth:      
      description: Depth of the water storage tank corresponding to this observation      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
        type: Property      
    tankDiameter:      
      description: Diameter of Cylindrical or Spherical water storage tanks      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
        type: Property      
    tankLength:      
      description: Length of the Cuboid shaped water storage tank      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
        type: Property      
    tankName:      
      description: Name of the water storage tank corresponding to this observation      
      type: string      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
    tankShape:      
      description: 'Physical shape of the water storage tank corresponding to this observation. ENUM: [Cylindrical, Conical, Cuboid, Spherical]'      
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
      description: Total MLDs of water discharged from the water storage tank corresponding to this observation      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
        type: Property      
    turbidityTSA:      
      description: Measurement of the amount of light that is scattered by material in the water when a light is shined through the water      
      properties:      
        avgOverTime:      
          description: Describes the average value of a time-series data over a specified duration in past. The duration is specified using another parameter in the value descriptor object related to this value      
          type: number      
          x-ngsi:      
            model: https://schema.org/Number      
            type: Property      
        instValue:      
          description: Describes the instantaneous value (associated with the current timestamp) of a time varying quantity      
          type: number      
          x-ngsi:      
            model: https://schema.org/Number      
            type: Property      
        maxOverTime:      
          description: Describes the maximum value of a time-series data over a specified duration in past. The duration is specified using another parameter in the value descriptor object related to this value      
          type: number      
          x-ngsi:      
            model: https://schema.org/Number      
            type: Property      
        minOverTime:      
          description: Describes the minimum value of a time-series data over a specified duration in past. The duration is specified using another parameter in the value descriptor object related to this value      
          type: number      
          x-ngsi:      
            model: https://schema.org/Number      
            type: Property      
      type: object      
      x-ngsi:      
        type: Property      
    uncompensatedTDS:      
      description: The value of TDS (Total Dissolved Solids) level in the water without temperature compensation      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
        type: Property      
    waterFlow:      
      description: Flow or current of water flowing from the water storage tank corresponding to this observation      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
        type: Property      
    waterLevel:      
      description: Current water level in the water storage tank corresponding to this observation      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
        type: Property      
    waterPressure:      
      description: Pressure of water flowing from the water storage tank corresponding to this observation      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
        type: Property      
    waterTemperature:      
      description: Water temperature in the water storage tank corresponding to this observation      
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
  "compensatedTDS": 25,  
  "uncompensatedTDS": 27  
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
    "type": "Number",  
    "value": 10  
  },  
  "totalML": {  
    "type": "Number",  
    "value": 250  
  },  
  "tankCapacity": {  
    "type": "Number",  
    "value": 500  
  },  
  "waterFlow": {  
    "type": "Number",  
    "value": 14  
  },  
  "tankBreadth": {  
    "type": "Number",  
    "value": 50  
  },  
  "tankDepth": {  
    "type": "Number",  
    "value": 200  
  },  
  "flowrate": {  
    "type": "Number",  
    "value": 70  
  },  
  "tankLength": {  
    "type": "Number",  
    "value": 300  
  },  
  "waterTemperature": {  
    "type": "Number",  
    "value": 20  
  },  
  "waterPressure": {  
    "type": "Number",  
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
    "type": "Number",  
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
    "type": "DateTime",  
    "value": "2021-03-11T15:51:02+05:30"  
  },  
  "compensatedTDS": {  
    "type": "Number",  
    "value": 25  
  },  
  "uncompensatedTDS": {  
    "type": "Number",  
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
  "compensatedTDS": 25,  
  "uncompensatedTDS": 27,  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.WaterDistribution/master/context.jsonld"  
  ]  
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
  },  
  "@context": [  
		"https://raw.githubusercontent.com/smart-data-models/dataModel.WaterDistribution/master/context.jsonld"  
	]  
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
