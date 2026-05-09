export type ScenarioCategory =
  | 'Travel'
  | 'Accommodation'
  | 'Dining'
  | 'Shopping'
  | 'Daily Life'
  | 'WorkStudy'
  | 'Social'
  | 'Culture'
  | 'Health'
  | 'Tech'
  | 'Miscellaneous';

export type ScenarioTerm = {
  id: string;
  italian: string;
  english: string;
};

export type ScenarioPhrase = {
  id: string;
  italian: string;
  english: string;
};

export type ScenarioSentence = {
  id: string;
  italian: string;
  english: string;
  grammarPoint: string;
};

export type Scenario = {
  id: number;
  category: ScenarioCategory;
  title: string;
  description: string;
  vocabulary: ScenarioTerm[];
  phrases: ScenarioPhrase[];
  sentences: ScenarioSentence[];
};

type TermPair = readonly [italian: string, english: string];

type ScenarioBlueprint = {
  id: number;
  category: ScenarioCategory;
  title: string;
  description: string;
  focus: TermPair[];
};

const essentialConnectors: TermPair[] = [
  ['sì', 'yes'],
  ['no', 'no'],
  ['grazie', 'thank you'],
  ['prego', 'you are welcome'],
  ['scusi', 'excuse me'],
  ['per favore', 'please'],
  ['va bene', 'okay'],
  ['non capisco', 'I do not understand'],
  ['vorrei', 'I would like'],
  ['posso', 'I can / may I'],
  ['devo', 'I must'],
  ['voglio', 'I want'],
];

const categoryVocabulary: Record<ScenarioCategory, TermPair[]> = {
  Travel: [
    ['biglietto', 'ticket'],
    ['treno', 'train'],
    ['autobus', 'bus'],
    ['aereo', 'airplane'],
    ['stazione', 'station'],
    ['aeroporto', 'airport'],
    ['binario', 'platform'],
    ['partenza', 'departure'],
    ['arrivo', 'arrival'],
    ['ritardo', 'delay'],
    ['valigia', 'suitcase'],
    ['passaporto', 'passport'],
    ['mappa', 'map'],
    ['taxi', 'taxi'],
    ['fermata', 'stop'],
  ],
  Accommodation: [
    ['hotel', 'hotel'],
    ['camera', 'room'],
    ['prenotazione', 'reservation'],
    ['chiave', 'key'],
    ['documento', 'ID document'],
    ['bagno', 'bathroom'],
    ['letto', 'bed'],
    ['colazione', 'breakfast'],
    ['ascensore', 'elevator'],
    ['ricezione', 'reception'],
    ['notte', 'night'],
    ['piano', 'floor'],
    ['asciugamano', 'towel'],
    ['wifi', 'Wi-Fi'],
    ['conto', 'bill'],
  ],
  Dining: [
    ['ristorante', 'restaurant'],
    ['tavolo', 'table'],
    ['menù', 'menu'],
    ['acqua', 'water'],
    ['vino', 'wine'],
    ['caffè', 'coffee'],
    ['conto', 'bill'],
    ['piatto', 'dish'],
    ['pane', 'bread'],
    ['pasta', 'pasta'],
    ['pizza', 'pizza'],
    ['carne', 'meat'],
    ['pesce', 'fish'],
    ['dolce', 'dessert'],
    ['cameriere', 'waiter'],
  ],
  Shopping: [
    ['negozio', 'shop'],
    ['prezzo', 'price'],
    ['sconto', 'discount'],
    ['taglia', 'size'],
    ['colore', 'color'],
    ['cassa', 'cash register'],
    ['contanti', 'cash'],
    ['carta', 'card'],
    ['ricevuta', 'receipt'],
    ['borsa', 'bag'],
    ['scarpe', 'shoes'],
    ['maglia', 'shirt'],
    ['pantaloni', 'trousers'],
    ['regalo', 'gift'],
    ['mercato', 'market'],
  ],
  'Daily Life': [
    ['casa', 'home'],
    ['strada', 'street'],
    ['giorno', 'day'],
    ['sera', 'evening'],
    ['mattina', 'morning'],
    ['tempo', 'time / weather'],
    ['famiglia', 'family'],
    ['amico', 'friend'],
    ['lavoro', 'work'],
    ['spesa', 'groceries'],
    ['farmacia', 'pharmacy'],
    ['banca', 'bank'],
    ['posta', 'post office'],
    ['chiuso', 'closed'],
    ['aperto', 'open'],
  ],
  WorkStudy: [
    ['ufficio', 'office'],
    ['scuola', 'school'],
    ['lezione', 'lesson'],
    ['riunione', 'meeting'],
    ['collega', 'colleague'],
    ['studente', 'student'],
    ['insegnante', 'teacher'],
    ['computer', 'computer'],
    ['email', 'email'],
    ['orario', 'schedule'],
    ['compito', 'assignment'],
    ['domanda', 'question'],
    ['risposta', 'answer'],
    ['progetto', 'project'],
    ['pausa', 'break'],
  ],
  Social: [
    ['ciao', 'hello / bye'],
    ['piacere', 'nice to meet you'],
    ['nome', 'name'],
    ['amico', 'friend'],
    ['festa', 'party'],
    ['invito', 'invitation'],
    ['messaggio', 'message'],
    ['telefono', 'phone'],
    ['famiglia', 'family'],
    ['compleanno', 'birthday'],
    ['domani', 'tomorrow'],
    ['oggi', 'today'],
    ['insieme', 'together'],
    ['scusa', 'sorry'],
    ['auguri', 'best wishes'],
  ],
  Culture: [
    ['museo', 'museum'],
    ['chiesa', 'church'],
    ['teatro', 'theater'],
    ['cinema', 'cinema'],
    ['musica', 'music'],
    ['arte', 'art'],
    ['biglietto', 'ticket'],
    ['orario', 'opening time'],
    ['guida', 'guide'],
    ['mostra', 'exhibition'],
    ['piazza', 'square'],
    ['statua', 'statue'],
    ['storia', 'history'],
    ['foto', 'photo'],
    ['entrata', 'entrance'],
  ],
  Health: [
    ['dottore', 'doctor'],
    ['farmacia', 'pharmacy'],
    ['medicina', 'medicine'],
    ['dolore', 'pain'],
    ['febbre', 'fever'],
    ['allergia', 'allergy'],
    ['aiuto', 'help'],
    ['ospedale', 'hospital'],
    ['appuntamento', 'appointment'],
    ['ricetta', 'prescription'],
    ['testa', 'head'],
    ['stomaco', 'stomach'],
    ['tosse', 'cough'],
    ['malato', 'sick'],
    ['meglio', 'better'],
  ],
  Tech: [
    ['telefono', 'phone'],
    ['computer', 'computer'],
    ['internet', 'internet'],
    ['wifi', 'Wi-Fi'],
    ['password', 'password'],
    ['app', 'app'],
    ['messaggio', 'message'],
    ['foto', 'photo'],
    ['caricatore', 'charger'],
    ['batteria', 'battery'],
    ['schermo', 'screen'],
    ['email', 'email'],
    ['file', 'file'],
    ['connessione', 'connection'],
    ['problema', 'problem'],
  ],
  Miscellaneous: [
    ['informazione', 'information'],
    ['problema', 'problem'],
    ['aiuto', 'help'],
    ['persona', 'person'],
    ['posto', 'place'],
    ['cosa', 'thing'],
    ['momento', 'moment'],
    ['numero', 'number'],
    ['nome', 'name'],
    ['indirizzo', 'address'],
    ['vicino', 'near'],
    ['lontano', 'far'],
    ['facile', 'easy'],
    ['difficile', 'difficult'],
    ['sicuro', 'safe / sure'],
  ],
};

