<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
엔티티: WaterDistributionNetwork  
=============================<!-- /10-Header -->  
<!-- 15-License -->  
[오픈 라이선스](https://github.com/smart-data-models//dataModel.WaterDistribution/blob/master/WaterDistributionNetwork/LICENSE.md)  
[문서 자동 생성](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
글로벌 설명: **도시 내 상수도망에 대한 데이터 모델**.  
버전: 0.0.2  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## 속성 목록  

<sup><sub>[*] 속성에 유형이 없는 것은 여러 유형 또는 다른 형식/패턴을 가질 수 있기 때문입니다</sub></sup>.  
- `address[object]`: 우편 주소  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: 국가. 예: 스페인  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)  
	- `addressLocality[string]`: 도로명 주소가 있는 지역 및 해당 지역 내 지역  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)  
	- `addressRegion[string]`: 해당 지역이 위치한 지역과 해당 국가의 지역  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)  
	- `district[string]`: 지구는 일부 국가에서는 지방 정부에서 관리하는 행정 구역의 일종입니다.    
	- `postOfficeBoxNumber[string]`: 사서함 주소의 우체국 사서함 번호입니다. 예: 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)  
	- `postalCode[string]`: 우편 번호입니다. 예: 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)  
	- `streetAddress[string]`: 거리 주소  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)  
	- `streetNr[string]`: 공공 도로의 특정 건물을 식별하는 번호    
