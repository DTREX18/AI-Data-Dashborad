// Base API configuration for connecting to FastAPI backend

export const API_BASE_URL = process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000"

export class APIClient {
  static async post(endpoint: string, data: any) {
    const response = await fetch(`${API_BASE_URL}${endpoint}`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(data),
    })
    return response.json()
  }

  static async get(endpoint: string) {
    const response = await fetch(`${API_BASE_URL}${endpoint}`)
    return response.json()
  }

  static async uploadFile(endpoint: string, file: File) {
    const formData = new FormData()
    formData.append("file", file)
    const response = await fetch(`${API_BASE_URL}${endpoint}`, {
      method: "POST",
      body: formData,
    })
    return response.json()
  }
}
