<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
Entità: Rete di distribuzione dell'acqua    
========================================<!-- /10-Header -->    
<!-- 15-License -->    
[Licenza aperta](https://github.com/smart-data-models//dataModel.WaterDistribution/blob/master/WaterDistributionNetwork/LICENSE.md)    
[documento generato automaticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
Descrizione globale: **Un modello di dati per la rete idrica di una città.**    
versione: 0.0.1    
<!-- /20-Description -->    
<!-- 30-PropertiesList -->    
## Elenco delle proprietà    
<sup><sub>[*] Se non c'è un tipo in un attributo è perché potrebbe avere diversi tipi o diversi formati/modelli</sub></sup>.    
- `address[object]`: L'indirizzo postale  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: Il paese. Ad esempio, la Spagna  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)    
	- `addressLocality[string]`: La località in cui si trova l'indirizzo civico e che si trova nella regione  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)    
	- `addressRegion[string]`: La regione in cui si trova la località, e che si trova nel paese  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)    
	- `district[string]`: Un distretto è un tipo di divisione amministrativa che, in alcuni paesi, è gestita dal governo locale.      
	- `postOfficeBoxNumber[string]`: Il numero di casella postale per gli indirizzi di casella postale. Ad esempio, 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)    
	- `postalCode[string]`: Il codice postale. Ad esempio, 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)    
	- `streetAddress[string]`: L'indirizzo stradale  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)    
