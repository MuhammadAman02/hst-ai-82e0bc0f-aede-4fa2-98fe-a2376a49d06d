from nicegui import ui
import random
from datetime import datetime
from typing import List

# Add custom CSS for modern styling
ui.add_head_html('''
<style>
    .greeting-container {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        min-height: 100vh;
        padding: 2rem;
    }
    
    .greeting-card {
        background: rgba(255, 255, 255, 0.95);
        backdrop-filter: blur(10px);
        border-radius: 20px;
        box-shadow: 0 20px 40px rgba(0, 0, 0, 0.1);
        padding: 3rem;
        max-width: 600px;
        margin: 0 auto;
        text-align: center;
    }
    
    .greeting-title {
        font-size: 3rem;
        font-weight: 700;
        background: linear-gradient(135deg, #667eea, #764ba2);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 1rem;
    }
    
    .greeting-subtitle {
        font-size: 1.2rem;
        color: #6b7280;
        margin-bottom: 2rem;
    }
    
    .greeting-emoji {
        font-size: 4rem;
        margin: 1rem 0;
        animation: bounce 2s infinite;
    }
    
    @keyframes bounce {
        0%, 20%, 50%, 80%, 100% {
            transform: translateY(0);
        }
        40% {
            transform: translateY(-10px);
        }
        60% {
            transform: translateY(-5px);
        }
    }
    
    .greeting-button {
        background: linear-gradient(135deg, #667eea, #764ba2);
        border: none;
        color: white;
        padding: 1rem 2rem;
        border-radius: 50px;
        font-size: 1.1rem;
        font-weight: 600;
        cursor: pointer;
        transition: all 0.3s ease;
        margin: 0.5rem;
    }
    
    .greeting-button:hover {
        transform: translateY(-2px);
        box-shadow: 0 10px 20px rgba(102, 126, 234, 0.3);
    }
    
    .greeting-input {
        border: 2px solid #e5e7eb;
        border-radius: 10px;
        padding: 1rem;
        font-size: 1rem;
        width: 100%;
        margin: 1rem 0;
        transition: border-color 0.3s ease;
    }
    
    .greeting-input:focus {
        border-color: #667eea;
        outline: none;
    }
    
    .greeting-response {
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
        color: white;
        padding: 1.5rem;
        border-radius: 15px;
        margin: 1rem 0;
        font-size: 1.1rem;
        font-weight: 500;
    }
    
    .greeting-stats {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
        gap: 1rem;
        margin: 2rem 0;
    }
    
    .stat-card {
        background: #f8fafc;
        padding: 1rem;
        border-radius: 10px;
        text-align: center;
    }
    
    .stat-number {
        font-size: 2rem;
        font-weight: 700;
        color: #667eea;
    }
    
    .stat-label {
        font-size: 0.9rem;
        color: #6b7280;
        margin-top: 0.5rem;
    }
</style>
''')

class GreetingApp:
    def __init__(self):
        self.greeting_count = 0
        self.user_name = ""
        self.greetings_history: List[str] = []
        self.start_time = datetime.now()
        
        # Fun greeting responses
        self.greeting_responses = [
            "Hello there! 👋 Great to meet you!",
            "Hi! 🌟 Hope you're having a wonderful day!",
            "Hey! 🎉 Welcome to our friendly corner of the internet!",
            "Greetings! 🚀 Ready for something awesome?",
            "Hello! ✨ You've just made my day brighter!",
            "Hi there! 🌈 Thanks for stopping by!",
            "Hey! 🎊 What brings you here today?",
            "Hello! 🌸 Lovely to see you!",
        ]
        
        self.emojis = ["👋", "🌟", "🎉", "🚀", "✨", "🌈", "🎊", "🌸", "💫", "🎈"]

app_state = GreetingApp()