const blueprints: ScenarioBlueprint[] = [
  {id: 1, category: 'Travel', title: 'Airport Arrival', description: 'Arrive at an Italian airport and ask for basic arrival help.', focus: [['uscita', 'exit'], ['bagagli', 'luggage'], ['controllo', 'control'], ['dogana', 'customs'], ['navetta', 'shuttle'], ['terminal', 'terminal'], ['ritiro bagagli', 'baggage claim'], ['volo', 'flight']]},
  {id: 2, category: 'Travel', title: 'Passport Control', description: 'Answer simple questions at border control.', focus: [['motivo', 'reason'], ['vacanza', 'holiday'], ['lavoro', 'work'], ['indirizzo', 'address'], ['durata', 'duration'], ['timbro', 'stamp'], ['permesso', 'permit'], ['residenza', 'residence']]},
  {id: 3, category: 'Travel', title: 'Baggage Claim', description: 'Find luggage and report a missing bag.', focus: [['nastro', 'carousel'], ['borsa', 'bag'], ['perso', 'lost'], ['etichetta', 'tag'], ['ufficio bagagli', 'baggage office'], ['descrizione', 'description'], ['nero', 'black'], ['grande', 'large']]},
  {id: 4, category: 'Travel', title: 'Taxi From Airport', description: 'Take a taxi from the airport to an address.', focus: [['indirizzo', 'address'], ['centro', 'center'], ['tariffa', 'fare'], ['metro', 'meter'], ['ricevuta', 'receipt'], ['destra', 'right'], ['sinistra', 'left'], ['qui va bene', 'here is fine']]},
  {id: 5, category: 'Travel', title: 'Train Ticket', description: 'Buy a train ticket and confirm time and platform.', focus: [['andata', 'one way'], ['ritorno', 'return'], ['regionale', 'regional train'], ['freccia', 'high-speed train'], ['posto', 'seat'], ['seconda classe', 'second class'], ['obliterare', 'validate'], ['macchinetta', 'machine']]},
  {id: 6, category: 'Travel', title: 'Train Platform', description: 'Ask where to board and understand changes.', focus: [['binario due', 'platform two'], ['sottopassaggio', 'underpass'], ['cambio', 'change'], ['coincidenza', 'connection'], ['carrozza', 'coach'], ['posto finestrino', 'window seat'], ['annuncio', 'announcement'], ['in ritardo', 'delayed']]},
  {id: 7, category: 'Travel', title: 'Bus Ticket', description: 'Buy and validate a local bus ticket.', focus: [['tabaccheria', 'tobacco shop'], ['biglietto urbano', 'city ticket'], ['validare', 'validate'], ['autista', 'driver'], ['linea', 'line'], ['orario bus', 'bus schedule'], ['fermata giusta', 'right stop'], ['direzione', 'direction']]},
  {id: 8, category: 'Travel', title: 'Metro Directions', description: 'Use the metro and ask for the correct line.', focus: [['linea rossa', 'red line'], ['linea verde', 'green line'], ['cambio metro', 'metro transfer'], ['uscita metro', 'metro exit'], ['scale', 'stairs'], ['biglietteria', 'ticket office'], ['mappa metro', 'metro map'], ['capolinea', 'last stop']]},
  {id: 9, category: 'Travel', title: 'Asking Directions', description: 'Ask for walking directions in town.', focus: [['dritto', 'straight'], ['angolo', 'corner'], ['semaforo', 'traffic light'], ['ponte', 'bridge'], ['piazza', 'square'], ['vicino', 'near'], ['lontano', 'far'], ['a piedi', 'on foot']]},
  {id: 10, category: 'Travel', title: 'Renting a Car', description: 'Pick up a rental car and ask about basic terms.', focus: [['patente', 'driver license'], ['assicurazione', 'insurance'], ['benzina', 'gasoline'], ['diesel', 'diesel'], ['cambio manuale', 'manual transmission'], ['deposito', 'deposit'], ['graffio', 'scratch'], ['contratto', 'contract']]},
  {id: 11, category: 'Travel', title: 'Gas Station', description: 'Get fuel and pay at a service station.', focus: [['pieno', 'full tank'], ['self service', 'self service'], ['servito', 'attended service'], ['pompa', 'pump'], ['benzina senza piombo', 'unleaded gas'], ['litro', 'liter'], ['pressione', 'pressure'], ['scontrino', 'receipt']]},
  {id: 12, category: 'Travel', title: 'Parking', description: 'Ask where and how to park.', focus: [['parcheggio', 'parking'], ['strisce blu', 'blue paid lines'], ['ticket parcheggio', 'parking ticket'], ['ora', 'hour'], ['multa', 'fine'], ['garage', 'garage'], ['posto libero', 'free spot'], ['permesso', 'permit']]},
  {id: 13, category: 'Travel', title: 'Lost in a City', description: 'Explain that you are lost and ask for help.', focus: [['mi sono perso', 'I am lost'], ['indirizzo hotel', 'hotel address'], ['telefono scarico', 'dead phone'], ['polizia', 'police'], ['mappa offline', 'offline map'], ['zona', 'area'], ['ritornare', 'return'], ['aiutarmi', 'help me']]},
  {id: 14, category: 'Travel', title: 'Buying Ferry Tickets', description: 'Buy ferry tickets and ask about boarding.', focus: [['traghetto', 'ferry'], ['porto', 'port'], ['isola', 'island'], ['ponte', 'deck'], ['cabina', 'cabin'], ['imbarco', 'boarding'], ['mare', 'sea'], ['orario traghetto', 'ferry time']]},
  {id: 15, category: 'Travel', title: 'Bike Rental', description: 'Rent a bike and ask about return time.', focus: [['bicicletta', 'bicycle'], ['casco', 'helmet'], ['lucchetto', 'lock'], ['cauzione', 'deposit'], ['pista ciclabile', 'bike lane'], ['restituzione', 'return'], ['ora inclusa', 'included hour'], ['rotto', 'broken']]},
  {id: 16, category: 'Travel', title: 'Travel Emergency', description: 'Ask for urgent help while traveling.', focus: [['emergenza', 'emergency'], ['ambulanza', 'ambulance'], ['furto', 'theft'], ['portafoglio', 'wallet'], ['ambasciata', 'embassy'], ['denuncia', 'report'], ['sicurezza', 'safety'], ['subito', 'right away']]},
  {id: 17, category: 'Accommodation', title: 'Hotel Check-In', description: 'Check in at a hotel and confirm your booking.', focus: [['check-in', 'check-in'], ['cognome', 'last name'], ['camera singola', 'single room'], ['camera doppia', 'double room'], ['passaporto', 'passport'], ['firma', 'signature'], ['tassa di soggiorno', 'city tax'], ['codice', 'code']]},
  {id: 18, category: 'Accommodation', title: 'Hotel Check-Out', description: 'Check out, pay, and ask for a receipt.', focus: [['check-out', 'check-out'], ['minibar', 'minibar'], ['pagamento', 'payment'], ['fattura', 'invoice'], ['ricevuta', 'receipt'], ['deposito bagagli', 'luggage storage'], ['tardi', 'late'], ['camera libera', 'room free']]},
  {id: 19, category: 'Accommodation', title: 'Room Problem', description: 'Report a problem with the room.', focus: [['aria condizionata', 'air conditioning'], ['riscaldamento', 'heating'], ['rumore', 'noise'], ['luce', 'light'], ['doccia', 'shower'], ['rotto', 'broken'], ['sporco', 'dirty'], ['cambiare camera', 'change room']]},
  {id: 20, category: 'Accommodation', title: 'Asking for Towels', description: 'Ask housekeeping for towels and supplies.', focus: [['sapone', 'soap'], ['carta igienica', 'toilet paper'], ['coperta', 'blanket'], ['cuscino', 'pillow'], ['pulizia', 'cleaning'], ['asciugamani puliti', 'clean towels'], ['phon', 'hair dryer'], ['subito', 'right away']]},
  {id: 21, category: 'Accommodation', title: 'Breakfast at Hotel', description: 'Ask about breakfast options and times.', focus: [['buffet', 'buffet'], ['succo', 'juice'], ['cornetto', 'croissant'], ['uova', 'eggs'], ['formaggio', 'cheese'], ['senza glutine', 'gluten free'], ['orario colazione', 'breakfast time'], ['sala', 'room / hall']]},
  {id: 22, category: 'Accommodation', title: 'Apartment Key Pickup', description: 'Meet a host and collect apartment keys.', focus: [['appartamento', 'apartment'], ['host', 'host'], ['citofono', 'intercom'], ['portone', 'building door'], ['serratura', 'lock'], ['codice porta', 'door code'], ['consegna chiavi', 'key handoff'], ['regole', 'rules']]},
  {id: 23, category: 'Accommodation', title: 'Wi-Fi at Hotel', description: 'Ask for Wi-Fi details and report connection trouble.', focus: [['rete', 'network'], ['password wifi', 'Wi-Fi password'], ['segnale', 'signal'], ['lento', 'slow'], ['non funziona', 'does not work'], ['router', 'router'], ['piano terra', 'ground floor'], ['riprovare', 'try again']]},
  {id: 24, category: 'Accommodation', title: 'Laundry Service', description: 'Ask about washing clothes during a stay.', focus: [['lavanderia', 'laundry'], ['lavatrice', 'washing machine'], ['asciugatrice', 'dryer'], ['detersivo', 'detergent'], ['camicia', 'shirt'], ['domani mattina', 'tomorrow morning'], ['prezzo lavaggio', 'washing price'], ['stirare', 'iron']]},
  {id: 25, category: 'Accommodation', title: 'Extending Stay', description: 'Ask to stay extra nights.', focus: [['prolungare', 'extend'], ['un altra notte', 'one more night'], ['disponibile', 'available'], ['stesso prezzo', 'same price'], ['cambiare stanza', 'change room'], ['calendario', 'calendar'], ['alta stagione', 'high season'], ['conferma', 'confirmation']]},
  {id: 26, category: 'Accommodation', title: 'Hostel Dorm', description: 'Navigate a hostel dorm and shared facilities.', focus: [['ostello', 'hostel'], ['letto a castello', 'bunk bed'], ['armadietto', 'locker'], ['bagno condiviso', 'shared bathroom'], ['cucina comune', 'shared kitchen'], ['silenzio', 'quiet'], ['lenzuola', 'sheets'], ['lucchetto', 'lock']]},
  {id: 27, category: 'Dining', title: 'Restaurant Reservation', description: 'Reserve a table at a restaurant.', focus: [['prenotare', 'reserve'], ['due persone', 'two people'], ['alle otto', 'at eight'], ['nome prenotazione', 'reservation name'], ['terrazza', 'terrace'], ['interno', 'inside'], ['confermare', 'confirm'], ['occupato', 'busy']]},
  {id: 28, category: 'Dining', title: 'Ordering Coffee', description: 'Order coffee at an Italian bar.', focus: [['espresso', 'espresso'], ['cappuccino', 'cappuccino'], ['macchiato', 'macchiato'], ['zucchero', 'sugar'], ['banco', 'counter'], ['tazza', 'cup'], ['cornetto', 'croissant'], ['freddo', 'cold']]},
  {id: 29, category: 'Dining', title: 'Ordering Pizza', description: 'Order pizza and ask about toppings.', focus: [['margherita', 'margherita'], ['funghi', 'mushrooms'], ['prosciutto', 'ham'], ['mozzarella', 'mozzarella'], ['pomodoro', 'tomato'], ['piccante', 'spicy'], ['da portare via', 'to go'], ['forno', 'oven']]},
  {id: 30, category: 'Dining', title: 'Ordering Pasta', description: 'Choose a pasta dish and ask simple questions.', focus: [['spaghetti', 'spaghetti'], ['penne', 'penne'], ['sugo', 'sauce'], ['ragù', 'meat sauce'], ['carbonara', 'carbonara'], ['parmigiano', 'parmesan'], ['porzione', 'portion'], ['al dente', 'firm to the bite']]},
  {id: 31, category: 'Dining', title: 'Gelato Shop', description: 'Buy gelato and choose flavors.', focus: [['gelato', 'gelato'], ['cono', 'cone'], ['coppetta', 'cup'], ['gusto', 'flavor'], ['cioccolato', 'chocolate'], ['pistacchio', 'pistachio'], ['fragola', 'strawberry'], ['due gusti', 'two flavors']]},
  {id: 32, category: 'Dining', title: 'Paying the Bill', description: 'Ask for the bill and split payment.', focus: [['pagare', 'pay'], ['dividere', 'split'], ['mancia', 'tip'], ['servizio', 'service'], ['pos', 'card terminal'], ['bancomat', 'debit card'], ['totale', 'total'], ['separato', 'separate']]},
  {id: 33, category: 'Dining', title: 'Food Allergies', description: 'Explain allergies and ask about ingredients.', focus: [['arachidi', 'peanuts'], ['latte', 'milk'], ['glutine', 'gluten'], ['uova', 'eggs'], ['ingredienti', 'ingredients'], ['senza', 'without'], ['allergico', 'allergic'], ['pericoloso', 'dangerous']]},
  {id: 34, category: 'Dining', title: 'Vegetarian Meal', description: 'Ask for vegetarian or vegan options.', focus: [['vegetariano', 'vegetarian'], ['vegano', 'vegan'], ['verdure', 'vegetables'], ['formaggio', 'cheese'], ['senza carne', 'without meat'], ['senza pesce', 'without fish'], ['legumi', 'legumes'], ['insalata', 'salad']]},
  {id: 35, category: 'Dining', title: 'Wine Bar', description: 'Order wine and ask for a recommendation.', focus: [['rosso', 'red'], ['bianco', 'white'], ['bicchiere', 'glass'], ['bottiglia', 'bottle'], ['secco', 'dry'], ['dolce', 'sweet'], ['locale', 'local'], ['consigliare', 'recommend']]},
  {id: 36, category: 'Dining', title: 'Bakery', description: 'Buy bread and pastries at a bakery.', focus: [['panetteria', 'bakery'], ['focaccia', 'focaccia'], ['pane integrale', 'whole-grain bread'], ['brioche', 'brioche'], ['grammi', 'grams'], ['mezzo chilo', 'half kilo'], ['fresco', 'fresh'], ['tagliato', 'sliced']]},
  {id: 37, category: 'Dining', title: 'Street Food', description: 'Order simple street food.', focus: [['arancino', 'rice ball'], ['panino', 'sandwich'], ['porchetta', 'roast pork'], ['supplì', 'fried rice ball'], ['cartoccio', 'paper cone'], ['salsa', 'sauce'], ['caldo', 'hot'], ['pronto', 'ready']]},
  {id: 38, category: 'Dining', title: 'Breakfast Bar', description: 'Have a quick breakfast at a bar.', focus: [['latte', 'milk'], ['orzo', 'barley coffee'], ['spremuta', 'fresh juice'], ['marmellata', 'jam'], ['burro', 'butter'], ['biscotto', 'cookie'], ['pagare prima', 'pay first'], ['scontrino', 'receipt']]},
  {id: 39, category: 'Dining', title: 'Cooking Class', description: 'Follow simple instructions in a cooking class.', focus: [['ricetta', 'recipe'], ['tagliare', 'cut'], ['mescolare', 'mix'], ['cuocere', 'cook'], ['farina', 'flour'], ['olio', 'oil'], ['sale', 'salt'], ['padella', 'pan']]},
  {id: 40, category: 'Dining', title: 'Market Lunch', description: 'Buy ingredients for a simple lunch.', focus: [['pomodori', 'tomatoes'], ['mozzarella fresca', 'fresh mozzarella'], ['basilico', 'basil'], ['prosciutto crudo', 'cured ham'], ['olive', 'olives'], ['frutta', 'fruit'], ['coltello', 'knife'], ['piatto piccolo', 'small plate']]},
  {id: 41, category: 'Shopping', title: 'Clothing Store', description: 'Ask for sizes and try on clothes.', focus: [['camerino', 'fitting room'], ['piccolo', 'small'], ['medio', 'medium'], ['grande', 'large'], ['provare', 'try on'], ['giacca', 'jacket'], ['vestito', 'dress'], ['commesso', 'shop assistant']]},
  {id: 42, category: 'Shopping', title: 'Shoe Store', description: 'Buy shoes and ask for a size.', focus: [['numero', 'shoe size'], ['comodo', 'comfortable'], ['stretto', 'tight'], ['largo', 'wide'], ['paio', 'pair'], ['calzini', 'socks'], ['pelle', 'leather'], ['sportive', 'sneakers']]},
  {id: 43, category: 'Shopping', title: 'Grocery Store', description: 'Buy groceries and ask where items are.', focus: [['carrello', 'cart'], ['cestino', 'basket'], ['latte', 'milk'], ['uova', 'eggs'], ['riso', 'rice'], ['pasta secca', 'dry pasta'], ['scaffale', 'shelf'], ['cassiere', 'cashier']]},
  {id: 44, category: 'Shopping', title: 'Outdoor Market', description: 'Shop for produce at an outdoor market.', focus: [['banco', 'stall'], ['chilo', 'kilo'], ['maturo', 'ripe'], ['assaggiare', 'taste'], ['fragole', 'strawberries'], ['mele', 'apples'], ['zucchine', 'zucchini'], ['sacchetto', 'small bag']]},
  {id: 45, category: 'Shopping', title: 'Pharmacy Purchase', description: 'Buy simple pharmacy items.', focus: [['cerotti', 'bandages'], ['crema', 'cream'], ['vitamine', 'vitamins'], ['mal di testa', 'headache'], ['raffreddore', 'cold'], ['gocce', 'drops'], ['farmacista', 'pharmacist'], ['dose', 'dose']]},
  {id: 46, category: 'Shopping', title: 'Souvenir Shop', description: 'Buy souvenirs and gifts.', focus: [['cartolina', 'postcard'], ['magnete', 'magnet'], ['artigianale', 'handmade'], ['ceramica', 'ceramic'], ['ricordo', 'souvenir'], ['incartare', 'wrap'], ['fragile', 'fragile'], ['spedire', 'send']]},
  {id: 47, category: 'Shopping', title: 'Electronics Store', description: 'Buy chargers and basic electronics.', focus: [['adattatore', 'adapter'], ['cavo', 'cable'], ['presa', 'socket'], ['garanzia', 'warranty'], ['modello', 'model'], ['auricolari', 'earbuds'], ['memoria', 'storage'], ['compatibile', 'compatible']]},
  {id: 48, category: 'Shopping', title: 'Bookstore', description: 'Find a book or language material.', focus: [['libreria', 'bookstore'], ['libro', 'book'], ['quaderno', 'notebook'], ['dizionario', 'dictionary'], ['romanzo', 'novel'], ['autore', 'author'], ['reparto', 'section'], ['copertina', 'cover']]},
  {id: 49, category: 'Shopping', title: 'Returning an Item', description: 'Return or exchange something you bought.', focus: [['reso', 'return'], ['cambio', 'exchange'], ['difetto', 'defect'], ['rotto', 'broken'], ['rimborso', 'refund'], ['scontrino', 'receipt'], ['politica', 'policy'], ['entro trenta giorni', 'within thirty days']]},
  {id: 50, category: 'Shopping', title: 'Paying by Card', description: 'Handle card payment questions.', focus: [['contactless', 'contactless'], ['pin', 'PIN'], ['firma', 'signature'], ['rifiutata', 'declined'], ['approvata', 'approved'], ['terminale', 'terminal'], ['importo', 'amount'], ['riprovare', 'try again']]},
  {id: 51, category: 'Daily Life', title: 'At the Bank', description: 'Ask simple questions at a bank.', focus: [['conto corrente', 'bank account'], ['prelievo', 'withdrawal'], ['deposito', 'deposit'], ['bancomat', 'ATM'], ['documento', 'ID'], ['codice fiscale', 'tax code'], ['sportello', 'counter'], ['modulo', 'form']]},
  {id: 52, category: 'Daily Life', title: 'At the Post Office', description: 'Send mail and ask about stamps.', focus: [['francobollo', 'stamp'], ['pacco', 'package'], ['lettera', 'letter'], ['spedizione', 'shipping'], ['destinatario', 'recipient'], ['mittente', 'sender'], ['raccomandata', 'registered mail'], ['coda', 'line']]},
  {id: 53, category: 'Daily Life', title: 'Haircut', description: 'Ask for a simple haircut.', focus: [['parrucchiere', 'hairdresser'], ['taglio', 'cut'], ['corto', 'short'], ['spuntare', 'trim'], ['barba', 'beard'], ['lavaggio', 'wash'], ['appuntamento', 'appointment'], ['specchio', 'mirror']]},
  {id: 54, category: 'Daily Life', title: 'Laundry Machine', description: 'Use a laundromat.', focus: [['lavanderia automatica', 'laundromat'], ['gettone', 'token'], ['programma', 'cycle'], ['temperatura', 'temperature'], ['bianchi', 'whites'], ['colorati', 'colors'], ['asciugare', 'dry'], ['finito', 'finished']]},
  {id: 55, category: 'Daily Life', title: 'Weather Small Talk', description: 'Talk about the weather simply.', focus: [['sole', 'sun'], ['pioggia', 'rain'], ['vento', 'wind'], ['nuvoloso', 'cloudy'], ['caldo', 'hot'], ['freddo', 'cold'], ['ombrello', 'umbrella'], ['previsioni', 'forecast']]},
  {id: 56, category: 'Daily Life', title: 'Making an Appointment', description: 'Schedule a basic appointment.', focus: [['appuntamento', 'appointment'], ['disponibile', 'available'], ['alle dieci', 'at ten'], ['lunedì', 'Monday'], ['martedì', 'Tuesday'], ['conferma', 'confirmation'], ['spostare', 'move / reschedule'], ['cancellare', 'cancel']]},
  {id: 57, category: 'Daily Life', title: 'At the Gym', description: 'Ask about gym access and classes.', focus: [['palestra', 'gym'], ['abbonamento', 'membership'], ['lezione prova', 'trial class'], ['spogliatoio', 'changing room'], ['tapis roulant', 'treadmill'], ['peso', 'weight'], ['istruttore', 'trainer'], ['acqua', 'water']]},
  {id: 58, category: 'Daily Life', title: 'At the Library', description: 'Ask for a library card and find books.', focus: [['biblioteca', 'library'], ['tessera', 'card'], ['prestito', 'loan'], ['silenzio', 'silence'], ['sala lettura', 'reading room'], ['scadenza', 'due date'], ['catalogo', 'catalog'], ['restituire', 'return']]},
  {id: 59, category: 'Daily Life', title: 'Talking to a Neighbor', description: 'Handle simple neighbor conversation.', focus: [['vicino di casa', 'neighbor'], ['palazzo', 'building'], ['rumore', 'noise'], ['porta', 'door'], ['scala', 'staircase'], ['posta', 'mail'], ['gentile', 'kind'], ['ci vediamo', 'see you']]},
  {id: 60, category: 'Daily Life', title: 'Household Repair', description: 'Report a repair problem at home.', focus: [['idraulico', 'plumber'], ['elettricista', 'electrician'], ['perdita', 'leak'], ['rubinetto', 'tap'], ['presa elettrica', 'power outlet'], ['caldaia', 'boiler'], ['riparare', 'repair'], ['urgente', 'urgent']]},
  {id: 61, category: 'WorkStudy', title: 'First Day at Work', description: 'Introduce yourself at work.', focus: [['nuovo', 'new'], ['responsabile', 'manager'], ['scrivania', 'desk'], ['badge', 'badge'], ['colleghi', 'colleagues'], ['mansione', 'task'], ['pausa pranzo', 'lunch break'], ['benvenuto', 'welcome']]},
  {id: 62, category: 'WorkStudy', title: 'Team Meeting', description: 'Participate in a simple meeting.', focus: [['agenda', 'agenda'], ['punto', 'point'], ['nota', 'note'], ['decisione', 'decision'], ['accordo', 'agreement'], ['problema', 'problem'], ['prossimo passo', 'next step'], ['verbale', 'minutes']]},
  {id: 63, category: 'WorkStudy', title: 'Asking for Clarification', description: 'Say you do not understand and ask to repeat.', focus: [['ripetere', 'repeat'], ['spiegare', 'explain'], ['lentamente', 'slowly'], ['esempio', 'example'], ['chiaro', 'clear'], ['dubbio', 'doubt'], ['significa', 'means'], ['capire', 'understand']]},
  {id: 64, category: 'WorkStudy', title: 'Email Follow-Up', description: 'Discuss a simple work email.', focus: [['allegato', 'attachment'], ['oggetto', 'subject'], ['rispondere', 'reply'], ['inoltrare', 'forward'], ['bozza', 'draft'], ['scadenza', 'deadline'], ['ricevuto', 'received'], ['inviare', 'send']]},
  {id: 65, category: 'WorkStudy', title: 'University Class', description: 'Ask about a class at university.', focus: [['università', 'university'], ['aula', 'classroom'], ['professore', 'professor'], ['esame', 'exam'], ['voto', 'grade'], ['appunti', 'notes'], ['semestre', 'semester'], ['iscrizione', 'enrollment']]},
  {id: 66, category: 'WorkStudy', title: 'Language School', description: 'Talk about language school needs.', focus: [['corso', 'course'], ['livello A1', 'A1 level'], ['grammatica', 'grammar'], ['conversazione', 'conversation'], ['pronuncia', 'pronunciation'], ['esercizio', 'exercise'], ['classe', 'class'], ['certificato', 'certificate']]},
  {id: 67, category: 'WorkStudy', title: 'Job Interview', description: 'Answer basic interview questions.', focus: [['colloquio', 'interview'], ['esperienza', 'experience'], ['curriculum', 'CV'], ['disponibilità', 'availability'], ['stipendio', 'salary'], ['contratto', 'contract'], ['orario flessibile', 'flexible schedule'], ['iniziare', 'start']]},
  {id: 68, category: 'WorkStudy', title: 'Coworking Space', description: 'Use a coworking space.', focus: [['postazione', 'workspace'], ['sala riunioni', 'meeting room'], ['stampante', 'printer'], ['prenotare sala', 'book a room'], ['giornaliero', 'daily'], ['mensile', 'monthly'], ['silenziosa', 'quiet'], ['accesso', 'access']]},
  {id: 69, category: 'WorkStudy', title: 'Printing Documents', description: 'Print or scan documents.', focus: [['stampare', 'print'], ['scannerizzare', 'scan'], ['fronte retro', 'double-sided'], ['bianco e nero', 'black and white'], ['colore', 'color'], ['pagina', 'page'], ['formato A4', 'A4 size'], ['chiavetta USB', 'USB stick']]},
  {id: 70, category: 'WorkStudy', title: 'Study Group', description: 'Arrange a study session.', focus: [['studiare', 'study'], ['biblioteca', 'library'], ['ripasso', 'review'], ['capitolo', 'chapter'], ['insieme', 'together'], ['domande', 'questions'], ['esercizi', 'exercises'], ['pausa caffè', 'coffee break']]},
  {id: 71, category: 'Social', title: 'Introducing Yourself', description: 'Meet someone and give simple personal details.', focus: [['mi chiamo', 'my name is'], ['vengo da', 'I come from'], ['abito a', 'I live in'], ['anni', 'years old'], ['lingua', 'language'], ['studio italiano', 'I study Italian'], ['piacere mio', 'my pleasure'], ['di dove sei', 'where are you from']]},
  {id: 72, category: 'Social', title: 'Making Plans', description: 'Make simple plans with a friend.', focus: [['uscire', 'go out'], ['cinema', 'cinema'], ['cena', 'dinner'], ['alle sette', 'at seven'], ['ci sei', 'are you in'], ['va bene per te', 'is it okay for you'], ['forse', 'maybe'], ['sicuro', 'sure']]},
  {id: 73, category: 'Social', title: 'Inviting a Friend', description: 'Invite a friend to an activity.', focus: [['vuoi venire', 'do you want to come'], ['con noi', 'with us'], ['sabato', 'Saturday'], ['domenica', 'Sunday'], ['aperitivo', 'aperitif'], ['posto carino', 'nice place'], ['fammi sapere', 'let me know'], ['volentieri', 'gladly']]},
  {id: 74, category: 'Social', title: 'At a Party', description: 'Have small talk at a party.', focus: [['musica alta', 'loud music'], ['conosci', 'you know'], ['bevanda', 'drink'], ['ballare', 'dance'], ['divertente', 'fun'], ['amici comuni', 'mutual friends'], ['restare', 'stay'], ['andare via', 'leave']]},
  {id: 75, category: 'Social', title: 'Phone Call', description: 'Handle a short phone call.', focus: [['pronto', 'hello on phone'], ['chi parla', 'who is speaking'], ['non sento', 'I cannot hear'], ['richiamare', 'call back'], ['numero sbagliato', 'wrong number'], ['messaggio vocale', 'voice message'], ['occupato', 'busy'], ['a dopo', 'see you later']]},
  {id: 76, category: 'Social', title: 'Texting a Friend', description: 'Send simple text messages.', focus: [['scrivere', 'write'], ['rispondere', 'reply'], ['emoji', 'emoji'], ['arrivo', 'I am arriving'], ['sono qui', 'I am here'], ['ritardo cinque minuti', 'five minutes late'], ['mandare posizione', 'send location'], ['ok perfetto', 'okay perfect']]},
  {id: 77, category: 'Social', title: 'Apologizing', description: 'Apologize and explain simply.', focus: [['mi dispiace', 'I am sorry'], ['colpa mia', 'my fault'], ['ritardo', 'delay'], ['traffico', 'traffic'], ['dimenticato', 'forgotten'], ['problema', 'problem'], ['non volevo', 'I did not mean to'], ['scusami', 'forgive me']]},
  {id: 78, category: 'Social', title: 'Compliments', description: 'Give and receive simple compliments.', focus: [['bello', 'beautiful'], ['bravo', 'good / skilled'], ['ottimo', 'excellent'], ['mi piace', 'I like it'], ['che carino', 'how cute'], ['complimenti', 'congratulations'], ['grazie mille', 'thanks a lot'], ['anche tu', 'you too']]},
  {id: 79, category: 'Social', title: 'Birthday Wishes', description: 'Wish someone happy birthday.', focus: [['buon compleanno', 'happy birthday'], ['tanti auguri', 'best wishes'], ['regalo', 'gift'], ['torta', 'cake'], ['candeline', 'candles'], ['festa sorpresa', 'surprise party'], ['brindisi', 'toast'], ['felice', 'happy']]},
  {id: 80, category: 'Social', title: 'Saying Goodbye', description: 'End conversations politely.', focus: [['arrivederci', 'goodbye'], ['a presto', 'see you soon'], ['buona giornata', 'have a good day'], ['buona serata', 'good evening'], ['ci sentiamo', 'we will talk'], ['salutami', 'say hi to'], ['devo andare', 'I have to go'], ['è stato bello', 'it was nice']]},
  {id: 81, category: 'Culture', title: 'Museum Tickets', description: 'Buy museum tickets and ask about exhibits.', focus: [['intero', 'full price'], ['ridotto', 'reduced'], ['audioguida', 'audio guide'], ['prenotazione online', 'online booking'], ['sala', 'hall'], ['quadro', 'painting'], ['scultura', 'sculpture'], ['guardaroba', 'cloakroom']]},
  {id: 82, category: 'Culture', title: 'Church Visit', description: 'Visit a church respectfully.', focus: [['messa', 'mass'], ['silenzio', 'silence'], ['spalle coperte', 'covered shoulders'], ['altare', 'altar'], ['cupola', 'dome'], ['affresco', 'fresco'], ['ingresso libero', 'free entry'], ['offerta', 'donation']]},
  {id: 83, category: 'Culture', title: 'Cinema Tickets', description: 'Buy cinema tickets.', focus: [['film', 'film'], ['spettacolo', 'showtime'], ['posti', 'seats'], ['sottotitoli', 'subtitles'], ['doppiato', 'dubbed'], ['popcorn', 'popcorn'], ['fila', 'row'], ['schermo', 'screen']]},
  {id: 84, category: 'Culture', title: 'Theater Evening', description: 'Attend a theater show.', focus: [['palco', 'stage'], ['platea', 'stalls'], ['balcone', 'balcony'], ['programma', 'program'], ['attore', 'actor'], ['intervallo', 'intermission'], ['applauso', 'applause'], ['sipario', 'curtain']]},
  {id: 85, category: 'Culture', title: 'Live Music', description: 'Go to a live music event.', focus: [['concerto', 'concert'], ['band', 'band'], ['cantante', 'singer'], ['biglietto online', 'online ticket'], ['ingresso', 'entry'], ['posto in piedi', 'standing place'], ['volume', 'volume'], ['bis', 'encore']]},
  {id: 86, category: 'Culture', title: 'Art Gallery', description: 'Discuss simple art preferences.', focus: [['galleria', 'gallery'], ['artista', 'artist'], ['moderno', 'modern'], ['classico', 'classical'], ['colore', 'color'], ['disegno', 'drawing'], ['mi interessa', 'I am interested'], ['catalogo', 'catalog']]},
  {id: 87, category: 'Culture', title: 'Guided Tour', description: 'Join a guided tour.', focus: [['tour guidato', 'guided tour'], ['gruppo', 'group'], ['punto incontro', 'meeting point'], ['durata', 'duration'], ['auricolare', 'headset'], ['seguire', 'follow'], ['pausa foto', 'photo break'], ['domande finali', 'final questions']]},
  {id: 88, category: 'Culture', title: 'Historic Site', description: 'Ask basic questions at a historic site.', focus: [['rovine', 'ruins'], ['castello', 'castle'], ['mura', 'walls'], ['secolo', 'century'], ['antico', 'ancient'], ['restauro', 'restoration'], ['percorso', 'route'], ['vista', 'view']]},
  {id: 89, category: 'Culture', title: 'Festival', description: 'Attend a local festival.', focus: [['sagra', 'local festival'], ['processione', 'procession'], ['fuochi d artificio', 'fireworks'], ['bancarella', 'stall'], ['tradizione', 'tradition'], ['costume', 'costume'], ['programma festa', 'festival program'], ['piazza principale', 'main square']]},
  {id: 90, category: 'Culture', title: 'Sports Match', description: 'Attend or discuss a sports match.', focus: [['partita', 'match'], ['stadio', 'stadium'], ['squadra', 'team'], ['tifoso', 'fan'], ['goal', 'goal'], ['posto numerato', 'numbered seat'], ['arbitro', 'referee'], ['risultato', 'score']]},
  {id: 91, category: 'Culture', title: 'Italian Customs', description: 'Ask about social customs.', focus: [['abitudine', 'habit'], ['educato', 'polite'], ['salutare', 'greet'], ['orario cena', 'dinner time'], ['coperto', 'cover charge'], ['mancia', 'tip'], ['gesto', 'gesture'], ['normale', 'normal']]},
  {id: 92, category: 'Culture', title: 'Local History', description: 'Ask simple questions about local history.', focus: [['fondato', 'founded'], ['medioevo', 'Middle Ages'], ['romano', 'Roman'], ['famiglia nobile', 'noble family'], ['leggenda', 'legend'], ['monumento', 'monument'], ['quartiere antico', 'old district'], ['racconto', 'story']]},
  {id: 93, category: 'Health', title: 'Pharmacy Symptoms', description: 'Describe common symptoms at a pharmacy.', focus: [['mal di gola', 'sore throat'], ['naso chiuso', 'blocked nose'], ['pastiglie', 'lozenges'], ['sciroppo', 'syrup'], ['termometro', 'thermometer'], ['dose giornaliera', 'daily dose'], ['effetto', 'effect'], ['sonnolenza', 'sleepiness']]},
  {id: 94, category: 'Health', title: 'Doctor Appointment', description: 'Book and attend a doctor appointment.', focus: [['medico', 'doctor'], ['sintomo', 'symptom'], ['visita', 'visit'], ['pressione', 'blood pressure'], ['assicurazione sanitaria', 'health insurance'], ['tessera sanitaria', 'health card'], ['diagnosi', 'diagnosis'], ['controllo', 'checkup']]},
  {id: 95, category: 'Health', title: 'Emergency Room', description: 'Ask for urgent medical help.', focus: [['pronto soccorso', 'emergency room'], ['incidente', 'accident'], ['respirare', 'breathe'], ['sangue', 'blood'], ['infermiere', 'nurse'], ['attesa', 'wait'], ['dolore forte', 'strong pain'], ['subito', 'immediately']]},
  {id: 96, category: 'Health', title: 'Dental Problem', description: 'Explain a dental issue.', focus: [['dentista', 'dentist'], ['dente', 'tooth'], ['gengiva', 'gum'], ['carie', 'cavity'], ['pulizia denti', 'teeth cleaning'], ['anestesia', 'anesthesia'], ['mordere', 'bite'], ['sensibile', 'sensitive']]},
  {id: 97, category: 'Health', title: 'Buying Medicine', description: 'Buy medicine and understand dosage.', focus: [['compressa', 'tablet'], ['capsula', 'capsule'], ['prima dei pasti', 'before meals'], ['dopo i pasti', 'after meals'], ['due volte al giorno', 'twice a day'], ['controindicazione', 'contraindication'], ['generico', 'generic'], ['scatola', 'box']]},
  {id: 98, category: 'Tech', title: 'Buying a SIM Card', description: 'Buy a prepaid SIM card.', focus: [['sim', 'SIM'], ['ricaricabile', 'prepaid'], ['dati', 'data'], ['minuti', 'minutes'], ['documento', 'ID'], ['attivazione', 'activation'], ['piano mensile', 'monthly plan'], ['copertura', 'coverage']]},
  {id: 99, category: 'Tech', title: 'Wi-Fi Problem', description: 'Troubleshoot Wi-Fi access.', focus: [['non si collega', 'it does not connect'], ['nome rete', 'network name'], ['riavviare', 'restart'], ['segnale debole', 'weak signal'], ['codice errato', 'wrong code'], ['assistenza', 'support'], ['modem', 'modem'], ['online', 'online']]},
  {id: 100, category: 'Tech', title: 'Phone Repair', description: 'Ask about repairing a phone.', focus: [['riparazione', 'repair'], ['vetro rotto', 'broken glass'], ['schermo nero', 'black screen'], ['preventivo', 'quote'], ['pezzo', 'part'], ['garanzia', 'warranty'], ['backup', 'backup'], ['tempo necessario', 'time needed']]},
  {id: 101, category: 'Tech', title: 'Charging Devices', description: 'Ask for chargers and outlets.', focus: [['caricare', 'charge'], ['presa USB', 'USB port'], ['power bank', 'power bank'], ['adattatore europeo', 'European adapter'], ['cavo lightning', 'Lightning cable'], ['cavo USB-C', 'USB-C cable'], ['batteria scarica', 'low battery'], ['presa libera', 'free outlet']]},
  {id: 102, category: 'Tech', title: 'Using a Map App', description: 'Use a map app for directions.', focus: [['posizione', 'location'], ['percorso', 'route'], ['navigazione', 'navigation'], ['a piedi', 'walking'], ['in auto', 'by car'], ['salvare', 'save'], ['offline', 'offline'], ['aggiornare', 'update']]},
  {id: 103, category: 'Tech', title: 'Video Call', description: 'Handle a simple video call.', focus: [['videochiamata', 'video call'], ['microfono', 'microphone'], ['telecamera', 'camera'], ['muto', 'muted'], ['condividere schermo', 'share screen'], ['connessione lenta', 'slow connection'], ['sentire bene', 'hear well'], ['vedere bene', 'see well']]},
  {id: 104, category: 'Tech', title: 'Online Booking', description: 'Make or discuss an online booking.', focus: [['sito web', 'website'], ['prenotazione online', 'online reservation'], ['conferma email', 'email confirmation'], ['codice QR', 'QR code'], ['account', 'account'], ['pagamento online', 'online payment'], ['errore', 'error'], ['annullare', 'cancel']]},
  {id: 105, category: 'Tech', title: 'ATM Machine', description: 'Use an ATM in Italian.', focus: [['prelevare', 'withdraw'], ['saldo', 'balance'], ['conto', 'account'], ['carta inserita', 'card inserted'], ['pin errato', 'wrong PIN'], ['commissione', 'fee'], ['contanti disponibili', 'cash available'], ['operazione', 'operation']]},
  {id: 106, category: 'Miscellaneous', title: 'Police Report', description: 'File a basic police report.', focus: [['polizia', 'police'], ['carabinieri', 'Carabinieri'], ['furto', 'theft'], ['documento perso', 'lost document'], ['denuncia', 'report'], ['descrizione persona', 'person description'], ['data', 'date'], ['firma', 'signature']]},
  {id: 107, category: 'Miscellaneous', title: 'Asking for Help', description: 'Ask a stranger for help politely.', focus: [['può aiutarmi', 'can you help me'], ['ho bisogno', 'I need'], ['non so', 'I do not know'], ['cercare', 'look for'], ['problema piccolo', 'small problem'], ['grazie davvero', 'thank you really'], ['molto gentile', 'very kind'], ['un momento', 'one moment']]},
  {id: 108, category: 'Miscellaneous', title: 'Talking About Money', description: 'Discuss simple money amounts.', focus: [['euro', 'euro'], ['centesimo', 'cent'], ['cambio', 'change'], ['banconota', 'banknote'], ['moneta', 'coin'], ['caro', 'expensive'], ['economico', 'cheap'], ['budget', 'budget']]},
  {id: 109, category: 'Miscellaneous', title: 'Time and Dates', description: 'Ask about times, dates, and schedules.', focus: [['che ore sono', 'what time is it'], ['mezzogiorno', 'noon'], ['mezzanotte', 'midnight'], ['settimana', 'week'], ['mese', 'month'], ['anno', 'year'], ['calendario', 'calendar'], ['puntuale', 'on time']]},
  {id: 110, category: 'Miscellaneous', title: 'Explaining a Mistake', description: 'Explain a misunderstanding or simple mistake.', focus: [['errore', 'mistake'], ['sbagliato', 'wrong'], ['pensavo', 'I thought'], ['confuso', 'confused'], ['riprovare', 'try again'], ['correggere', 'correct'], ['non volevo', 'I did not mean to'], ['va tutto bene', 'everything is okay']]},
];

