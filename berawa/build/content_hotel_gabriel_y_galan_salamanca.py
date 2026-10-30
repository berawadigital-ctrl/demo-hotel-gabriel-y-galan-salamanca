# Contenido de la demo Hotel Gabriel y Galán (Salamanca) (es/en/fr/de). Hechos de hotelgabrielygalan.com leidos el 30/10/2026 (ver berawa/sources.json). Lo no publicado no se afirma; sin valoraciones ni opiniones de clientes.
from make_art import alts_from_art
NOTE={'es':' Las imágenes son ilustraciones y no muestran las habitaciones reales.','en':' Images are illustrations and do not show the actual rooms.','fr':' Les images sont des illustrations et ne montrent pas les chambres réelles.','de':' Die Bilder sind Illustrationen und zeigen nicht die tatsächlichen Zimmer.'}
H={'es':['Habitación individual','Doble y matrimonio'],'en':['Single room','Twin and double'],'fr':['Chambre individuelle','Twin et double'],'de':['Einzelzimmer','Zweibett- und Doppelzimmer']}
RD={
'es':['Para 1 persona, con cama individual. Ideal para viajes de trabajo o estancias en solitario.','Doble con 2 camas individuales (máximo 2 personas) o de matrimonio con cama doble. Baño privado, TV, wifi, calefacción y aire acondicionado.'],
'en':['For 1 person, with a single bed. Ideal for business trips or solo stays.','Twin with 2 single beds (up to 2 people) or double with a double bed. Private bathroom, TV, wifi, heating and air conditioning.'],
'fr':['Pour 1 personne, avec lit simple. Idéale pour les voyages d’affaires ou les séjours en solo.','Twin avec 2 lits simples (2 personnes maximum) ou double avec grand lit. Salle de bain privée, TV, wifi, chauffage et climatisation.'],
'de':['Für 1 Person mit Einzelbett. Ideal für Geschäftsreisen oder Alleinreisende.','Zweibettzimmer mit 2 Einzelbetten (höchstens 2 Personen) oder Doppelzimmer mit Doppelbett. Eigenes Bad, TV, WLAN, Heizung und Klimaanlage.']}
ART={
'hero':('arches',9701,['#2a2233','#d9a05e','#f0cd95','#6a4a2a','#523820','#2e1f12']),
'intro':('columns',9702,['#f0ebe2','#f9f5ee','#6a4a2a','#523820','#2e1f12']),
'r1':('skyline',9711,['#e9ebef','#dca46a','#f1d1a1','#3f3552','#302841','#1c1726']),
'r2':('arches',9712,['#ede4d6','#d39a5d','#3f3552','#2a2233','#16121b']),
'g1':('columns',9721,['#ece6dc','#f6f0e6','#8a5a2e','#6a4422','#3b2613']),
'g2':('skyline',9722,['#2a2233','#dca262','#f1cf9a','#5a4060','#46324b','#29202c']),
'g3':('hills',9723,['#ecebe2','#efe1c4','#d69d62','#b0a27a','#857853','#5b5238']),
'g4':('arches',9724,['#e9ddca','#cf955a','#6a4a2a','#2a2233','#16121b'])}
IMGS=dict(hero='hero',intro='intro',rooms=['r1','r2'],gallery=['g1','g2','g3','g4'])
ALTS=alts_from_art(ART)
T={
'es':dict(title='Hotel Gabriel y Galán · Hotel urbano en el centro de Salamanca',see_rooms='Ver las habitaciones',hero_k='Salamanca · Plaza Gabriel y Galán',hero_t='Tu comodidad es nuestra prioridad',hero_s='Habitaciones cómodas y funcionales en pleno centro de Salamanca, para ocio, pareja o trabajo.',
 intro_t='Salamanca, a un paso',intro_p1='28 habitaciones recientemente reformadas, con materiales de calidad y una decoración sencilla, en el corazón de la ciudad: cada rincón se descubre caminando.',
 intro_p2='Recepción personalizada de 09:00 a 22:00, wifi gratis las 24 horas, consigna de equipaje el último día y vado en la puerta para descargar la maleta.',
 stats=['28 habitaciones','Recepción 09:00–22:00','Wifi gratis 24 h','3 parkings a 50 m'],nav_rooms='Habitaciones',rooms_t='Nuestras habitaciones',rooms_s='Individual, doble con 2 camas y de matrimonio.',
 svcs=['Wifi gratis 24 h','Aire acondicionado','Calefacción','Cunas gratuitas bajo petición','Consigna de equipajes','Información turística'],
 around_s='En pleno centro de Salamanca; tres parkings a menos de 50 metros y zona de carga y descarga en la puerta.',
 loc_p='Plaza Gabriel y Galán 3 · 37005 Salamanca. Check-in de 14:00 a 22:00 y check-out antes de las 12:00.',
 chips=['¿Qué habitaciones tenéis?','¿A qué hora es el check-in?','¿Hay parking?','¿Cómo reservo?']),
'en':dict(title='Hotel Gabriel y Galán · City hotel in central Salamanca',see_rooms='See the rooms',hero_k='Salamanca · Plaza Gabriel y Galán',hero_t='Your comfort is our priority',hero_s='Comfortable, practical rooms right in the centre of Salamanca, for leisure, couples or work.',
 intro_t='Salamanca, one step away',intro_p1='28 recently renovated rooms with quality materials and simple decor, in the heart of the city: every corner can be discovered on foot.',
 intro_p2='Personal reception from 09:00 to 22:00, free wifi 24 hours, luggage storage on your last day and a loading bay at the door for your suitcase.',
 stats=['28 rooms','Reception 09:00–22:00','Free wifi 24 h','3 car parks within 50 m'],nav_rooms='Rooms',rooms_t='Our rooms',rooms_s='Single, twin with 2 beds and double.',
 svcs=['Free wifi 24 h','Air conditioning','Heating','Free cots on request','Luggage storage','Tourist information'],
 around_s='Right in the centre of Salamanca; three car parks less than 50 metres away and a loading area at the door.',
 loc_p='Plaza Gabriel y Galán 3 · 37005 Salamanca. Check-in from 14:00 to 22:00 and check-out before 12:00.',
 chips=['Which rooms do you have?','What time is check-in?','Is there parking?','How do I book?']),
'fr':dict(title='Hotel Gabriel y Galán · Hôtel urbain au centre de Salamanque',see_rooms='Voir les chambres',hero_k='Salamanque · Plaza Gabriel y Galán',hero_t='Votre confort est notre priorité',hero_s='Des chambres confortables et pratiques en plein centre de Salamanque, pour les loisirs, en couple ou pour le travail.',
 intro_t='Salamanque, à deux pas',intro_p1='28 chambres récemment rénovées, avec des matériaux de qualité et une décoration simple, au cœur de la ville : tout se découvre à pied.',
 intro_p2='Réception personnalisée de 09:00 à 22:00, wifi gratuit 24 h/24, consigne à bagages le dernier jour et arrêt minute devant la porte pour décharger.',
 stats=['28 chambres','Réception 09:00–22:00','Wifi gratuit 24 h','3 parkings à 50 m'],nav_rooms='Chambres',rooms_t='Nos chambres',rooms_s='Individuelle, twin à 2 lits et double.',
 svcs=['Wifi gratuit 24 h','Climatisation','Chauffage','Lits bébé gratuits sur demande','Consigne à bagages','Information touristique'],
 around_s='En plein centre de Salamanque ; trois parkings à moins de 50 mètres et zone de déchargement devant la porte.',
 loc_p='Plaza Gabriel y Galán 3 · 37005 Salamanque. Arrivée de 14:00 à 22:00 et départ avant 12:00.',
 chips=['Quelles chambres avez-vous ?','À quelle heure est le check-in ?','Y a-t-il un parking ?','Comment réserver ?']),
'de':dict(title='Hotel Gabriel y Galán · Stadthotel im Zentrum von Salamanca',see_rooms='Zimmer ansehen',hero_k='Salamanca · Plaza Gabriel y Galán',hero_t='Ihr Komfort ist unsere Priorität',hero_s='Bequeme, praktische Zimmer mitten in Salamanca – für Freizeit, Paare oder Geschäftsreisen.',
 intro_t='Salamanca direkt vor der Tür',intro_p1='28 kürzlich renovierte Zimmer mit hochwertigen Materialien und schlichter Einrichtung im Herzen der Stadt: Alles lässt sich zu Fuß entdecken.',
 intro_p2='Persönliche Rezeption von 09:00 bis 22:00 Uhr, kostenloses WLAN rund um die Uhr, Gepäckaufbewahrung am Abreisetag und Ladezone vor der Tür.',
 stats=['28 Zimmer','Rezeption 09:00–22:00','WLAN gratis 24 h','3 Parkhäuser in 50 m'],nav_rooms='Zimmer',rooms_t='Unsere Zimmer',rooms_s='Einzel-, Zweibett- und Doppelzimmer.',
 svcs=['WLAN gratis 24 h','Klimaanlage','Heizung','Kostenlose Kinderbetten auf Anfrage','Gepäckaufbewahrung','Touristeninformation'],
 around_s='Mitten im Zentrum von Salamanca; drei Parkhäuser weniger als 50 Meter entfernt und Ladezone vor der Tür.',
 loc_p='Plaza Gabriel y Galán 3 · 37005 Salamanca. Check-in von 14:00 bis 22:00 Uhr, Check-out vor 12:00 Uhr.',
 chips=['Welche Zimmer gibt es?','Wann ist der Check-in?','Gibt es einen Parkplatz?','Wie kann ich buchen?'])}
