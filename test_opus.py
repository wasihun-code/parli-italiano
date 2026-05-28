import asyncio
import edge_tts

async def amain() -> None:
    communicate = edge_tts.Communicate("Ciao, come va?", "it-IT-ElsaNeural")
    await communicate.save("test_out.opus")

if __name__ == "__main__":
    asyncio.run(amain())