function slug(input: string): string {
  return input
    .normalize('NFD')
    .replace(/[\u0300-\u036f]/g, '')
    .toLowerCase()
    .replace(/[^a-z0-9]+/g, '-')
    .replace(/^-|-$/g, '');
}

function uniqueTerms(...groups: TermPair[][]): TermPair[] {
  const seen = new Set<string>();
  const terms: TermPair[] = [];

  for (const group of groups) {
    for (const term of group) {
      const key = term[0].toLocaleLowerCase('it-IT');
      if (!seen.has(key)) {
        seen.add(key);
        terms.push(term);
      }
    }
  }

  return terms;
}

function buildVocabulary(blueprint: ScenarioBlueprint): ScenarioTerm[] {
  return uniqueTerms(
    essentialConnectors,
    categoryVocabulary[blueprint.category],
    blueprint.focus,
  )
    .slice(0, 50)
    .map(([italian, english], index) => ({
      id: `s${blueprint.id}-v${index + 1}-${slug(italian)}`,
      italian,
      english,
    }));
}

function focusTerm(blueprint: ScenarioBlueprint, index: number): TermPair {
  const term = blueprint.focus[index];
  if (!term) {
    throw new Error(
      `Scenario ${blueprint.id} ${blueprint.title} is missing focus term ${index + 1}`,
    );
  }

  return term;
}