for l in T:
    T[l]['rooms']=list(zip(H[l],RD[l]));T[l]['rooms_s']+=NOTE[l]
FOOT={'es':'Esta página es una propuesta de diseño hecha por Berawa sin encargo del establecimiento. Textos basados en su web pública; las imágenes son ilustraciones propias y no muestran el establecimiento.',
'en':'This page is a design proposal made by Berawa without any commission from the business. Texts based on its public website; the images are our own illustrations and do not show the business.',
'fr':"Cette page est une proposition de design réalisée par Berawa sans commande de l'établissement. Textes basés sur son site public ; les images sont des illustrations propres et ne montrent pas l'établissement.",
'de':'Diese Seite ist ein Designvorschlag von Berawa, ohne Auftrag der Unterkunft erstellt. Die Texte beruhen auf deren öffentlicher Website; die Bilder sind eigene Illustrationen und zeigen die Unterkunft nicht.'}
RB='https://hotelgabrielygalan.com/reservas/'
BOOK=dict(mode='engine',url={l:RB for l in ('es','en','fr','de')})
D=dict(name='Hotel Gabriel y Galán',ac='#2a2233',ac2='#6a4a2a',ac2_a11y='#523820',book=BOOK,around=['Plaza Mayor de Salamanca','Casco histórico'],foot=FOOT,
 address='Plaza Gabriel y Galán 3 · 37005 Salamanca',phones=['923 671 155','642 513 046'],emails=['reservas@hotelgabrielygalan.com'],maps='Hotel Gabriel y Galán, Plaza Gabriel y Galán 3, 37005 Salamanca',t=T)
