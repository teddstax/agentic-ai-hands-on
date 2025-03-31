# 🧠 Agentic AI Workshop Script – Langflow + OpenAI + Astra DB

## 🎯 Doel van de workshop
Leer hoe je een eenvoudige AI-agent bouwt met Langflow, deze verrijkt met Retrieval-Augmented Generation (RAG) via Astra DB, en vervolgens uitbreidt met tools voor krachtige agentic AI-functionaliteit.

---

## 🛠️ Benodigdheden (vooraf installeren)
```bash
pip install langflow openai astrapy python-dotenv
```

Zorg ook voor:
- Een OpenAI API key
- Een Astra DB account en project met aangemaakte vector-collectie

---

## 📦 Workshop Stappenplan

### 1. 🔹 Introductie: Wat is een Agent?
Een agent is een AI die input ontvangt, context begrijpt en acties onderneemt via tools of geheugen. We bouwen vandaag een simpele agent en breiden die uit met geheugen, kennis, en tools.

---

### 2. 🧱 Setup van een Eenvoudige Langflow Agent
**Doel:** Maak een flow met input → model → output

#### Stappen:
1. Open Langflow of gebruik Python-code:
```python
from langflow import LangflowGraph
from langflow.base.components import ChatInput, ChatOutput, OpenAIModel

graph = LangflowGraph(name="SimpleAgent")

input_node = ChatInput(name="UserInput")
model_node = OpenAIModel(name="OpenAIModel", model_name="gpt-4")
output_node = ChatOutput(name="AgentOutput")

graph.connect(input_node, model_node)
graph.connect(model_node, output_node)
```
2. Test een simpele prompt zoals:
> "Wat is het verschil tussen AI en machine learning?"

---

### 3. 📚 Retrieval-Augmented Generation (RAG) met Astra DB
**Doel:** Voeg externe kennis toe aan je agent

#### Voorbereiding:
- Upload een dataset naar je Astra DB (bijv. een aantal documenten over het onderwerp 'duurzaamheid')
- Verzamel je `ASTRA_DB_TOKEN`, `API_ENDPOINT`, `KEYSPACE`, en `COLLECTION_NAME`

#### Stappen:
```python
from langflow.components.vectorstores import AstraDBVectorStore
from langflow.components.retrievers import VectorStoreRetriever
from langflow.components.memory import ContextualMemory

astra_vectorstore = AstraDBVectorStore(
    name="AstraStore",
    token="<ASTRA_DB_TOKEN>",
    api_endpoint="<ASTRA_DB_API_ENDPOINT>",
    keyspace="<ASTRA_DB_KEYSPACE>",
    collection_name="knowledge"
)

retriever = VectorStoreRetriever(name="AstraRetriever")
memory = ContextualMemory(name="ContextualMemory")

graph.connect(astra_vectorstore, retriever)
graph.connect(retriever, memory)
graph.connect(input_node, memory)
graph.connect(memory, model_node)
```

#### Voorbeeldvraag:
> "Wat zijn de belangrijkste principes van circulaire economie?"

---

### 4. 🧠 Agentic Gedrag toevoegen met Tools
**Doel:** Laat de agent zelfstandig taken uitvoeren met tools zoals web search of rekenen

#### Stappen:
```python
from langflow.components.tools import ToolNode

search_tool = ToolNode(name="SearchTool", tool_type="web_search")
calculator_tool = ToolNode(name="Calculator", tool_type="math")

graph.connect(input_node, search_tool)
graph.connect(search_tool, model_node)
graph.connect(input_node, calculator_tool)
graph.connect(calculator_tool, model_node)
```

#### Voorbeeldvragen:
> "Zoek het laatste nieuws over CO2-compensatie"
> 
> "Wat is 1,5 keer de CO2-uitstoot van Nederland in 2023?"

---

## 🌍 Case: Duurzame Toekomstscenario's (voor Agentic AI)
**Context:** Stel je hebt een AI-agent die overheidsdocumenten, klimaatakkoorden en economische rapporten heeft geïndexeerd in Astra DB. Je wilt hem vragen laten beantwoorden en plannen laten opstellen op basis van real-world kennis.

#### Voorbeelden:
- "Stel een stappenplan op voor een stad om in 2035 CO2-neutraal te zijn."
- "Welke subsidies zijn beschikbaar in Nederland voor circulair bouwen?"
- "Maak een inschatting van de economische impact van een 10% reductie in stikstof."

---

## ✅ Afronden & Reflectie
- Wat heb je gebouwd?
- Hoe zie je de rol van agentic AI in jouw werkveld?
- Wat zijn ethische overwegingen bij het inzetten van zelfredzame AI-systemen?

---

## 🧩 Bonus: Vervolg
- Integreer je eigen API’s als tools
- Voeg planningsmodules toe (langchain agents, task decomposition)
- Gebruik voice- of multimodale input

Veel succes en plezier met het bouwen van je eigen Agentic AI! 🚀
