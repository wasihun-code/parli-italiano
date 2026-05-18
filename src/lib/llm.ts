export type LlmMessage = {
  role: string;
  content: string;
};

const OLLAMA_CHAT_URL = '/ollama/api/chat';
const OLLAMA_MODEL = import.meta.env.VITE_OLLAMA_MODEL || 'llama3.1:8b';

type OllamaChatResponse = {
  message?: {
    content?: string;
  };
  error?: string;
};

export async function initLlama(): Promise<void> {
  return undefined;
}

export async function generateResponse(messages: LlmMessage[], customModel: string = OLLAMA_MODEL): Promise<string> {
  const model = customModel;
  console.log(`[LLM] Starting request to model: ${model}`, { messageCount: messages.length });

  const controller = new AbortController();
  // Increase timeout to 10 minutes to accommodate slow model loading on 8GB RAM
  const timeoutId = setTimeout(() => controller.abort(), 600000);

  try {
    const response = await fetch(OLLAMA_CHAT_URL, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'ngrok-skip-browser-warning': 'true',
      },
      body: JSON.stringify({
        model,
        messages,
        stream: false,
      }),
      signal: controller.signal,
    });
    clearTimeout(timeoutId);

    console.log(`[LLM] Received response status: ${response.status} ${response.statusText}`);

    const responseText = await response.text();
    if (!response.ok) {
      console.error(`[LLM] Error response: ${responseText}`);
      throw new Error(`Ollama responded with ${response.status}: ${responseText.slice(0, 300)}`);
    }

    console.log(`[LLM] Raw response text length: ${responseText.length}`);


    let data: OllamaChatResponse;
    try {
      data = JSON.parse(responseText) as OllamaChatResponse;
    } catch (error) {
      throw new Error(`Ollama proxy returned non-JSON content: ${responseText.slice(0, 300)}`, {cause: error});
    }

    if (data.error) {
      throw new Error(`Ollama returned an error: ${data.error}`);
    }

    const content = data.message?.content?.trim();
    if (!content) {
      throw new Error('Ollama returned an empty response.');
    }

    return content;
  } catch (error) {
    console.error('Ollama chat request failed', error);
    const detail = error instanceof Error ? ` ${error.message}` : '';
    throw new Error(`Antonio cannot reach Ollama through the app server.${detail}`, {cause: error});
  }
}

export async function unloadLlama(): Promise<void> {
  return undefined;
}