META=dict(repo='demo-hotel-gabriel-y-galan-salamanca',name='Hotel Gabriel y Galán',legal_name='AFI HOTELES S.L.',registry_ids=['B70960943'],
 url='https://hotelgabrielygalan.com/',domain='hotelgabrielygalan.com',municipality='Salamanca',province='Salamanca',sector='hotel urbano de 28 habitaciones en el centro de Salamanca',
 read_at='2026-10-30T09:11:00+01:00',created_at='2026-10-30T09:10:00+01:00',built_at='2026-10-30T09:25:00+01:00',audit_date='2026-10-30T09:06:08+01:00',
 rating=dict(value=4.4,coincide=['telefono','web'],date='2026-10-29T12:59:41+01:00',url='https://www.google.com/maps/place/HOTEL+GABRIEL+Y+GALAN/@40.9701976,-5.662083,17z/data=!4m9!3m8!1s0xd3f276698bb102d:0xabc72a5d325e9422!5m2!4m1!1i2!8m2!3d40.9701976!4d-5.662083!16s%2Fg%2F11vz7czy9q'),
 book=dict(mode='engine',url=RB,note='motor de reservas real de su web (página /reservas/ con el motor embebido «Disponibilidad y reservas»), HTTP 200 comprobado el 30/10/2026; su web solo está en español, mismo enlace en los 4 idiomas.'),first_of_type='no aplica: alojamiento con precedente en demos anteriores')
QS={
'es':[('¿Qué habitaciones tenéis?','K01'),('¿A qué hora es el check-in?','K02'),('¿Hay parking?','K03'),('¿Hay wifi?','K04'),('¿Tenéis cuna para el bebé?','K05'),('¿Puedo dejar las maletas?','K06'),('¿Dónde está el hotel?','K07'),('¿Cómo reservo?','K08'),('¿Podéis confirmarme disponibilidad para mañana?','K08'),('¿Qué tarjetas aceptáis?','K09'),('¿Trabajáis con empresas?','K10'),('¿Tenéis piscina?',None),('¿Hay gimnasio?',None)],
'en':[('Which rooms do you have?','K01'),('What time is check-in?','K02'),('Is there parking?','K03'),('Is there wifi?','K04'),('Do you have a cot for the baby?','K05'),('Can I leave my luggage?','K06'),('Where is the hotel?','K07'),('How do I book?','K08'),('Can you confirm availability for tomorrow?','K08'),('Which cards do you accept?','K09'),('Do you have rates for companies?','K10'),('Do you have a swimming pool?',None),('Is there a gym?',None)],
'fr':[('Quelles chambres avez-vous ?','K01'),('À quelle heure est le check-in ?','K02'),('Y a-t-il un parking ?','K03'),('Y a-t-il le wifi ?','K04'),('Avez-vous un lit bébé ?','K05'),('Puis-je laisser mes bagages ?','K06'),("Où se trouve l'hôtel ?",'K07'),('Comment réserver ?','K08'),('Pouvez-vous me confirmer la disponibilité pour demain ?','K08'),('Quelles cartes acceptez-vous ?','K09'),('Avez-vous des offres pour les entreprises ?','K10'),('Avez-vous une piscine ?',None),('Y a-t-il une salle de sport ?',None)],
'de':[('Welche Zimmer gibt es?','K01'),('Wann ist der Check-in?','K02'),('Gibt es einen Parkplatz?','K03'),('Gibt es WLAN?','K04'),('Haben Sie ein Kinderbett?','K05'),('Kann ich mein Gepäck abgeben?','K06'),('Wo liegt das Hotel?','K07'),('Wie kann ich buchen?','K08'),('Können Sie mir die Verfügbarkeit für morgen bestätigen?','K08'),('Welche Karten akzeptieren Sie?','K09'),('Gibt es Angebote für Firmen?','K10'),('Haben Sie ein Schwimmbad?',None),('Gibt es ein Fitnessstudio?',None)]}