- `alternateName[string]`: 이 항목의 대체 이름  - `areaServed[string]`: 서비스 또는 제공 품목이 제공되는 지리적 영역  . Model: [https://schema.org/Text](https://schema.org/Text)- `clTSA[object]`: 물 속의 염화물 농도  	- `avgOverTime[number]`: 과거 지정된 기간 동안의 시계열 데이터의 평균값을 설명합니다. 기간은 이 값과 관련된 값 설명자 객체의 다른 매개 변수를 사용하여 지정합니다.  . Model: [https://schema.org/Number](https://schema.org/Number)  
	- `instValue[number]`: 시간 변동 수량의 순간 값(현재 타임스탬프와 연관)을 설명합니다.  . Model: [https://schema.org/Number](https://schema.org/Number)  
	- `maxOverTime[number]`: 과거 지정된 기간 동안의 시계열 데이터의 최대값을 설명합니다. 기간은 이 값과 관련된 값 설명자 객체의 다른 매개 변수를 사용하여 지정됩니다.  . Model: [https://schema.org/Number](https://schema.org/Number)  
	- `minOverTime[number]`: 과거 지정된 기간 동안의 시계열 데이터의 최소값을 설명합니다. 기간은 이 값과 관련된 값 설명자 객체의 다른 매개 변수를 사용하여 지정됩니다.  . Model: [https://schema.org/Number](https://schema.org/Number)  
- `compensatedTDS[number]`: 온도 보정이 적용된 물의 총 용존 고형물(TDS) 수준 값입니다.  . Model: [https://schema.org/Number](https://schema.org/Number)- `dataProvider[string]`: 조화된 데이터 엔티티의 공급자를 식별하는 일련의 문자열입니다.  - `dateCreated[date-time]`: 엔티티 생성 타임스탬프. 이는 일반적으로 스토리지 플랫폼에서 할당합니다.  - `dateModified[date-time]`: 엔티티의 마지막 수정 타임스탬프입니다. 이는 일반적으로 스토리지 플랫폼에서 할당합니다.  - `description[string]`: 이 항목에 대한 설명  - `deviceInfo[object]`: 관찰과 관련된 장치에 대한 정보  	- `deviceBatteryStatus[string]`: 보고 디바이스의 배터리 충전 상태(연결됨, 연결 끊김)를 제공합니다.  . Model: [https://schema.org/Text](https://schema.org/Text)  
	- `deviceID[string]`: 이 관측에 해당하는 물리적 센서/측정 스테이션의 장치 ID  . Model: [https://schema.org/Text](https://schema.org/Text)  
	- `deviceModel[object]`: 고려 중인 장치, 센서 또는 시스템의 정보를 설명합니다.    
	- `deviceName[string]`: 이 관측에 해당하는 센서 디바이스/스테이션의 디바이스 이름 또는 스테이션 이름입니다.  . Model: [https://schema.org/Text](https://schema.org/Text)  
	- `deviceSimNumber[string]`: 폐기물 관리 차량에 있는 기기의 심 번호를 제공합니다.  . Model: [https://schema.org/Text](https://schema.org/Text)  
	- `measurand[string]`: 디바이스가 감지/관찰/측정하는 속성/특성  . Model: [https://schema.org/Text](https://schema.org/Text)  
	- `rfID[string]`: RFID 리더의 ID를 제공합니다.  . Model: [https://schema.org/Text](https://schema.org/Text)  
- `flowrate[number]`: 이 관측값에 해당하는 물 저장 탱크에 유입/유출되는 물의 양입니다.  . Model: [https://schema.org/Number](https://schema.org/Number)- `id[*]`: 엔티티의 고유 식별자  - `location[*]`: 항목에 대한 지오숀 참조입니다. 포인트, 라인 문자열, 다각형, 멀티포인트, 멀티라인 문자열 또는 멀티폴리곤일 수 있습니다.  - `name[string]`: 이 항목의 이름  - `observationDateTime[date-time]`: 마지막으로 보고된 관찰 시간  . Model: [https://schema.org/Date-Time](https://schema.org/Date-Time)- `owner[array]`: 소유자의 고유 ID를 참조하는 JSON 인코딩된 문자 시퀀스가 포함된 목록입니다.  - `pHTSA[object]`: 물에서 관찰되는 산도 또는 염기성 수준  	- `avgOverTime[number]`: 과거 지정된 기간 동안의 시계열 데이터의 평균값을 설명합니다. 기간은 이 값과 관련된 값 설명자 객체의 다른 매개 변수를 사용하여 지정합니다.  . Model: [https://schema.org/Number](https://schema.org/Number)  
	- `instValue[number]`: 시간 변동 수량의 순간 값(현재 타임스탬프와 연관)을 설명합니다.  . Model: [https://schema.org/Number](https://schema.org/Number)  
	- `maxOverTime[number]`: 과거 지정된 기간 동안의 시계열 데이터의 최대값을 설명합니다. 기간은 이 값과 관련된 값 설명자 객체의 다른 매개 변수를 사용하여 지정됩니다.  . Model: [https://schema.org/Number](https://schema.org/Number)  
	- `minOverTime[number]`: 과거 지정된 기간 동안의 시계열 데이터의 최소값을 설명합니다. 기간은 이 값과 관련된 값 설명자 객체의 다른 매개 변수를 사용하여 지정됩니다.  . Model: [https://schema.org/Number](https://schema.org/Number)  
- `seeAlso[*]`: 항목에 대한 추가 리소스를 가리키는 URL 목록  - `source[string]`: 엔티티 데이터의 원본 소스를 URL로 제공하는 일련의 문자입니다. 소스 공급자의 정규화된 도메인 이름 또는 소스 개체에 대한 URL을 사용하는 것이 좋습니다.  - `tankBreadth[number]`: 직육면체 모양의 물 저장 탱크의 폭  . Model: [https://schema.org/Number](https://schema.org/Number)- `tankCapacity[number]`: 이 관측치에 해당하는 물 저장 탱크가 저장할 수 있는 최대 물의 양은 다음과 같습니다.  . Model: [https://schema.org/Number](https://schema.org/Number)- `tankDepth[number]`: 이 관측에 해당하는 물 저장 탱크의 깊이  . Model: [https://schema.org/Number](https://schema.org/Number)- `tankDiameter[number]`: 원통형 또는 구형 물 저장 탱크의 직경  . Model: [https://schema.org/Number](https://schema.org/Number)- `tankLength[number]`: 직육면체 모양의 물 저장 탱크의 길이  . Model: [https://schema.org/Number](https://schema.org/Number)- `tankName[string]`: 이 관측에 해당하는 물 저장 탱크의 이름  . Model: [https://schema.org/Text](https://schema.org/Text)- `tankShape[string]`: 이 관측에 해당하는 물 저장 탱크의 물리적 모양입니다. ENUM: [원통형, 원뿔형, 직육면체, 구형]  . Model: [https://schema.org/Text](https://schema.org/Text)- `totalML[number]`: 이 관측에 해당하는 저수조에서 배출된 물의 총 MLD는 다음과 같습니다.  . Model: [https://schema.org/Number](https://schema.org/Number)- `turbidityTSA[object]`: 빛을 물속에 비췄을 때 물속의 물질에 의해 산란되는 빛의 양을 측정합니다.  	- `avgOverTime[number]`: 과거 지정된 기간 동안의 시계열 데이터의 평균값을 설명합니다. 기간은 이 값과 관련된 값 설명자 객체의 다른 매개 변수를 사용하여 지정합니다.  . Model: [https://schema.org/Number](https://schema.org/Number)  
	- `instValue[number]`: 시간 변동 수량의 순간 값(현재 타임스탬프와 연관)을 설명합니다.  . Model: [https://schema.org/Number](https://schema.org/Number)  
	- `maxOverTime[number]`: 과거 지정된 기간 동안의 시계열 데이터의 최대값을 설명합니다. 기간은 이 값과 관련된 값 설명자 객체의 다른 매개 변수를 사용하여 지정됩니다.  . Model: [https://schema.org/Number](https://schema.org/Number)  
	- `minOverTime[number]`: 과거 지정된 기간 동안의 시계열 데이터의 최소값을 설명합니다. 기간은 이 값과 관련된 값 설명자 객체의 다른 매개 변수를 사용하여 지정됩니다.  . Model: [https://schema.org/Number](https://schema.org/Number)  
- `type[string]`: NGSI 엔티티 유형. WaterDistributionNetwork여야 합니다.  - `uncompensatedTDS[number]`: 온도 보정 없이 물속의 총 용존 고형물(TDS) 수준 값  . Model: [https://schema.org/Number](https://schema.org/Number)- `waterFlow[number]`: 이 관측값에 해당하는 물 저장 탱크에서 흐르는 물의 유량 또는 전류입니다.  . Model: [https://schema.org/Number](https://schema.org/Number)- `waterLevel[number]`: 이 관측값에 해당하는 물 저장 탱크의 현재 수위  . Model: [https://schema.org/Number](https://schema.org/Number)- `waterPressure[number]`: 이 관측값에 해당하는 물 저장 탱크에서 흐르는 물의 압력  . Model: [https://schema.org/Number](https://schema.org/Number)- `waterTemperature[number]`: 이 관측값에 해당하는 물 저장 탱크의 물 온도  . Model: [https://schema.org/Number](https://schema.org/Number)<!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
필수 속성  
- `id`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## 속성에 대한 데이터 모델 설명  
알파벳순으로 정렬(자세한 내용을 보려면 클릭)  
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
    type:    
      description: NGSI Entity type. It has to be WaterDistributionNetwork    
      enum:    
        - WaterDistributionNetwork    
      type: string    
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
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2023 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.WaterDistribution/blob/master/WaterDistributionNetwork/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/SmartWater/WaterDistributionNetwork/schema.json    
  x-model-tags: ""    
  x-version: 0.0.2    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## 페이로드 예시  
#### WaterDistributionNetwork NGSI-v2 키 값 예시  
다음은 JSON-LD 형식의 WaterDistributionNetwork를 키 값으로 사용하는 예제입니다. 이는 `옵션=키값`을 사용할 때 NGSI-v2와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
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
#### WaterDistributionNetwork NGSI-v2 정규화 예제  
다음은 정규화된 JSON-LD 형식의 WaterDistributionNetwork의 예입니다. 이는 옵션을 사용하지 않을 때 NGSI-v2와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
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
#### WaterDistributionNetwork NGSI-LD 키 값 예시  
다음은 JSON-LD 형식의 WaterDistributionNetwork를 키 값으로 사용하는 예제입니다. 이는 `옵션=키값`을 사용할 때 NGSI-LD와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
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
#### WaterDistributionNetwork NGSI-LD 정규화 예시  
다음은 정규화된 JSON-LD 형식의 WaterDistributionNetwork의 예입니다. 이는 옵션을 사용하지 않을 때 NGSI-LD와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
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
크기 단위를 다루는 방법에 대한 답변은 [FAQ 10](https://smartdatamodels.org/index.php/faqs/)을 참조하세요.  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
