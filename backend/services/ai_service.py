import httpx
import json
from config import OPENROUTER_API_KEY, OPENROUTER_BASE_URL, OPENROUTER_MODEL
from typing import Dict, Any, Optional

class AIService:
    @staticmethod
    async def query_ai(question: str, context: Optional[str] = None, model: str = OPENROUTER_MODEL) -> Dict[str, Any]:
        """Query OpenRouter AI with data context"""
        
        system_prompt = """You are a data analyst AI assistant. You have access to dataset information and should provide 
        clear, actionable insights based on the data context provided. Be concise and specific."""
        
        if context:
            system_prompt += f"\n\nDataset Context:\n{context}"
        
        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": question}
        ]
        
        try:
            headers = {
                "Authorization": f"Bearer {OPENROUTER_API_KEY}",
                "HTTP-Referer": "https://analytics-dashboard.app",
                "X-Title": "AI Data Analytics Dashboard",
                "Content-Type": "application/json"
            }
            
            payload = {
                "model": model,
                "messages": messages,
                "temperature": 0.7,
                "max_tokens": 1000
            }
            
            async with httpx.AsyncClient() as client:
                response = await client.post(
                    f"{OPENROUTER_BASE_URL}/chat/completions",
                    headers=headers,
                    json=payload,
                    timeout=30.0
                )
            
            if response.status_code == 200:
                result = response.json()
                answer = result['choices'][0]['message']['content']
                
                return {
                    "answer": answer,
                    "confidence": 0.9,
                    "model": model
                }
            else:
                return {
                    "answer": "Error querying AI",
                    "error": response.text,
                    "confidence": 0
                }
        
        except Exception as e:
            return {
                "answer": f"Error: {str(e)}",
                "confidence": 0,
                "error": str(e)
            }
    
    @staticmethod
    async def generate_report(dataset_summary: str, model: str = OPENROUTER_MODEL) -> Dict[str, Any]:
        """Generate AI-powered report"""
        
        prompt = f"""Based on the following dataset analysis, generate a professional data report with:
1. Executive Summary (2-3 sentences)
2. Key Findings (3-5 bullet points)
3. Recommendations (2-3 actionable items)

Dataset Summary:
{dataset_summary}

Please format as structured JSON."""
        
        messages = [
            {"role": "user", "content": prompt}
        ]
        
        try:
            headers = {
                "Authorization": f"Bearer {OPENROUTER_API_KEY}",
                "HTTP-Referer": "https://analytics-dashboard.app",
                "X-Title": "AI Data Analytics Dashboard"
            }
            
            payload = {
                "model": model,
                "messages": messages,
                "temperature": 0.7,
                "max_tokens": 2000
            }
            
            async with httpx.AsyncClient() as client:
                response = await client.post(
                    f"{OPENROUTER_BASE_URL}/chat/completions",
                    headers=headers,
                    json=payload
                )
            
            if response.status_code == 200:
                result = response.json()
                content = result['choices'][0]['message']['content']
                
                return {
                    "report": content,
                    "status": "success"
                }
            else:
                return {
                    "report": None,
                    "error": response.text,
                    "status": "error"
                }
        
        except Exception as e:
            return {
                "report": None,
                "error": str(e),
                "status": "error"
            }