@ui.page('/')
def index():
    with ui.column().classes('greeting-container'):
        with ui.card().classes('greeting-card'):
            # Main greeting section
            ui.html('<div class="greeting-emoji">🤖</div>')
            ui.html('<h1 class="greeting-title">Hello!</h1>')
            ui.html('<p class="greeting-subtitle">Welcome to HST AI Greeting App</p>')
            
            # Interactive greeting section
            with ui.column().classes('w-full'):
                name_input = ui.input(
                    label="What's your name?",
                    placeholder="Enter your name here..."
                ).classes('greeting-input')
                
                greeting_display = ui.html('')
                
                def greet_user():
                    if name_input.value.strip():
                        app_state.user_name = name_input.value.strip()
                        app_state.greeting_count += 1
                        
                        # Select random greeting and emoji
                        greeting = random.choice(app_state.greeting_responses)
                        emoji = random.choice(app_state.emojis)
                        
                        # Personalized greeting
                        personalized_greeting = f"Hello {app_state.user_name}! {greeting} {emoji}"
                        app_state.greetings_history.append(personalized_greeting)
                        
                        # Update display
                        greeting_display.content = f'<div class="greeting-response">{personalized_greeting}</div>'
                        
                        # Update stats
                        update_stats()
                        
                        # Clear input
                        name_input.value = ""
                    else:
                        greeting_display.content = '<div class="greeting-response">Please enter your name first! 😊</div>'
                
                def surprise_greeting():
                    app_state.greeting_count += 1
                    surprise_messages = [
                        "🎉 Surprise! You're awesome!",
                        "✨ Random fact: You're amazing!",
                        "🌟 Surprise greeting activated!",
                        "🎊 You've been randomly selected for awesomeness!",
                        "🚀 Surprise! Hope this makes you smile!",
                    ]
                    message = random.choice(surprise_messages)
                    app_state.greetings_history.append(message)
                    greeting_display.content = f'<div class="greeting-response">{message}</div>'
                    update_stats()
                
                # Buttons
                with ui.row().classes('w-full justify-center'):
                    ui.button("Say Hello!", on_click=greet_user).classes('greeting-button')
                    ui.button("Surprise Me!", on_click=surprise_greeting).classes('greeting-button')
            
            # Stats section
            stats_container = ui.html('')
            
            def update_stats():
                uptime = datetime.now() - app_state.start_time
                uptime_minutes = int(uptime.total_seconds() / 60)
                
                stats_html = f'''
                <div class="greeting-stats">
                    <div class="stat-card">
                        <div class="stat-number">{app_state.greeting_count}</div>
                        <div class="stat-label">Greetings</div>
                    </div>
                    <div class="stat-card">
                        <div class="stat-number">{len(set(app_state.greetings_history))}</div>
                        <div class="stat-label">Unique Messages</div>
                    </div>
                    <div class="stat-card">
                        <div class="stat-number">{uptime_minutes}</div>
                        <div class="stat-label">Minutes Online</div>
                    </div>
                </div>
                '''
                stats_container.content = stats_html
            
            # Initialize stats
            update_stats()
            
            # Recent greetings section
            recent_greetings = ui.column().classes('w-full')
            
            def show_history():
                recent_greetings.clear()
                if app_state.greetings_history:
                    with recent_greetings:
                        ui.html('<h3 style="text-align: center; color: #667eea; margin: 2rem 0 1rem 0;">Recent Greetings</h3>')
                        for greeting in app_state.greetings_history[-5:]:  # Show last 5
                            ui.html(f'<div style="background: #f8fafc; padding: 0.5rem 1rem; margin: 0.25rem 0; border-radius: 8px; font-size: 0.9rem;">{greeting}</div>')
            
            ui.button("Show Recent Greetings", on_click=show_history).classes('greeting-button')
            
            # Footer
            ui.html('''
            <div style="text-align: center; margin-top: 3rem; color: #6b7280; font-size: 0.9rem;">
                <p>Built with ❤️ using NiceGUI</p>
                <p>HST AI Python Engineer - Production Ready Applications</p>
            </div>
            ''')

@ui.page('/health')
def health_check():
    """Health check endpoint for deployment monitoring"""
    return {"status": "healthy", "timestamp": datetime.now().isoformat()}