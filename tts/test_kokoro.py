import os
os.environ['PHONEMIZER_ESPEAK_LIBRARY'] = '/usr/lib/libespeak-ng.so.1'

# Set it directly on the class BEFORE kokoro imports anything
from phonemizer.backend.espeak.wrapper import EspeakWrapper
EspeakWrapper.set_library('/usr/lib/libespeak-ng.so.1')

from kokoro import KPipeline
import soundfile as sf

pipeline = KPipeline(lang_code='it')
generator = pipeline("Ciao, come stai? Benvenuto!", voice='if_sara')

for i, (_, _, audio) in enumerate(generator):
    sf.write("test_italian.wav", audio, 24000)
    print("✅ Success! Saved test_italian.wav")
    break