- `alternateName[string]`: Un nome alternativo per questa voce  - `areaServed[string]`: L'area geografica in cui viene fornito il servizio o l'articolo offerto.  . Model: [https://schema.org/Text](https://schema.org/Text)- `clTSA[object]`: Concentrazione di cloruri nell'acqua  	- `avgOverTime[number]`: Descrive il valore medio di una serie temporale di dati per una durata specificata nel passato. La durata è specificata utilizzando un altro parametro nell'oggetto descrittore di valore relativo a questo valore.  . Model: [https://schema.org/Number](https://schema.org/Number)    
	- `instValue[number]`: Descrive il valore istantaneo (associato al timestamp corrente) di una quantità variabile nel tempo.  . Model: [https://schema.org/Number](https://schema.org/Number)    
	- `maxOverTime[number]`: Descrive il valore massimo di una serie temporale di dati per una durata specificata nel passato. La durata è specificata utilizzando un altro parametro nell'oggetto descrittore di valore relativo a questo valore.  . Model: [https://schema.org/Number](https://schema.org/Number)    
- `compensatedTDS[number]`: Il valore del livello di TDS (Solidi Disciolti Totali) nell'acqua con compensazione della temperatura  . Model: [https://schema.org/Number](https://schema.org/Number)- `dataProvider[string]`: una sequenza di caratteri che identifica il fornitore dell'entità di dati armonizzata  - `dateCreated[date-time]`: Timestamp di creazione dell'entità. Di solito viene assegnato dalla piattaforma di archiviazione  - `dateModified[date-time]`: Timestamp dell'ultima modifica dell'entità. Di solito viene assegnato dalla piattaforma di archiviazione  - `description[string]`: Descrizione dell'articolo  - `deviceInfo[object]`: Informazioni sul dispositivo associato alle osservazioni  	- `deviceBatteryStatus[string]`: Indica lo stato di carica della batteria del dispositivo segnalato (collegato, scollegato).  . Model: [https://schema.org/Text](https://schema.org/Text)    
	- `deviceID[string]`: ID dispositivo del sensore fisico/stazione di misura corrispondente a questa osservazione  . Model: [https://schema.org/Text](https://schema.org/Text)    
	- `deviceModel[object]`: Descrive le informazioni del dispositivo, del sensore o del sistema in esame.      
	- `deviceName[string]`: Nome del dispositivo o della stazione del dispositivo/stazione del sensore corrispondente a questa osservazione.  . Model: [https://schema.org/Text](https://schema.org/Text)    
	- `deviceSimNumber[string]`: Indica il numero di sim del dispositivo nel veicolo per la gestione dei rifiuti.  . Model: [https://schema.org/Text](https://schema.org/Text)    
	- `measurand[string]`: Proprietà/percezioni rilevate/osservate/misurate dal dispositivo  . Model: [https://schema.org/Text](https://schema.org/Text)    
- `flowrate[number]`: Volume d'acqua in entrata/uscita dal serbatoio corrispondente a questa osservazione  . Model: [https://schema.org/Number](https://schema.org/Number)- `id[*]`: Identificatore univoco dell'entità  - `location[*]`: Riferimento geojson all'elemento. Può essere un punto, una stringa di linea, un poligono, un multi-punto, una stringa di linea o un poligono multiplo.  - `name[string]`: Il nome di questo elemento  - `observationDateTime[date-time]`: Ultima ora di osservazione segnalata  . Model: [https://schema.org/Date-Time](https://schema.org/Date-Time)- `owner[array]`: Un elenco contenente una sequenza di caratteri codificata JSON che fa riferimento agli ID univoci dei proprietari.  - `pHTSA[object]`: Livello di acidità o basicità osservato nell'acqua  	- `avgOverTime[number]`: Descrive il valore medio di una serie temporale di dati per una durata specificata nel passato. La durata è specificata utilizzando un altro parametro nell'oggetto descrittore di valore relativo a questo valore.  . Model: [https://schema.org/Number](https://schema.org/Number)    
	- `instValue[number]`: Descrive il valore istantaneo (associato al timestamp corrente) di una quantità variabile nel tempo.  . Model: [https://schema.org/Number](https://schema.org/Number)    
	- `maxOverTime[number]`: Descrive il valore massimo di una serie temporale di dati per una durata specificata nel passato. La durata è specificata utilizzando un altro parametro nell'oggetto descrittore di valore relativo a questo valore.  . Model: [https://schema.org/Number](https://schema.org/Number)    
- `seeAlso[*]`: elenco di uri che puntano a risorse aggiuntive sull'elemento  - `source[string]`: Una sequenza di caratteri che indica la fonte originale dei dati dell'entità come URL. Si consiglia di utilizzare il nome di dominio completamente qualificato del provider di origine o l'URL dell'oggetto di origine.  - `tankBreadth[number]`: Larghezza del serbatoio di stoccaggio dell'acqua a forma cuboidale  . Model: [https://schema.org/Number](https://schema.org/Number)- `tankCapacity[number]`: Quantità massima di acqua che il serbatoio corrispondente a questa osservazione può contenere  . Model: [https://schema.org/Number](https://schema.org/Number)- `tankDepth[number]`: Profondità del serbatoio di stoccaggio dell'acqua corrispondente a questa osservazione  . Model: [https://schema.org/Number](https://schema.org/Number)- `tankDiameter[number]`: Diametro dei serbatoi di stoccaggio dell'acqua cilindrici o sferici  . Model: [https://schema.org/Number](https://schema.org/Number)- `tankLength[number]`: Lunghezza del serbatoio di stoccaggio dell'acqua a forma di cuboide  . Model: [https://schema.org/Number](https://schema.org/Number)- `tankName[string]`: Nome del serbatoio di stoccaggio dell'acqua corrispondente a questa osservazione  . Model: [https://schema.org/Text](https://schema.org/Text)- `tankShape[string]`: Forma fisica del serbatoio di stoccaggio dell'acqua corrispondente a questa osservazione. ENUM: [Cilindrico, Conico, Cuboide, Sferico].  . Model: [https://schema.org/Text](https://schema.org/Text)- `totalML[number]`: MLD totali di acqua scaricati dal serbatoio di accumulo corrispondenti a questa osservazione  . Model: [https://schema.org/Number](https://schema.org/Number)- `turbidityTSA[object]`: Misura della quantità di luce che viene diffusa dal materiale presente nell'acqua quando una luce viene fatta passare attraverso l'acqua.  	- `avgOverTime[number]`: Descrive il valore medio di una serie temporale di dati per una durata specificata nel passato. La durata è specificata utilizzando un altro parametro nell'oggetto descrittore di valore relativo a questo valore.  . Model: [https://schema.org/Number](https://schema.org/Number)    
	- `instValue[number]`: Descrive il valore istantaneo (associato al timestamp corrente) di una quantità variabile nel tempo.  . Model: [https://schema.org/Number](https://schema.org/Number)    
	- `maxOverTime[number]`: Descrive il valore massimo di una serie temporale di dati per una durata specificata nel passato. La durata è specificata utilizzando un altro parametro nell'oggetto descrittore di valore relativo a questo valore.  . Model: [https://schema.org/Number](https://schema.org/Number)    
- `uncompensatedTDS[number]`: Il valore del livello di TDS (Solidi totali disciolti) nell'acqua senza compensazione della temperatura.  . Model: [https://schema.org/Number](https://schema.org/Number)- `waterFlow[number]`: Flusso o corrente dell'acqua che scorre dal serbatoio di accumulo corrispondente a questa osservazione  . Model: [https://schema.org/Number](https://schema.org/Number)- `waterLevel[number]`: Livello attuale dell'acqua nel serbatoio corrispondente a questa osservazione  . Model: [https://schema.org/Number](https://schema.org/Number)- `waterPressure[number]`: Pressione dell'acqua che scorre dal serbatoio corrispondente a questa osservazione  . Model: [https://schema.org/Number](https://schema.org/Number)- `waterTemperature[number]`: Temperatura dell'acqua nell'accumulatore corrispondente a questa osservazione  . Model: [https://schema.org/Number](https://schema.org/Number)<!-- /30-PropertiesList -->    
<!-- 35-RequiredProperties -->    
Proprietà richieste    
- `id`  - `type`  <!-- /35-RequiredProperties -->    
<!-- 40-RequiredProperties -->    
<!-- /40-RequiredProperties -->    
<!-- 50-DataModelHeader -->    
## Modello di dati descrizione delle proprietà    
Ordinati in ordine alfabetico (clicca per i dettagli)    
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
## Esempi di payload    
#### WaterDistributionNetwork Valori-chiave NGSI-v2 Esempio    
Ecco un esempio di WaterDistributionNetwork in formato JSON-LD come valori-chiave. Questo è compatibile con NGSI-v2 quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.    
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
#### WaterDistributionNetwork NGSI-v2 normalizzato Esempio    
Ecco un esempio di WaterDistributionNetwork in formato JSON-LD normalizzato. Questo è compatibile con NGSI-v2 quando non si utilizzano opzioni e restituisce i dati di contesto di una singola entità.    
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
#### WaterDistributionNetwork Valori-chiave NGSI-LD Esempio    
Ecco un esempio di WaterDistributionNetwork in formato JSON-LD come valori-chiave. Questo è compatibile con NGSI-LD quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.    
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
#### WaterDistributionNetwork NGSI-LD normalizzato Esempio    
Ecco un esempio di WaterDistributionNetwork in formato JSON-LD normalizzato. Questo è compatibile con NGSI-LD quando non si utilizzano opzioni e restituisce i dati di contesto di una singola entità.    
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
Vedere [FAQ 10](https://smartdatamodels.org/index.php/faqs/) per ottenere una risposta su come gestire le unità di grandezza.    
<!-- /95-Units -->    
<!-- 97-LastFooter -->    
---    
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->    
