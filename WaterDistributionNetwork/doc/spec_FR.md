<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entité : WaterDistributionNetwork  
=================================<!-- /10-Header -->  
<!-- 15-License -->  
[Licence ouverte] (https://github.com/smart-data-models//dataModel.WaterDistribution/blob/master/WaterDistributionNetwork/LICENSE.md)  
[document généré automatiquement] (https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Description globale : **Modèle de données pour le réseau d'approvisionnement en eau d'une ville.**  
version : 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## Liste des propriétés  

<sup><sub>[*] S'il n'y a pas de type dans un attribut, c'est parce qu'il pourrait avoir plusieurs types ou différents formats/modèles</sub></sup>.  
- `address[object]`: L'adresse postale  . Model: [https://schema.org/address](https://schema.org/address)- `alternateName[string]`: Un nom alternatif pour cet élément  - `areaServed[string]`: La zone géographique où un service ou un article offert est fourni  . Model: [https://schema.org/Text](https://schema.org/Text)- `clTSA[object]`: Concentration de chlorures dans l'eau.  . Model: [https://schema.org/Text](https://schema.org/Text)- `compensatedTDS[number]`: La valeur du niveau de TDS (Total Dissolved Solids) dans l'eau avec compensation de la température.  . Model: [https://schema.org/Number](https://schema.org/Number)- `dataProvider[string]`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées.  - `dateCreated[string]`: Horodatage de la création de l'entité. Celui-ci sera généralement attribué par la plateforme de stockage.  - `dateModified[string]`: Horodatage de la dernière modification de l'entité. Il sera généralement attribué par la plateforme de stockage.  - `description[string]`: Une description de cet article  - `deviceInfo[object]`: Informations sur le dispositif associé aux observations.  . Model: [https://schema.org/Text](https://schema.org/Text)- `flowrate[number]`: Volume d'eau entrant/sortant du réservoir de stockage d'eau correspondant à cette observation.  . Model: [https://schema.org/Number](https://schema.org/Number)- `id[*]`: Identifiant unique de l'entité  - `location[*]`: Référence Geojson à l'élément. Il peut s'agir d'un point, d'une ligne, d'un polygone, d'un point multiple, d'une ligne multiple ou d'un polygone multiple.  - `name[string]`: Le nom de cet élément.  - `observationDateTime[string]`: Dernière heure d'observation signalée.  . Model: [https://schema.org/Text](https://schema.org/Text)- `owner[array]`: Une liste contenant une séquence de caractères codée en JSON référençant les identifiants uniques du ou des propriétaires.  - `pHTSA[object]`: Niveau d'acidité ou de basicité observé dans l'eau.  . Model: [https://schema.org/Text](https://schema.org/Text)- `seeAlso[*]`: liste d'uri pointant vers des ressources supplémentaires sur l'article  - `source[string]`: Une séquence de caractères donnant la source originale des données de l'entité sous forme d'URL. Il est recommandé d'utiliser le nom de domaine entièrement qualifié du fournisseur source ou l'URL de l'objet source.  - `tankBreadth[number]`: Largeur du réservoir de stockage d'eau de forme cubique.  . Model: [https://schema.org/Number](https://schema.org/Number)- `tankCapacity[number]`: Quantité maximale d'eau que peut contenir le réservoir de stockage d'eau correspondant à cette observation.  . Model: [https://schema.org/Number](https://schema.org/Number)- `tankDepth[number]`: Profondeur du réservoir d'eau correspondant à cette observation.  . Model: [https://schema.org/Number](https://schema.org/Number)- `tankDiameter[number]`: Diamètre des réservoirs de stockage d'eau cylindriques ou sphériques.  . Model: [https://schema.org/Number](https://schema.org/Number)- `tankLength[number]`: Longueur du réservoir de stockage d'eau de forme cubique.  . Model: [https://schema.org/Number](https://schema.org/Number)- `tankName[string]`: Nom du réservoir de stockage d'eau correspondant à cette observation.  . Model: [https://schema.org/Text](https://schema.org/Text)- `tankShape[string]`: Forme physique du réservoir de stockage d'eau correspondant à cette observation. ENUM : [Cylindrique, Conique, Cuboïde, Sphérique].  . Model: [https://schema.org/Text](https://schema.org/Text)- `totalML[number]`: Total des MLD d'eau déversés du réservoir de stockage d'eau correspondant à cette observation.  . Model: [https://schema.org/Number](https://schema.org/Number)- `turbidityTSA[object]`: Mesure de la quantité de lumière qui est diffusée par les matériaux présents dans l'eau lorsqu'une lumière traverse l'eau.  . Model: [https://schema.org/Text](https://schema.org/Text)- `uncompensatedTDS[number]`: La valeur du niveau de TDS (Total Dissolved Solids) dans l'eau sans compensation de température.  . Model: [https://schema.org/Number](https://schema.org/Number)- `waterFlow[number]`: Débit ou courant d'eau s'écoulant du réservoir de stockage d'eau correspondant à cette observation.  . Model: [https://schema.org/Number](https://schema.org/Number)- `waterLevel[number]`: Niveau d'eau actuel dans le réservoir de stockage d'eau correspondant à cette observation.  . Model: [https://schema.org/Number](https://schema.org/Number)- `waterPressure[number]`: Pression de l'eau s'écoulant du réservoir de stockage de l'eau correspondant à cette observation.  . Model: [https://schema.org/Number](https://schema.org/Number)- `waterTemperature[number]`: Température de l'eau dans le réservoir de stockage de l'eau correspondant à cette observation.  . Model: [https://schema.org/Number](https://schema.org/Number)<!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Propriétés requises  
- `id`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## Description des propriétés du modèle de données  
Classés par ordre alphabétique (cliquez pour plus de détails)  
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
      description: Concentration of chlorides in the water.    
      properties:    
        avgOverTime:    
          description: 'Property. Model:''https://schema.org/Text. Describes the average value of a time-series data over a specified duration in past. The duration is specified using another parameter in the value descriptor object related to this value'    
          type: number    
        instValue:    
          description: 'Property. Model:''https://schema.org/Text.Describes the instantaneous value (associated with the current timestamp) of a time varying quantity.'    
          type: number    
        maxOverTime:    
          description: 'Property. Model:''https://schema.org/Text.Describes the maximum value of a time-series data over a specified duration in past. The duration is specified using another parameter in the value descriptor object related to this value'    
          type: number    
        minOverTime:    
          description: 'Property. Model:''https://schema.org/Text. Describes the minimum value of a time-series data over a specified duration in past. The duration is specified using another parameter in the value descriptor object related to this value'    
          type: number    
      type: object    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    compensatedTDS:    
      description: The value of TDS (Total Dissolved Solids) level in the water with temperature compensation.    
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
      description: Information about the device associated with the observations.    
      properties:    
        deviceBatteryStatus:    
          description: 'Property. Model:''https://schema.org/Text.Gives the Battery charging status of the reporting device(Connected, Disconnected).'    
          type: string    
        deviceID:    
          description: 'Property. Model:''https://schema.org/Text. Device ID of the physical sensor/ measurement station corresponding to this observation.'    
          type: string    
        deviceModel:    
          description: 'Property. Model:''https://schema.org/Text. Describes the information of the device, sensor or system in consideration.'    
          properties:    
            brandName:    
              description: 'Property. Model:''https://schema.org/Text.	Name of the brand associated with an entity, e.g., sensor, device etc.'    
              type: string    
            manufacturerName:    
              description: 'Property. Model:''https://schema.org/Text.	Name of the manufacturer associated with an entity, e.g., sensor, device etc.'    
              type: string    
            modelName:    
              description: 'Property. Model:''https://schema.org/Text.	Name of a specific model associated with an entity, e.g., sensor, device etc.'    
              type: string    
            modelURL:    
              description: 'Property. Model:''https://schema.org/Text.	URL providing further information of a specific model associated with an entity, e.g., sensor, device etc.'    
              type: string    
          type: object    
        deviceName:    
          description: 'Property. Model:''https://schema.org/Text.Device Name or Station name of the sensor device/station corresponding to this observation.'    
          type: string    
        deviceSimNumber:    
          description: 'Property. Model:''https://schema.org/Text. Gives the sim number of the device in the waste management vehicle.'    
          type: string    
        measurand:    
          description: 'Property. Model:''https://schema.org/Text. Property/properties sensed/observed/measured by the device.'    
          type: string    
        rfID:    
          description: 'Property. Model:''https://schema.org/Text.Gives the ID of the RFID reader.'    
          type: string    
      type: object    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    flowrate:    
      description: Volume of water flowing in/out of the water storage tank corresponding to this observation.    
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
        - description: Geoproperty. Geojson reference to the item. Point    
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
        - description: Geoproperty. Geojson reference to the item. LineString    
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
        - description: Geoproperty. Geojson reference to the item. Polygon    
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
        - description: Geoproperty. Geojson reference to the item. MultiPoint    
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
        - description: Geoproperty. Geojson reference to the item. MultiLineString    
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
        - description: Geoproperty. Geojson reference to the item. MultiLineString    
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
        type: Geoproperty    
    name:    
      description: The name of this item.    
      type: string    
      x-ngsi:    
        type: Property    
    observationDateTime:    
      description: Last reported time of observation.    
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
      description: Acidity level or basicity level obsevered in the water.    
      properties:    
        avgOverTime:    
          description: 'Property. Model:''https://schema.org/Text. Describes the average value of a time-series data over a specified duration in past. The duration is specified using another parameter in the value descriptor object related to this value'    
          type: number    
        instValue:    
          description: 'Property. Model:''https://schema.org/Text.Describes the instantaneous value (associated with the current timestamp) of a time varying quantity.'    
          type: number    
        maxOverTime:    
          description: 'Property. Model:''https://schema.org/Text.Describes the maximum value of a time-series data over a specified duration in past. The duration is specified using another parameter in the value descriptor object related to this value'    
          type: number    
        minOverTime:    
          description: 'Property. Model:''https://schema.org/Text. Describes the minimum value of a time-series data over a specified duration in past. The duration is specified using another parameter in the value descriptor object related to this value'    
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
      description: Breadth of the Cuboid shaped water storage tank.    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tankCapacity:    
      description: Maximum amount of water the water storage tank corresponding to this observation can hold.    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tankDepth:    
      description: Depth of the water storage tank corresponding to this observation.    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tankDiameter:    
      description: Diameter of Cylindrical or Spherical water storage tanks.    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tankLength:    
      description: Length of the Cuboid shaped water storage tank.    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tankName:    
      description: Name of the water storage tank corresponding to this observation.    
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
      description: Total MLDs of water discharged from the water storage tank corresponding to this observation.    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    turbidityTSA:    
      description: Measurement of the amount of light that is scattered by material in the water when a light is shined through the water.    
      properties:    
        avgOverTime:    
          description: 'Property. Model:''https://schema.org/Text. Describes the average value of a time-series data over a specified duration in past. The duration is specified using another parameter in the value descriptor object related to this value'    
          type: number    
        instValue:    
          description: 'Property. Model:''https://schema.org/Text.Describes the instantaneous value (associated with the current timestamp) of a time varying quantity.'    
          type: number    
        maxOverTime:    
          description: 'Property. Model:''https://schema.org/Text.Describes the maximum value of a time-series data over a specified duration in past. The duration is specified using another parameter in the value descriptor object related to this value'    
          type: number    
        minOverTime:    
          description: 'Property. Model:''https://schema.org/Text. Describes the minimum value of a time-series data over a specified duration in past. The duration is specified using another parameter in the value descriptor object related to this value'    
          type: number    
      type: object    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    uncompensatedTDS:    
      description: The value of TDS (Total Dissolved Solids) level in the water without temperature compensation.    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    waterFlow:    
      description: Flow or current of water flowing from the water storage tank corresponding to this observation.    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    waterLevel:    
      description: Current water level in the water storage tank corresponding to this observation.    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    waterPressure:    
      description: Pressure of water flowing from the water storage tank corresponding to this observation.    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    waterTemperature:    
      description: Water temperature in the water storage tank corresponding to this observation.    
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
## Exemples de charges utiles  
#### WaterDistributionNetwork Valeurs-clés NGSI-v2 Exemple  
Voici un exemple de WaterDistributionNetwork au format JSON-LD sous forme de valeurs-clés. Ceci est compatible avec NGSI-v2 lorsque l'on utilise `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
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
#### Réseau de distribution d'eau NGSI-v2 normalisé Exemple  
Voici un exemple d'un WaterDistributionNetwork au format JSON-LD tel que normalisé. Ce format est compatible avec la NGSI-v2 lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
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
#### WaterDistributionNetwork Valeurs-clés NGSI-LD Exemple  
Voici un exemple de WaterDistributionNetwork au format JSON-LD sous forme de valeurs-clés. Ceci est compatible avec NGSI-LD quand on utilise `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
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
#### Réseau de distribution d'eau NGSI-LD normalisé Exemple  
Voici un exemple d'un WaterDistributionNetwork au format JSON-LD tel que normalisé. Ce format est compatible avec NGSI-LD lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
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
Voir [FAQ 10](https://smartdatamodels.org/index.php/faqs/) pour obtenir une réponse sur la façon de traiter les unités de magnitude.  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
