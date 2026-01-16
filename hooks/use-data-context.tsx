"use client"

import type React from "react"

import { createContext, useContext } from "react"

interface DataContextType {
  fileId: string
  filename: string
}

const DataContext = createContext<DataContextType | null>(null)

export function useDataContext() {
  const context = useContext(DataContext)
  if (!context) {
    // Return default values if context not available
    return {
      fileId: "",
      filename: "",
    }
  }
  return context
}

export function DataProvider({
  children,
  fileId,
  filename,
}: { children: React.ReactNode; fileId: string; filename: string }) {
  return <DataContext.Provider value={{ fileId, filename }}>{children}</DataContext.Provider>
}
