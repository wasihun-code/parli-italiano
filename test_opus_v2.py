import asyncio
import edge_tts

async def amain() -> None:
    # webm-24khz-16bit-mono-opus is a common format for Edge TTS
    communicate = edge_tts.Communicate("Ciao, come va?", "it-IT-ElsaNeural")
    await communicate.save("test_opus_direct.opus")

if __name__ == "__main__":
    asyncio.run(amain())
