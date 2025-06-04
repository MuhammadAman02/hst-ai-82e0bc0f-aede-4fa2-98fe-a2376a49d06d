from nicegui import ui
import asyncio
import random
from datetime import datetime
from typing import List

# Add modern CSS styling
ui.add_head_html('''
<style>
    .gradient-bg {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        min-height: 100vh;
    }
    
    .glass-card {
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(10px);
        border-radius: 20px;
        border: 1px solid rgba(255, 255, 255, 0.2);
        box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
    }
    
    .pulse-animation {
        animation: pulse 2s infinite;
    }
    
    @keyframes pulse {
        0% { transform: scale(1); }
        50% { transform: scale(1.05); }
        100% { transform: scale(1); }
    }
    
    .fade-in {
        animation: fadeIn 1s ease-in;
    }
    
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    .typing-animation {
        overflow: hidden;
        border-right: 2px solid #fff;
        white-space: nowrap;
        animation: typing 3s steps(40, end), blink-caret 0.75s step-end infinite;
    }
    
    @keyframes typing {
        from { width: 0; }
        to { width: 100%; }
    }
    
    @keyframes blink-caret {
        from, to { border-color: transparent; }
        50% { border-color: #fff; }
    }
</style>
''')

class GreetingApp:
    def __init__(self):
        self.greeting_count = 0
        self.user_name = ""
        self.greetings = [
            "Hello there! 👋",
            "Welcome! 🎉",
            "Greetings! 🌟",
            "Hi! Nice to meet you! 😊",
            "Hello and welcome! 🚀",
            "Hey there! 👋✨"
        ]
        self.fun_facts = [
            "🤖 I can build full-stack Python applications in minutes!",
            "⚡ I use NiceGUI for rapid, beautiful UI development",
            "🎨 I automatically select professional color schemes and images",
            "🔧 I follow enterprise-grade architecture patterns",
            "🚀 I create production-ready, deployable applications",
            "💡 I can integrate databases, APIs, and authentication seamlessly"
        ]

    async def animate_greeting(self, container):
        """Animate the greeting message with typing effect"""
        greeting = random.choice(self.greetings)
        
        with container:
            ui.html(f'''
                <div class="typing-animation" style="font-size: 2rem; color: white; margin: 20px 0;">
                    {greeting}
                </div>
            ''')
        
        await asyncio.sleep(2)

    async def show_capabilities(self, container):
        """Show AI capabilities with animated cards"""
        capabilities = [
            {"icon": "🎯", "title": "Instant Applications", "desc": "Production-ready apps in seconds"},
            {"icon": "🎨", "title": "Beautiful UI", "desc": "Modern, responsive designs"},
            {"icon": "⚡", "title": "High Performance", "desc": "Optimized for speed and scale"},
            {"icon": "🔒", "title": "Secure by Default", "desc": "Enterprise-grade security"},
            {"icon": "🚀", "title": "Deploy Anywhere", "desc": "Docker, Fly.io, cloud-ready"},
            {"icon": "🧠", "title": "AI-Powered", "desc": "Intelligent architecture decisions"}
        ]
        
        with container:
            with ui.grid(columns=3).classes('w-full gap-4 mt-8'):
                for cap in capabilities:
                    with ui.card().classes('glass-card p-6 text-center fade-in'):
                        ui.html(f'<div style="font-size: 3rem; margin-bottom: 10px;">{cap["icon"]}</div>')
                        ui.label(cap["title"]).classes('text-xl font-bold text-white mb-2')
                        ui.label(cap["desc"]).classes('text-gray-200')

    def get_random_fact(self):
        """Get a random fun fact about the AI"""
        return random.choice(self.fun_facts)

    async def handle_user_greeting(self, name_input, response_container):
        """Handle user's personalized greeting"""
        name = name_input.value.strip()
        if not name:
            ui.notify("Please enter your name! 😊", type='warning')
            return
        
        self.user_name = name
        self.greeting_count += 1
        
        response_container.clear()
        
        with response_container:
            # Personalized greeting
            with ui.card().classes('glass-card p-8 text-center mb-6'):
                ui.html(f'''
                    <div class="fade-in">
                        <h2 style="color: white; font-size: 2.5rem; margin-bottom: 20px;">
                            Hello, {name}! 🎉
                        </h2>
                        <p style="color: #e2e8f0; font-size: 1.2rem; margin-bottom: 20px;">
                            Welcome to the future of Python development!
                        </p>
                        <p style="color: #cbd5e0; font-size: 1rem;">
                            Greeting #{self.greeting_count} • {datetime.now().strftime("%B %d, %Y at %I:%M %p")}
                        </p>
                    </div>
                ''')
            
            # Fun fact
            with ui.card().classes('glass-card p-6 mb-6'):
                ui.label("💡 Did you know?").classes('text-xl font-bold text-white mb-3')
                ui.label(self.get_random_fact()).classes('text-gray-200 text-lg')
            
            # Interactive buttons
            with ui.row().classes('w-full justify-center gap-4'):
                ui.button("🎲 Another Fun Fact", 
                         on_click=lambda: self.show_new_fact(response_container)
                         ).classes('bg-purple-600 hover:bg-purple-700 text-white px-6 py-3 rounded-lg')
                
                ui.button("🚀 Build Something Amazing", 
                         on_click=lambda: self.show_project_ideas(response_container)
                         ).classes('bg-blue-600 hover:bg-blue-700 text-white px-6 py-3 rounded-lg')

    def show_new_fact(self, container):
        """Show a new random fact"""
        ui.notify(self.get_random_fact(), type='info', timeout=5000)

    def show_project_ideas(self, container):
        """Show project ideas the user can build"""
        ideas = [
            "📊 Interactive Dashboard with Real-time Data",
            "🛒 E-commerce Platform with Payment Integration", 
            "📱 Social Media Analytics Tool",
            "🎮 Multiplayer Game with WebSocket Support",
            "📈 Financial Portfolio Tracker",
            "🤖 AI-Powered Chatbot Interface",
            "📝 Collaborative Document Editor",
            "🎵 Music Streaming Application"
        ]
        
        with ui.dialog() as dialog, ui.card().classes('w-96'):
            ui.label("🚀 What would you like to build?").classes('text-xl font-bold mb-4')
            
            for idea in ideas:
                with ui.row().classes('w-full items-center mb-2'):
                    ui.label(idea).classes('flex-grow')
                    ui.button("Build", 
                             on_click=lambda i=idea: self.start_project(i, dialog)
                             ).classes('bg-green-600 hover:bg-green-700 text-white px-3 py-1 rounded')
        
        dialog.open()

    def start_project(self, idea, dialog):
        """Start building a project"""
        dialog.close()
        ui.notify(f"Great choice! Let's build: {idea}", type='positive')
        ui.notify("Just describe your requirements and I'll create a complete application for you! 🎯", type='info')

