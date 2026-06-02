import json

translations = {
    'abbiamo': 'we have', 'abbinati': 'matching', 'accettata': 'accepted', 'affare': 'bargain', 
    'aiutarla': 'help you', 'anche': 'also', 'arrivederci': 'goodbye', 'artigianato': 'craftsmanship', 
    'attenzione': 'attention', 'avete': 'you have', 'avvolgo': 'I wrap', 'bancomat': 'debit card', 
    'bella': 'beautiful', 'belli': 'beautiful', 'bellissime': 'very beautiful', 'bellissimi': 'very beautiful', 
    'bene': 'well', 'benissimo': 'very well', 'benvenuto': 'welcome', 'bicchieri': 'glasses', 
    'buona': 'good', 'buongiorno': 'good morning', 'carta': 'card', 'cartoline': 'postcards', 
    'casa': 'home', 'centesimi': 'cents', 'ceramica': 'ceramic', 'ceramiche': 'ceramics', 
    'cerca': 'looks for', 'cercando': 'looking for', 'cercava': 'was looking for', 'cerco': 'I look for', 
    'certamente': 'certainly', 'certo': 'sure', 'che': 'that', 'cinquanta': 'fifty', 
    'cinque': 'five', 'città': 'city', 'clienti': 'customers', 'codice': 'code', 
    'colorati': 'colored', 'comprare': 'to buy', 'con': 'with', 'confezione': 'packaging', 
    'contanti': 'cash', 'corretto': 'correct', 'costa': 'costs', 'costano': 'they cost', 
    'così': 'so', 'dei': 'some', 'della': 'of the', 'delle': 'some', 
    'desidera': 'desires', 'devo': 'I must', 'dipinte': 'painted', 'due': 'two', 
    'ecco': 'here is', 'esattamente': 'exactly', 'euro': 'euro', 'faccia': 'face/do', 
    'faccio': 'I do', 'fatto': 'done', 'favore': 'favor', 'fondo': 'bottom', 
    'fragili': 'fragile', 'francobolli': 'stamps', 'giornata': 'day', 'gli': 'the', 
    'gratuita': 'free', 'grazie': 'thank you', 'idea': 'idea', 'importi': 'amounts', 
    'inserire': 'to insert', 'inserito': 'inserted', 'lavorati': 'worked', 'legno': 'wood', 
    'lei': 'you/she', 'lettore': 'reader', 'locale': 'local', 'madre': 'mother', 
    'magnete': 'magnet', 'magneti': 'magnets', 'mano': 'hand', 'mia': 'my', 
    'mille': 'thousand', 'molte': 'many', 'molto': 'very', 'nel': 'in the', 
    'nella': 'in the', 'nessun': 'no', 'non': 'not', 'nostre': 'our', 
    'nostri': 'our', 'oggetti': 'objects', 'oggi': 'today', 'ora': 'now', 
    'ottima': 'excellent', 'ottimo': 'excellent', 'pacchetto': 'package', 'paga': 'pays', 
    'pagare': 'to pay', 'particolare': 'particular', 'per': 'for', 'perfetto': 'perfect', 
    'pezzo': 'piece', 'piatti': 'plates', 'piccola': 'small', 'piccoli': 'small', 
    'piccolo': 'small', 'pos': 'POS', 'posso': 'I can', 'posto': 'place', 
    'prendo': 'I take', 'preoccupi': 'worry', 'prezzo': 'price', 'problema': 'problem', 
    'prodotto': 'product', 'proprio': 'just/own', 'protettiva': 'protective', 'può': 'can', 
    'qualcosa': 'something', 'quanti': 'how many', 'quanto': 'how much', 'quello': 'that', 
    'questa': 'this', 'questi': 'these', 'qui': 'here', 'quindi': 'therefore', 
    'quindici': 'fifteen', 'regalo': 'gift', 'ringrazio': 'I thank', 'salve': 'hello', 
    'scaffale': 'shelf', 'scatola': 'box', 'scelta': 'choice', 'scontrino': 'receipt', 
    'segreto': 'secret', 'sei': 'six', 'serve': 'is needed', 'servono': 'are needed', 
    'set': 'set', 'sette': 'seven', 'signore': 'sir', 'sono': 'are', 
    'sto': 'I am', 'sullo': 'on the', 'tipica': 'typical', 'tipico': 'typical', 
    'totale': 'total', 'transazione': 'transaction', 'tre': 'three', 'trenta': 'thirty', 
    'trovare': 'to find', 'trovato': 'found', 'tutto': 'all', 'uno': 'one', 
    'vedo': 'I see', 'verde': 'green', 'volte': 'times', 'vorrei': 'I would like'
}

file_path = 'src/data/exports/shopping/souvenir_shop/shopping_souvenir_shop_vocabulary.json'
with open(file_path, 'r') as f:
    data = json.load(f)

for item in data:
    if not item.get('english'):
        item['english'] = translations.get(item['italian'], 'missing')

with open(file_path, 'w') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print("Updated vocabulary translations.")