function buildPhrases(blueprint: ScenarioBlueprint): ScenarioPhrase[] {
  const f = blueprint.focus;
  const pairs: TermPair[] = [
    [`Vorrei ${f[0]?.[0] || 'questo'}`, `I would like ${f[0]?.[1] || 'this'}`],
    [`Dov'è ${f[1]?.[0] || 'l\'uscita'}?`, `Where is ${f[1]?.[1] || 'the exit'}?`],
    [`Posso avere ${f[2]?.[0] || 'un\'informazione'}?`, `May I have ${f[2]?.[1] || 'some information'}?`],
    [`Non capisco ${f[3]?.[0] || 'bene'}`, `I do not understand ${f[3]?.[1] || 'well'}`],
    [`Per favore, ${f[4]?.[0] || 'mi aiuti'}`, `Please, ${f[4]?.[1] || 'help me'}`],
    [`Grazie mille`, `Thank you very much`],
  ];

  return pairs.map(([italian, english], index) => ({
    id: `s${blueprint.id}-p${index + 1}`,
    italian,
    english,
  }));
}

function buildSentences(blueprint: ScenarioBlueprint): ScenarioSentence[] {
  const a = focusTerm(blueprint, 0);
  const b = focusTerm(blueprint, 1);
  const c = focusTerm(blueprint, 2);
  const d = focusTerm(blueprint, 3);
  const e = focusTerm(blueprint, 4);
  const f = focusTerm(blueprint, 5);
  const g = focusTerm(blueprint, 6);
  const h = focusTerm(blueprint, 7);
  const pairs: Array<TermPair & {grammarPoint?: string}> = [
    Object.assign([`Vorrei ${a[0]}, per favore.`, `I would like ${a[1]}, please.`] as TermPair, {grammarPoint: 'Vorrei + noun/phrase for polite requests.'}),
    Object.assign([`Dov'è ${b[0]}?`, `Where is ${b[1]}?`] as TermPair, {grammarPoint: "Dov'è combines dove + è for where is."}),
    Object.assign([`Posso avere ${c[0]}?`, `May I have ${c[1]}?`] as TermPair, {grammarPoint: 'Posso avere is a polite service request.'}),
    Object.assign([`Non capisco ${d[0]}.`, `I do not understand ${d[1]}.`] as TermPair, {grammarPoint: 'Non goes before the verb for negation.'}),
    Object.assign([`È possibile con ${e[0]}?`, `Is it possible with ${e[1]}?`] as TermPair, {grammarPoint: 'È possibile asks if something is possible.'}),
    Object.assign([`Devo trovare ${f[0]}.`, `I have to find ${f[1]}.`] as TermPair, {grammarPoint: 'Devo + infinitive expresses obligation.'}),
    Object.assign([`Questo è ${g[0]}.`, `This is ${g[1]}.`] as TermPair, {grammarPoint: 'Questo è identifies a thing or situation.'}),
    Object.assign([`Va bene per ${h[0]}.`, `It is okay for ${h[1]}.`] as TermPair, {grammarPoint: 'Va bene confirms acceptance.'}),
  ];

  return pairs.map((sentence, index) => ({
    id: `s${blueprint.id}-s${index + 1}`,
    italian: sentence[0],
    english: sentence[1],
    grammarPoint: sentence.grammarPoint ?? 'Simple A1 sentence pattern.',
  }));
}

export const scenarios: Scenario[] = blueprints.map(blueprint => ({
  ...blueprint,
  vocabulary: buildVocabulary(blueprint),
  phrases: buildPhrases(blueprint),
  sentences: buildSentences(blueprint),
}));

export const scenarioCatalog = scenarios.map(({id, category, title, description}) => ({
  id,
  category,
  title,
  description,
}));