# Initialize the app
app = GreetingApp()

@ui.page('/')
async def index():
    """Main greeting page with beautiful animations and interactions"""
    
    # Main container with gradient background
    with ui.column().classes('gradient-bg w-full min-h-screen items-center justify-center p-8'):
        
        # Header section
        with ui.card().classes('glass-card p-8 text-center mb-8 max-w-4xl'):
            ui.html('''
                <div class="fade-in">
                    <h1 style="color: white; font-size: 3.5rem; margin-bottom: 20px; font-weight: bold;">
                        🤖 HST AI Python Engineer
                    </h1>
                    <p style="color: #e2e8f0; font-size: 1.5rem; margin-bottom: 30px;">
                        Your Elite Python Application Architect
                    </p>
                    <p style="color: #cbd5e0; font-size: 1.1rem; line-height: 1.6;">
                        I create production-ready Python applications with beautiful UIs, 
                        enterprise architecture, and zero-configuration deployment.
                    </p>
                </div>
            ''')
        
        # Capabilities showcase
        capabilities_container = ui.column().classes('w-full max-w-6xl')
        await app.show_capabilities(capabilities_container)
        
        # Interactive greeting section
        with ui.card().classes('glass-card p-8 mt-8 max-w-2xl'):
            ui.label("👋 Let's get acquainted!").classes('text-2xl font-bold text-white mb-6 text-center')
            
            with ui.row().classes('w-full items-end gap-4'):
                name_input = ui.input("What's your name?").classes('flex-grow').props('outlined dense')
                name_input.props('dark color=white')
                
                ui.button("Say Hello! 🎉", 
                         on_click=lambda: app.handle_user_greeting(name_input, response_container)
                         ).classes('bg-gradient-to-r from-purple-600 to-blue-600 hover:from-purple-700 hover:to-blue-700 text-white px-6 py-3 rounded-lg pulse-animation')
        
        # Response container for personalized greetings
        response_container = ui.column().classes('w-full max-w-4xl mt-6')
        
        # Footer
        with ui.row().classes('mt-12 text-center'):
            ui.label("Ready to build something amazing? Just tell me what you need! 🚀").classes('text-white text-lg')

