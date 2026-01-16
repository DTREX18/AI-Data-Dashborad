from fastapi import APIRouter, HTTPException, Body
from services.ai_service import AIService
from models.schemas import ChatMessage, AIResponse

router = APIRouter()

@router.post("/ai/chat", response_model=AIResponse)
async def chat_with_data(message: ChatMessage = Body(...)):
    """Chat with your data using AI"""
    try:
        result = await AIService.query_ai(message.question, message.context)
        
        return AIResponse(
            answer=result.get("answer", "No response"),
            confidence=result.get("confidence", 0)
        )
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
