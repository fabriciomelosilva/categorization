from fastapi import FastAPI
from pydantic import BaseModel
import spacy
 
app = FastAPI()
 
# Carrega o modelo de português
nlp = spacy.load('pt_core_news_lg')
 
class Texto(BaseModel):
    texto: str
 
@app.post("/entidades")
async def obter_entidades(dados: Texto):
    doc = nlp(dados.texto)
    entidades = [{"texto": ent.text, "categoria": ent.label_} for ent in doc.ents]
    return {"entidades": entidades}