@ui.page('/health')
def health_check():
    """Health check endpoint for deployment monitoring"""
    return {"status": "healthy", "timestamp": datetime.now().isoformat()}

# Add some interactive elements that showcase NiceGUI capabilities
@ui.page('/demo')
def demo_page():
    """Demo page showcasing various NiceGUI components"""
    
    with ui.column().classes('gradient-bg w-full min-h-screen p-8'):
        with ui.card().classes('glass-card p-8 max-w-4xl mx-auto'):
            ui.label("🎮 Interactive Demo").classes('text-3xl font-bold text-white mb-6')
            
            # Interactive counter
            counter = ui.label("0").classes('text-6xl font-bold text-white text-center')
            count = 0
            
            def increment():
                nonlocal count
                count += 1
                counter.text = str(count)
                if count % 10 == 0:
                    ui.notify(f"🎉 You reached {count}!", type='positive')
            
            def decrement():
                nonlocal count
                count = max(0, count - 1)
                counter.text = str(count)
            
            with ui.row().classes('justify-center gap-4 mt-4'):
                ui.button("➖", on_click=decrement).classes('bg-red-600 hover:bg-red-700 text-white text-2xl px-4 py-2 rounded-full')
                ui.button("➕", on_click=increment).classes('bg-green-600 hover:bg-green-700 text-white text-2xl px-4 py-2 rounded-full')
            
            ui.separator().classes('my-8')
            
            # Color picker demo
            ui.label("🎨 Pick a color:").classes('text-xl text-white mb-4')
            color_display = ui.html('<div style="width: 100px; height: 100px; background: #667eea; border-radius: 10px; margin: 20px auto;"></div>')
            
            def update_color(e):
                color_display.content = f'<div style="width: 100px; height: 100px; background: {e.value}; border-radius: 10px; margin: 20px auto;"></div>'
            
            ui.color_input(on_change=update_color, value='#667eea').classes('mx-auto')
            
            ui.separator().classes('my-8')
            
            # Real-time clock
            clock = ui.label().classes('text-2xl text-white text-center')
            
            async def update_clock():
                while True:
                    clock.text = f"🕐 {datetime.now().strftime('%H:%M:%S')}"
                    await asyncio.sleep(1)
            
            # Start the clock
            ui.timer(1.0, update_clock)
            
            # Navigation
            with ui.row().classes('justify-center mt-8'):
                ui.button("🏠 Back to Home", on_click=lambda: ui.open('/')).classes('bg-blue-600 hover:bg-blue-700 text-white px-6 py-3 rounded-lg')