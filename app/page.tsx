"use client"

import { useState } from "react"
import Dashboard from "@/components/dashboard"

export default function Home() {
  const [sidebarOpen, setSidebarOpen] = useState(true)

  return (
    <main className="flex h-screen bg-background">
      <Dashboard sidebarOpen={sidebarOpen} setSidebarOpen={setSidebarOpen} />
    </main>
  )
}
