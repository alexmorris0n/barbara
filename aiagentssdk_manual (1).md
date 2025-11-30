# SignalWire AI Agents SDK in Python

**By Brian West and Anthony Minessale II**

---

# Table of Contents


## Getting Started

- What You'll Learn
  - Agent
  - SWML (SignalWire Markup Language)
  - SWAIG Functions
  - Skills
- Installation
  - System Requirements
  - Basic Installation
  - Verify Installation
  - Installation Extras
  - Installation from Source
  - Virtual Environment Setup
  - Quick Verification Script
  - Troubleshooting
  - What Gets Installed
  - Next Steps
- Quick Start: Your First Agent
  - The Minimal Agent
  - Run the Agent
  - Test the Agent
  - What Just Happened?
  - Adding a Custom Function
  - Using the Debug Endpoint
  - Test with swaig-test CLI
  - Complete Example with Multiple Features
  - Next Steps
- Development Environment Setup
  - Recommended Project Structure
  - Create the Project
  - Environment Variables
  - Loading Environment Variables
  - The .gitignore File
  - Requirements File
  - IDE Configuration
  - Using swaig-test for Development
  - Development Workflow
  - Sample Agent Module
  - Testing Your Agent
  - Next Steps
- Exposing Your Agent to the Internet
  - Why You Need a Public URL
  - Installing ngrok
  - Create an ngrok Account (Free)
  - Basic Usage
  - Test the Tunnel
  - ngrok Web Interface
  - Static Domains (Recommended)
  - Understanding Basic Authentication
  - Configure Your Agent for ngrok
  - Complete Development Setup
  - Using a Script
  - Alternative Tunneling Solutions
  - Production Alternatives
  - Troubleshooting
  - What's Next?
  - You've Completed Phase 1!

## Core Concepts

- What You'll Learn
  - AuthMixin - Authentication & Security
  - WebMixin - HTTP Server & Routing
  - SWMLService - SWML Document Generation
  - PromptMixin - Prompt Management
  - ToolMixin - SWAIG Function Management
  - SkillMixin - Skill Plugin Management
  - AIConfigMixin - AI Behavior Configuration
  - ServerlessMixin - Deployment Adapters
  - StateMixin - State Management
  - ToolRegistry
  - PromptManager
  - SessionManager
  - SkillManager
  - SchemaUtils
  - VerbHandlerRegistry
- SWML (SignalWire Markup Language)
  - What is SWML?
  - SWML Document Structure
  - Common Verbs
  - A Complete SWML Example
  - The `ai` Verb in Detail
  - How Your Agent Generates SWML
  - SWML Rendering Pipeline
  - Viewing Your SWML
  - SWML Schema Validation
  - Common SWML Patterns
  - Next Steps
- SWAIG (SignalWire AI Gateway)
  - What is SWAIG?
  - SWAIG in SWML
  - Defining SWAIG Functions
  - Function Handler Signature
  - SwaigFunctionResult
  - Common Actions
  - SWAIG Request Flow
  - SWAIG Request Format
  - SWAIG Response Format
  - Function Parameters (JSON Schema)
  - Webhook Security
  - Testing SWAIG Functions
  - Best Practices
  - Next Steps
- Request Lifecycle
  - The Complete Call Flow
  - Phase 1: Call Setup
  - Phase 2: SWML Generation
  - Phase 3: AI Conversation
  - Phase 4: Function Calls
  - Phase 5: Call End
  - Handling Post-Prompt
  - Request/Response Headers
  - Debugging the Lifecycle
  - Error Handling
  - Next Steps
- Security
  - Security Layers
  - HTTP Basic Authentication
  - Function Token Security
  - HTTPS Configuration
  - Security Best Practices
  - Configuring SignalWire Webhooks
  - Summary
  - Next Steps

## Building Agents

- What You'll Learn
  - Pattern 1: Class-Based Agent
  - Pattern 2: Functional Agent
  - Pattern 3: Multi-Agent Server
  - Method 1: Class-Based (Recommended)
  - Method 2: Instance-Based
  - Method 3: Declarative (PROMPT_SECTIONS)
  - Configuration Methods
  - Runtime Methods
- Static vs Dynamic Agents
  - Understanding the Difference
  - Static Agents
  - Dynamic Agents
  - Request Data Fields
  - Dynamic Function Registration
  - Multi-Tenant Applications
  - Comparison Summary
  - Best Practices
- Prompts & POM
  - Why POM?
  - POM Structure
  - Adding Sections
  - Subsections
  - Declarative Prompts (PROMPT_SECTIONS)
  - POM Builder Direct Access
  - Post-Call Prompts
  - Voice-Optimized Prompts
  - Prompt Best Practices
  - Generated Prompt Output
  - Returns
  - Billing
- Voice & Language
  - Voice Configuration Overview
  - Adding a Language
  - Available TTS Engines
  - Filler Phrases
  - Multi-Language Support
  - Pronunciation Rules
  - Set Multiple Pronunciations
  - Voice Selection Guide
  - Dynamic Voice Selection
  - Language Codes Reference
  - Complete Voice Configuration Example
- AI Parameters
  - Parameter Categories
  - Setting Parameters
  - Essential Parameters
  - Use Case Presets
  - Tuning Guide
  - Complete Example
  - More Parameters
- Hints
  - Why Use Hints?
  - Adding Simple Hints
  - What to Hint
  - Hint Examples by Use Case
  - Pattern Hints (Advanced)
  - Organizing Hints
  - Dynamic Hints
  - Hint Best Practices
  - Testing Hints
  - Complete Example
  - Next Steps
- Call Flow Customization
  - Understanding Call Flow
  - Verb Insertion Methods
  - Pre-Answer Verbs
  - Post-Answer Verbs
  - Post-AI Verbs
  - Complete Example
  - Controlling Answer Behavior
  - Dynamic Call Flow
  - Clear Methods
  - Method Chaining
  - Related Documentation

## SWAIG Functions

- What You'll Learn
- Parameters
  - Parameter Structure
  - Parameter Types
  - String Parameters
  - Enum Parameters
  - Number Parameters
  - Boolean Parameters
  - Array Parameters
  - Object Parameters
  - Optional vs Required Parameters
  - Default Values
  - Parameter Descriptions
  - Complex Example
  - Validating Parameters
  - Parameter Best Practices
- Results & Actions
  - Basic Results
  - SwaigFunctionResult Components
  - Method Chaining
  - Call Transfer
  - Send SMS
  - Payment Processing
  - Call Recording
  - Audio Tapping
  - Call Control
  - Hang Up
  - Speech Control
  - Background Audio
  - Update Global Data
  - Metadata Management
  - Context Switching
  - Function Control
  - Conference & Rooms
  - Post-Processing
  - Multiple Actions
  - Advanced: Execute Raw SWML
  - Action Reference
- DataMap
  - When to Use DataMap
  - DataMap Flow
  - Basic DataMap
  - Variable Substitution
  - DataMap Builder Methods
  - Complete Example
  - DataMap Best Practices
- Native Functions
  - What Are Native Functions?
  - Enabling Native Functions
  - Web Search Function
  - Debug Function
  - Call Transfers
  - Combining Native and Custom Functions
  - When to Use Native vs Custom Functions
  - Native Functions Reference
  - Next Steps

## Skills

- What You'll Learn
  - Use Built-in Skills When:
  - Create Custom Skills When:
  - Use SWAIG Functions When:
  - SkillBase (Abstract Base Class)
  - SkillRegistry (Discovery & Loading)
  - 1. Tools (Functions)
  - 2. Prompt Sections
  - 3. Speech Hints
  - 4. Global Data
- Built-in Skills
  - Available Skills
  - datetime
  - math
  - web_search
  - wikipedia_search
  - weather_api
  - joke
  - play_background_file
  - swml_transfer
  - datasphere
  - native_vector_search
  - Skills Summary Table
- Adding Skills
  - Basic Usage
  - With Configuration
  - Method Chaining
  - Multiple Skills
  - Checking Loaded Skills
  - Removing Skills
  - Multi-Instance Skills
  - SWAIG Fields
  - Error Handling
  - Skills with Environment Variables
  - Complete Example
  - Best Practices
- Custom Skills
  - Skill Structure
  - Basic Custom Skill
  - Required Class Attributes
  - Required Methods
  - Optional Methods
  - Parameter Schema
  - Multi-Instance Skills
  - Complete Example
  - Using Custom Skills
- Skill Configuration
  - Configuration Methods
  - Parameter Dictionary
  - Parameter Schema
  - Parameter Properties
  - Environment Variables
  - SWAIG Fields
  - External Skill Directories
  - Entry Points
  - Listing Available Skills
  - Multi-Instance Configuration
  - Configuration Validation
  - Complete Configuration Example
  - Configuration Best Practices
  - Next Steps

## Advanced Topics

- What You'll Learn
  - Contexts & Workflows
  - State Management
  - Call Recording
  - Call Transfer
  - Multi-Agent Servers
  - Search & Knowledge
  - set_text()
  - add_section() / add_bullets()
  - set_step_criteria()
  - set_valid_steps()
  - set_functions()
  - set_valid_contexts()
  - set_isolated()
  - set_system_prompt()
  - set_user_prompt()
  - set_consolidate()
  - set_full_reset()
  - add_enter_filler() / add_exit_filler()
  - Within Context (Steps)
  - Between Contexts
  - Context Entry Behavior
- State Management
  - State Types Overview
  - Global Data
  - Metadata
  - Post-Prompt Data
  - Accessing Call Information
  - State Flow Diagram
  - Complete Example
  - DataMap Variable Access
  - State Methods Summary
  - Best Practices
- Call Recording
  - Recording Overview
  - Basic Recording
  - Recording Parameters
  - Stereo Recording
  - Direction Options
  - Recording with Webhook
  - Auto-Stop Recording
  - Stop Recording
  - Recording with Beep
  - Complete Example
  - Recording Best Practices
- Call Transfer
  - Transfer Types
  - Basic Phone Transfer
  - Connect Method Parameters
  - Permanent vs Temporary Transfer
  - SIP Transfer
  - Transfer with Caller ID Override
  - SWML Transfer
  - Transfer Flow
  - Department Transfer Example
  - Sending SMS During Transfer
  - Post-Process Transfer
  - Transfer Methods Summary
  - Best Practices
- Multi-Agent Servers
  - When to Use AgentServer
  - Basic AgentServer
  - AgentServer Configuration
  - Registering Agents
  - Server Architecture
  - Managing Agents
  - SIP Routing
  - SIP Routing Flow
  - Health Check Endpoint
  - Serverless Deployment
  - Complete Example
  - AgentServer Methods Summary
  - Best Practices
- Search & Knowledge
  - Search System Overview
  - Building Search Indexes
  - Chunking Strategies
  - Installing Search Dependencies
  - Using Search in Agents
  - Skill Configuration Options
  - pgvector Backend
  - Search Flow
  - CLI Commands
  - Complete Example
  - Multiple Knowledge Bases
  - Search Best Practices

## Deployment

- What You'll Learn
  - Custom Host and Port
  - Using serve() Directly
  - View SWML Output
  - Using swaig-test CLI
  - Using ngrok
  - Using localtunnel
- Production Deployment
  - Production Checklist
  - Environment Variables
  - Running with Uvicorn Workers
  - Systemd Service
  - Nginx Reverse Proxy
  - Production Architecture
  - SSL Configuration
  - Health Checks
  - Logging Configuration
  - Monitoring
  - Scaling Considerations
  - Security Best Practices
- Serverless Deployment
  - Serverless Overview
  - AWS Lambda
  - Google Cloud Functions
  - Azure Functions
  - Testing Serverless Locally
  - Force Mode Override
  - Serverless Best Practices
  - Multi-Agent Serverless
  - Environment Detection
- Docker & Kubernetes
  - Dockerfile
  - requirements.txt
  - Application Entry Point
  - Building and Running
  - Docker Compose
  - Kubernetes Deployment
  - Kubernetes Architecture
  - Deploying to Kubernetes
  - Horizontal Pod Autoscaler
  - Multi-Architecture Builds
  - Container Best Practices
- CGI Mode
  - CGI Overview
  - CGI Detection
  - Basic CGI Script
  - CGI Request Flow
  - Apache Configuration
  - nginx Configuration
  - CGI Host Configuration
  - Testing CGI Locally
  - Authentication in CGI Mode
  - Directory Structure
  - Shared Hosting Deployment
  - CGI Best Practices
  - Common CGI Issues
  - Migration from CGI

## SignalWire Integration

- What You'll Learn
  - Step 1: Account Setup
  - Step 2: Phone Number
  - Step 3: Deploy Agent
  - Step 4: Connect
- Phone Numbers
  - Purchasing Numbers
  - Number Types
  - Number Features
  - Managing Numbers
  - Number Settings
  - SIP Endpoints
  - Number Porting
  - Costs
  - Multiple Numbers
- Mapping Numbers
  - Overview
  - Configure Voice URL
  - URL Format
  - HTTPS Requirements
  - Using ngrok for Development
  - Basic Authentication
  - Multi-Agent Server
  - SWML Scripts
  - Fallback URL
  - Status Callbacks
  - Verification Checklist
- Testing
  - Testing Stages
  - swaig-test CLI
  - Local Server Testing
  - Using ngrok
  - Test Call Checklist
  - Viewing Logs
  - Debugging with Logs
  - Testing Transfers
  - Testing SMS
  - Load Testing
  - Common Test Scenarios
  - Automated Testing
- Troubleshooting
  - Connection Issues
  - Authentication Errors
  - SWML Errors
  - No Speech Response
  - Function Not Called
  - Function Errors
  - SSL Certificate Issues
  - Timeout Issues
  - Quick Diagnostic Steps
  - Getting Help
  - Common Error Messages
  - Logging for Debugging

## Prefab Agents

- What Are Prefabs?
  - InfoGatherer
  - FAQBot
  - Survey
  - Receptionist
  - Concierge
  - Questions
  - key_name Values
  - Dynamic Questions
- FAQBot
  - Basic Usage
  - FAQ Format
  - Constructor Parameters
  - With Categories
  - Built-in Functions
  - Custom Persona
  - Complete Example
  - Best Practices
- Survey
  - Basic Usage
  - Question Types
  - Question Format
  - Constructor Parameters
  - Built-in Functions
  - Survey Flow
  - Complete Example
  - Best Practices
- Receptionist
  - Basic Usage
  - Department Format
  - Constructor Parameters
  - Built-in Functions
  - Call Flow
  - Complete Example
  - Best Practices
- Concierge
  - Basic Usage
  - Amenity Format
  - Constructor Parameters
  - Built-in Functions
  - Concierge Flow
  - Complete Example
  - Best Practices

## Reference

- Reference Overview
  - API Reference
  - CLI Tools
  - Configuration
  - Creating an Agent
  - Defining a Function
  - Returning Actions
  - prompt_add_section
  - prompt_add_text
  - get_prompt
  - add_language
  - set_voice
  - tool (decorator)
  - define_tool
  - add_skill
  - list_available_skills
  - set_params
  - add_hints
  - add_pronounce
  - set_global_data
  - get_full_url
  - set_web_hook_url
  - set_post_prompt_url
  - run
  - get_app
  - serverless_handler
  - cloud_function_handler
  - azure_function_handler
  - on_summary
  - set_dynamic_config_callback
  - enable_sip_routing
  - register_sip_username
- SWMLService API
  - Class Definition
  - Constructor
  - Core Responsibilities
  - Document Methods
  - Auto-Generated Verb Methods
  - Server Methods
  - Authentication Methods
  - URL Building Methods
  - Routing Methods
  - Security Configuration
  - Schema Utils
  - Verb Registry
  - Instance Attributes
  - Usage Example
  - Relationship to AgentBase
- SWAIG Function API
  - Overview
  - Decorator Syntax
  - Decorator Parameter Details
  - Parameter Types
  - Type Mapping
  - Programmatic Definition
  - Handler Function Signature
  - Raw Data Contents
  - Accessing Raw Data
  - Secure Functions
  - Fillers and Wait Files
  - Return Value Requirements
  - Complete Example
- SwaigFunctionResult API
  - Class Definition
  - Constructor
  - Core Concept
  - Basic Methods
  - Call Control Actions
  - Speech Actions
  - Data Actions
  - Media Actions
  - Recording Actions
  - Messaging Actions
  - Payment Actions
  - Context Actions
  - Conference Actions
  - Tap/Stream Actions
  - SIP Actions
  - Advanced Actions
  - Settings Actions
  - Method Chaining
  - to_dict Method
- DataMap API
  - Class Definition
  - Overview
  - Constructor
  - Core Methods
  - Parameter Types
  - Webhook Methods
  - Output Methods
  - Variable Patterns
  - Expression Methods
  - Array Processing
  - Foreach Configuration
  - Webhook Expressions
  - Registering with Agent
  - Complete Example
- SkillBase API
  - Class Definition
  - Overview
  - Class Attributes
  - Class Attributes Reference
  - Constructor
  - Instance Attributes
  - Abstract Methods (Must Implement)
  - Helper Methods
  - Optional Override Methods
  - Parameter Schema
  - Parameter Schema Fields
  - Complete Skill Example
  - Using Skills
  - Skill Directory Structure
- ContextBuilder API
  - Class Definitions
  - Overview
  - Step Class
  - Step Context Switch Methods
  - ContextBuilder Class
  - Using with AgentBase
  - Multiple Contexts Example
  - Step Flow Diagram
  - Generated SWML Structure
- swaig-test CLI
  - Overview
  - Command Syntax
  - Quick Reference
  - Basic Usage
  - Actions
  - Common Options
  - SWML Generation
  - SWML Generation Options
  - Function Execution
  - Function Execution Options
  - Multi-Agent Files
  - Dynamic Agent Testing
  - Data Customization Options
  - Advanced Data Overrides
  - Serverless Simulation
  - Environment Variables
  - DataMap Function Testing
  - Cross-Platform Testing
  - Output Options
  - Extended Help
  - Complete Workflow Examples
  - Exit Codes
  - Troubleshooting
- sw-search CLI
  - Overview
  - Architecture
  - Command Modes
  - Quick Start
  - Building Indexes
  - Chunking Strategies
  - Model Selection
  - File Filtering
  - Tags and Metadata
  - Searching Indexes
  - Interactive Search Shell
  - PostgreSQL/pgvector Backend
  - Migration
  - Local vs Remote Modes
  - Remote Search CLI
  - Validation
  - JSON Export
  - NLP Backend Selection
  - Complete Configuration Example
  - Using with Skills
  - Output Formats
  - Installation Requirements
  - API Reference
  - Troubleshooting
  - Related Documentation
- Environment Variables
  - Overview
  - Authentication Variables
  - SSL/TLS Variables
  - Proxy Variables
  - Security Variables
  - Logging Variables
  - Skills Variables
  - Serverless Platform Variables
  - Quick Reference
  - Example .env File
  - Loading Environment Variables
  - Environment Detection
- Config Files
  - Overview
  - File Formats
  - File Discovery
  - Service Section
  - Security Section
  - Configuration Sections
  - Agent Section
  - Skills Section
  - Logging Section
  - Environment Variable Substitution
  - Complete Example
  - Using Config Files
  - Priority Order
  - Config Validation
  - Multiple Configurations
- SWML Schema
  - Overview
  - Basic Structure
  - Required Fields
  - AI Verb
  - AI Verb Parameters
  - SWAIG Object
  - Function Definition
  - Common Verbs
  - Contexts Structure
  - Step Structure
  - DataMap Structure
  - Prompt Object (POM)
  - Language Configuration
  - Model Parameters
  - Schema Validation
  - Full Example

## Examples

- How to Use This Chapter
  - By Feature
  - By Complexity
  - Minimal Agent
  - Agent with Function
  - Agent with Transfer
  - Minimal Agent
  - Class-Based Agent
  - Simple Function
  - Function with Multiple Parameters
  - Secure Function
  - Weather Lookup
  - Expression-Based Control
  - Simple Transfer
  - Temporary Transfer
  - DateTime Skill
  - Search Skill
  - Setting Initial State
  - Enable Call Recording
  - Send Confirmation SMS
  - Serving Static Files Alongside Agents
  - Speech Recognition Hints
  - Pronunciation Rules
- Examples by Complexity
  - Beginner Examples
  - Intermediate Examples
  - Advanced Examples
  - Expert Examples
  - Complexity Progression

## Appendix

- About This Chapter
  - Temperature
  - Reasoning Effort
  - Key Timeouts
  - Hard Stop Time
  - Hold Music with Tone
- Design Patterns
  - Overview
  - Decorator Pattern
  - Class-Based Agent Pattern
  - Multi-Agent Router Pattern
  - State Machine Pattern (Contexts)
  - DataMap Integration Pattern
  - Skill Composition Pattern
  - Dynamic Configuration Pattern
  - Pattern Selection Guide
- Best Practices
  - Overview
  - Prompt Design
  - Function Design
  - Error Handling
  - Security
  - Performance
  - Testing
  - Monitoring
  - Production Readiness Checklist
- Troubleshooting
  - Quick Diagnostics
  - Startup Issues
  - Function Issues
  - Connection Issues
  - Speech Recognition Issues
  - Timing Issues
  - DataMap Issues
  - Variable Syntax Reference
  - Skill Issues
  - Serverless Issues
  - Common Error Messages
  - Getting Help
- Migration Guide
  - Current Version
  - Before Upgrading
  - Upgrading
  - Migration from Raw SWML
  - Common Migration Tasks
  - Class-Based Migration
  - Multi-Agent Migration
  - Testing After Migration
  - Getting Help
- Changelog
  - Version History
  - Version 1.0.4
  - Version 1.0.3
  - Version 1.0.2
  - Version 1.0.1
  - Version 1.0.0
  - Versioning Policy
  - Upgrade Notifications
  - Reporting Issues
  - Contributing

---

# Part: Getting Started

---

# Getting Started

> **Summary**: Everything you need to install the SignalWire Agents SDK, create your first voice AI agent, and connect it to the SignalWire platform.

## What You'll Learn

This chapter walks you through the complete setup process:

1. **Introduction** - Understand what the SDK does and key concepts
2. **Installation** - Install the SDK and verify it works
3. **Quick Start** - Build your first agent in under 5 minutes
4. **Development Environment** - Set up a professional development workflow
5. **Exposing Your Agent** - Make your agent accessible to SignalWire using ngrok

## Prerequisites

Before starting, ensure you have:

- **Python 3.8 or higher** installed on your system
- **pip** (Python package manager)
- A **terminal/command line** interface
- A **text editor or IDE** (VS Code, PyCharm, etc.)
- (Optional) A **SignalWire account** for testing with real phone calls

## Time to Complete

| Section | Time |
|---------|------|
| Introduction | 5 min read |
| Installation | 5 min |
| Quick Start | 5 min |
| Dev Environment | 10 min |
| Exposing Agents | 10 min |
| **Total** | **~35 minutes** |

## By the End of This Chapter

You will have:

- A working voice AI agent
- Accessible via public URL
- Ready to connect to SignalWire phone numbers

```diagram
┌──────────────┐    ┌──────────────┐    ┌─────────────────┐
│  SignalWire  │◄──►│    ngrok     │◄──►│  Your Agent     │
│    Cloud     │    │   (tunnel)   │    │  localhost:3000 │
└──────────────┘    └──────────────┘    └─────────────────┘
```

## What is the SignalWire Agents SDK?

The SignalWire Agents SDK lets you create **voice AI agents** - intelligent phone-based assistants that can:

- Answer incoming phone calls automatically
- Have natural conversations using AI (GPT-4, Claude, etc.)
- Execute custom functions (check databases, call APIs, etc.)
- Transfer calls, play audio, and manage complex call flows
- Scale from development to production seamlessly

## How It Works

```diagram
┌─────────────────────────────────────────────────────────────────────────────┐
│                         High-Level Architecture                             │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│   Phone Call                                                                │
│       │                                                                     │
│       ▼                                                                     │
│  ┌─────────────────┐                    ┌─────────────────┐                 │
│  │                 │   SWML Request     │                 │                 │
│  │   SignalWire    │ ─────────────────► │   Your Agent    │                 │
│  │     Cloud       │                    │  (Python Server)│                 │
│  │                 │   SWML Response    │                 │                 │
│  │  • Routes calls │ ◄───────────────── │  • Defines AI   │                 │
│  │  • Runs AI      │                    │    behavior     │                 │
│  │  • Handles TTS  │   Function Calls   │  • Provides     │                 │
│  │  • Handles STT  │ ─────────────────► │    functions    │                 │
│  │                 │                    │  • Handles      │                 │
│  │                 │   Function Results │    webhooks     │                 │
│  │                 │ ◄───────────────── │                 │                 │
│  └─────────────────┘                    └─────────────────┘                 │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

**The flow:**

1. A caller dials your SignalWire phone number
2. SignalWire requests instructions from your agent (via HTTP)
3. Your agent returns **SWML** (SignalWire Markup Language) - a JSON document describing how to handle the call
4. SignalWire's AI talks to the caller based on your configuration
5. When the AI needs to perform actions, it calls your **SWAIG functions** (webhooks)
6. Your functions return results, and the AI continues the conversation

## Key Concepts

### Agent

An **Agent** is your voice AI application. It's a Python class that:

- Defines the AI's personality and behavior (via prompts)
- Provides functions the AI can call (SWAIG functions)
- Configures voice, language, and AI parameters
- Runs as a web server that responds to SignalWire requests

```python
from signalwire_agents import AgentBase


class MyAgent(AgentBase):
    def __init__(self):
        super().__init__(name="my-agent")
        # Configure your agent here
```

### SWML (SignalWire Markup Language)

**SWML** is a JSON format that tells SignalWire how to handle calls. Your agent generates SWML automatically - you don't write it by hand.

```json
{
  "version": "1.0.0",
  "sections": {
    "main": [
      {"answer": {}},
      {"ai": {
        "prompt": {"text": "You are a helpful assistant..."},
        "SWAIG": {"functions": [...]}
      }}
    ]
  }
}
```

### SWAIG Functions

**SWAIG** (SignalWire AI Gateway) functions are tools your AI can use during a conversation. When a caller asks something that requires action, the AI calls your function.

```python
@agent.tool(description="Look up a customer by phone number")
def lookup_customer(phone_number: str) -> str:
    customer = database.find(phone_number)
    return f"Customer: {customer.name}, Account: {customer.id}"
```

### Skills

**Skills** are reusable plugins that add capabilities to your agent. The SDK includes built-in skills for common tasks:

- `datetime` - Get current time and date
- `web_search` - Search the web
- `weather_api` - Get weather information
- `math` - Perform calculations

```python
agent.add_skill("datetime")
agent.add_skill("web_search", google_api_key="...")
```

## What You Can Build

| Use Case | Description |
|----------|-------------|
| **Customer Service** | Answer FAQs, route calls, collect information |
| **Appointment Scheduling** | Book, reschedule, and cancel appointments |
| **Surveys & Feedback** | Conduct phone surveys, collect responses |
| **IVR Systems** | Interactive voice menus with AI intelligence |
| **Receptionist** | Screen calls, take messages, transfer to staff |
| **Notifications** | Outbound calls for alerts, reminders, confirmations |

## SDK Features

| Category | Features |
|----------|----------|
| Core | AgentBase class, SWAIG function decorators, Prompt building (POM), Voice & language config, Speech hints, Built-in skills |
| Advanced | Multi-step workflows (Contexts), Multi-agent servers, Call recording, Call transfer (SIP, PSTN), State management, Vector search integration |
| Deployment | Local dev server, Production (uvicorn), AWS Lambda, Google Cloud Functions, Azure Functions, CGI mode, Docker/Kubernetes |
| Developer Tools | swaig-test CLI, SWML debugging, Function testing, Serverless simulation |
| Prefab Agents | InfoGathererAgent, FAQBotAgent, SurveyAgent, ReceptionistAgent, ConciergeAgent |
| DataMap | Direct API calls from SignalWire, No webhook server needed, Variable expansion, Response mapping |

## Minimal Example

Here's the simplest possible agent:

```python
from signalwire_agents import AgentBase


class HelloAgent(AgentBase):
    def __init__(self):
        super().__init__(name="hello")
        self.prompt_add_section("Role", "You are a friendly assistant.")


if __name__ == "__main__":
    agent = HelloAgent()
    agent.run()
```

This agent:

- Starts a web server on port 3000
- Returns SWML that configures an AI assistant
- Uses the default voice and language settings
- Has no custom functions (just conversation)

## Next Steps

Now that you understand what the SDK does, let's install it and build something real.


---

## Installation

> **Summary**: Install the SignalWire Agents SDK using pip and verify everything works correctly.

### System Requirements

| Requirement | Minimum | Recommended |
|-------------|---------|-------------|
| Python | 3.8+ | 3.10+ |
| pip | 20.0+ | Latest |
| OS | Linux, macOS, Windows | Any |
| Memory | 512MB | 1GB+ |

### Basic Installation

Install the SDK from PyPI:

```bash
pip install signalwire-agents
```

This installs the core SDK with all essential features for building voice AI agents.

### Verify Installation

Confirm the installation was successful:

```bash
python -c "from signalwire_agents import AgentBase; print('SignalWire Agents SDK installed successfully!')"
```

You should see:

```
SignalWire Agents SDK installed successfully!
```

### Installation Extras

The SDK provides optional extras for additional features:

#### Search Capabilities

```bash
## Query-only (read .swsearch files) - ~400MB
pip install signalwire-agents[search-queryonly]

## Build indexes + vector search - ~500MB
pip install signalwire-agents[search]

## Full document processing (PDF, DOCX) - ~600MB
pip install signalwire-agents[search-full]

## NLP features (spaCy) - ~600MB
pip install signalwire-agents[search-nlp]

## All search features - ~700MB
pip install signalwire-agents[search-all]
```

#### Database Support

```bash
## PostgreSQL vector database support
pip install signalwire-agents[pgvector]
```

#### Development Dependencies

```bash
## All development tools (testing, linting)
pip install signalwire-agents[dev]
```

### Installation from Source

For development or to get the latest changes:

```bash
## Clone the repository
git clone https://github.com/signalwire/signalwire-agents.git
cd signalwire-agents

## Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

## Install in development mode
pip install -e .

## Or with extras
pip install -e ".[search,dev]"
```

### Virtual Environment Setup

Always use a virtual environment to avoid conflicts:

```bash
## Create virtual environment
python -m venv venv

## Activate (Linux/macOS)
source venv/bin/activate

## Activate (Windows Command Prompt)
venv\Scripts\activate

## Activate (Windows PowerShell)
venv\Scripts\Activate.ps1

## Install the SDK
pip install signalwire-agents

## Verify activation (should show venv path)
which python
```

### Quick Verification Script

```python
#!/usr/bin/env python3
## verify_install.py - Verify SignalWire Agents SDK installation
"""Verify SignalWire Agents SDK installation."""

def main():
    print("Checking SignalWire Agents SDK installation...\n")

    # Check core import
    try:
        from signalwire_agents import AgentBase
        print("[OK] Core SDK: AgentBase imported successfully")
    except ImportError as e:
        print(f"[FAIL] Core SDK: Failed to import AgentBase - {e}")
        return False

    # Check SWAIG function support
    try:
        from signalwire_agents import SwaigFunctionResult
        print("[OK] SWAIG: SwaigFunctionResult imported successfully")
    except ImportError as e:
        print(f"[FAIL] SWAIG: Failed to import SwaigFunctionResult - {e}")
        return False

    # Check prefabs
    try:
        from signalwire_agents.prefabs import InfoGathererAgent
        print("[OK] Prefabs: InfoGathererAgent imported successfully")
    except ImportError as e:
        print(f"[FAIL] Prefabs: Failed to import - {e}")

    # Check search (optional)
    try:
        from signalwire_agents.search import SearchEngine
        print("[OK] Search: SearchEngine available")
    except ImportError:
        print("[SKIP] Search: Not installed (optional)")

    print("\n" + "="*50)
    print("Installation verification complete!")
    print("="*50)
    return True


if __name__ == "__main__":
    main()
```

Run it:

```bash
python verify_install.py
```

Expected output:

```
Checking SignalWire Agents SDK installation...

[OK] Core SDK: AgentBase imported successfully
[OK] SWAIG: SwaigFunctionResult imported successfully
[OK] Prefabs: InfoGathererAgent imported successfully
[SKIP] Search: Not installed (optional)

==================================================
Installation verification complete!
==================================================
```

### Troubleshooting

#### Common Issues

| Problem | Cause | Solution |
|---------|-------|----------|
| `ModuleNotFoundError: No module named 'signalwire_agents'` | Package not installed | Run `pip install signalwire-agents` |
| `pip: command not found` | pip not in PATH | Use `python -m pip install signalwire-agents` |
| Permission errors | Installing globally without sudo | Use virtual environment or `pip install --user` |
| Old pip version | pip can't resolve dependencies | Run `pip install --upgrade pip` |
| Conflicts with other packages | Dependency version mismatch | Use a fresh virtual environment |

#### Python Version Check

Ensure you have Python 3.8+:

```bash
python --version
## or
python3 --version
```

If you have multiple Python versions:

```bash
## Use specific version
python3.10 -m venv venv
source venv/bin/activate
pip install signalwire-agents
```

#### Upgrade Existing Installation

```bash
pip install --upgrade signalwire-agents
```

#### Clean Reinstall

```bash
pip uninstall signalwire-agents
pip cache purge
pip install signalwire-agents
```

### What Gets Installed

The SDK installs these core dependencies:

| Package | Purpose |
|---------|---------|
| `fastapi` | Web framework for serving SWML |
| `uvicorn` | ASGI server for running the agent |
| `pydantic` | Data validation and settings |
| `structlog` | Structured logging |
| `httpx` | HTTP client for API calls |

### Next Steps

Now that the SDK is installed, let's create your first agent.



---

## Quick Start: Your First Agent

> **Summary**: Build a working voice AI agent in under 5 minutes with a single Python file.

### The Minimal Agent

```python
#!/usr/bin/env python3
## my_first_agent.py - A simple voice AI agent
"""
My First SignalWire Agent

A simple voice AI agent that greets callers and has conversations.
"""

from signalwire_agents import AgentBase


class MyFirstAgent(AgentBase):
    def __init__(self):
        super().__init__(name="my-first-agent")

        # Set the voice
        self.add_language("English", "en-US", "rime.spore")

        # Define the AI's personality and behavior
        self.prompt_add_section(
            "Role",
            "You are a friendly and helpful assistant. Greet the caller warmly "
            "and help them with any questions they have. Keep responses concise "
            "and conversational."
        )

        self.prompt_add_section(
            "Guidelines",
            body="Follow these rules:",
            bullets=[
                "Be friendly and professional",
                "Keep responses brief (1-2 sentences when possible)",
                "If you don't know something, say so honestly",
                "End conversations politely when the caller is done"
            ]
        )


if __name__ == "__main__":
    agent = MyFirstAgent()
    print("Starting My First Agent...")
    print("Server running at: http://localhost:3000")
    print("Press Ctrl+C to stop")
    agent.run()
```

### Run the Agent

Start your agent:

```bash
python my_first_agent.py
```

You'll see output like:

```
[12:29:56] INFO     security_config (info:72) security_config_loaded
    (service=SWMLService, ssl_enabled=False, domain=None,
    allowed_hosts=['*'], cors_origins=['*'], max_request_size=10485760,
    rate_limit=60, use_hsts=True, has_basic_auth=False)
[12:29:56] INFO     swml_service    (info:72) service_initializing
    (service=my-first-agent, route=, host=0.0.0.0, port=3000)
[12:29:56] INFO     agent_base      (info:72) agent_initializing
    (agent=my-first-agent, route=/, host=0.0.0.0, port=3000)
Starting My First Agent...
Server running at: http://localhost:3000
Press Ctrl+C to stop
[12:29:56] INFO     agent_base      (info:72) agent_starting
    (agent=my-first-agent, url=http://localhost:3000, username=signalwire,
    password_length=43, auth_source=provided, ssl_enabled=False)
Agent 'my-first-agent' is available at:
URL: http://localhost:3000
Basic Auth: signalwire:7vVZ8iMTOWL0Y7-BG6xaN3qhjmcm4Sf59nORNdlF9bs
    (source: provided)
INFO:     Started server process [49982]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:3000 (Press CTRL+C to quit)
```

**Note:** The SDK shows:

- Security configuration (SSL, CORS, rate limits)
- Service initialization details
- Basic auth credentials (username and password)
- Server startup information

### Test the Agent

Open a new terminal and test with curl. Use the Basic Auth credentials shown in the agent output:

```bash
## Get the SWML document (what SignalWire receives)
## Replace the password with the one from your agent's output
curl -u signalwire:7vVZ8iMTOWL0Y7-BG6xaN3qhjmcm4Sf59nORNdlF9bs \
  http://localhost:3000/
```

**Note:** The `-u` flag provides Basic Auth credentials in the format `username:password`. Use the exact password shown in your agent's startup output.

You'll see JSON output like:

```json
{
  "version": "1.0.0",
  "sections": {
    "main": [
      {"answer": {}},
      {
        "ai": {
          "prompt": {
            "text": "# Role\nYou are a friendly and helpful assistant..."
          },
          "languages": [
            {"name": "English", "code": "en-US", "voice": "rime.spore"}
          ]
        }
      }
    ]
  }
}
```

### What Just Happened?

**1. You run: `python my_first_agent.py`**

Agent starts a web server on port 3000.

**2. SignalWire (or curl) sends: `GET http://localhost:3000/`**

Agent returns SWML document (JSON).

**3. SWML tells SignalWire:**
- Answer the call
- Use this AI prompt (your personality config)
- Use this voice (rime.spore)
- Use English language

**4. SignalWire's AI:**
- Converts caller's speech to text (STT)
- Sends text to AI model (GPT-4, etc.)
- Gets AI response
- Converts response to speech (TTS)

### Adding a Custom Function

Let's add a function the AI can call:

```python
#!/usr/bin/env python3
## my_first_agent_with_function.py - Agent with custom function
"""
My First SignalWire Agent - With Custom Function
"""

from signalwire_agents import AgentBase, SwaigFunctionResult


class MyFirstAgent(AgentBase):
    def __init__(self):
        super().__init__(name="my-first-agent")

        # Set the voice
        self.add_language("English", "en-US", "rime.spore")

        # Define the AI's personality
        self.prompt_add_section(
            "Role",
            "You are a friendly assistant who can tell jokes. "
            "When someone asks for a joke, use your tell_joke function."
        )

        # Register the custom function
        self.define_tool(
            name="tell_joke",
            description="Tell a joke to the caller",
            parameters={"type": "object", "properties": {}},
            handler=self.tell_joke
        )

    def tell_joke(self, args, raw_data):
        """Return a joke for the AI to tell."""
        import random
        jokes = [
            "Why do programmers prefer dark mode? Because light attracts bugs!",
            "Why did the Python programmer need glasses? Because they couldn't C!",
            "What's a programmer's favorite hangout spot? Foo Bar!",
        ]
        joke = random.choice(jokes)
        return SwaigFunctionResult(f"Here's a joke: {joke}")


if __name__ == "__main__":
    agent = MyFirstAgent()
    print("Starting My First Agent (with jokes!)...")
    print("Server running at: http://localhost:3000")
    agent.run()
```

Now when a caller asks for a joke, the AI will call your `tell_joke` function!

### Using the Debug Endpoint

The agent provides a debug endpoint to inspect its configuration:

```bash
curl http://localhost:3000/debug
```

This shows detailed information about:

- Registered functions
- Prompt configuration
- Voice settings
- Authentication credentials

### Test with swaig-test CLI

The SDK includes a CLI tool for testing:

```bash
## Show the SWML document
swaig-test my_first_agent.py --dump-swml

## List available functions
swaig-test my_first_agent.py --list-tools

## Test a function
swaig-test my_first_agent.py --exec tell_joke
```

### Complete Example with Multiple Features

Here's a more complete example showing common patterns:

```python
#!/usr/bin/env python3
## complete_first_agent.py - Complete agent example with multiple features
"""
Complete First Agent Example

Demonstrates:

- Voice configuration
- AI parameters
- Prompt sections
- Custom functions
- Speech hints
"""

from signalwire_agents import AgentBase, SwaigFunctionResult


class CompleteFirstAgent(AgentBase):
    def __init__(self):
        super().__init__(
            name="complete-agent",
            auto_answer=True,
            record_call=False
        )

        # Voice and language
        self.add_language("English", "en-US", "rime.spore")

        # AI behavior parameters
        self.set_params({
            "end_of_speech_timeout": 500,      # Wait 500ms for speaker to finish
            "attention_timeout": 15000         # 15 second attention span
        })

        # Speech recognition hints (improves accuracy)
        self.add_hints([
            "SignalWire",
            "SWML",
            "AI agent"
        ])

        # Prompt sections
        self.prompt_add_section(
            "Identity",
            "You are Alex, a helpful AI assistant created by SignalWire."
        )

        self.prompt_add_section(
            "Capabilities",
            body="You can help callers with:",
            bullets=[
                "Answering general questions",
                "Telling jokes",
                "Providing the current time",
                "Basic conversation"
            ]
        )

        self.prompt_add_section(
            "Style",
            "Keep responses brief and friendly. Use a conversational tone."
        )

        # Register functions
        self.define_tool(
            name="get_current_time",
            description="Get the current time",
            parameters={"type": "object", "properties": {}},
            handler=self.get_current_time
        )

        self.define_tool(
            name="tell_joke",
            description="Tell a random joke",
            parameters={"type": "object", "properties": {}},
            handler=self.tell_joke
        )

    def get_current_time(self, args, raw_data):
        """Return the current time."""
        from datetime import datetime
        now = datetime.now()
        return SwaigFunctionResult(f"The current time is {now.strftime('%I:%M %p')}")

    def tell_joke(self, args, raw_data):
        """Return a random joke."""
        import random
        jokes = [
            "Why do programmers prefer dark mode? Because light attracts bugs!",
            "Why did the developer go broke? Because they used up all their cache!",
            "There are only 10 types of people: those who understand binary and those who don't.",
        ]
        return SwaigFunctionResult(random.choice(jokes))


if __name__ == "__main__":
    agent = CompleteFirstAgent()

    print("="*60)
    print("Complete First Agent")
    print("="*60)
    print(f"Server: http://localhost:3000")
    print(f"Debug:  http://localhost:3000/debug")
    print("")
    print("Features:")
    print("  - Custom voice (rime.spore)")
    print("  - Speech hints for better recognition")
    print("  - Two custom functions (time, jokes)")
    print("="*60)

    agent.run()
```

### Next Steps

Your agent is running locally, but SignalWire can't reach `localhost`. You need to expose it to the internet.


**Or skip to: [Exposing Your Agent](01_05_exposing-agents.md)** - Make your agent accessible via ngrok


---

## Development Environment Setup

> **Summary**: Configure a professional development environment for building SignalWire agents with proper project structure, environment variables, and debugging tools.

### Recommended Project Structure

```
my-agent-project/
├── venv/                       # Virtual environment
├── agents/                     # Your agent modules
│   ├── __init__.py
│   ├── customer_service.py
│   └── support_agent.py
├── skills/                     # Custom skills (optional)
│   └── my_custom_skill/
│       ├── __init__.py
│       └── skill.py
├── tests/                      # Test files
│   ├── __init__.py
│   └── test_agents.py
├── .env                        # Environment variables (not in git)
├── .env.example                # Example env file (in git)
├── .gitignore
├── requirements.txt
└── main.py                     # Entry point
```

### Create the Project

```bash
## Create project directory
mkdir my-agent-project
cd my-agent-project

## Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

## Install dependencies
pip install signalwire-agents

## Create directory structure
mkdir -p agents skills tests

## Create initial files
touch agents/__init__.py
touch tests/__init__.py
touch .env .env.example .gitignore requirements.txt main.py
```

### Environment Variables

Create a `.env` file for configuration:

```bash
## .env - DO NOT COMMIT THIS FILE

## Authentication
## These set your agent's basic auth credentials.
## If not set, SDK uses username "signalwire" with an auto-generated
## password that changes on every invocation (printed to console).
SWML_BASIC_AUTH_USER=my_username
SWML_BASIC_AUTH_PASSWORD=my_secure_password_here

## Server Configuration
SWML_PROXY_URL_BASE=https://my-agent.ngrok.io

## SSL (optional, for production)
SWML_SSL_ENABLED=false
SWML_SSL_CERT_PATH=
SWML_SSL_KEY_PATH=

## Skill API Keys (as needed)
GOOGLE_API_KEY=your_google_api_key
GOOGLE_CX_ID=your_custom_search_id
WEATHER_API_KEY=your_weather_api_key

## Logging
SIGNALWIRE_LOG_MODE=default
```

**Important**: The `SWML_BASIC_AUTH_USER` and `SWML_BASIC_AUTH_PASSWORD` environment variables let you set stable credentials for your agent. Without these:

- Username defaults to `signalwire`
- Password is randomly generated on each startup
- The generated password is printed to the console

For development, you can leave these unset and use the printed credentials. For production, always set explicit values.

Create `.env.example` as a template (safe to commit):

```bash
## .env.example - Template for environment variables

## Authentication (optional - SDK generates credentials if not set)
SWML_BASIC_AUTH_USER=
SWML_BASIC_AUTH_PASSWORD=

## Server Configuration
SWML_PROXY_URL_BASE=

## Skill API Keys
GOOGLE_API_KEY=
WEATHER_API_KEY=
```

### Loading Environment Variables

Install python-dotenv:

```bash
pip install python-dotenv
```

Load in your agent:

```python
#!/usr/bin/env python3
## main.py - Main entry point with environment loading
"""Main entry point with environment loading."""

import os
from dotenv import load_dotenv

## Load environment variables from .env file
load_dotenv()

from agents.customer_service import CustomerServiceAgent


def main():
    agent = CustomerServiceAgent()

    # Use environment variables
    host = os.getenv("AGENT_HOST", "0.0.0.0")
    port = int(os.getenv("AGENT_PORT", "3000"))

    print(f"Starting agent on {host}:{port}")
    agent.run(host=host, port=port)


if __name__ == "__main__":
    main()
```

### The .gitignore File

```gitignore
## Virtual environment
venv/
.venv/
env/

## Environment variables
.env
.env.local
.env.*.local

## Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
build/
dist/
*.egg-info/

## IDE
.idea/
.vscode/
*.swp
*.swo
*~

## Testing
.pytest_cache/
.coverage
htmlcov/

## Logs
*.log

## OS
.DS_Store
Thumbs.db
```

### Requirements File

Create `requirements.txt`:

```
signalwire-agents>=1.0.4
python-dotenv>=1.0.0
```

Or generate from current environment:

```bash
pip freeze > requirements.txt
```

### IDE Configuration

#### VS Code

Create `.vscode/settings.json`:

```json
{
    "python.defaultInterpreterPath": "${workspaceFolder}/venv/bin/python",
    "python.envFile": "${workspaceFolder}/.env",
    "python.testing.pytestEnabled": true,
    "python.testing.pytestArgs": ["tests"],
    "editor.formatOnSave": true,
    "python.formatting.provider": "black"
}
```

Create `.vscode/launch.json` for debugging:

```json
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Run Agent",
            "type": "python",
            "request": "launch",
            "program": "${workspaceFolder}/main.py",
            "console": "integratedTerminal",
            "envFile": "${workspaceFolder}/.env"
        },
        {
            "name": "Run Current File",
            "type": "python",
            "request": "launch",
            "program": "${file}",
            "console": "integratedTerminal",
            "envFile": "${workspaceFolder}/.env"
        },
        {
            "name": "Test Agent with swaig-test",
            "type": "python",
            "request": "launch",
            "module": "signalwire_agents.cli.test_swaig",
            "args": ["${file}", "--dump-swml"],
            "console": "integratedTerminal"
        }
    ]
}
```

#### PyCharm

1. Open Settings → Project → Python Interpreter
2. Select your virtual environment
3. Go to Run → Edit Configurations
4. Create a Python configuration:
   - Script path: `main.py`
   - Working directory: Project root
   - Environment variables: Load from `.env`

### Using swaig-test for Development

The `swaig-test` CLI is essential for development:

```bash
## View SWML output (formatted)
swaig-test agents/customer_service.py --dump-swml

## View raw SWML JSON
swaig-test agents/customer_service.py --dump-swml --raw

## List all registered functions
swaig-test agents/customer_service.py --list-tools

## Execute a specific function
swaig-test agents/customer_service.py --exec get_customer --customer_id 12345

## Simulate serverless environment
swaig-test agents/customer_service.py --simulate-serverless lambda --dump-swml
```

### Development Workflow

**1. Edit Code**

Modify your agent in `agents/`.

**2. Quick Test**
- `swaig-test agents/my_agent.py --dump-swml`
- Verify SWML looks correct

**3. Function Test**
- `swaig-test agents/my_agent.py --exec my_function --arg value`
- Verify function returns expected result

**4. Run Server**
- `python main.py`
- `curl http://localhost:3000/`

**5. Integration Test**
- Start ngrok (see next section)
- Configure SignalWire webhook
- Make test call

### Sample Agent Module

```python
#!/usr/bin/env python3
## customer_service.py - Customer service agent
"""
Customer Service Agent

A production-ready customer service agent template.
"""

import os
from signalwire_agents import AgentBase, SwaigFunctionResult


class CustomerServiceAgent(AgentBase):
    """Customer service voice AI agent."""

    def __init__(self):
        super().__init__(
            name="customer-service",
            route="/",
            host="0.0.0.0",
            port=int(os.getenv("AGENT_PORT", "3000"))
        )

        self._configure_voice()
        self._configure_prompts()
        self._configure_functions()

    def _configure_voice(self):
        """Set up voice and language."""
        self.add_language("English", "en-US", "rime.spore")

        self.set_params({
            "end_of_speech_timeout": 500,
            "attention_timeout": 15000,
        })

        self.add_hints([
            "account",
            "billing",
            "support",
            "representative"
        ])

    def _configure_prompts(self):
        """Set up AI prompts."""
        self.prompt_add_section(
            "Role",
            "You are a helpful customer service representative for Acme Corp. "
            "Help customers with their questions about accounts, billing, and products."
        )

        self.prompt_add_section(
            "Guidelines",
            body="Follow these guidelines:",
            bullets=[
                "Be professional and courteous",
                "Ask clarifying questions when needed",
                "Offer to transfer to a human if you cannot help",
                "Keep responses concise"
            ]
        )

    def _configure_functions(self):
        """Register SWAIG functions."""
        self.define_tool(
            name="lookup_account",
            description="Look up a customer account by phone number or account ID",
            parameters={
                "type": "object",
                "properties": {
                    "identifier": {
                        "type": "string",
                        "description": "Phone number or account ID"
                    }
                },
                "required": ["identifier"]
            },
            handler=self.lookup_account
        )

        self.define_tool(
            name="transfer_to_human",
            description="Transfer the call to a human representative",
            parameters={"type": "object", "properties": {}},
            handler=self.transfer_to_human
        )

    def lookup_account(self, args, raw_data):
        """Look up account information."""
        identifier = args.get("identifier", "")

        # In production, query your database here
        return SwaigFunctionResult(
            f"Found account for {identifier}: Status is Active, Balance is $0.00"
        )

    def transfer_to_human(self, args, raw_data):
        """Transfer to human support."""
        return SwaigFunctionResult(
            "Transferring you to a human representative now."
        ).connect("+15551234567", final=True, from_addr="+15559876543")


## Allow running directly for testing
if __name__ == "__main__":
    agent = CustomerServiceAgent()
    agent.run()
```

### Testing Your Agent

```python
#!/usr/bin/env python3
## test_agents.py - Tests for agents
"""Tests for agents."""

import pytest
from agents.customer_service import CustomerServiceAgent


class TestCustomerServiceAgent:
    """Test customer service agent."""

    def setup_method(self):
        """Set up test fixtures."""
        self.agent = CustomerServiceAgent()

    def test_agent_name(self):
        """Test agent has correct name."""
        assert self.agent.name == "customer-service"

    def test_lookup_account(self):
        """Test account lookup function."""
        result = self.agent.lookup_account(
            {"identifier": "12345"},
            {}
        )
        assert "Found account" in result

    def test_has_functions(self):
        """Test agent has expected functions."""
        functions = self.agent._tool_registry.get_function_names()
        assert "lookup_account" in functions
        assert "transfer_to_human" in functions
```

Run tests:

```bash
pytest tests/ -v
```

### Next Steps

Your development environment is ready. Now let's expose your agent to the internet so SignalWire can reach it.



---

## Exposing Your Agent to the Internet

> **Summary**: Use ngrok to create a public URL for your local agent so SignalWire can send webhook requests to it.

### Why You Need a Public URL

SignalWire's cloud needs to reach your agent via HTTP:

```diagram
┌─────────────────────────────────────────────────────────────────────────────┐
│                         The Problem                                         │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  SignalWire Cloud                        Your Computer                      │
│  ┌─────────────────┐                    ┌─────────────────┐                 │
│  │                 │                    │                 │                 │
│  │  Needs to send  │     CANNOT         │  localhost:3000 │                 │
│  │  HTTP requests  │ ───── X ─────────► │                 │                 │
│  │                 │     REACH          │  (Not on the    │                 │
│  └─────────────────┘                    │   internet)     │                 │
│                                         └─────────────────┘                 │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────────┐
│                         The Solution: ngrok                                 │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  SignalWire Cloud        ngrok Cloud           Your Computer                │
│  ┌─────────────────┐    ┌─────────────────┐   ┌─────────────────┐           │
│  │                 │    │                 │   │                 │           │
│  │  Sends request  │───►│  abc123.ngrok.io│──►│  localhost:3000 │           │
│  │  to public URL  │    │  (tunnel)       │   │                 │           │
│  │                 │◄───│                 │◄──│                 │           │
│  └─────────────────┘    └─────────────────┘   └─────────────────┘           │
│                                                                             │
│  https://abc123.ngrok.io  ───►  tunnels to  ───►  http://localhost:3000     │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Installing ngrok

#### macOS (Homebrew)

```bash
brew install ngrok
```

#### Linux

```bash
## Download
curl -s https://ngrok-agent.s3.amazonaws.com/ngrok.asc | \
  sudo tee /etc/apt/trusted.gpg.d/ngrok.asc >/dev/null && \
  echo "deb https://ngrok-agent.s3.amazonaws.com buster main" | \
  sudo tee /etc/apt/sources.list.d/ngrok.list

## Install
sudo apt update && sudo apt install ngrok
```

#### Windows

```powershell
## Using Chocolatey
choco install ngrok

## Or download from https://ngrok.com/download
```

#### Direct Download

Visit [ngrok.com/download](https://ngrok.com/download) and download for your platform.

### Create an ngrok Account (Free)

1. Go to [ngrok.com](https://ngrok.com) and sign up
2. Get your auth token from the dashboard
3. Configure ngrok with your token:

```bash
ngrok config add-authtoken YOUR_AUTH_TOKEN_HERE
```

This enables:

- Longer session times
- Custom subdomains (paid)
- Multiple tunnels

### Basic Usage

Start your agent in one terminal:

```bash
## Terminal 1
python my_agent.py
```

Start ngrok in another terminal:

```bash
## Terminal 2
ngrok http 3000
```

You'll see output like:

```
ngrok                                                           (Ctrl+C to quit)

Session Status                online
Account                       your-email@example.com (Plan: Free)
Version                       3.x.x
Region                        United States (us)
Latency                       45ms
Web Interface                 http://127.0.0.1:4040
Forwarding                    https://abc123def456.ngrok-free.app -> http://localhost:3000

Connections                   ttl     opn     rt1     rt5     p50     p90
                              0       0       0.00    0.00    0.00    0.00
```

Your public URL is: `https://abc123def456.ngrok-free.app`

### Test the Tunnel

```bash
## Test locally
curl http://localhost:3000/

## Test through ngrok (use YOUR URL from ngrok output)
curl https://abc123def456.ngrok-free.app/
```

Both should return the same SWML document.

### ngrok Web Interface

ngrok provides a web interface at `http://127.0.0.1:4040` showing:

- All requests coming through the tunnel
- Request/response headers and bodies
- Timing information
- Ability to replay requests

This is invaluable for debugging SignalWire webhook calls!

### Static Domains (Recommended)

Free ngrok gives you random URLs that change each restart. For easier development, use a static domain:

#### Free Static Domain (ngrok account required)

1. Go to ngrok Dashboard → Domains
2. Create a free static domain (e.g., `your-name.ngrok-free.app`)
3. Use it:

```bash
ngrok http 3000 --domain=your-name.ngrok-free.app
```

Now your URL stays the same across restarts!

### Understanding Basic Authentication

**Important:** The SDK automatically secures your agent with HTTP Basic Authentication. Every time you start your agent, you'll see:

```
Agent 'my-agent' is available at:
URL: http://localhost:3000
Basic Auth: signalwire:7vVZ8iMTOWL0Y7-BG6xaN3qhjmcm4Sf59nORNdlF9bs (source: provided)
```

**The password changes on every restart** unless you set environment variables.

#### Setting Persistent Credentials

For development, set these environment variables to use the same credentials across restarts:

```bash
## In your .env file or shell
export SWML_BASIC_AUTH_USER=signalwire
export SWML_BASIC_AUTH_PASSWORD=your-secure-password-here
```

Then start your agent:

```bash
python my_agent.py
```

Now it will show:

```
Basic Auth: signalwire:your-secure-password-here (source: environment)
```

**Why this matters:**
- SignalWire needs these credentials to call your agent
- Random passwords mean reconfiguring SignalWire on every restart
- Set environment variables once for consistent development

### Configure Your Agent for ngrok

Set the `SWML_PROXY_URL_BASE` environment variable so your agent generates correct webhook URLs:

```bash
## In your .env file
SWML_PROXY_URL_BASE=https://your-name.ngrok-free.app
SWML_BASIC_AUTH_USER=signalwire
SWML_BASIC_AUTH_PASSWORD=your-secure-password-here
```

Or set them when running:

```bash
SWML_PROXY_URL_BASE=https://your-name.ngrok-free.app \
SWML_BASIC_AUTH_USER=signalwire \
SWML_BASIC_AUTH_PASSWORD=your-secure-password-here \
python my_agent.py
```

This ensures:

- SWAIG function webhook URLs point to your public ngrok URL, not localhost
- Authentication credentials remain consistent across restarts

### Complete Development Setup

Here's the full workflow:

```bash
## Terminal 1: Start ngrok with static domain
ngrok http 3000 --domain=your-name.ngrok-free.app

## Terminal 2: Start agent with environment variables
export SWML_PROXY_URL_BASE=https://your-name.ngrok-free.app
export SWML_BASIC_AUTH_USER=signalwire
export SWML_BASIC_AUTH_PASSWORD=your-secure-password-here
python my_agent.py

## Terminal 3: Test (use the credentials from Terminal 2)
curl -u signalwire:your-secure-password-here https://your-name.ngrok-free.app/
curl -u signalwire:your-secure-password-here https://your-name.ngrok-free.app/debug
```

### Using a Script

Create `start-dev.sh`:

```bash
#!/bin/bash
## start-dev.sh - Start development environment

NGROK_DOMAIN="your-name.ngrok-free.app"
AUTH_USER="signalwire"
AUTH_PASS="your-secure-password-here"

echo "Starting development environment..."
echo "Public URL: https://${NGROK_DOMAIN}"
echo "Basic Auth: ${AUTH_USER}:${AUTH_PASS}"
echo ""

## Start ngrok in background
ngrok http 3000 --domain=${NGROK_DOMAIN} &
NGROK_PID=$!

## Wait for ngrok to start
sleep 2

## Start agent with environment variables
export SWML_PROXY_URL_BASE="https://${NGROK_DOMAIN}"
export SWML_BASIC_AUTH_USER="${AUTH_USER}"
export SWML_BASIC_AUTH_PASSWORD="${AUTH_PASS}"
python my_agent.py

## Cleanup on exit
trap "kill $NGROK_PID 2>/dev/null" EXIT
```

Make it executable:

```bash
chmod +x start-dev.sh
./start-dev.sh
```

### Alternative Tunneling Solutions

#### Cloudflare Tunnel (Free)

```bash
## Install cloudflared
brew install cloudflared  # macOS

## Quick tunnel (no account needed)
cloudflared tunnel --url http://localhost:3000
```

#### localtunnel (Free, no signup)

```bash
## Install
npm install -g localtunnel

## Run
lt --port 3000
```

#### tailscale Funnel (Requires Tailscale)

```bash
## If you use Tailscale
tailscale funnel 3000
```

### Production Alternatives

For production, don't use ngrok. Instead:

| Option | Description |
|--------|-------------|
| **Cloud VM** | Deploy to AWS, GCP, Azure, DigitalOcean |
| **Serverless** | AWS Lambda, Google Cloud Functions, Azure Functions |
| **Container** | Docker on Kubernetes, ECS, Cloud Run |
| **VPS** | Any server with a public IP |

See the [Deployment](../07_deployment/07_00_deployment.md) chapter for production deployment guides.

### Troubleshooting

#### ngrok shows "ERR_NGROK_108"

Your auth token is invalid or expired. Get a new one from the ngrok dashboard:

```bash
ngrok config add-authtoken YOUR_NEW_TOKEN
```

#### Connection refused

Your agent isn't running or is on a different port:

```bash
## Check agent is running
curl http://localhost:3000/

## If using different port
ngrok http 8080
```

#### Webhook URLs still show localhost

Set `SWML_PROXY_URL_BASE`:

```bash
export SWML_PROXY_URL_BASE=https://your-domain.ngrok-free.app
python my_agent.py
```

#### ngrok tunnel expires

Free ngrok tunnels expire after a few hours. Solutions:

- Restart ngrok
- Use a static domain (stays same after restart)
- Upgrade to paid ngrok plan
- Use an alternative like Cloudflare Tunnel

### What's Next?

Your agent is now accessible at a public URL. You're ready to connect it to SignalWire!

### You've Completed Phase 1!

- [x] Installed the SDK
- [x] Created your first agent
- [x] Set up development environment
- [x] Exposed agent via ngrok

Your agent is ready at: `https://your-domain.ngrok-free.app`

**Next Chapter: [Core Concepts](../02_core-concepts/02_00_core-concepts.md)** - Deep dive into SWML, SWAIG, and agent architecture

**Or jump to: [SignalWire Integration](../08_signalwire-integration/08_00_signalwire-integration.md)** - Connect your agent to phone numbers


# Part: Core Concepts

---

# Core Concepts

> **Summary**: Understand the fundamental architecture, protocols, and patterns that power the SignalWire Agents SDK.

## What You'll Learn

This chapter covers the foundational concepts you need to build effective voice AI agents:

1. **Architecture** - How AgentBase and its mixins work together
2. **SWML** - The markup language that controls call flows
3. **SWAIG** - The gateway that lets AI call your functions
4. **Lifecycle** - How requests flow through the system
5. **Security** - Authentication and token-based function security

## Prerequisites

Before diving into these concepts, you should have:

- Completed the [Getting Started](../01_getting-started/01_00_getting-started.md) chapter
- A working agent running locally
- Basic understanding of HTTP request/response patterns

## The Big Picture

```diagram
┌─────────────────────────────────────────────────────────────────────────────┐
│                    SignalWire Agents SDK Architecture                       │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  Incoming Call                                                              │
│       │                                                                     │
│       ▼                                                                     │
│  ┌─────────────────────────────────────────────────────────────────────┐    │
│  │                      SignalWire Cloud                               │    │
│  │  • Receives call                                                    │    │
│  │  • Requests SWML from your agent                                    │    │
│  │  • Executes AI conversation                                         │    │
│  │  • Calls SWAIG functions when AI needs tools                        │    │
│  └─────────────────────────────────────────────────────────────────────┘    │
│                               │                                             │
│          HTTP Requests        │        HTTP Responses                       │
│          (GET /, POST /swaig) │        (SWML JSON)                          │
│                               ▼                                             │
│  ┌─────────────────────────────────────────────────────────────────────┐    │
│  │                        Your Agent                                   │    │
│  │  ┌───────────────────────────────────────────────────────────────┐  │    │
│  │  │                      AgentBase                                │  │    │
│  │  │  ┌──────────┐ ┌──────────┐ ┌───────────┐ ┌───────────┐        │  │    │
│  │  │  │AuthMixin │ │ WebMixin │ │ ToolMixin │ │SkillMixin │        │  │    │
│  │  │  └──────────┘ └──────────┘ └───────────┘ └───────────┘        │  │    │
│  │  │  ┌──────────┐ ┌──────────┐ ┌───────────┐ ┌───────────┐        │  │    │
│  │  │  │PromptMix │ │AIConfig  │ │Serverless │ │StateMixin │        │  │    │
│  │  │  └──────────┘ └──────────┘ └───────────┘ └───────────┘        │  │    │
│  │  │                        │                                      │  │    │
│  │  │                ┌───────────────┐                              │  │    │
│  │  │                │  SWMLService  │                              │  │    │
│  │  │                │  (Generates   │                              │  │    │
│  │  │                │   SWML JSON)  │                              │  │    │
│  │  │                └───────────────┘                              │  │    │
│  │  └───────────────────────────────────────────────────────────────┘  │    │
│  └─────────────────────────────────────────────────────────────────────┘    │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

## Key Terminology

| Term | Definition |
|------|------------|
| **AgentBase** | The base class all agents inherit from |
| **SWML** | SignalWire Markup Language - JSON format for call instructions |
| **SWAIG** | SignalWire AI Gateway - System for AI to call your functions |
| **Mixin** | A class providing specific functionality to AgentBase |
| **POM** | Prompt Object Model - Structured prompt building |
| **DataMap** | Declarative REST API integration |

## Chapter Contents

| Section | Description |
|---------|-------------|
| [Architecture](02_01_architecture.md) | AgentBase class and mixin composition |
| [SWML](02_02_swml.md) | Understanding SWML document structure |
| [SWAIG](02_03_swaig.md) | How AI calls your functions |
| [Lifecycle](02_04_lifecycle.md) | Request/response flow |
| [Security](02_05_security.md) | Authentication and token security |

## Why These Concepts Matter

Understanding these core concepts helps you:

- **Debug effectively** - Know where to look when things go wrong
- **Build efficiently** - Use the right tool for each task
- **Scale confidently** - Understand how the system handles load
- **Extend properly** - Add custom functionality the right way

## The Mixin Composition Pattern

AgentBase doesn't inherit from a single monolithic class. Instead, it combines eight specialized mixins:

```diagram
┌─────────────────────────────────────────────────────────────────────────────┐
│                              AgentBase                                      │
│                    (Your agents inherit from this)                          │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  Inherits from (in MRO order):                                              │
│                                                                             │
│  ┌──────────────┐    ┌──────────────┐    ┌──────────────┐                   │
│  │  AuthMixin   │───►│  WebMixin    │───►│ SWMLService  │                   │
│  │              │    │              │    │   (Base)     │                   │
│  │ • Basic auth │    │ • FastAPI    │    │ • Schema     │                   │
│  │ • Credentials│    │ • Routes     │    │ • Render     │                   │
│  │ • Validation │    │ • Server     │    │ • Verbs      │                   │
│  └──────────────┘    └──────────────┘    └──────────────┘                   │
│         │                   │                   │                           │
│         ▼                   ▼                   ▼                           │
│  ┌──────────────┐    ┌──────────────┐    ┌──────────────┐                   │
│  │ PromptMixin  │───►│  ToolMixin   │───►│  SkillMixin  │                   │
│  │              │    │              │    │              │                   │
│  │ • POM        │    │ • SWAIG Fns  │    │ • Skill Mgmt │                   │
│  │ • Sections   │    │ • Decorators │    │ • Registry   │                   │
│  │ • Templates  │    │ • DataMap    │    │ • Loading    │                   │
│  └──────────────┘    └──────────────┘    └──────────────┘                   │
│         │                   │                   │                           │
│         ▼                   ▼                   ▼                           │
│  ┌──────────────┐    ┌──────────────┐    ┌──────────────┐                   │
│  │AIConfigMixin │───►│ServerlessMix │───►│  StateMixin  │                   │
│  │              │    │              │    │              │                   │
│  │ • Languages  │    │ • Lambda     │    │ • Session    │                   │
│  │ • Hints      │    │ • CGI        │    │ • Call State │                   │
│  │ • Params     │    │ • Azure      │    │ • Persistence│                   │
│  └──────────────┘    └──────────────┘    └──────────────┘                   │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

## Each Mixin's Role

### AuthMixin - Authentication & Security

Handles basic HTTP authentication for webhook endpoints.

```python
from signalwire_agents import AgentBase

class MyAgent(AgentBase):
    def __init__(self):
        super().__init__(name="my-agent")
        # Auth credentials auto-generated or from environment:
        # SWML_BASIC_AUTH_USER, SWML_BASIC_AUTH_PASSWORD
```

**Key methods:**
- Validates incoming requests against stored credentials
- Generates credentials if not provided via environment
- Protects SWAIG function endpoints

### WebMixin - HTTP Server & Routing

Manages the FastAPI application and HTTP endpoints.

```python
# Automatically registers these routes:
# GET  /          → Returns SWML document
# POST /          → Returns SWML document
# POST /swaig     → Handles SWAIG function calls
# POST /post_prompt → Receives call summaries
# GET  /debug     → Debug information (dev only)
```

**Key features:**
- Runs uvicorn server via `agent.run()`
- Handles proxy detection (ngrok, load balancers)
- Manages request/response lifecycle

### SWMLService - SWML Document Generation

The foundation for building SWML documents.

```python
# SWMLService provides:
# - Schema validation against SWML spec
# - Verb handler registry
# - Document rendering pipeline
```

**Key responsibilities:**
- Validates SWML structure against JSON schema
- Registers verb handlers (answer, ai, connect, etc.)
- Renders final SWML JSON

### PromptMixin - Prompt Management

Manages AI system prompts using POM (Prompt Object Model).

```python
agent.prompt_add_section(
    "Role",
    "You are a helpful customer service agent."
)

agent.prompt_add_section(
    "Guidelines",
    body="Follow these rules:",
    bullets=[
        "Be concise",
        "Be professional",
        "Escalate when needed"
    ]
)
```

**Key features:**
- Structured prompt building with sections
- Support for bullets, subsections
- Post-prompt for call summaries

### ToolMixin - SWAIG Function Management

Handles registration and execution of SWAIG functions.

```python
agent.define_tool(
    name="get_balance",
    description="Get account balance",
    parameters={
        "account_id": {
            "type": "string",
            "description": "The account ID"
        }
    },
    handler=self.get_balance
)
```

**Key features:**
- Multiple registration methods (define_tool, decorators, DataMap)
- Parameter validation
- Security token generation

### SkillMixin - Skill Plugin Management

Loads and manages reusable skill plugins.

```python
# Load built-in skill
agent.add_skill("datetime")

# Load skill with configuration
agent.add_skill("web_search",
    google_api_key="...",
    google_cx_id="..."
)
```

**Key features:**
- Auto-discovery of skill modules
- Dependency checking
- Configuration validation

### AIConfigMixin - AI Behavior Configuration

Configures the AI's voice, language, and behavior parameters.

```python
agent.add_language("English", "en-US", "rime.spore")

agent.set_params({
    "end_of_speech_timeout": 500,
    "attention_timeout": 15000
})

agent.add_hints(["SignalWire", "SWML", "AI agent"])
```

**Key features:**
- Voice and language settings
- Speech recognition hints
- AI behavior parameters

### ServerlessMixin - Deployment Adapters

Provides handlers for serverless deployments.

```python
# AWS Lambda
handler = agent.serverless_handler

# Google Cloud Functions
def my_function(request):
    return agent.cloud_function_handler(request)

# Azure Functions
def main(req):
    return agent.azure_function_handler(req)
```

**Key features:**
- Environment auto-detection
- Request/response adaptation
- URL generation for each platform

### StateMixin - State Management

Manages session and call state.

```python
# State is passed via global_data in SWML
# and preserved across function calls
```

**Key features:**
- Session tracking
- State persistence patterns
- Call context management

## Key Internal Components

Beyond the mixins, AgentBase uses several internal managers:

### ToolRegistry
- Stores SWAIG functions
- Handles function lookup
- Generates webhook URLs

### PromptManager
- Manages prompt sections
- Builds POM structure
- Handles post-prompts

### SessionManager
- Token generation
- Token validation
- Security enforcement

### SkillManager
- Skill discovery
- Skill loading
- Configuration validation

### SchemaUtils
- SWML schema loading
- Document validation
- Schema-driven help

### VerbHandlerRegistry
- Verb registration
- Handler dispatch
- Custom verb support

## Creating Your Own Agent

When you create an agent, you get all mixin functionality automatically:

```python
from signalwire_agents import AgentBase, SwaigFunctionResult


class CustomerServiceAgent(AgentBase):
    def __init__(self):
        super().__init__(name="customer-service")

        # AIConfigMixin methods
        self.add_language("English", "en-US", "rime.spore")
        self.set_params({"end_of_speech_timeout": 500})

        # PromptMixin methods
        self.prompt_add_section("Role", "You are a helpful agent.")

        # ToolMixin methods
        self.define_tool(
            name="lookup_order",
            description="Look up an order by ID",
            parameters={
                "order_id": {"type": "string", "description": "Order ID"}
            },
            handler=self.lookup_order
        )

        # SkillMixin methods
        self.add_skill("datetime")

    def lookup_order(self, args, raw_data):
        order_id = args.get("order_id")
        # Your business logic here
        return SwaigFunctionResult(f"Order {order_id}: Shipped, arrives tomorrow")


if __name__ == "__main__":
    agent = CustomerServiceAgent()
    agent.run()  # WebMixin method
```

## Benefits of This Architecture

| Benefit | Description |
|---------|-------------|
| **Separation of Concerns** | Each mixin handles one domain |
| **Easy to Understand** | Look at one mixin for one feature |
| **Extensible** | Override specific mixin methods |
| **Testable** | Test mixins independently |
| **Type-Safe** | Full type hints throughout |

## Next Steps

Now that you understand how AgentBase is structured, let's look at the SWML documents it generates.


---

## SWML (SignalWire Markup Language)

> **Summary**: SWML is the JSON format that tells SignalWire how to handle calls. Your agent generates SWML automatically - you configure the agent, and it produces the right SWML.

### What is SWML?

SWML (SignalWire Markup Language) is a document that instructs SignalWire how to handle a phone call. SWML can be written in JSON or YAML format - **this guide uses JSON throughout**. When a call comes in, SignalWire requests SWML from your agent, then executes the instructions.

```diagram
┌─────────────────────────────────────────────────────────────────────────────┐
│                              SWML Flow                                      │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  1. Call Arrives                                                            │
│       │                                                                     │
│       ▼                                                                     │
│  2. SignalWire requests: GET https://your-agent.com/                        │
│       │                                                                     │
│       ▼                                                                     │
│  3. Your agent returns SWML JSON                                            │
│       │                                                                     │
│       ▼                                                                     │
│  4. SignalWire executes the SWML instructions                               │
│       │                                                                     │
│       ▼                                                                     │
│  5. AI conversation begins based on SWML config                             │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### SWML Document Structure

Every SWML document has this structure:

```json
{
  "version": "1.0.0",
  "sections": {
    "main": [
      { "verb1": { ...config } },
      { "verb2": { ...config } },
      { "verb3": { ...config } }
    ]
  }
}
```

**Key parts:**
- `version`: Always `"1.0.0"`
- `sections`: Contains named sections (usually just `main`)
- Each section is an array of **verbs** (instructions)

### Common Verbs

| Verb | Purpose | Example |
|------|---------|---------|
| `answer` | Answer the incoming call | `{"answer": {}}` |
| `ai` | Start AI conversation | `{"ai": {...config}}` |
| `connect` | Transfer to another number | `{"connect": {"to": "+1..."}}` |
| `play` | Play audio file | `{"play": {"url": "..."}}` |
| `record_call` | Record the call | `{"record_call": {"format": "mp4"}}` |
| `hangup` | End the call | `{"hangup": {}}` |

### A Complete SWML Example

Here's what your agent generates:

```json
{
  "version": "1.0.0",
  "sections": {
    "main": [
      {
        "answer": {}
      },
      {
        "ai": {
          "prompt": {
            "text": "# Role\nYou are a helpful customer service agent.\n\n# Guidelines\n- Be professional\n- Be concise"
          },
          "post_prompt": "Summarize what was discussed",
          "post_prompt_url": "https://your-agent.com/post_prompt",
          "SWAIG": {
            "defaults": {
              "web_hook_url": "https://your-agent.com/swaig"
            },
            "functions": [
              {
                "function": "get_balance",
                "description": "Get the customer's account balance",
                "parameters": {
                  "type": "object",
                  "properties": {
                    "account_id": {
                      "type": "string",
                      "description": "The account ID"
                    }
                  },
                  "required": ["account_id"]
                }
              }
            ]
          },
          "hints": ["account", "balance", "payment"],
          "languages": [
            {
              "name": "English",
              "code": "en-US",
              "voice": "rime.spore"
            }
          ],
          "params": {
            "end_of_speech_timeout": 500,
            "attention_timeout": 15000
          }
        }
      }
    ]
  }
}
```

### The `ai` Verb in Detail

The `ai` verb is the heart of voice AI agents. Here's what each part does:

```json
{
  "ai": {
    "prompt": {},            // What the AI should do (system prompt)
    "post_prompt": "...",    // Instructions for summarizing the call
    "post_prompt_url": "...",// Where to send the summary
    "SWAIG": {},             // Functions the AI can call
    "hints": [],             // Words to help speech recognition
    "languages": [],         // Voice and language settings
    "params": {},            // AI behavior parameters
    "global_data": {}        // Data available throughout the call
  }
}
```

#### prompt

The AI's system prompt - its personality and instructions:

```json
{
  "prompt": {
    "text": "You are a helpful assistant..."
  }
}
```

Or using POM (Prompt Object Model):

```json
{
  "prompt": {
    "pom": [
      {
        "section": "Role",
        "body": "You are a customer service agent"
      },
      {
        "section": "Rules",
        "bullets": ["Be concise", "Be helpful"]
      }
    ]
  }
}
```

#### SWAIG

Defines functions the AI can call:

```json
{
  "SWAIG": {
    "defaults": {
      "web_hook_url": "https://your-agent.com/swaig"
    },
    "functions": [
      {
        "function": "check_order",
        "description": "Check order status",
        "parameters": {
          "type": "object",
          "properties": {
            "order_id": {"type": "string"}
          }
        }
      }
    ]
  }
}
```

#### hints

Words that help speech recognition accuracy:

```json
{
  "hints": ["SignalWire", "SWML", "account number", "order ID"]
}
```

#### languages

Voice and language configuration:

```json
{
  "languages": [
    {
      "name": "English",
      "code": "en-US",
      "voice": "rime.spore"
    }
  ]
}
```

#### params

AI behavior settings:

```json
{
  "params": {
    "end_of_speech_timeout": 500,
    "attention_timeout": 15000,
    "barge_match_string": "stop|cancel|quit"
  }
}
```

### How Your Agent Generates SWML

You don't write SWML by hand. Your agent configuration becomes SWML:

```python
from signalwire_agents import AgentBase


class MyAgent(AgentBase):
    def __init__(self):
        super().__init__(name="my-agent")

        # This becomes languages in SWML
        self.add_language("English", "en-US", "rime.spore")

        # This becomes prompt in SWML
        self.prompt_add_section("Role", "You are helpful.")

        # This becomes hints in SWML
        self.add_hints(["help", "support"])

        # This becomes params in SWML
        self.set_params({"end_of_speech_timeout": 500})

        # This becomes SWAIG.functions in SWML
        self.define_tool(
            name="get_help",
            description="Get help information",
            parameters={},
            handler=self.get_help
        )
```

When SignalWire requests SWML, the agent's `_render_swml()` method:

1. Collects all configuration (prompts, languages, hints, params)
2. Builds the SWAIG functions array with webhook URLs
3. Assembles the complete SWML document
4. Returns JSON to SignalWire

### SWML Rendering Pipeline

```diagram
┌─────────────────────────────────────────────────────────────────────────────┐
│                        SWML Rendering Pipeline                              │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  1. Request Arrives (GET /)                                                 │
│       │                                                                     │
│       ▼                                                                     │
│  2. _render_swml() called                                                   │
│       │                                                                     │
│       ├───► Get prompt (text or POM)                                        │
│       ├───► Get post-prompt                                                 │
│       ├───► Collect SWAIG functions                                         │
│       ├───► Generate security tokens                                        │
│       ├───► Build webhook URLs                                              │
│       ├───► Collect hints, languages, params                                │
│       │                                                                     │
│       ▼                                                                     │
│  3. Assemble AI verb                                                        │
│       │                                                                     │
│       ▼                                                                     │
│  4. Build document: answer + ai verbs                                       │
│       │                                                                     │
│       ▼                                                                     │
│  5. Return SWML JSON                                                        │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Viewing Your SWML

You can see the SWML your agent generates:

```bash
## Using curl
curl http://localhost:3000/

## Using swaig-test CLI
swaig-test my_agent.py --dump-swml

## Pretty-printed
swaig-test my_agent.py --dump-swml --raw | jq '.'
```

### SWML Schema Validation

The SDK validates SWML against the official schema:

- Located at `signalwire_agents/core/schema.json`
- Catches invalid configurations before sending to SignalWire
- Provides helpful error messages

### Common SWML Patterns

#### Auto-Answer with AI

```json
{
  "version": "1.0.0",
  "sections": {
    "main": [
      {"answer": {}},
      {"ai": {...}}
    ]
  }
}
```

#### Record the Call

```json
{
  "version": "1.0.0",
  "sections": {
    "main": [
      {"answer": {}},
      {"record_call": {"format": "mp4", "stereo": true}},
      {"ai": {...}}
    ]
  }
}
```

#### Transfer After AI

When a SWAIG function returns a transfer action, the SWML for transfer is embedded in the response:

```json
{
  "response": "Transferring you now",
  "action": [
    {"transfer": true},
    {
      "swml": {
        "version": "1.0.0",
        "sections": {
          "main": [
            {"connect": {"to": "+15551234567", "from": "+15559876543"}}
          ]
        }
      }
    }
  ]
}
```

### Next Steps

Now that you understand SWML structure, let's look at SWAIG - how AI calls your functions.



---

## SWAIG (SignalWire AI Gateway)

> **Summary**: SWAIG is the system that lets the AI call your functions during a conversation. You define functions, SignalWire calls them via webhooks, and your responses guide the AI.

### What is SWAIG?

SWAIG (SignalWire AI Gateway) connects the AI conversation to your backend logic. When the AI decides it needs to perform an action (like looking up an order or checking a balance), it calls a SWAIG function that you've defined.

```diagram
┌─────────────────────────────────────────────────────────────────────────────┐
│                           SWAIG Function Flow                               │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  User: "What's my account balance?"                                         │
│       │                                                                     │
│       ▼                                                                     │
│  ┌─────────────────────────────────────────────────────────────────────┐    │
│  │                    SignalWire AI Engine                             │    │
│  │  1. Transcribes speech                                              │    │
│  │  2. Understands intent: "user wants account balance"                │    │
│  │  3. Decides to call: get_balance(account_id="12345")                │    │
│  └─────────────────────────────────────────────────────────────────────┘    │
│       │                                                                     │
│       │  POST /swaig                                                        │
│       │  {"function": "get_balance", "argument": {"account_id": "12345"}}   │
│       ▼                                                                     │
│  ┌─────────────────────────────────────────────────────────────────────┐    │
│  │                      Your Agent                                     │    │
│  │  def get_balance(self, args, raw_data):                             │    │
│  │      account_id = args.get("account_id")                            │    │
│  │      balance = lookup_balance(account_id)                           │    │
│  │      return SwaigFunctionResult(f"Balance is ${balance}")           │    │
│  └─────────────────────────────────────────────────────────────────────┘    │
│       │                                                                     │
│       │  Response: {"response": "Balance is $150.00"}                       │
│       ▼                                                                     │
│  ┌─────────────────────────────────────────────────────────────────────┐    │
│  │                    SignalWire AI Engine                             │    │
│  │  Speaks: "Your account balance is one hundred fifty dollars."       │    │
│  └─────────────────────────────────────────────────────────────────────┘    │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### SWAIG in SWML

When your agent generates SWML, it includes SWAIG function definitions in the `ai` verb:

```json
{
  "version": "1.0.0",
  "sections": {
    "main": [
      {
        "ai": {
          "SWAIG": {
            "defaults": {
              "web_hook_url": "https://your-agent.com/swaig"
            },
            "functions": [
              {
                "function": "get_balance",
                "description": "Get the customer's current account balance",
                "parameters": {
                  "type": "object",
                  "properties": {
                    "account_id": {
                      "type": "string",
                      "description": "The customer's account ID"
                    }
                  },
                  "required": ["account_id"]
                }
              }
            ]
          }
        }
      }
    ]
  }
}
```

### Defining SWAIG Functions

There are three ways to define SWAIG functions in your agent:

#### Method 1: define_tool()

The most explicit way to register a function:

```python
from signalwire_agents import AgentBase, SwaigFunctionResult


class MyAgent(AgentBase):
    def __init__(self):
        super().__init__(name="my-agent")

        self.define_tool(
            name="get_balance",
            description="Get account balance for a customer",
            parameters={
                "type": "object",
                "properties": {
                    "account_id": {
                        "type": "string",
                        "description": "The account ID to look up"
                    }
                },
                "required": ["account_id"]
            },
            handler=self.get_balance
        )

    def get_balance(self, args, raw_data):
        account_id = args.get("account_id")
        # Your business logic here
        return SwaigFunctionResult(f"Account {account_id} has a balance of $150.00")
```

#### Method 2: @swaig_function Decorator

A cleaner approach using decorators:

```python
from signalwire_agents import AgentBase, SwaigFunctionResult, swaig_function


class MyAgent(AgentBase):
    def __init__(self):
        super().__init__(name="my-agent")

    @swaig_function(
        description="Get account balance for a customer",
        parameters={
            "account_id": {
                "type": "string",
                "description": "The account ID to look up"
            }
        }
    )
    def get_balance(self, args, raw_data):
        account_id = args.get("account_id")
        return SwaigFunctionResult(f"Account {account_id} has a balance of $150.00")
```

#### Method 3: DataMap (Serverless)

For direct API integration without code:

```python
from signalwire_agents import AgentBase


class MyAgent(AgentBase):
    def __init__(self):
        super().__init__(name="my-agent")

        self.data_map.add_tool(
            name="get_balance",
            description="Get account balance",
            parameters={
                "account_id": {
                    "type": "string",
                    "description": "The account ID"
                }
            },
            data_map={
                "webhooks": [
                    {
                        "url": "https://api.example.com/accounts/${enc:args.account_id}/balance",
                        "method": "GET",
                        "headers": {
                            "Authorization": "Bearer ${env.API_KEY}"
                        },
                        "output": {
                            "response": "Account balance is $${balance}",
                            "action": [{"set_global_data": {"balance": "${balance}"}}]
                        }
                    }
                ]
            }
        )
```

### Function Handler Signature

Every SWAIG function handler receives two arguments:

```python
def my_function(self, args, raw_data):
    """
    args: dict - The parsed arguments from the AI
        Example: {"account_id": "12345", "include_history": True}

    raw_data: dict - The complete request payload from SignalWire
        Contains metadata, call info, and conversation context
    """
    pass
```

#### The raw_data Payload

The `raw_data` contains rich context about the call:

```python
def my_function(self, args, raw_data):
    # Call metadata
    # Call information (nested under 'call' key)
    call_data = raw_data.get("call", {})
    call_id = call_data.get("call_id") or raw_data.get("call_id")  # Fallback for compatibility
    call_sid = raw_data.get("call_sid")

    # Caller information (from nested call object)
    from_number = call_data.get("from") or call_data.get("from_number")
    to_number = call_data.get("to") or call_data.get("to_number")

    # Global data (shared state)
    global_data = raw_data.get("global_data", {})
    customer_name = global_data.get("customer_name")

    # Conversation context
    meta_data = raw_data.get("meta_data", {})

    return SwaigFunctionResult("Processed")
```

### SwaigFunctionResult

Always return a `SwaigFunctionResult` from your handlers:

```python
from signalwire_agents import SwaigFunctionResult


def simple_response(self, args, raw_data):
    # Simple text response - AI will speak this
    return SwaigFunctionResult("Your order has been placed successfully.")


def response_with_actions(self, args, raw_data):
    result = SwaigFunctionResult("Transferring you now.")

    # Add actions to control call behavior
    result.add_action("transfer", True)
    result.add_action("swml", {
        "version": "1.0.0",
        "sections": {
            "main": [
                {"connect": {"to": "+15551234567", "from": "+15559876543"}}
            ]
        }
    })

    return result


def response_with_data(self, args, raw_data):
    result = SwaigFunctionResult("I've saved your preferences.")

    # Store data for later functions
    result.add_action("set_global_data", {
        "user_preference": "email",
        "confirmed": True
    })

    return result
```

### Common Actions

| Action | Purpose | Example |
|--------|---------|---------|
| `set_global_data` | Store data for later use | `{"key": "value"}` |
| `transfer` | End AI, prepare for transfer | `True` |
| `swml` | Execute SWML after AI ends | `{"version": "1.0.0", ...}` |
| `stop` | End the AI conversation | `True` |
| `toggle_functions` | Enable/disable functions | `[{"active": false, "function": "fn_name"}]` |
| `say` | Speak text immediately | `"Please hold..."` |
| `play_file` | Play audio file | `"https://example.com/hold_music.mp3"` |

### SWAIG Request Flow

```diagram
┌─────────────────────────────────────────────────────────────────────────────┐
│                        SWAIG Request Processing                             │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  1. SignalWire sends POST to /swaig                                         │
│       │                                                                     │
│       ▼                                                                     │
│  2. Agent validates authentication (Basic Auth)                             │
│       │                                                                     │
│       ▼                                                                     │
│  3. Agent validates function-specific token (if configured)                 │
│       │                                                                     │
│       ▼                                                                     │
│  4. Agent looks up function in ToolRegistry                                 │
│       │                                                                     │
│       ├───► Function found ───► Execute handler                             │
│       │                              │                                      │
│       │                              ▼                                      │
│       │                         Return SwaigFunctionResult                  │
│       │                              │                                      │
│       │                              ▼                                      │
│       │                         Format JSON response                        │
│       │                                                                     │
│       └───► Function not found ───► Return error response                   │
│                                                                             │
│  5. Response sent to SignalWire                                             │
│       │                                                                     │
│       ▼                                                                     │
│  6. AI incorporates response into conversation                              │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### SWAIG Request Format

SignalWire sends a POST request with this structure:

```json
{
  "action": "swaig_action",
  "function": "get_balance",
  "argument": {
    "parsed": [
      {
        "account_id": "12345"
      }
    ],
    "raw": "{\"account_id\": \"12345\"}"
  },
  "call": {
    "call_id": "uuid-here",
    "from": "+15551234567",
    "from_number": "+15551234567",
    "to": "+15559876543",
    "to_number": "+15559876543",
    "direction": "inbound"
  },
  "call_id": "uuid-here",
  "call_sid": "call-sid-here",
  "global_data": {
    "customer_name": "John Doe"
  },
  "meta_data": {},
  "ai_session_id": "session-uuid"
}
```

**Important Note on Request Structure:**
- Call information (caller/callee numbers, call_id, direction) is **nested under the `call` key**
- Always use defensive access: `call_data = raw_data.get("call", {})`
- Some fields may also appear at the top level for backwards compatibility
- Use the pattern shown in "Accessing Call Information" above for robust code

### SWAIG Response Format

Your agent responds with:

```json
{
  "response": "The account balance is $150.00",
  "action": [
    {
      "set_global_data": {
        "last_balance_check": "2024-01-15T10:30:00Z"
      }
    }
  ]
}
```

Or for a transfer:

```json
{
  "response": "Transferring you to a specialist now.",
  "action": [
    {"transfer": true},
    {
      "swml": {
        "version": "1.0.0",
        "sections": {
          "main": [
            {"connect": {"to": "+15551234567", "from": "+15559876543"}}
          ]
        }
      }
    }
  ]
}
```

### Function Parameters (JSON Schema)

SWAIG functions use JSON Schema for parameter definitions:

```python
self.define_tool(
    name="search_orders",
    description="Search customer orders",
    parameters={
        "type": "object",
        "properties": {
            "customer_id": {
                "type": "string",
                "description": "Customer ID to search for"
            },
            "status": {
                "type": "string",
                "enum": ["pending", "shipped", "delivered", "cancelled"],
                "description": "Filter by order status"
            },
            "limit": {
                "type": "integer",
                "description": "Maximum number of results",
                "default": 10
            },
            "include_details": {
                "type": "boolean",
                "description": "Include full order details",
                "default": False
            }
        },
        "required": ["customer_id"]
    },
    handler=self.search_orders
)
```

### Webhook Security

SWAIG endpoints support multiple security layers:

1. **Basic Authentication**: HTTP Basic Auth on all requests
2. **Function Tokens**: Per-function security tokens
3. **HTTPS**: TLS encryption in transit

```python
## Function-specific token security
self.define_tool(
    name="sensitive_action",
    description="Perform a sensitive action",
    parameters={...},
    handler=self.sensitive_action,
    secure=True  # Enables per-function token validation
)
```

### Testing SWAIG Functions

Use `swaig-test` to test functions locally:

```bash
## List all registered functions
swaig-test my_agent.py --list-tools

## Execute a function with arguments
swaig-test my_agent.py --exec get_balance --account_id 12345

## View the SWAIG configuration in SWML
swaig-test my_agent.py --dump-swml | grep -A 50 '"SWAIG"'
```

### Best Practices

1. **Keep functions focused**: One function, one purpose
2. **Write clear descriptions**: Help the AI understand when to use each function
3. **Validate inputs**: Check for required arguments
4. **Handle errors gracefully**: Return helpful error messages
5. **Use global_data**: Share state between function calls
6. **Log for debugging**: Track function calls and responses

```python
def get_balance(self, args, raw_data):
    account_id = args.get("account_id")

    if not account_id:
        return SwaigFunctionResult(
            "I need an account ID to look up the balance. "
            "Could you provide your account number?"
        )

    try:
        balance = self.lookup_balance(account_id)
        return SwaigFunctionResult(f"Your current balance is ${balance:.2f}")
    except AccountNotFoundError:
        return SwaigFunctionResult(
            "I couldn't find an account with that ID. "
            "Could you verify the account number?"
        )
```

### Next Steps

Now that you understand how SWAIG connects AI to your code, let's trace the complete lifecycle of a request through the system.



---

## Request Lifecycle

> **Summary**: Trace the complete journey of a call through the SignalWire Agents SDK, from incoming call to conversation end.

### The Complete Call Flow

Understanding the request lifecycle helps you debug issues and optimize your agents. Here's the complete flow:

```diagram
┌─────────────────────────────────────────────────────────────────────────────┐
│                         Complete Call Lifecycle                             │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  PHASE 1: Call Setup                                                        │
│  ┌──────────────────────────────────────────────────────────────────────┐   │
│  │  1. Caller dials your phone number                                   │   │
│  │  2. SignalWire receives the call                                     │   │
│  │  3. SignalWire checks webhook configuration for the number           │   │
│  │  4. SignalWire requests SWML: POST https://your-agent.com/           │   │
│  └──────────────────────────────────────────────────────────────────────┘   │
│       │                                                                     │
│       ▼                                                                     │
│  PHASE 2: SWML Generation                                                   │
│  ┌──────────────────────────────────────────────────────────────────────┐   │
│  │  5. Your agent receives the HTTP request                             │   │
│  │  6. Agent builds SWML document (prompts, functions, languages)       │   │
│  │  7. Agent generates security tokens for SWAIG functions              │   │
│  │  8. Agent returns SWML JSON response                                 │   │
│  └──────────────────────────────────────────────────────────────────────┘   │
│       │                                                                     │
│       ▼                                                                     │
│  PHASE 3: AI Conversation                                                   │
│  ┌──────────────────────────────────────────────────────────────────────┐   │
│  │  9. SignalWire executes SWML (answers call, starts AI)               │   │
│  │  10. AI speaks greeting from prompt                                  │   │
│  │  11. User speaks, AI listens and transcribes                         │   │
│  │  12. AI processes and responds (loop continues)                      │   │
│  └──────────────────────────────────────────────────────────────────────┘   │
│       │                                                                     │
│       ▼                                                                     │
│  PHASE 4: Function Calls (as needed)                                        │
│  ┌──────────────────────────────────────────────────────────────────────┐   │
│  │  13. AI decides to call a function                                   │   │
│  │  14. SignalWire sends POST to /swaig with function name and args     │   │
│  │  15. Your agent executes the handler                                 │   │
│  │  16. Agent returns SwaigFunctionResult                               │   │
│  │  17. AI incorporates result and continues conversation               │   │
│  └──────────────────────────────────────────────────────────────────────┘   │
│       │                                                                     │
│       ▼                                                                     │
│  PHASE 5: Call End                                                          │
│  ┌──────────────────────────────────────────────────────────────────────┐   │
│  │  18. Call ends (hangup, transfer, or timeout)                        │   │
│  │  19. AI generates summary using post_prompt                          │   │
│  │  20. SignalWire sends POST to /post_prompt with summary              │   │
│  │  21. Your agent receives and processes summary                       │   │
│  └──────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Phase 1: Call Setup

When a call arrives at SignalWire:

```diagram
┌─────────────────────────────────────────────────────────────────────────────┐
│                              Call Setup                                     │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  Caller                    SignalWire                   Your Agent          │
│    │                           │                            │               │
│    │    Dial +1-555-123-4567   │                            │               │
│    │──────────────────────────►│                            │               │
│    │                           │                            │               │
│    │                           │  Look up webhook config    │               │
│    │                           │  for this phone number     │               │
│    │                           │                            │               │
│    │                           │  POST /                    │               │
│    │                           │───────────────────────────►│               │
│    │                           │                            │               │
│    │                           │  Content-Type: application/json            │
│    │                           │  Authorization: Basic xxx  │               │
│    │                           │                            │               │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

**Key points:**
- SignalWire knows which agent to contact based on phone number configuration
- The request includes Basic Auth credentials
- POST is the default; GET requests are also supported for SWML retrieval

### Phase 2: SWML Generation

Your agent builds and returns the SWML document:

```python
## Inside AgentBase._render_swml()

def _render_swml(self, request_body=None):
    """Generate SWML document for this agent."""

    # 1. Build the prompt (POM or text)
    prompt = self._build_prompt()

    # 2. Collect all SWAIG functions
    functions = self._tool_registry.get_functions()

    # 3. Generate webhook URLs with security tokens
    webhook_url = self._build_webhook_url("/swaig")

    # 4. Assemble AI configuration
    ai_config = {
        "prompt": prompt,
        "post_prompt": self._post_prompt,
        "post_prompt_url": self._build_webhook_url("/post_prompt"),
        "SWAIG": {
            "defaults": {"web_hook_url": webhook_url},
            "functions": functions
        },
        "hints": self._hints,
        "languages": self._languages,
        "params": self._params
    }

    # 5. Build complete SWML document
    swml = {
        "version": "1.0.0",
        "sections": {
            "main": [
                {"answer": {}},
                {"ai": ai_config}
            ]
        }
    }

    return swml
```

### Phase 3: AI Conversation

Once SignalWire has the SWML, it executes the instructions:

```diagram
┌─────────────────────────────────────────────────────────────────────────────┐
│                          AI Conversation Loop                               │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│         ┌───────────────────────────────────────────────────┐               │
│         │                                                   │               │
│         ▼                                                   │               │
│  ┌─────────────┐    ┌─────────────┐    ┌─────────────┐      │               │
│  │   Listen    │───►│  Transcribe │───►│  Process    │      │               │
│  │   (STT)     │    │   Speech    │    │   Intent    │      │               │
│  └─────────────┘    └─────────────┘    └─────────────┘      │               │
│                                              │              │               │
│                                              ▼              │               │
│                                    ┌─────────────────┐      │               │
│                                    │  Need function? │      │               │
│                                    └─────────────────┘      │               │
│                                      │           │          │               │
│                                     Yes          No         │               │
│                                      │           │          │               │
│                                      ▼           ▼          │               │
│                             ┌─────────────┐ ┌─────────────┐ │               │
│                             │ Call SWAIG  │ │  Generate   │ │               │
│                             │  Function   │ │  Response   │ │               │
│                             └─────────────┘ └─────────────┘ │               │
│                                      │           │          │               │
│                                      └─────┬─────┘          │               │
│                                            │                │               │
│                                            ▼                │               │
│                                    ┌─────────────┐          │               │
│                                    │   Speak     │──────────┘               │
│                                    │   (TTS)     │                          │
│                                    └─────────────┘                          │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

**AI Parameters that control this loop:**

| Parameter | Default | Purpose |
|-----------|---------|---------|
| `end_of_speech_timeout` | 500ms | Wait time after user stops speaking |
| `attention_timeout` | 15000ms | Max silence before AI prompts |
| `inactivity_timeout` | 30000ms | Max silence before ending call |
| `barge_match_string` | - | Words that immediately interrupt AI |

### Phase 4: Function Calls

When the AI needs to call a function:

```diagram
┌─────────────────────────────────────────────────────────────────────────────┐
│                          SWAIG Function Call                                │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  SignalWire AI                                           Your Agent         │
│       │                                                       │             │
│       │  POST /swaig                                          │             │
│       │  Authorization: Basic xxx                             │             │
│       │  Content-Type: application/json                       │             │
│       │                                                       │             │
│       │  {                                                    │             │
│       │    "action": "swaig_action",                          │             │
│       │    "function": "get_balance",                         │             │
│       │    "argument": {                                      │             │
│       │      "parsed": [{"account_id": "12345"}]              │             │
│       │    },                                                 │             │
│       │    "call_id": "...",                                  │             │
│       │    "global_data": {...}                               │             │
│       │  }                                                    │             │
│       │──────────────────────────────────────────────────────►│             │
│       │                                                       │             │
│       │                                            ┌──────────┴───────────┐ │
│       │                                            │ 1. Validate auth     │ │
│       │                                            │ 2. Find handler      │ │
│       │                                            │ 3. Execute function  │ │
│       │                                            │ 4. Build response    │ │
│       │                                            └──────────┬───────────┘ │
│       │                                                       │             │
│       │  200 OK                                               │             │
│       │  {                                                    │             │
│       │    "response": "Balance is $150.00",                  │             │
│       │    "action": [...]                                    │             │
│       │  }                                                    │             │
│       │◄──────────────────────────────────────────────────────│             │
│       │                                                       │             │
│       │  AI speaks the response                               │             │
│       │  and continues conversation                           │             │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Phase 5: Call End

When the call ends, the post-prompt summary is sent:

```diagram
┌─────────────────────────────────────────────────────────────────────────────┐
│                             Call Ending                                     │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  Trigger Events:                                                            │
│  ├── User hangs up                                                          │
│  ├── Agent triggers transfer action                                         │
│  ├── Agent triggers stop action                                             │
│  ├── Inactivity timeout                                                     │
│  └── Error condition                                                        │
│       │                                                                     │
│       ▼                                                                     │
│  ┌─────────────────────────────────────────────────────────────────────┐    │
│  │  AI generates summary using post_prompt instructions                │    │
│  │                                                                     │    │
│  │  Example post_prompt:                                               │    │
│  │  "Summarize: caller's issue, resolution status, any follow-up"      │    │
│  └─────────────────────────────────────────────────────────────────────┘    │
│       │                                                                     │
│       ▼                                                                     │
│  POST /post_prompt                                                          │
│  {                                                                          │
│    "post_prompt_data": {                                                    │
│      "raw": "Customer called about billing issue. Resolved by...",          │
│      "parsed": {...},                                                       │
│      "substituted": "..."                                                   │
│    },                                                                       │
│    "call_id": "...",                                                        │
│    "caller_id_num": "+15551234567",                                         │
│    "call_duration": 180                                                     │
│  }                                                                          │
│       │                                                                     │
│       ▼                                                                     │
│  Your agent receives summary for logging, CRM update, analytics             │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Handling Post-Prompt

Configure post-prompt handling in your agent:

```python
from signalwire_agents import AgentBase


class MyAgent(AgentBase):
    def __init__(self):
        super().__init__(name="my-agent")

        # Set the post-prompt instruction
        self.set_post_prompt(
            "Summarize this call including: "
            "1) The caller's main question or issue "
            "2) How it was resolved "
            "3) Any follow-up actions needed"
        )

        # Or use structured post-prompt with JSON output
        self.set_post_prompt_json({
            "issue": "string - the caller's main issue",
            "resolution": "string - how the issue was resolved",
            "follow_up": "boolean - whether follow-up is needed",
            "sentiment": "string - caller sentiment (positive/neutral/negative)"
        })

    def on_post_prompt(self, data):
        """Handle the call summary."""
        summary = data.get("post_prompt_data", {})
        call_id = data.get("call_id")

        # Log to your system
        self.log_call_summary(call_id, summary)

        # Update CRM
        self.update_crm(data)
```

### Request/Response Headers

#### SWML Request (GET or POST /)

```http
GET / HTTP/1.1
Host: your-agent.com
Authorization: Basic c2lnbmFsd2lyZTpwYXNzd29yZA==
Accept: application/json
X-Forwarded-For: signalwire-ip
X-Forwarded-Proto: https
```

#### SWML Response

```http
HTTP/1.1 200 OK
Content-Type: application/json

{"version": "1.0.0", "sections": {...}}
```

#### SWAIG Request (POST /swaig)

```http
POST /swaig HTTP/1.1
Host: your-agent.com
Authorization: Basic c2lnbmFsd2lyZTpwYXNzd29yZA==
Content-Type: application/json

{"action": "swaig_action", "function": "...", ...}
```

#### SWAIG Response

```http
HTTP/1.1 200 OK
Content-Type: application/json

{"response": "...", "action": [...]}
```

### Debugging the Lifecycle

#### View SWML Output

```bash
## See what your agent returns
curl -u signalwire:password http://localhost:3000/ | jq '.'

## Using swaig-test
swaig-test my_agent.py --dump-swml
```

#### Test Function Calls

```bash
## Call a function directly
swaig-test my_agent.py --exec get_balance --account_id 12345

## With verbose output
swaig-test my_agent.py --exec get_balance --account_id 12345 --verbose
```

#### Monitor Live Traffic

```python
from signalwire_agents import AgentBase


class DebugAgent(AgentBase):
    def __init__(self):
        super().__init__(name="debug-agent")

    def on_swml_request(self, request_data=None, callback_path=None, request=None):
        """Called when SWML is requested."""
        if request:
            print(f"SWML requested from: {request.client.host}")
            print(f"Headers: {dict(request.headers)}")

    def on_swaig_request(self, function_name, args, raw_data):
        """Called before each SWAIG function."""
        print(f"Function called: {function_name}")
        print(f"Arguments: {args}")
        print(f"Call ID: {raw_data.get('call_id')}")
```

### Error Handling

#### SWML Errors

If your agent can't generate SWML:

```python
def _render_swml(self):
    try:
        return self._build_swml()
    except Exception as e:
        # Return minimal valid SWML
        return {
            "version": "1.0.0",
            "sections": {
                "main": [
                    {"answer": {}},
                    {"play": {"url": "https://example.com/error.mp3"}},
                    {"hangup": {}}
                ]
            }
        }
```

#### SWAIG Errors

If a function fails:

```python
def get_balance(self, args, raw_data):
    try:
        balance = self.lookup_balance(args.get("account_id"))
        return SwaigFunctionResult(f"Your balance is ${balance}")
    except DatabaseError:
        return SwaigFunctionResult(
            "I'm having trouble accessing account information right now. "
            "Please try again in a moment."
        )
    except Exception as e:
        # Log the error but return user-friendly message
        self.logger.error(f"Function error: {e}")
        return SwaigFunctionResult(
            "I encountered an unexpected error. "
            "Let me transfer you to a representative."
        )
```

### Next Steps

Now that you understand the complete lifecycle, let's look at how security works throughout this flow.



---

## Security

> **Summary**: The SDK provides layered security through HTTP Basic Authentication for all requests and optional per-function token validation for sensitive operations.

### Security Layers

The SignalWire Agents SDK implements multiple security layers:

#### Layer 1: Transport Security (HTTPS)
- TLS encryption in transit
- Certificate validation

#### Layer 2: HTTP Basic Authentication
- Username/password validation
- Applied to all webhook endpoints

#### Layer 3: Function Token Security (Optional)
- Per-function security tokens
- Cryptographic validation

### HTTP Basic Authentication

Every request to your agent is protected by HTTP Basic Auth.

#### How It Works

1. **SignalWire sends request** with `Authorization: Basic <base64-encoded-credentials>` header
2. **Agent extracts header** and Base64 decodes credentials
3. **Agent splits** the decoded string into username and password
4. **Agent compares** credentials against configured values
5. **Result**: Match returns 200 + response; No match returns 401 Denied

#### Configuring Credentials

**Option 1: Environment Variables (Recommended for production)**

```bash
## Set explicit credentials
export SWML_BASIC_AUTH_USER=my_secure_username
export SWML_BASIC_AUTH_PASSWORD=my_very_secure_password_here
```

**Option 2: Let SDK Generate Credentials (Development)**

If you don't set credentials, the SDK:

- Uses username: `signalwire`
- Generates a random password on each startup
- Prints the password to the console

```bash
$ python my_agent.py
INFO: Agent 'my-agent' starting...
INFO: Basic Auth credentials:
INFO:   Username: signalwire
INFO:   Password: a7b3x9k2m5n1p8q4  # Use this in SignalWire webhook config
```

#### Credentials in Your Agent

```python
from signalwire_agents import AgentBase
import os


class MyAgent(AgentBase):
    def __init__(self):
        super().__init__(
            name="my-agent",
            # Credentials from environment or defaults
            basic_auth_user=os.getenv("SWML_BASIC_AUTH_USER"),
            basic_auth_password=os.getenv("SWML_BASIC_AUTH_PASSWORD")
        )
```

### Function Token Security

For sensitive operations, enable per-function token validation.

#### How Function Tokens Work

**SWML Generation (GET /)**

1. Agent generates SWML
2. For each secure function, generate unique token
3. Token embedded in function's `web_hook_url`

```json
"functions": [{
  "function": "transfer_funds",
  "web_hook_url": "https://agent.com/swaig?token=abc123xyz..."
}]
```

**Function Call (POST /swaig)**

1. SignalWire calls webhook URL with token
2. Agent extracts token from request
3. Agent validates token cryptographically
4. If valid, execute function
5. If invalid, reject with 403

#### Enabling Token Security

```python
from signalwire_agents import AgentBase, SwaigFunctionResult


class SecureAgent(AgentBase):
    def __init__(self):
        super().__init__(name="secure-agent")

        # Regular function - Basic Auth only
        self.define_tool(
            name="get_balance",
            description="Get account balance",
            parameters={...},
            handler=self.get_balance
        )

        # Secure function - Basic Auth + Token validation
        self.define_tool(
            name="transfer_funds",
            description="Transfer funds between accounts",
            parameters={...},
            handler=self.transfer_funds,
            secure=True  # Enable token security
        )

    def get_balance(self, args, raw_data):
        return SwaigFunctionResult("Balance is $150.00")

    def transfer_funds(self, args, raw_data):
        # This only executes if token is valid
        return SwaigFunctionResult("Transfer complete")
```

#### Token Generation

Tokens are generated using cryptographic hashing:

```python
## Simplified view of token generation
import hashlib
import secrets

def generate_function_token(function_name, secret_key, call_context):
    """Generate a secure token for a function."""
    # Combine function name, secret, and context
    token_input = f"{function_name}:{secret_key}:{call_context}"

    # Generate cryptographic hash
    token = hashlib.sha256(token_input.encode()).hexdigest()

    return token
```

### HTTPS Configuration

For production, enable HTTPS:

#### Using SSL Certificates

```bash
## Environment variables for SSL
export SWML_SSL_ENABLED=true
export SWML_SSL_CERT_PATH=/path/to/cert.pem
export SWML_SSL_KEY_PATH=/path/to/key.pem
export SWML_DOMAIN=my-agent.example.com
```

```python
from signalwire_agents import AgentBase


class SecureAgent(AgentBase):
    def __init__(self):
        super().__init__(
            name="secure-agent",
            ssl_enabled=True,
            ssl_cert_path="/path/to/cert.pem",
            ssl_key_path="/path/to/key.pem"
        )
```

#### Using a Reverse Proxy (Recommended)

Most production deployments use a reverse proxy for SSL:

**Traffic Flow**: SignalWire → HTTPS → nginx/Caddy (SSL termination) → HTTP → Your Agent (localhost:3000)

**Benefits**:

- SSL handled by proxy
- Easy certificate management
- Load balancing
- Additional security headers

Set the proxy URL so your agent generates correct webhook URLs:

```bash
export SWML_PROXY_URL_BASE=https://my-agent.example.com
```

### Security Best Practices

#### 1. Never Commit Credentials

```gitignore
## .gitignore
.env
.env.local
*.pem
*.key
```

#### 2. Use Strong Passwords

```bash
## Generate a strong password
python -c "import secrets; print(secrets.token_urlsafe(32))"
```

#### 3. Validate All Inputs

```python
def transfer_funds(self, args, raw_data):
    amount = args.get("amount")
    to_account = args.get("to_account")

    # Validate inputs
    if not amount or not isinstance(amount, (int, float)):
        return SwaigFunctionResult("Invalid amount specified")

    if amount <= 0:
        return SwaigFunctionResult("Amount must be positive")

    if amount > 10000:
        return SwaigFunctionResult(
            "Transfers over $10,000 require additional verification"
        )

    if not to_account or len(to_account) != 10:
        return SwaigFunctionResult("Invalid account number")

    # Proceed with transfer
    return SwaigFunctionResult(f"Transferred ${amount} to account {to_account}")
```

#### 4. Use Secure Functions for Sensitive Operations

```python
## Mark sensitive functions as secure
self.define_tool(
    name="delete_account",
    description="Delete a customer account",
    parameters={...},
    handler=self.delete_account,
    secure=True  # Always use token security for destructive operations
)

self.define_tool(
    name="change_password",
    description="Change account password",
    parameters={...},
    handler=self.change_password,
    secure=True
)

self.define_tool(
    name="transfer_funds",
    description="Transfer money",
    parameters={...},
    handler=self.transfer_funds,
    secure=True
)
```

#### 5. Log Security Events

```python
import logging


class SecureAgent(AgentBase):
    def __init__(self):
        super().__init__(name="secure-agent")
        self.logger = logging.getLogger(__name__)

    def transfer_funds(self, args, raw_data):
        call_id = raw_data.get("call_id")
        caller = raw_data.get("caller_id_num")
        amount = args.get("amount")
        to_account = args.get("to_account")

        # Log the sensitive operation
        self.logger.info(
            f"Transfer initiated: call_id={call_id}, "
            f"caller={caller}, amount={amount}, to={to_account}"
        )

        # Process transfer
        result = self.process_transfer(amount, to_account)

        self.logger.info(
            f"Transfer completed: call_id={call_id}, result={result}"
        )

        return SwaigFunctionResult(f"Transfer of ${amount} complete")
```

#### 6. Implement Rate Limiting

```python
from collections import defaultdict
from time import time


class RateLimitedAgent(AgentBase):
    def __init__(self):
        super().__init__(name="rate-limited-agent")
        self.call_counts = defaultdict(list)
        self.rate_limit = 10  # calls per minute

    def check_rate_limit(self, caller_id):
        """Check if caller has exceeded rate limit."""
        now = time()
        minute_ago = now - 60

        # Clean old entries
        self.call_counts[caller_id] = [
            t for t in self.call_counts[caller_id] if t > minute_ago
        ]

        # Check limit
        if len(self.call_counts[caller_id]) >= self.rate_limit:
            return False

        # Record this call
        self.call_counts[caller_id].append(now)
        return True

    def get_balance(self, args, raw_data):
        caller = raw_data.get("caller_id_num")

        if not self.check_rate_limit(caller):
            return SwaigFunctionResult(
                "You've made too many requests. Please wait a moment."
            )

        # Process normally
        return SwaigFunctionResult("Your balance is $150.00")
```

### Configuring SignalWire Webhooks

When setting up your phone number in SignalWire:

| Setting | Value |
|---------|-------|
| Handle Calls Using | SWML Script |
| SWML Script URL | `https://my-agent.example.com/` |
| Request Method | POST |
| Authentication | HTTP Basic Auth |
| Username | Your configured username |
| Password | Your configured password |

### Summary

| Security Feature | When to Use | How to Enable |
|-----------------|-------------|---------------|
| **Basic Auth** | Always | Automatic (set env vars for custom) |
| **Function Tokens** | Sensitive operations | `secure=True` on define_tool |
| **HTTPS** | Production | SSL certs or reverse proxy |
| **Input Validation** | All functions | Manual validation in handlers |
| **Rate Limiting** | Public-facing agents | Manual implementation |
| **Logging** | All security events | Python logging module |

### Next Steps

You now understand the core concepts of the SignalWire Agents SDK. Let's move on to building agents.



# Part: Building Agents

---

# Building Agents

> **Summary**: Learn how to build voice AI agents using AgentBase, from basic configuration to advanced prompt engineering and voice customization.

## What You'll Learn

This chapter covers everything you need to build production-quality agents:

1. **AgentBase** - The foundation class and its capabilities
2. **Static vs Dynamic** - Choosing the right pattern for your use case
3. **Prompts & POM** - Crafting effective prompts with the Prompt Object Model
4. **Voice & Language** - Configuring voices and multi-language support
5. **AI Parameters** - Tuning conversation behavior
6. **Hints** - Improving speech recognition accuracy
7. **Call Flow** - Customizing when and how calls are answered

## Prerequisites

Before building agents, you should understand:

- Core concepts from Chapter 2 (SWML, SWAIG, Lifecycle)
- Basic Python class structure
- How SignalWire processes calls

## Agent Architecture Overview

```diagram
┌─────────────────────────────────────────────────────────────────────────────┐
│                          Agent Components                                   │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  ┌───────────────────────────────────────────────────────────────────┐      │
│  │                       Your Agent Class                            │      │
│  │                      (extends AgentBase)                          │      │
│  └───────────────────────────────────────────────────────────────────┘      │
│                                    │                                        │
│                                    ▼                                        │
│  ┌───────────────────────────────────────────────────────────────────┐      │
│  │                        Configuration                              │      │
│  ├───────────────────────────────────────────────────────────────────┤      │
│  │                                                                   │      │
│  │  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐                │      │
│  │  │   Prompts   │  │    Voice    │  │  AI Params  │                │      │
│  │  ├─────────────┤  ├─────────────┤  ├─────────────┤                │      │
│  │  │ • Role      │  │ • Language  │  │ • Timeouts  │                │      │
│  │  │ • Guidelines│  │ • Voice     │  │ • Barge     │                │      │
│  │  │ • Rules     │  │ • TTS Engine│  │ • Attention │                │      │
│  │  └─────────────┘  └─────────────┘  └─────────────┘                │      │
│  │                                                                   │      │
│  │  ┌─────────────┐  ┌─────────────┐  ┌───────────────┐              │      │
│  │  │    Hints    │  │  Functions  │  │   Skills      │              │      │
│  │  ├─────────────┤  ├─────────────┤  ├───────────────┤              │      │
│  │  │ • Keywords  │  │ • Tools     │  │ • Plugins     │              │      │
│  │  │ • Names     │  │ • DataMap   │  │ • Add-ons     │              │      │
│  │  │ • Terms     │  │ • Handlers  │  │ • Integrations│              │      │
│  │  └─────────────┘  └─────────────┘  └───────────────┘              │      │
│  └───────────────────────────────────────────────────────────────────┘      │
│                                    │                                        │
│                                    ▼                                        │
│  ┌───────────────────────────────────────────────────────────────────┐      │
│  │                         SWML Output                               │      │
│  │                    (Generated automatically)                      │      │
│  └───────────────────────────────────────────────────────────────────┘      │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

## A Complete Agent Example

Here's what a production agent looks like:

```python
from signalwire_agents import AgentBase, SwaigFunctionResult

class CustomerSupportAgent(AgentBase):
    """Production customer support agent."""

    def __init__(self):
        super().__init__(
            name="customer-support",
            route="/support"
        )

        # Voice configuration
        self.add_language("English", "en-US", "rime.spore")

        # AI behavior
        self.set_params({
            "end_of_speech_timeout": 500,
            "attention_timeout": 15000,
            "inactivity_timeout": 30000
        })

        # Prompts
        self.prompt_add_section(
            "Role",
            "You are Alex, a friendly customer support agent for Acme Inc."
        )

        self.prompt_add_section(
            "Guidelines",
            body="Follow these guidelines:",
            bullets=[
                "Be helpful and professional",
                "Ask clarifying questions when needed",
                "Keep responses concise for voice",
                "Offer to transfer if you cannot help"
            ]
        )

        # Speech recognition hints
        self.add_hints([
            "Acme", "account number", "order status",
            "refund", "billing", "representative"
        ])

        # Functions
        self.define_tool(
            name="check_order",
            description="Look up an order by order number",
            parameters={
                "type": "object",
                "properties": {
                    "order_number": {
                        "type": "string",
                        "description": "The order number to look up"
                    }
                },
                "required": ["order_number"]
            },
            handler=self.check_order
        )

        # Skills
        self.add_skill("datetime")

        # Post-call summary
        self.set_post_prompt(
            "Summarize: issue type, resolution, customer satisfaction"
        )

    def check_order(self, args, raw_data):
        order_number = args.get("order_number")
        # Your business logic here
        return SwaigFunctionResult(
            f"Order {order_number}: Shipped on Monday, arriving Thursday"
        )

if __name__ == "__main__":
    agent = CustomerSupportAgent()
    agent.run(host="0.0.0.0", port=3000)
```

## Chapter Contents

| Section | Description |
|---------|-------------|
| [AgentBase](03_01_agent-base.md) | Core class and constructor options |
| [Static vs Dynamic](03_02_static-vs-dynamic.md) | Choosing the right pattern |
| [Prompts & POM](03_03_prompts-pom.md) | Prompt engineering for voice AI |
| [Voice & Language](03_04_voice-language.md) | Voice selection and multi-language |
| [AI Parameters](03_05_ai-parameters.md) | Behavior tuning |
| [Hints](03_06_hints.md) | Speech recognition improvement |
| [Call Flow](03_07_call-flow.md) | Customizing call answer behavior |

## Key Patterns

### Pattern 1: Class-Based Agent

Best for complex agents with multiple functions:

```python
class MyAgent(AgentBase):
    def __init__(self):
        super().__init__(name="my-agent")
        self.configure()

    def configure(self):
        # All configuration here
        pass
```

### Pattern 2: Functional Agent

Quick agents for simple use cases:

```python
from signalwire_agents import AgentBase

agent = AgentBase(name="simple-agent")
agent.add_language("English", "en-US", "rime.spore")
agent.prompt_add_section("Role", "You are a helpful assistant.")
agent.run()
```

### Pattern 3: Multi-Agent Server

Multiple agents on one server:

```python
from signalwire_agents import AgentServer

server = AgentServer()
server.register(SupportAgent(), "/support")
server.register(SalesAgent(), "/sales")
server.register(BillingAgent(), "/billing")
server.run(port=3000)
```

## Testing Your Agent

Always test before deploying:

```bash
# View SWML output
swaig-test my_agent.py --dump-swml

# List registered functions
swaig-test my_agent.py --list-tools

# Test a function
swaig-test my_agent.py --exec check_order --order_number 12345
```

Let's start with understanding AgentBase in depth.

## Class Overview

```diagram
┌─────────────────────────────────────────────────────────────────────────────┐
│                            AgentBase Inheritance                            │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│                               AgentBase                                     │
│                                   │                                         │
│                 ┌─────────────────┼────────────────┐                        │
│                 │                 │                │                        │
│                 ▼                 ▼                ▼                        │
│           ┌──────────┐      ┌──────────┐    ┌───────────┐                   │
│           │ AuthMixin│      │ WebMixin │    │SWMLService│                   │
│           └──────────┘      └──────────┘    └───────────┘                   │
│                                                                             │
│           ┌───────────┐     ┌──────────┐    ┌──────────┐                    │
│           │PromptMixin│     │ ToolMixin│    │SkillMixin│                    │
│           └───────────┘     └──────────┘    └──────────┘                    │
│                                                                             │
│           ┌─────────────┐   ┌───────────────┐                               │
│           │AIConfigMixin│   │ServerlessMixin│                               │
│           └─────────────┘   └───────────────┘                               │
│                                                                             │
│           ┌──────────┐                                                      │
│           │StateMixin│                                                      │
│           └──────────┘                                                      │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

## Constructor Parameters

```python
from signalwire_agents import AgentBase

agent = AgentBase(
    # Required
    name="my-agent",                    # Unique agent identifier

    # Server Configuration
    route="/",                          # HTTP route path (default: "/")
    host="0.0.0.0",                     # Bind address (default: "0.0.0.0")
    port=3000,                          # Server port (default: 3000)

    # Authentication
    basic_auth=("user", "pass"),        # Override env var credentials

    # Behavior
    auto_answer=True,                   # Answer calls automatically
    use_pom=True,                       # Use Prompt Object Model

    # Recording
    record_call=False,                  # Enable call recording
    record_format="mp4",                # Recording format
    record_stereo=True,                 # Stereo recording

    # Tokens and Security
    token_expiry_secs=3600,             # Function token expiration

    # Advanced
    default_webhook_url=None,           # Override webhook URL
    agent_id=None,                      # Custom agent ID (auto-generated)
    native_functions=None,              # Built-in SignalWire functions
    schema_path=None,                   # Custom SWML schema path
    suppress_logs=False,                # Disable logging
    config_file=None                    # Load from config file
)
```

## Parameter Reference

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `name` | str | Required | Unique identifier for the agent |
| `route` | str | "/" | HTTP route where agent is accessible |
| `host` | str | "0.0.0.0" | IP address to bind server |
| `port` | int | 3000 | Port number for server |
| `basic_auth` | tuple | None | (username, password) for auth |
| `use_pom` | bool | True | Enable Prompt Object Model |
| `auto_answer` | bool | True | Auto-answer incoming calls |
| `record_call` | bool | False | Enable call recording |
| `record_format` | str | "mp4" | Recording file format |
| `record_stereo` | bool | True | Record in stereo |
| `token_expiry_secs` | int | 3600 | Token validity period |
| `native_functions` | list | None | SignalWire native functions |
| `suppress_logs` | bool | False | Disable agent logs |

## Creating an Agent

### Method 1: Class-Based (Recommended)

```python
from signalwire_agents import AgentBase, SwaigFunctionResult


class MyAgent(AgentBase):
    def __init__(self):
        super().__init__(name="my-agent")
        self._setup()

    def _setup(self):
        # Voice
        self.add_language("English", "en-US", "rime.spore")

        # Prompts
        self.prompt_add_section("Role", "You are a helpful assistant.")

        # Functions
        self.define_tool(
            name="greet",
            description="Greet the user",
            parameters={},
            handler=self.greet
        )

    def greet(self, args, raw_data):
        return SwaigFunctionResult("Hello! How can I help you today?")


if __name__ == "__main__":
    agent = MyAgent()
    agent.run()
```

### Method 2: Instance-Based

```python
from signalwire_agents import AgentBase

agent = AgentBase(name="quick-agent")
agent.add_language("English", "en-US", "rime.spore")
agent.prompt_add_section("Role", "You are a helpful assistant.")
agent.run()
```

### Method 3: Declarative (PROMPT_SECTIONS)

```python
from signalwire_agents import AgentBase


class DeclarativeAgent(AgentBase):
    PROMPT_SECTIONS = {
        "Role": "You are a helpful customer service agent.",
        "Guidelines": [
            "Be professional and courteous",
            "Ask clarifying questions when needed",
            "Keep responses concise"
        ],
        "Rules": {
            "body": "Always follow these rules:",
            "bullets": [
                "Never share customer data",
                "Escalate complex issues"
            ]
        }
    }

    def __init__(self):
        super().__init__(name="declarative-agent")
        self.add_language("English", "en-US", "rime.spore")
```

## Key Methods

### Configuration Methods

```python
# Voice and Language
agent.add_language(name, code, voice)       # Add language support
agent.set_languages(languages)               # Set all languages at once

# Prompts
agent.prompt_add_section(title, body)        # Add prompt section
agent.prompt_add_subsection(parent, title)   # Add subsection
agent.set_post_prompt(text)                  # Set post-call summary prompt

# AI Parameters
agent.set_params(params_dict)                # Set AI behavior parameters
agent.set_param_value(key, value)            # Set single parameter

# Speech Recognition
agent.add_hints(hints_list)                  # Add speech hints
agent.add_hint(hint_string)                  # Add single hint

# Functions
agent.define_tool(name, description, ...)   # Define SWAIG function
agent.add_skill(skill_name)                 # Add a skill

# Pronunciation
agent.add_pronunciation(replace, with_text)  # Add pronunciation rule
```

### Runtime Methods

```python
# Start server
agent.run(host="0.0.0.0", port=3000)

# Get SWML document
swml = agent.get_swml()

# Access components
agent.pom              # Prompt Object Model
agent.data_map         # DataMap builder
```

## Agent Lifecycle

```diagram
┌─────────────────────────────────────────────────────────────────────────────┐
│                            Agent Lifecycle                                  │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  1. Instantiation                                                           │
│     └── __init__() called                                                   │
│         ├── Mixins initialized                                              │
│         ├── Config loaded                                                   │
│         └── Routes registered                                               │
│                                                                             │
│  2. Configuration                                                           │
│     └── Setup methods called                                                │
│         ├── add_language()                                                  │
│         ├── prompt_add_section()                                            │
│         ├── define_tool()                                                   │
│         └── add_skill()                                                     │
│                                                                             │
│  3. Server Start                                                            │
│     └── run() called                                                        │
│         ├── FastAPI app created                                             │
│         ├── Routes mounted                                                  │
│         └── Uvicorn started                                                 │
│                                                                             │
│  4. Request Handling                                                        │
│     ├── GET /  ──► Return SWML document                                     │
│     ├── POST / ──► Return SWML document                                     │
│     └── POST /swaig ──► Execute SWAIG function                              │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

## Configuration File

Load configuration from a YAML/JSON file:

```python
agent = AgentBase(
    name="my-agent",
    config_file="config/agent.yaml"
)
```

```yaml
# config/agent.yaml
name: my-agent
route: /support
host: 0.0.0.0
port: 3000
```

## Environment Variables

AgentBase respects these environment variables:

| Variable | Purpose |
|----------|---------|
| `SWML_BASIC_AUTH_USER` | Basic auth username |
| `SWML_BASIC_AUTH_PASSWORD` | Basic auth password |
| `SWML_PROXY_URL_BASE` | Base URL for webhooks behind proxy |
| `SWML_SSL_ENABLED` | Enable SSL |
| `SWML_SSL_CERT_PATH` | SSL certificate path |
| `SWML_SSL_KEY_PATH` | SSL key path |
| `SWML_DOMAIN` | Domain for SSL |

## Multi-Agent Server

Run multiple agents on one server:

```python
from signalwire_agents import AgentServer


class SupportAgent(AgentBase):
    def __init__(self):
        super().__init__(name="support", route="/support")
        # ... configuration


class SalesAgent(AgentBase):
    def __init__(self):
        super().__init__(name="sales", route="/sales")
        # ... configuration


# Register multiple agents
server = AgentServer()
server.register(SupportAgent())
server.register(SalesAgent())
server.run(host="0.0.0.0", port=3000)
```

Access agents at:

- `http://localhost:3000/support`
- `http://localhost:3000/sales`

## Best Practices

1. **Use class-based agents** for anything beyond simple prototypes
2. **Organize configuration** into logical private methods
3. **Set explicit credentials** in production via environment variables
4. **Use meaningful agent names** for logging and debugging
5. **Test with swaig-test** before deploying

```python
class WellOrganizedAgent(AgentBase):
    def __init__(self):
        super().__init__(name="organized-agent")
        self._configure_voice()
        self._configure_prompts()
        self._configure_functions()
        self._configure_skills()

    def _configure_voice(self):
        self.add_language("English", "en-US", "rime.spore")
        self.set_params({
            "end_of_speech_timeout": 500,
            "attention_timeout": 15000
        })

    def _configure_prompts(self):
        self.prompt_add_section("Role", "You are a helpful assistant.")

    def _configure_functions(self):
        self.define_tool(
            name="help",
            description="Get help",
            parameters={},
            handler=self.get_help
        )

    def _configure_skills(self):
        self.add_skill("datetime")

    def get_help(self, args, raw_data):
        return SwaigFunctionResult("I can help you with...")
```



---

## Static vs Dynamic Agents

> **Summary**: Choose between static agents (fixed configuration) and dynamic agents (runtime customization) based on whether you need per-call personalization.

### Understanding the Difference

| Aspect | Static Agent | Dynamic Agent |
|--------|--------------|---------------|
| **Configuration** | Set once at startup | Per-request based on call data |
| **Behavior** | Same for all callers | Different for different callers |

**Use Static When:**
- Same prompt for everyone
- Generic assistant
- Simple IVR
- FAQ bot

**Use Dynamic When:**
- Personalized greetings
- Caller-specific data
- Account-based routing
- Multi-tenant applications

### Static Agents

Static agents have fixed configuration determined at instantiation time.

#### Example: Static Customer Service Agent

```python
from signalwire_agents import AgentBase, SwaigFunctionResult


class StaticSupportAgent(AgentBase):
    """Same behavior for all callers."""

    def __init__(self):
        super().__init__(name="static-support")

        self.add_language("English", "en-US", "rime.spore")

        self.prompt_add_section(
            "Role",
            "You are a customer service agent for Acme Corp. "
            "Help callers with general inquiries about our products."
        )

        self.prompt_add_section(
            "Guidelines",
            bullets=[
                "Be helpful and professional",
                "Answer questions about products",
                "Transfer complex issues to support"
            ]
        )

        self.define_tool(
            name="get_store_hours",
            description="Get store hours",
            parameters={},
            handler=self.get_store_hours
        )

    def get_store_hours(self, args, raw_data):
        return SwaigFunctionResult(
            "We're open Monday through Friday, 9 AM to 5 PM."
        )


if __name__ == "__main__":
    agent = StaticSupportAgent()
    agent.run()
```

### Dynamic Agents

Dynamic agents customize their behavior based on the incoming request using the `on_swml_request` method.

#### The on_swml_request Method

```python
def on_swml_request(self, request_data=None, callback_path=None, request=None):
    """
    Called before SWML is generated for each request.

    Args:
        request_data: Optional dict containing the parsed POST body from SignalWire.
                     Call information is nested under the 'call' key:
                     - call["call_id"]: Unique call identifier
                     - call["from"]: Caller's phone number
                     - call["from_number"]: Alternative caller number field
                     - call["to"]: Number that was called
                     - call["direction"]: "inbound" or "outbound"
        callback_path: Optional callback path for routing
        request: Optional FastAPI Request object for accessing query params, headers, etc.

    Returns:
        Optional dict with modifications to apply (usually None for simple cases)
    """
    pass
```

#### Example: Dynamic Personalized Agent

```python
from signalwire_agents import AgentBase, SwaigFunctionResult


class DynamicPersonalizedAgent(AgentBase):
    """Customizes greeting based on caller."""

    # Simulated customer database
    CUSTOMERS = {
        "+15551234567": {"name": "John Smith", "tier": "gold", "account": "A001"},
        "+15559876543": {"name": "Jane Doe", "tier": "platinum", "account": "A002"},
    }

    def __init__(self):
        super().__init__(name="dynamic-agent")

        self.add_language("English", "en-US", "rime.spore")

        # Base configuration
        self.set_params({
            "end_of_speech_timeout": 500,
            "attention_timeout": 15000
        })

        # Functions available to all callers
        self.define_tool(
            name="get_account_status",
            description="Get the caller's account status",
            parameters={},
            handler=self.get_account_status
        )

        # Store caller info for function access
        self._current_caller = None

    def on_swml_request(self, request_data=None, callback_path=None, request=None):
        """Customize behavior based on caller."""
        # Extract call data (nested under 'call' key in request_data)
        call_data = (request_data or {}).get("call", {})
        caller_num = call_data.get("from") or call_data.get("from_number", "")

        # Look up caller in database
        customer = self.CUSTOMERS.get(caller_num)

        if customer:
            # Known customer - personalized experience
            self._current_caller = customer

            self.prompt_add_section(
                "Role",
                f"You are a premium support agent for Acme Corp. "
                f"You are speaking with {customer['name']}, a {customer['tier']} member."
            )

            self.prompt_add_section(
                "Context",
                f"Customer account: {customer['account']}\n"
                f"Membership tier: {customer['tier'].upper()}"
            )

            if customer["tier"] == "platinum":
                self.prompt_add_section(
                    "Special Treatment",
                    "This is a platinum customer. Prioritize their requests and "
                    "offer expedited service on all issues."
                )
        else:
            # Unknown caller - generic experience
            self._current_caller = None

            self.prompt_add_section(
                "Role",
                "You are a customer service agent for Acme Corp. "
                "Help the caller with their inquiry and offer to create an account."
            )

    def get_account_status(self, args, raw_data):
        if self._current_caller:
            return SwaigFunctionResult(
                f"Account {self._current_caller['account']} is active. "
                f"Tier: {self._current_caller['tier'].upper()}"
            )
        return SwaigFunctionResult(
            "No account found. Would you like to create one?"
        )


if __name__ == "__main__":
    agent = DynamicPersonalizedAgent()
    agent.run()
```

### Request Data Fields

The `request_data` dictionary is the parsed POST body from SignalWire. Call information is **nested under the `call` key**:

| Field | Description | Example |
|-------|-------------|---------|
| `call["call_id"]` | Unique call identifier | `"a1b2c3d4-..."` |
| `call["from"]` | Caller's phone number | `"+15551234567"` |
| `call["from_number"]` | Alternative caller number field | `"+15551234567"` |
| `call["to"]` | Number that was called | `"+15559876543"` |
| `call["direction"]` | Call direction | `"inbound"` |

**Important:** Always use defensive access when working with `request_data`:

```python
def on_swml_request(self, request_data=None, callback_path=None, request=None):
    call_data = (request_data or {}).get("call", {})
    caller_num = call_data.get("from") or call_data.get("from_number", "")
    call_id = call_data.get("call_id", "")
```

### Dynamic Function Registration

You can also register functions dynamically based on the caller:

```python
class DynamicFunctionsAgent(AgentBase):
    """Different functions for different callers."""

    ADMIN_NUMBERS = ["+15551111111", "+15552222222"]

    def __init__(self):
        super().__init__(name="dynamic-functions")
        self.add_language("English", "en-US", "rime.spore")

        # Base functions for everyone
        self.define_tool(
            name="get_info",
            description="Get general information",
            parameters={},
            handler=self.get_info
        )

    def on_swml_request(self, request_data=None, callback_path=None, request=None):
        call_data = (request_data or {}).get("call", {})
        caller_num = call_data.get("from") or call_data.get("from_number", "")

        self.prompt_add_section("Role", "You are a helpful assistant.")

        # Add admin functions only for admin callers
        if caller_num in self.ADMIN_NUMBERS:
            self.prompt_add_section(
                "Admin Access",
                "This caller has administrator privileges. "
                "They can access system administration functions."
            )

            self.define_tool(
                name="admin_reset",
                description="Reset system configuration (admin only)",
                parameters={},
                handler=self.admin_reset
            )

            self.define_tool(
                name="admin_report",
                description="Generate system report (admin only)",
                parameters={},
                handler=self.admin_report
            )

    def get_info(self, args, raw_data):
        return SwaigFunctionResult("General information...")

    def admin_reset(self, args, raw_data):
        return SwaigFunctionResult("System reset initiated.")

    def admin_report(self, args, raw_data):
        return SwaigFunctionResult("Report generated: All systems operational.")
```

### Multi-Tenant Applications

Dynamic agents are ideal for multi-tenant scenarios:

```python
class MultiTenantAgent(AgentBase):
    """Different branding per tenant."""

    TENANTS = {
        "+15551111111": {
            "company": "Acme Corp",
            "voice": "rime.spore",
            "greeting": "Welcome to Acme Corp support!"
        },
        "+15552222222": {
            "company": "Beta Industries",
            "voice": "rime.marsh",
            "greeting": "Thank you for calling Beta Industries!"
        }
    }

    def __init__(self):
        super().__init__(name="multi-tenant")

    def on_swml_request(self, request_data=None, callback_path=None, request=None):
        call_data = (request_data or {}).get("call", {})
        called_num = call_data.get("to", "")

        tenant = self.TENANTS.get(called_num, {
            "company": "Default Company",
            "voice": "rime.spore",
            "greeting": "Hello!"
        })

        # Configure for this tenant
        self.add_language("English", "en-US", tenant["voice"])

        self.prompt_add_section(
            "Role",
            f"You are a customer service agent for {tenant['company']}. "
            f"Start by saying: {tenant['greeting']}"
        )
```

### Comparison Summary

| Aspect | Static | Dynamic |
|--------|--------|---------|
| **Configuration** | Once at startup | Per-request |
| **Performance** | Slightly faster | Minimal overhead |
| **Use Case** | Generic assistants | Personalized experiences |
| **Complexity** | Simpler | More complex |
| **Testing** | Easier | Requires more scenarios |
| **Method** | `__init__` only | `on_swml_request` |

### Best Practices

1. **Start static, go dynamic when needed** - Don't over-engineer
2. **Cache expensive lookups** - Database calls in `on_swml_request` add latency
3. **Clear prompts between calls** - Use `self.pom.clear()` if reusing sections
4. **Log caller info** - Helps with debugging dynamic behavior
5. **Test multiple scenarios** - Each caller path needs testing

```python
def on_swml_request(self, request_data=None, callback_path=None, request=None):
    # Clear previous dynamic configuration
    self.pom.clear()

    # Extract call data
    call_data = (request_data or {}).get("call", {})

    # Log for debugging
    self.log.info("request_received",
        caller=call_data.get("from") or call_data.get("from_number"),
        called=call_data.get("to")
    )

    # Configure based on request
    self._configure_for_caller(request_data)
```



---

## Prompts & POM

> **Summary**: The Prompt Object Model (POM) provides a structured way to build AI prompts using sections, subsections, and bullets rather than raw text.

### Why POM?

| Aspect | Raw Text Prompt | POM Structured Prompt |
|--------|-----------------|----------------------|
| **Format** | One long string | Organized sections with body, bullets, subsections |
| **Maintainability** | Hard to maintain | Easy to modify individual sections |
| **Structure** | No structure | Clear hierarchy (Role → Guidelines → Rules) |
| **Extensibility** | Difficult to extend | Reusable components |

**Raw Text Problems:**
- Everything mixed together in one string
- Hard to find and update specific instructions
- Difficult to share sections between agents

**POM Benefits:**
- Sections keep concerns separated
- Bullets make lists scannable
- Subsections add depth without clutter
- Renders to clean, formatted markdown

### POM Structure

```diagram
┌─────────────────────────────────────────────────────────────────────────────┐
│                          POM Hierarchy                                      │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  Prompt                                                                     │
│  │                                                                          │
│  ├── Section: "Role"                                                        │
│  │   └── body: "You are a customer service agent..."                        │
│  │                                                                          │
│  ├── Section: "Guidelines"                                                  │
│  │   ├── body: "Follow these guidelines:"                                   │
│  │   └── bullets:                                                           │
│  │       • "Be professional"                                                │
│  │       • "Ask clarifying questions"                                       │
│  │       • "Keep responses concise"                                         │
│  │                                                                          │
│  └── Section: "Rules"                                                       │
│      ├── body: "Adhere to these rules:"                                     │
│      └── subsections:                                                       │
│          ├── Subsection: "Security"                                         │
│          │   └── bullets: ["Never share passwords", ...]                    │
│          └── Subsection: "Privacy"                                          │
│              └── bullets: ["Don't ask for SSN", ...]                        │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Adding Sections

#### Basic Section with Body

```python
from signalwire_agents import AgentBase


class MyAgent(AgentBase):
    def __init__(self):
        super().__init__(name="my-agent")

        # Simple section with body text
        self.prompt_add_section(
            "Role",
            "You are a helpful customer service representative for Acme Corp."
        )
```

#### Section with Bullets

```python
## Section with bullet points
self.prompt_add_section(
    "Guidelines",
    body="Follow these guidelines when speaking with customers:",
    bullets=[
        "Be professional and courteous at all times",
        "Ask clarifying questions when the request is unclear",
        "Keep responses concise - this is a voice conversation",
        "Offer to transfer to a human if you cannot help"
    ]
)
```

#### Section with Numbered Bullets

```python
## Use numbered list instead of bullets
self.prompt_add_section(
    "Process",
    body="Follow this process for each call:",
    bullets=[
        "Greet the customer warmly",
        "Identify the reason for their call",
        "Resolve the issue or transfer",
        "Thank them and end the call"
    ],
    numbered_bullets=True  # 1. 2. 3. instead of bullets
)
```

### Subsections

Add nested structure within sections:

```python
## First, create the parent section
self.prompt_add_section(
    "Policies",
    body="Follow company policies in these areas:"
)

## Then add subsections
self.prompt_add_subsection(
    "Policies",           # Parent section title
    "Returns",            # Subsection title
    body="For return requests:",
    bullets=[
        "Items can be returned within 30 days",
        "Receipt is required for cash refunds",
        "Exchanges are always available"
    ]
)

self.prompt_add_subsection(
    "Policies",
    "Billing",
    body="For billing inquiries:",
    bullets=[
        "Verify customer identity first",
        "Review last 3 statements",
        "Offer payment plans if needed"
    ]
)
```

### Declarative Prompts (PROMPT_SECTIONS)

Define prompts declaratively as a class attribute:

```python
class DeclarativeAgent(AgentBase):
    PROMPT_SECTIONS = {
        "Role": "You are a friendly assistant for a pizza restaurant.",

        "Menu Knowledge": [
            "Small pizza: $10",
            "Medium pizza: $14",
            "Large pizza: $18",
            "Toppings: $1.50 each"
        ],

        "Order Process": {
            "body": "When taking orders:",
            "bullets": [
                "Confirm the size first",
                "List available toppings",
                "Repeat the order back",
                "Provide total price"
            ]
        },

        "Policies": {
            "body": "Restaurant policies:",
            "subsections": [
                {
                    "title": "Delivery",
                    "body": "Delivery information:",
                    "bullets": [
                        "Free delivery over $25",
                        "$5 fee under $25",
                        "30-45 minute delivery time"
                    ]
                },
                {
                    "title": "Pickup",
                    "bullets": [
                        "Ready in 15-20 minutes",
                        "Call when you arrive"
                    ]
                }
            ]
        }
    }

    def __init__(self):
        super().__init__(name="pizza-agent")
        self.add_language("English", "en-US", "rime.spore")
```

### POM Builder Direct Access

For advanced use, access the POM builder directly:

```python
class AdvancedAgent(AgentBase):
    def __init__(self):
        super().__init__(name="advanced-agent")

        # Direct POM access
        self.pom.section("Role").body(
            "You are an expert technical support agent."
        )

        self.pom.section("Expertise").bullets([
            "Network troubleshooting",
            "Software installation",
            "Hardware diagnostics"
        ])

        # Chain multiple calls
        (self.pom
            .section("Process")
            .body("Follow these steps:")
            .numbered_bullets([
                "Identify the issue",
                "Run diagnostics",
                "Apply solution",
                "Verify resolution"
            ]))
```

### Post-Call Prompts

Configure what happens after the call ends:

```python
## Set post-prompt for call summary
self.set_post_prompt(
    "Summarize this call including: "
    "1) The customer's issue "
    "2) How it was resolved "
    "3) Any follow-up needed"
)

## Alternative: Full post-prompt configuration
self.set_post_prompt_data({
    "text": "Generate a detailed call summary.",
    "temperature": 0.3,
    "top_p": 0.9
})
```

### Voice-Optimized Prompts

Write prompts optimized for voice conversations:

```python
class VoiceOptimizedAgent(AgentBase):
    def __init__(self):
        super().__init__(name="voice-agent")
        self.add_language("English", "en-US", "rime.spore")

        self.prompt_add_section(
            "Voice Guidelines",
            body="Optimize all responses for voice:",
            bullets=[
                "Keep sentences short - under 20 words",
                "Avoid technical jargon unless necessary",
                "Use conversational language, not formal",
                "Pause naturally between topics",
                "Don't list more than 3 items at once",
                "Spell out acronyms on first use"
            ]
        )

        self.prompt_add_section(
            "Response Style",
            bullets=[
                "Start responses with the key information",
                "Confirm understanding before long explanations",
                "Ask 'Does that make sense?' after complex topics",
                "Use filler words naturally: 'Let me check that for you'"
            ]
        )
```

### Prompt Best Practices

#### 1. Lead with Role Definition

```python
## Good - clear role first
self.prompt_add_section(
    "Role",
    "You are Sarah, a senior customer service representative "
    "at TechCorp with 5 years of experience helping customers "
    "with software products."
)
```

#### 2. Separate Concerns

```python
## Good - each section has one purpose
self.prompt_add_section("Role", "...")
self.prompt_add_section("Knowledge", "...")
self.prompt_add_section("Guidelines", "...")
self.prompt_add_section("Restrictions", "...")

## Bad - everything mixed together
self.prompt_add_section("Instructions",
    "You are an agent. Be nice. Don't share secrets. "
    "You know about products. Follow the rules..."
)
```

#### 3. Use Bullets for Lists

```python
## Good - scannable bullets
self.prompt_add_section(
    "Products",
    body="You can help with these products:",
    bullets=["Basic Plan - $10/mo", "Pro Plan - $25/mo", "Enterprise - Custom"]
)

## Bad - inline list
self.prompt_add_section(
    "Products",
    "Products include Basic Plan at $10/mo, Pro Plan at $25/mo, "
    "and Enterprise with custom pricing."
)
```

#### 4. Be Specific About Restrictions

```python
## Good - explicit restrictions
self.prompt_add_section(
    "Restrictions",
    bullets=[
        "Never share customer passwords or security codes",
        "Do not process refunds over $500 without transfer",
        "Cannot modify account ownership",
        "Must verify identity before account changes"
    ]
)
```

### Generated Prompt Output

POM converts your structure to formatted text:

```
## Role

You are Sarah, a customer service representative for Acme Corp.

## Guidelines

Follow these guidelines:

* Be professional and courteous
* Ask clarifying questions when needed
* Keep responses concise for voice

## Policies

### Returns

For return requests:

* Items can be returned within 30 days
* Receipt required for cash refunds

### Billing

For billing inquiries:

* Verify customer identity first
* Review recent statements
```



---

## Voice & Language

> **Summary**: Configure Text-to-Speech voices, languages, and pronunciation to create natural-sounding agents.

### Voice Configuration Overview

#### Language Configuration

| Parameter | Description | Example |
|-----------|-------------|---------|
| `name` | Human-readable name | `"English"` |
| `code` | Language code for STT | `"en-US"` |
| `voice` | TTS voice identifier | `"rime.spore"` or `"elevenlabs.josh:eleven_turbo_v2_5"` |

#### Fillers (Natural Speech)

| Parameter | Description | Example |
|-----------|-------------|---------|
| `speech_fillers` | Used during natural conversation pauses | `["Um", "Well", "So"]` |
| `function_fillers` | Used while executing a function | `["Let me check...", "One moment..."]` |

### Adding a Language

#### Basic Configuration

```python
from signalwire_agents import AgentBase


class MyAgent(AgentBase):
    def __init__(self):
        super().__init__(name="my-agent")

        # Basic language setup
        self.add_language(
            name="English",       # Display name
            code="en-US",         # Language code for STT
            voice="rime.spore"    # TTS voice
        )
```

#### Voice Format

The voice parameter uses the format `engine.voice:model` where model is optional:

```python
## Simple voice (engine.voice)
self.add_language("English", "en-US", "rime.spore")

## With model (engine.voice:model)
self.add_language("English", "en-US", "elevenlabs.josh:eleven_turbo_v2_5")
```

### Available TTS Engines

| Provider | Engine Code | Example Voice | Reference |
|----------|-------------|---------------|-----------|
| Amazon Polly | `amazon` | `amazon.Joanna-Neural` | [Voice IDs](https://developer.signalwire.com/voice/tts/amazon-polly#voice-ids) |
| Cartesia | `cartesia` | `cartesia.a167e0f3-df7e-4d52-a9c3-f949145efdab` | [Voice IDs](https://developer.signalwire.com/voice/tts/cartesia#voice-ids) |
| Deepgram | `deepgram` | `deepgram.aura-asteria-en` | [Voice IDs](https://developer.signalwire.com/voice/tts/deepgram#voice-ids) |
| ElevenLabs | `elevenlabs` | `elevenlabs.thomas` | [Voice IDs](https://developer.signalwire.com/voice/tts/elevenlabs#voice-ids) |
| Google Cloud | `gcloud` | `gcloud.en-US-Casual-K` | [Voice IDs](https://developer.signalwire.com/voice/tts/gcloud#voice-ids) |
| Microsoft Azure | `azure` | `azure.en-US-AvaNeural` | [Voice IDs](https://developer.signalwire.com/voice/tts/azure#voice-ids) |
| OpenAI | `openai` | `openai.alloy` | [Voice IDs](https://developer.signalwire.com/voice/tts/openai#voice-ids) |
| Rime | `rime` | `rime.luna:arcana` | [Voice IDs](https://developer.signalwire.com/voice/tts/rime#voices) |

### Filler Phrases

Add natural pauses and filler words:

```python
self.add_language(
    name="English",
    code="en-US",
    voice="rime.spore",
    speech_fillers=[
        "Um",
        "Well",
        "Let me think",
        "So"
    ],
    function_fillers=[
        "Let me check that for you",
        "One moment please",
        "I'm looking that up now",
        "Bear with me"
    ]
)
```

**Speech fillers**: Used during natural conversation pauses

**Function fillers**: Used while the AI is executing a function

### Multi-Language Support

Use `code="multi"` for automatic language detection and matching:

```python
class MultilingualAgent(AgentBase):
    def __init__(self):
        super().__init__(name="multilingual-agent")

        # Multi-language support (auto-detects and matches caller's language)
        self.add_language(
            name="Multilingual",
            code="multi",
            voice="rime.spore"
        )

        self.prompt_add_section(
            "Language",
            "Automatically detect and match the caller's language without "
            "prompting or asking them to verify. Respond naturally in whatever "
            "language they speak."
        )
```

The `multi` code supports: English, Spanish, French, German, Hindi, Russian, Portuguese, Japanese, Italian, and Dutch.

**Note**: Speech recognition hints do not work when using `code="multi"`. If you need hints for specific terms, use individual language codes instead.

For more control over individual languages with custom fillers:

```python
class CustomMultilingualAgent(AgentBase):
    def __init__(self):
        super().__init__(name="custom-multilingual")

        # English (primary)
        self.add_language(
            name="English",
            code="en-US",
            voice="rime.spore",
            speech_fillers=["Um", "Well", "So"],
            function_fillers=["Let me check that"]
        )

        # Spanish
        self.add_language(
            name="Spanish",
            code="es-MX",
            voice="rime.luna",
            speech_fillers=["Eh", "Pues", "Bueno"],
            function_fillers=["Dejame verificar", "Un momento"]
        )

        # French
        self.add_language(
            name="French",
            code="fr-FR",
            voice="rime.claire",
            speech_fillers=["Euh", "Alors", "Bon"],
            function_fillers=["Laissez-moi verifier", "Un instant"]
        )

        self.prompt_add_section(
            "Language",
            "Automatically detect and match the caller's language without "
            "prompting or asking them to verify."
        )
```

### Pronunciation Rules

Fix pronunciation of specific words:

```python
class AgentWithPronunciation(AgentBase):
    def __init__(self):
        super().__init__(name="pronunciation-agent")
        self.add_language("English", "en-US", "rime.spore")

        # Fix brand names
        self.add_pronunciation(
            replace="ACME",
            with_text="Ack-me"
        )

        # Fix technical terms
        self.add_pronunciation(
            replace="SQL",
            with_text="sequel"
        )

        # Case-insensitive matching
        self.add_pronunciation(
            replace="api",
            with_text="A P I",
            ignore_case=True
        )

        # Fix names
        self.add_pronunciation(
            replace="Nguyen",
            with_text="win"
        )
```

### Set Multiple Pronunciations

```python
## Set all pronunciations at once
self.set_pronunciations([
    {"replace": "ACME", "with": "Ack-me"},
    {"replace": "SQL", "with": "sequel"},
    {"replace": "API", "with": "A P I", "ignore_case": True},
    {"replace": "CEO", "with": "C E O"},
    {"replace": "ASAP", "with": "A sap"}
])
```

### Voice Selection Guide

| Use Case | Recommended Voice Style |
|----------|------------------------|
| Customer Service | Warm, friendly (`rime.spore`) |
| Technical Support | Clear, professional (`rime.marsh`) |
| Sales | Energetic, persuasive (elevenlabs voices) |
| Healthcare | Calm, reassuring |
| Legal/Finance | Formal, authoritative |

**Considerations:**
- Match voice personality to brand
- Test with actual callers
- Consider regional accents
- Evaluate TTS quality for your content

### Dynamic Voice Selection

Change voice based on context:

```python
class DynamicVoiceAgent(AgentBase):
    DEPARTMENT_VOICES = {
        "support": {"voice": "rime.spore", "name": "Alex"},
        "sales": {"voice": "rime.marsh", "name": "Jordan"},
        "billing": {"voice": "rime.coral", "name": "Morgan"}
    }

    def __init__(self):
        super().__init__(name="dynamic-voice")

    def on_swml_request(self, request_data=None, callback_path=None, request=None):
        # Determine department from called number
        call_data = (request_data or {}).get("call", {})
        called_num = call_data.get("to", "")

        if "555-1000" in called_num:
            dept = "support"
        elif "555-2000" in called_num:
            dept = "sales"
        else:
            dept = "billing"

        config = self.DEPARTMENT_VOICES[dept]

        self.add_language("English", "en-US", config["voice"])

        self.prompt_add_section(
            "Role",
            f"You are {config['name']}, a {dept} representative."
        )
```

### Language Codes Reference

Supported language codes:

| Language | Codes |
|----------|-------|
| Multilingual | `multi` (English, Spanish, French, German, Hindi, Russian, Portuguese, Japanese, Italian, Dutch) |
| Bulgarian | `bg` |
| Czech | `cs` |
| Danish | `da`, `da-DK` |
| Dutch | `nl` |
| English | `en`, `en-US`, `en-AU`, `en-GB`, `en-IN`, `en-NZ` |
| Finnish | `fi` |
| French | `fr`, `fr-CA` |
| German | `de` |
| Hindi | `hi` |
| Hungarian | `hu` |
| Indonesian | `id` |
| Italian | `it` |
| Japanese | `ja` |
| Korean | `ko`, `ko-KR` |
| Norwegian | `no` |
| Polish | `pl` |
| Portuguese | `pt`, `pt-BR`, `pt-PT` |
| Russian | `ru` |
| Spanish | `es`, `es-419` |
| Swedish | `sv`, `sv-SE` |
| Turkish | `tr` |
| Ukrainian | `uk` |
| Vietnamese | `vi` |

### Complete Voice Configuration Example

```python
from signalwire_agents import AgentBase


class FullyConfiguredVoiceAgent(AgentBase):
    def __init__(self):
        super().__init__(name="voice-configured")

        # Primary language with all options
        self.add_language(
            name="English",
            code="en-US",
            voice="rime.spore",
            speech_fillers=[
                "Um",
                "Well",
                "Let me see",
                "So"
            ],
            function_fillers=[
                "Let me look that up for you",
                "One moment while I check",
                "I'm searching for that now",
                "Just a second"
            ]
        )

        # Secondary language
        self.add_language(
            name="Spanish",
            code="es-MX",
            voice="rime.luna",
            speech_fillers=["Pues", "Bueno"],
            function_fillers=["Un momento", "Dejame ver"]
        )

        # Pronunciation fixes
        self.set_pronunciations([
            {"replace": "ACME", "with": "Ack-me"},
            {"replace": "www", "with": "dub dub dub"},
            {"replace": ".com", "with": "dot com"},
            {"replace": "@", "with": "at"}
        ])

        self.prompt_add_section(
            "Role",
            "You are a friendly customer service agent."
        )
```



---

## AI Parameters

> **Summary**: Tune conversation behavior with parameters for speech detection, timeouts, barge control, and AI model settings. For a complete parameter reference, see [AI Parameters Reference](../12_appendix/12_01_ai-parameters.md).

### Parameter Categories

| Category | Key Parameters | Purpose |
|----------|----------------|---------|
| **Speech Detection** | `end_of_speech_timeout` | Control when speech ends |
| **Timeouts** | `attention_timeout`, `inactivity_timeout` | Handle silence and idle callers |
| **Barge Control** | `barge_match_string` | Manage interruptions |
| **AI Model** | `temperature`, `top_p`, `max_tokens` | Tune response generation |

### Setting Parameters

```python
from signalwire_agents import AgentBase


class MyAgent(AgentBase):
    def __init__(self):
        super().__init__(name="my-agent")
        self.add_language("English", "en-US", "rime.spore")

        # Set multiple parameters at once
        self.set_params({
            "end_of_speech_timeout": 600,
            "attention_timeout": 15000,
            "inactivity_timeout": 45000,
            "temperature": 0.5
        })
```

### Essential Parameters

#### Speech Detection

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `end_of_speech_timeout` | int | 700 | Milliseconds of silence before speech is complete |
| `energy_level` | int | 52 | Minimum audio level in dB (0-100) |

```python
## Fast response - shorter silence detection
self.set_params({"end_of_speech_timeout": 400})

## Patient agent - longer silence tolerance
self.set_params({"end_of_speech_timeout": 1000})
```

#### Timeouts

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `attention_timeout` | int | 5000 | Milliseconds before prompting idle caller |
| `inactivity_timeout` | int | 600000 | Milliseconds before ending call (10 min default) |

```python
## Quick service - prompt quickly if silent
self.set_params({
    "attention_timeout": 5000,    # "Are you there?" after 5 seconds
    "inactivity_timeout": 30000   # End call after 30 seconds
})

## Patient service - give caller time to think
self.set_params({
    "attention_timeout": 20000,   # Wait 20 seconds before prompting
    "inactivity_timeout": 60000   # Wait full minute before ending
})
```

#### Barge Control

Barge-in allows callers to interrupt the AI while it's speaking.

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `barge_match_string` | str | - | Phrase required to trigger barge |
| `transparent_barge` | bool | true | Enable transparent barge mode |

```python
## Require specific phrase to interrupt
self.set_params({
    "barge_match_string": "excuse me"
})
```

#### AI Model

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `temperature` | float | 0.3 | Randomness (0-2, higher = more creative) |
| `top_p` | float | 1.0 | Nucleus sampling threshold |
| `max_tokens` | int | 256 | Maximum response length |
| `frequency_penalty` | float | 0.1 | Reduce repetitive phrases |

```python
## Consistent responses (FAQ bot)
self.set_params({"temperature": 0.2})

## Creative responses (entertainment)
self.set_params({"temperature": 0.9})

## Balanced for customer service
self.set_params({
    "temperature": 0.5,
    "frequency_penalty": 0.3
})
```

### Use Case Presets

#### Customer Service

```python
self.set_params({
    "end_of_speech_timeout": 600,
    "attention_timeout": 12000,
    "inactivity_timeout": 45000,
    "temperature": 0.5
})
```

#### Technical Support

```python
self.set_params({
    "end_of_speech_timeout": 800,    # Patient for complex explanations
    "attention_timeout": 20000,
    "inactivity_timeout": 60000,
    "temperature": 0.3               # Precise responses
})
```

#### IVR Menu

```python
self.set_params({
    "end_of_speech_timeout": 400,    # Quick response
    "attention_timeout": 8000,
    "inactivity_timeout": 20000,
    "temperature": 0.2               # Very consistent
})
```

### Tuning Guide

#### If callers are...

| Problem | Solution |
|---------|----------|
| Being cut off mid-sentence | Increase `end_of_speech_timeout` |
| Waiting too long for response | Decrease `end_of_speech_timeout` |
| Not hearing "Are you there?" | Decrease `attention_timeout` |
| Getting hung up on too fast | Increase `inactivity_timeout` |

#### If responses are...

| Problem | Solution |
|---------|----------|
| Too repetitive | Increase `frequency_penalty` |
| Too random/inconsistent | Decrease `temperature` |
| Too predictable | Increase `temperature` |
| Too long | Decrease `max_tokens` |

### Complete Example

```python
#!/usr/bin/env python3
## configured_agent.py - Agent with AI parameters configured
from signalwire_agents import AgentBase


class ConfiguredAgent(AgentBase):
    def __init__(self):
        super().__init__(name="configured-agent")
        self.add_language("English", "en-US", "rime.spore")

        self.set_params({
            # Speech detection
            "end_of_speech_timeout": 600,

            # Timeouts
            "attention_timeout": 15000,
            "inactivity_timeout": 45000,
        })

        self.prompt_add_section(
            "Role",
            "You are a helpful customer service agent."
        )


if __name__ == "__main__":
    agent = ConfiguredAgent()
    agent.run()
```

### More Parameters

For the complete list of all available parameters including:

- ASR configuration (diarization, smart formatting)
- Audio settings (volume, background music, hold music)
- Video parameters
- Advanced behavior controls
- SWAIG control parameters

See the **[AI Parameters Reference](../12_appendix/12_01_ai-parameters.md)** in the Appendix.


---

## Hints

> **Summary**: Speech hints improve recognition accuracy for domain-specific vocabulary, brand names, technical terms, and other words the STT engine might misinterpret.

### Why Use Hints?

```diagram
┌─────────────────────────────────────────────────────────────────────────────┐
│                           Speech Hints                                      │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  Without Hints                         With Hints                           │
│  ┌─────────────────────────────┐       ┌─────────────────────────────┐      │
│  │                             │       │                             │      │
│  │  Caller: "My Acme account"  │       │  Caller: "My Acme account"  │      │
│  │            │                │       │            │                │      │
│  │            ▼                │       │            ▼                │      │
│  │  STT:    "My acne account"  │       │  STT:    "My Acme account"  │      │
│  │            │                │       │            │                │      │
│  │        (misheard)           │       │        (correct!)           │      │
│  │                             │       │                             │      │
│  └─────────────────────────────┘       └─────────────────────────────┘      │
│                                                                             │
│  Hints tell the STT engine to listen for specific words and phrases         │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Adding Simple Hints

#### Single Hint

```python
from signalwire_agents import AgentBase


class MyAgent(AgentBase):
    def __init__(self):
        super().__init__(name="my-agent")
        self.add_language("English", "en-US", "rime.spore")

        # Add single hint
        self.add_hint("Acme")
        self.add_hint("SignalWire")
```

#### Multiple Hints

```python
## Add list of hints
self.add_hints([
    "Acme",
    "SignalWire",
    "API",
    "webhook",
    "SWML"
])
```

### What to Hint

| Category | Examples |
|----------|----------|
| **Brand Names** | Acme Corp, SignalWire, company name, product names |
| **Technical Terms** | API, webhook, OAuth, SDK, JSON |
| **Industry Jargon** | KYC, AML, SLA, EOD, PTO |
| **Names** | Employee names, customer names, location names |
| **Numbers/Codes** | Account numbers, ZIP codes, reference IDs |
| **Actions** | Transfer, escalate, reschedule |

### Hint Examples by Use Case

#### Customer Service

```python
self.add_hints([
    # Brand and products
    "Acme", "Acme Pro", "Acme Enterprise",

    # Common actions
    "account", "billing", "refund", "exchange", "return",
    "cancel", "upgrade", "downgrade",

    # Support terms
    "representative", "supervisor", "escalate", "ticket",
    "case number", "reference number"
])
```

#### Technical Support

```python
self.add_hints([
    # Product names
    "Windows", "macOS", "Linux", "Chrome", "Firefox",

    # Technical terms
    "reboot", "restart", "reinstall", "cache", "cookies",
    "browser", "firewall", "antivirus", "driver",

    # Error terms
    "error code", "blue screen", "crash", "freeze",
    "not responding", "won't start"
])
```

#### Healthcare

```python
self.add_hints([
    # Appointment terms
    "appointment", "reschedule", "cancel", "follow-up",

    # Medical terms
    "prescription", "refill", "pharmacy", "dosage",
    "medication", "symptoms", "diagnosis",

    # Department names
    "cardiology", "dermatology", "pediatrics", "radiology",

    # Common medications (if applicable)
    "Tylenol", "Advil", "Lipitor", "Metformin"
])
```

#### Financial Services

```python
self.add_hints([
    # Account terms
    "checking", "savings", "IRA", "401k", "Roth",

    # Transaction terms
    "transfer", "deposit", "withdrawal", "wire",
    "ACH", "routing number", "account number",

    # Services
    "mortgage", "auto loan", "credit card", "overdraft",

    # Verification
    "social security", "date of birth", "mother's maiden name"
])
```

### Pattern Hints (Advanced)

For words with specific patterns, use pattern hints:

```python
## Pattern hint with replacement
self.add_pattern_hint(
    hint="account number",           # What to listen for
    pattern=r"\d{8,12}",             # Regex pattern to match
    replace="${1}",                   # How to format it
    ignore_case=True
)

## Normalize variations
self.add_pattern_hint(
    hint="Acme",
    pattern=r"(acme|ackme|ac me)",   # Common mishearings
    replace="Acme",                   # Normalize to correct form
    ignore_case=True
)
```

### Organizing Hints

For large hint lists, organize by category:

```python
class OrganizedHintsAgent(AgentBase):
    # Hint categories
    BRAND_HINTS = ["Acme", "Acme Pro", "Acme Enterprise"]
    ACTION_HINTS = ["account", "billing", "refund", "cancel"]
    SUPPORT_HINTS = ["representative", "supervisor", "escalate"]

    def __init__(self):
        super().__init__(name="organized-hints")
        self.add_language("English", "en-US", "rime.spore")

        # Add all hint categories
        self.add_hints(self.BRAND_HINTS)
        self.add_hints(self.ACTION_HINTS)
        self.add_hints(self.SUPPORT_HINTS)
```

### Dynamic Hints

Add hints based on context:

```python
class DynamicHintsAgent(AgentBase):
    DEPARTMENT_HINTS = {
        "sales": ["pricing", "quote", "demo", "trial", "discount"],
        "support": ["ticket", "bug", "error", "fix", "issue"],
        "billing": ["invoice", "payment", "refund", "charge"]
    }

    def __init__(self):
        super().__init__(name="dynamic-hints")
        self.add_language("English", "en-US", "rime.spore")

        # Common hints for all departments
        self.add_hints(["Acme", "account", "help"])

    def on_swml_request(self, request_data=None, callback_path=None, request=None):
        call_data = (request_data or {}).get("call", {})
        called_num = call_data.get("to", "")

        # Add department-specific hints
        if "555-1000" in called_num:
            self.add_hints(self.DEPARTMENT_HINTS["sales"])
        elif "555-2000" in called_num:
            self.add_hints(self.DEPARTMENT_HINTS["support"])
        else:
            self.add_hints(self.DEPARTMENT_HINTS["billing"])
```

### Hint Best Practices

**DO:**
- Hint brand names and product names
- Hint technical terms specific to your domain
- Hint common employee/customer names
- Hint acronyms and abbreviations
- Test with actual callers to find missed words

**DON'T:**
- Hint common English words (already recognized well)
- Add hundreds of hints (quality over quantity)
- Hint full sentences (single words/short phrases work best)
- Forget to update hints when products/terms change

### Testing Hints

Use swaig-test to verify hints are included:

```bash
## View SWML including hints
swaig-test my_agent.py --dump-swml | grep -A 20 "hints"
```

Check the generated SWML for the hints array:

```json
{
  "version": "1.0.0",
  "sections": {
    "main": [{
      "ai": {
        "hints": [
          "Acme",
          "SignalWire",
          "account",
          "billing"
        ]
      }
    }]
  }
}
```

### Complete Example

```python
#!/usr/bin/env python3
## hinted_agent.py - Agent with speech recognition hints
from signalwire_agents import AgentBase, SwaigFunctionResult


class HintedAgent(AgentBase):
    def __init__(self):
        super().__init__(name="hinted-agent")
        self.add_language("English", "en-US", "rime.spore")

        # Brand hints
        self.add_hints([
            "Acme", "Acme Pro", "Acme Enterprise",
            "AcmePay", "AcmeCloud"
        ])

        # Product SKUs
        self.add_hints([
            "SKU", "A100", "A200", "A300",
            "PRO100", "ENT500"
        ])

        # Common actions
        self.add_hints([
            "account", "billing", "invoice", "refund",
            "cancel", "upgrade", "downgrade",
            "representative", "supervisor"
        ])

        # Technical terms
        self.add_hints([
            "API", "webhook", "integration",
            "OAuth", "SSO", "MFA"
        ])

        self.prompt_add_section(
            "Role",
            "You are a customer service agent for Acme Corporation."
        )

        self.define_tool(
            name="lookup_product",
            description="Look up product by SKU",
            parameters={
                "type": "object",
                "properties": {
                    "sku": {
                        "type": "string",
                        "description": "Product SKU like A100 or PRO100"
                    }
                },
                "required": ["sku"]
            },
            handler=self.lookup_product
        )

    def lookup_product(self, args, raw_data):
        sku = args.get("sku", "").upper()
        products = {
            "A100": "Acme Basic - $99/month",
            "A200": "Acme Standard - $199/month",
            "A300": "Acme Premium - $299/month",
            "PRO100": "Acme Pro - $499/month",
            "ENT500": "Acme Enterprise - Custom pricing"
        }
        if sku in products:
            return SwaigFunctionResult(f"{sku}: {products[sku]}")
        return SwaigFunctionResult(f"SKU {sku} not found.")


if __name__ == "__main__":
    agent = HintedAgent()
    agent.run()
```

### Next Steps

You now know how to build and configure agents. Next, learn about SWAIG functions to add custom capabilities.



---

## Call Flow Customization

> **Summary**: Control call flow with verb insertion points for pre-answer, post-answer, and post-AI actions.

### Understanding Call Flow

By default, `AgentBase` generates a simple call flow:

```
answer → ai
```

The SDK provides three insertion points to customize this flow:

```
┌─────────────────────────────────────────────────────────────────┐
│  PRE-ANSWER VERBS (call still ringing)                          │
│  • Ringback tones, call screening, conditional routing          │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│  ANSWER VERB (call connected)                                   │
│  • Automatic when auto_answer=True (default)                    │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│  POST-ANSWER VERBS (before AI)                                  │
│  • Welcome messages, disclaimers, hold music                    │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│  AI VERB (conversation)                                         │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│  POST-AI VERBS (after conversation)                             │
│  • Cleanup, transfers, surveys, logging                         │
└─────────────────────────────────────────────────────────────────┘
```

### Verb Insertion Methods

| Method | Purpose | Common Uses |
|--------|---------|-------------|
| `add_pre_answer_verb()` | Before answering | Ringback, screening, routing |
| `add_post_answer_verb()` | After answer, before AI | Announcements, disclaimers |
| `add_post_ai_verb()` | After AI ends | Cleanup, transfers, surveys |

### Pre-Answer Verbs

Pre-answer verbs run while the call is still ringing. Use them for:

- **Ringback tones**: Play audio before answering
- **Call screening**: Check caller ID or time
- **Conditional routing**: Route based on variables

```python
#!/usr/bin/env python3
from signalwire_agents import AgentBase


class RingbackAgent(AgentBase):
    """Agent that plays ringback tone before answering."""

    def __init__(self):
        super().__init__(name="ringback", port=3000)

        # Play US ringback tone before answering
        # IMPORTANT: auto_answer=False prevents play from answering the call
        self.add_pre_answer_verb("play", {
            "urls": ["ring:us"],
            "auto_answer": False
        })

        # Configure AI
        self.add_language("English", "en-US", "rime.spore")
        self.prompt_add_section("Role", "You are a helpful assistant.")


if __name__ == "__main__":
    agent = RingbackAgent()
    agent.run()
```

**Generated SWML:**
```json
{
  "sections": {
    "main": [
      {"play": {"urls": ["ring:us"], "auto_answer": false}},
      {"answer": {}},
      {"ai": {...}}
    ]
  }
}
```

#### Pre-Answer Safe Verbs

Only certain verbs can run before the call is answered:

| Verb | Pre-Answer Safe | Notes |
|------|-----------------|-------|
| `play` | Yes* | Requires `auto_answer: false` |
| `connect` | Yes* | Requires `auto_answer: false` |
| `sleep` | Yes | Wait for duration |
| `set` | Yes | Set variables |
| `request` | Yes | HTTP request |
| `switch` | Yes | Variable-based branching |
| `cond` | Yes | Conditional branching |
| `if` | Yes | If/then/else |
| `eval` | Yes | Evaluate expressions |
| `goto` | Yes | Jump to label |
| `label` | Yes | Define jump target |
| `hangup` | Yes | Reject call |
| `transfer` | Yes | Route elsewhere |

*These verbs auto-answer by default. Set `auto_answer: false` for pre-answer use.

#### Available Ringback Tones

| Tone | Description |
|------|-------------|
| `ring:us` | US ringback tone |
| `ring:uk` | UK ringback tone |
| `ring:it` | Italian ringback tone |
| `ring:at` | Austrian ringback tone |

### Post-Answer Verbs

Post-answer verbs run after the call is connected but before the AI speaks:

```python
#!/usr/bin/env python3
from signalwire_agents import AgentBase


class WelcomeAgent(AgentBase):
    """Agent that plays welcome message before AI."""

    def __init__(self):
        super().__init__(name="welcome", port=3000)

        # Play welcome announcement
        self.add_post_answer_verb("play", {
            "url": "say:Thank you for calling Acme Corporation. "
                   "Your call may be recorded for quality assurance."
        })

        # Brief pause before AI speaks
        self.add_post_answer_verb("sleep", {"time": 500})

        # Configure AI
        self.add_language("English", "en-US", "rime.spore")
        self.prompt_add_section(
            "Role",
            "You are a customer service representative. "
            "The caller has just heard the welcome message."
        )


if __name__ == "__main__":
    agent = WelcomeAgent()
    agent.run()
```

**Generated SWML:**
```json
{
  "sections": {
    "main": [
      {"answer": {}},
      {"play": {"url": "say:Thank you for calling..."}},
      {"sleep": {"time": 500}},
      {"ai": {...}}
    ]
  }
}
```

#### Common Post-Answer Uses

| Use Case | Example |
|----------|---------|
| Welcome message | `{"url": "say:Thank you for calling..."}` |
| Legal disclaimer | `{"url": "say:This call may be recorded..."}` |
| Hold music | `{"url": "https://example.com/hold.mp3"}` |
| Pause | `{"time": 500}` (milliseconds) |
| Recording | Use `record_call=True` in constructor |

### Post-AI Verbs

Post-AI verbs run after the AI conversation ends:

```python
#!/usr/bin/env python3
from signalwire_agents import AgentBase


class SurveyAgent(AgentBase):
    """Agent that logs call outcome after conversation."""

    def __init__(self):
        super().__init__(name="survey", port=3000)

        # Configure AI
        self.add_language("English", "en-US", "rime.spore")
        self.prompt_add_section("Role", "You are a support agent.")

        # After AI ends, log the call and hang up
        self.add_post_ai_verb("request", {
            "url": "https://api.example.com/call-complete",
            "method": "POST"
        })
        self.add_post_ai_verb("hangup", {})


if __name__ == "__main__":
    agent = SurveyAgent()
    agent.run()
```

#### Common Post-AI Uses

| Use Case | Verb | Example |
|----------|------|---------|
| Clean disconnect | `hangup` | `{}` |
| Transfer to human | `transfer` | `{"dest": "tel:+15551234567"}` |
| Post-call survey | `prompt` | DTMF collection |
| Log outcome | `request` | HTTP POST to API |
| Connect to queue | `enter_queue` | `{"name": "support"}` |

### Complete Example

Here's an agent with all three insertion points:

```python
#!/usr/bin/env python3
from signalwire_agents import AgentBase


class CallFlowAgent(AgentBase):
    """Agent demonstrating complete call flow customization."""

    def __init__(self):
        super().__init__(name="call-flow", port=3000)

        # PRE-ANSWER: Ringback tone
        self.add_pre_answer_verb("play", {
            "urls": ["ring:us"],
            "auto_answer": False
        })

        # POST-ANSWER: Welcome and disclaimer
        self.add_post_answer_verb("play", {
            "url": "say:Welcome to Acme Corporation."
        })
        self.add_post_answer_verb("play", {
            "url": "say:This call may be recorded for quality assurance."
        })
        self.add_post_answer_verb("sleep", {"time": 500})

        # Configure AI
        self.add_language("English", "en-US", "rime.spore")
        self.prompt_add_section(
            "Role",
            "You are a friendly customer service representative. "
            "The caller has just heard the welcome message."
        )
        self.set_params({
            "end_of_speech_timeout": 1000,
            "attention_timeout": 10000
        })

        # POST-AI: Clean disconnect
        self.add_post_ai_verb("hangup", {})


if __name__ == "__main__":
    agent = CallFlowAgent()
    agent.run()
```

**Generated SWML:**
```json
{
  "sections": {
    "main": [
      {"play": {"urls": ["ring:us"], "auto_answer": false}},
      {"answer": {}},
      {"play": {"url": "say:Welcome to Acme Corporation."}},
      {"play": {"url": "say:This call may be recorded..."}},
      {"sleep": {"time": 500}},
      {"ai": {...}},
      {"hangup": {}}
    ]
  }
}
```

### Controlling Answer Behavior

#### Disable Auto-Answer

Set `auto_answer=False` to prevent automatic answering:

```python
class ManualAnswerAgent(AgentBase):
    def __init__(self):
        # Disable auto-answer
        super().__init__(name="manual", port=3000, auto_answer=False)

        # Pre-answer: Play ringback
        self.add_pre_answer_verb("play", {
            "urls": ["ring:us"],
            "auto_answer": False
        })

        # Note: Without auto_answer, the AI will start without
        # explicitly answering. Use add_answer_verb() if you need
        # to answer at a specific point.
```

#### Customize Answer Verb

Use `add_answer_verb()` to configure the answer verb:

```python
# Set max call duration to 1 hour
agent.add_answer_verb({"max_duration": 3600})
```

### Dynamic Call Flow

Modify call flow based on caller information using `on_swml_request()`:

```python
class DynamicFlowAgent(AgentBase):
    def __init__(self):
        super().__init__(name="dynamic", port=3000)
        self.add_language("English", "en-US", "rime.spore")
        self.prompt_add_section("Role", "You are a receptionist.")

        # VIP numbers get special treatment
        self.vip_numbers = ["+15551234567", "+15559876543"]

    def on_swml_request(self, request_data=None, callback_path=None, request=None):
        call_data = (request_data or {}).get("call", {})
        caller = call_data.get("from", "")

        if caller in self.vip_numbers:
            # VIP: No ringback, immediate welcome
            self.clear_pre_answer_verbs()
            self.add_post_answer_verb("play", {
                "url": "say:Welcome back, valued customer!"
            })
        else:
            # Regular caller: Ringback tone
            self.add_pre_answer_verb("play", {
                "urls": ["ring:us"],
                "auto_answer": False
            })
```

### Clear Methods

Remove verbs from insertion points:

```python
agent.clear_pre_answer_verbs()   # Remove all pre-answer verbs
agent.clear_post_answer_verbs()  # Remove all post-answer verbs
agent.clear_post_ai_verbs()      # Remove all post-AI verbs
```

### Method Chaining

All verb insertion methods return `self` for chaining:

```python
agent = AgentBase(name="chained", port=3000)
agent.add_pre_answer_verb("play", {"urls": ["ring:us"], "auto_answer": False}) \
     .add_post_answer_verb("play", {"url": "say:Welcome"}) \
     .add_post_answer_verb("sleep", {"time": 500}) \
     .add_post_ai_verb("hangup", {})
```

### Related Documentation

- [AgentBase API](../10_reference/10_01_api-agent-base.md) - Full parameter reference
- [SWML Schema](../10_reference/10_12_swml-schema.md) - All available verbs
- [AI Parameters](03_05_ai-parameters.md) - Tuning AI behavior

# Part: SWAIG Functions

---

# SWAIG Functions

> **Summary**: SWAIG (SignalWire AI Gateway) functions let your AI agent call custom code to look up data, make API calls, and take actions during conversations.

## What You'll Learn

This chapter covers everything about SWAIG functions:

1. **Defining Functions** - Creating functions the AI can call
2. **Parameters** - Accepting arguments from the AI
3. **Results & Actions** - Returning data and triggering actions
4. **DataMap** - Serverless API integration without webhooks
5. **Native Functions** - Built-in SignalWire functions

## How SWAIG Functions Work

```diagram
┌─────────────────────────────────────────────────────────────────────────────┐
│                        SWAIG Function Flow                                  │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  1. Caller speaks                                                           │
│     "What's my order status for order 12345?"                               │
│              │                                                              │
│              ▼                                                              │
│  2. AI decides to call function                                             │
│     ┌─────────────────────────────────────────────┐                         │
│     │ AI: "I'll look that up using check_order"   │                         │
│     │ Function: check_order                       │                         │
│     │ Args: {"order_number": "12345"}             │                         │
│     └─────────────────────────────────────────────┘                         │
│              │                                                              │
│              ▼                                                              │
│  3. SignalWire calls your webhook                                           │
│     POST https://your-server.com/swaig                                      │
│     {"function": "check_order", "args": {...}}                              │
│              │                                                              │
│              ▼                                                              │
│  4. Your handler returns result                                             │
│     ┌─────────────────────────────────────────────┐                         │
│     │ SwaigFunctionResult(                        │                         │
│     │   "Order 12345 shipped Monday,              │                         │
│     │    arriving Thursday"                       │                         │
│     │ )                                           │                         │
│     └─────────────────────────────────────────────┘                         │
│              │                                                              │
│              ▼                                                              │
│  5. AI speaks result to caller                                              │
│     "Your order 12345 shipped Monday and                                    │
│      will arrive Thursday."                                                 │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

## Quick Start Example

Here's a complete agent with a SWAIG function:

```python
from signalwire_agents import AgentBase, SwaigFunctionResult

class OrderAgent(AgentBase):
    def __init__(self):
        super().__init__(name="order-agent")
        self.add_language("English", "en-US", "rime.spore")

        self.prompt_add_section(
            "Role",
            "You are an order status assistant. Help customers check their orders."
        )

        # Define a function the AI can call
        self.define_tool(
            name="check_order",
            description="Look up order status by order number",
            parameters={
                "type": "object",
                "properties": {
                    "order_number": {
                        "type": "string",
                        "description": "The order number to look up"
                    }
                },
                "required": ["order_number"]
            },
            handler=self.check_order
        )

    def check_order(self, args, raw_data):
        order_number = args.get("order_number")

        # Your business logic here - database lookup, API call, etc.
        orders = {
            "12345": "Shipped Monday, arriving Thursday",
            "67890": "Processing, ships tomorrow"
        }

        status = orders.get(order_number, "Order not found")
        return SwaigFunctionResult(f"Order {order_number}: {status}")

if __name__ == "__main__":
    agent = OrderAgent()
    agent.run()
```

## Function Types

| Type | Description |
|------|-------------|
| **Handler Functions** | Defined with `define_tool()`. Python handler runs on your server with full control over logic, database access, and API calls. |
| **DataMap Functions** | Serverless API integration that runs on SignalWire's servers. No webhook endpoint needed - direct REST API calls. |
| **Native Functions** | Built into SignalWire. No custom code required - handles transfer, recording, etc. |

## Chapter Contents

| Section | Description |
|---------|-------------|
| [Defining Functions](04_01_defining-functions.md) | Creating SWAIG functions with define_tool() |
| [Parameters](04_02_parameters.md) | Defining and validating function parameters |
| [Results & Actions](04_03_results-actions.md) | Returning results and triggering actions |
| [DataMap](04_04_datamap.md) | Serverless API integration |
| [Native Functions](04_05_native-functions.md) | Built-in SignalWire functions |

## When to Use SWAIG Functions

| Use Case | Approach |
|----------|----------|
| Database lookups | Handler function |
| Complex business logic | Handler function |
| Simple REST API calls | DataMap |
| Pattern-based responses | DataMap expressions |
| Call transfers | Native function or SwaigFunctionResult.connect() |
| SMS sending | SwaigFunctionResult.send_sms() |

## Key Concepts

**Handler Functions**: Python code that runs on your server when the AI decides to call a function. You have full access to databases, APIs, and any Python library.

**SwaigFunctionResult**: The return type for all SWAIG functions. Contains the response text the AI will speak and optional actions to execute.

**Parameters**: JSON Schema definitions that tell the AI what arguments your function accepts. The AI will extract these from the conversation.

**Actions**: Side effects like call transfers, SMS sending, or context changes that execute after the function completes.

**DataMap**: A way to define functions that call REST APIs without running any code on your server - the API calls happen directly on SignalWire's infrastructure.

Let's start by learning how to define functions.

## Basic Function Definition

```python
from signalwire_agents import AgentBase, SwaigFunctionResult


class MyAgent(AgentBase):
    def __init__(self):
        super().__init__(name="my-agent")
        self.add_language("English", "en-US", "rime.spore")

        # Define a function
        self.define_tool(
            name="get_weather",
            description="Get current weather for a city",
            parameters={
                "type": "object",
                "properties": {
                    "city": {
                        "type": "string",
                        "description": "City name"
                    }
                },
                "required": ["city"]
            },
            handler=self.get_weather
        )

    def get_weather(self, args, raw_data):
        city = args.get("city")
        # Your logic here
        return SwaigFunctionResult(f"The weather in {city} is sunny, 72 degrees")
```

## The define_tool() Method

**Required Parameters:**

| Parameter | Description |
|-----------|-------------|
| `name` | Unique function name (lowercase, underscores) |
| `description` | What the function does (helps AI decide when to use) |
| `parameters` | JSON Schema defining accepted arguments |
| `handler` | Python function to call |

**Optional Parameters:**

| Parameter | Description |
|-----------|-------------|
| `secure` | Require token validation (default: True) |
| `fillers` | Language-specific filler phrases |
| `webhook_url` | External webhook URL (overrides local handler) |
| `required` | List of required parameter names |

## Handler Function Signature

All handlers receive two arguments:

```python
def my_handler(self, args, raw_data):
    """
    Args:
        args: Dictionary of parsed function arguments
              {"city": "New York", "units": "fahrenheit"}

        raw_data: Full request data including:
              - call_id: Unique call identifier
              - caller_id_num: Caller's phone number
              - caller_id_name: Caller's name
              - called_id_num: Number that was called
              - And more...

    Returns:
        SwaigFunctionResult with response text and optional actions
    """
    return SwaigFunctionResult("Response text")
```

## Accessing Call Data

```python
def check_account(self, args, raw_data):
    # Get caller information
    caller_number = raw_data.get("caller_id_num", "")
    call_id = raw_data.get("call_id", "")

    # Get function arguments
    account_id = args.get("account_id")

    # Use both for your logic
    return SwaigFunctionResult(
        f"Account {account_id} for caller {caller_number} is active"
    )
```

## Multiple Functions

Register as many functions as your agent needs:

```python
class CustomerServiceAgent(AgentBase):
    def __init__(self):
        super().__init__(name="customer-service")
        self.add_language("English", "en-US", "rime.spore")

        # Order lookup
        self.define_tool(
            name="check_order",
            description="Look up order status by order number",
            parameters={
                "type": "object",
                "properties": {
                    "order_number": {
                        "type": "string",
                        "description": "The order number"
                    }
                },
                "required": ["order_number"]
            },
            handler=self.check_order
        )

        # Account balance
        self.define_tool(
            name="get_balance",
            description="Get account balance for a customer",
            parameters={
                "type": "object",
                "properties": {
                    "account_id": {
                        "type": "string",
                        "description": "Customer account ID"
                    }
                },
                "required": ["account_id"]
            },
            handler=self.get_balance
        )

        # Store hours
        self.define_tool(
            name="get_store_hours",
            description="Get store hours for a location",
            parameters={
                "type": "object",
                "properties": {
                    "location": {
                        "type": "string",
                        "description": "Store location or city"
                    }
                },
                "required": ["location"]
            },
            handler=self.get_store_hours
        )

    def check_order(self, args, raw_data):
        order_number = args.get("order_number")
        return SwaigFunctionResult(f"Order {order_number} is in transit")

    def get_balance(self, args, raw_data):
        account_id = args.get("account_id")
        return SwaigFunctionResult(f"Account {account_id} balance: $150.00")

    def get_store_hours(self, args, raw_data):
        location = args.get("location")
        return SwaigFunctionResult(f"{location} store: Mon-Fri 9AM-9PM, Sat-Sun 10AM-6PM")
```

## Function Fillers

Add per-function filler phrases for when the function is executing:

```python
self.define_tool(
    name="search_inventory",
    description="Search product inventory",
    parameters={
        "type": "object",
        "properties": {
            "product": {"type": "string", "description": "Product to search"}
        },
        "required": ["product"]
    },
    handler=self.search_inventory,
    fillers={
        "en-US": [
            "Let me check our inventory...",
            "Searching our stock now...",
            "One moment while I look that up..."
        ],
        "es-MX": [
            "Dejame revisar nuestro inventario...",
            "Buscando en nuestro stock..."
        ]
    }
)
```

## The @tool Decorator

Alternative syntax using decorators:

```python
from signalwire_agents import AgentBase, SwaigFunctionResult


class MyAgent(AgentBase):
    def __init__(self):
        super().__init__(name="my-agent")
        self.add_language("English", "en-US", "rime.spore")

    @AgentBase.tool(
        name="get_time",
        description="Get the current time",
        parameters={
            "type": "object",
            "properties": {
                "timezone": {
                    "type": "string",
                    "description": "Timezone (e.g., 'EST', 'PST')"
                }
            }
        }
    )
    def get_time(self, args, raw_data):
        timezone = args.get("timezone", "UTC")
        return SwaigFunctionResult(f"The current time in {timezone} is 3:45 PM")
```

## External Webhook Functions

Route function calls to an external webhook:

```python
self.define_tool(
    name="external_lookup",
    description="Look up data from external service",
    parameters={
        "type": "object",
        "properties": {
            "query": {"type": "string", "description": "Search query"}
        },
        "required": ["query"]
    },
    handler=None,  # No local handler
    webhook_url="https://external-service.com/api/lookup"
)
```

## Function Security

By default, functions require token validation. Disable for testing:

```python
# Secure function (default)
self.define_tool(
    name="secure_function",
    description="Requires token validation",
    parameters={"type": "object", "properties": {}},
    handler=self.secure_handler,
    secure=True  # Default
)

# Insecure function (testing only)
self.define_tool(
    name="test_function",
    description="No token validation (testing only)",
    parameters={"type": "object", "properties": {}},
    handler=self.test_handler,
    secure=False  # Disable for testing
)
```

## Writing Good Descriptions

The description helps the AI decide when to use your function:

```python
# Good - specific and clear
description="Look up order status by order number. Returns shipping status and estimated delivery date."

# Bad - too vague
description="Get order info"

# Good - mentions what triggers it
description="Check if a product is in stock. Use when customer asks about availability."

# Good - explains constraints
description="Transfer call to human support. Only use if customer explicitly requests to speak with a person."
```

## Testing Functions

Use swaig-test to test your functions:

```bash
# List all functions
swaig-test my_agent.py --list-tools

# Test a specific function
swaig-test my_agent.py --exec check_order --order_number 12345

# See the generated SWML
swaig-test my_agent.py --dump-swml
```

## Complete Example

```python
#!/usr/bin/env python3
# restaurant_agent.py - Restaurant order assistant
from signalwire_agents import AgentBase, SwaigFunctionResult


class RestaurantAgent(AgentBase):
    MENU = {
        "burger": {"price": 12.99, "description": "Angus beef burger with fries"},
        "pizza": {"price": 14.99, "description": "12-inch cheese pizza"},
        "salad": {"price": 9.99, "description": "Garden salad with dressing"}
    }

    def __init__(self):
        super().__init__(name="restaurant-agent")
        self.add_language("English", "en-US", "rime.spore")

        self.prompt_add_section(
            "Role",
            "You are a friendly restaurant order assistant."
        )

        self.define_tool(
            name="get_menu_item",
            description="Get details about a menu item including price and description",
            parameters={
                "type": "object",
                "properties": {
                    "item_name": {
                        "type": "string",
                        "description": "Name of the menu item"
                    }
                },
                "required": ["item_name"]
            },
            handler=self.get_menu_item,
            fillers={
                "en-US": ["Let me check the menu..."]
            }
        )

        self.define_tool(
            name="place_order",
            description="Place an order for menu items",
            parameters={
                "type": "object",
                "properties": {
                    "items": {
                        "type": "array",
                        "items": {"type": "string"},
                        "description": "List of menu items to order"
                    },
                    "special_requests": {
                        "type": "string",
                        "description": "Any special requests or modifications"
                    }
                },
                "required": ["items"]
            },
            handler=self.place_order,
            fillers={
                "en-US": ["Placing your order now..."]
            }
        )

    def get_menu_item(self, args, raw_data):
        item_name = args.get("item_name", "").lower()
        item = self.MENU.get(item_name)

        if item:
            return SwaigFunctionResult(
                f"{item_name.title()}: {item['description']}. Price: ${item['price']}"
            )
        return SwaigFunctionResult(f"Sorry, {item_name} is not on our menu.")

    def place_order(self, args, raw_data):
        items = args.get("items", [])
        special = args.get("special_requests", "")

        total = sum(
            self.MENU.get(item.lower(), {}).get("price", 0)
            for item in items
        )

        if total > 0:
            msg = f"Order placed: {', '.join(items)}. Total: ${total:.2f}"
            if special:
                msg += f" Special requests: {special}"
            return SwaigFunctionResult(msg)

        return SwaigFunctionResult("Could not place order. Please check item names.")


if __name__ == "__main__":
    agent = RestaurantAgent()
    agent.run()
```



---

## Parameters

> **Summary**: Define function parameters using JSON Schema to specify what arguments your functions accept. The AI extracts these from the conversation.

### Parameter Structure

Parameters use JSON Schema format:

```python
parameters={
    "type": "object",
    "properties": {
        "param_name": {
            "type": "string",           # Data type
            "description": "Description" # Help AI understand the parameter
        }
    },
    "required": ["param_name"]          # Required parameters
}
```

### Parameter Types

| Type | Description | Example Values |
|------|-------------|----------------|
| `string` | Text values | `"hello"`, `"12345"`, `"New York"` |
| `number` | Numeric values | `42`, `3.14`, `-10` |
| `integer` | Whole numbers only | `1`, `42`, `-5` |
| `boolean` | True/false | `true`, `false` |
| `array` | List of values | `["a", "b", "c"]` |
| `object` | Nested structure | `{"key": "value"}` |

### String Parameters

Basic string parameters:

```python
parameters={
    "type": "object",
    "properties": {
        "name": {
            "type": "string",
            "description": "Customer name"
        },
        "email": {
            "type": "string",
            "description": "Email address"
        },
        "phone": {
            "type": "string",
            "description": "Phone number in any format"
        }
    },
    "required": ["name"]
}
```

### Enum Parameters

Restrict to specific values:

```python
parameters={
    "type": "object",
    "properties": {
        "department": {
            "type": "string",
            "description": "Department to transfer to",
            "enum": ["sales", "support", "billing", "returns"]
        },
        "priority": {
            "type": "string",
            "description": "Issue priority level",
            "enum": ["low", "medium", "high", "urgent"]
        }
    },
    "required": ["department"]
}
```

### Number Parameters

```python
parameters={
    "type": "object",
    "properties": {
        "quantity": {
            "type": "integer",
            "description": "Number of items to order"
        },
        "amount": {
            "type": "number",
            "description": "Dollar amount"
        },
        "rating": {
            "type": "integer",
            "description": "Rating from 1 to 5",
            "minimum": 1,
            "maximum": 5
        }
    },
    "required": ["quantity"]
}
```

### Boolean Parameters

```python
parameters={
    "type": "object",
    "properties": {
        "gift_wrap": {
            "type": "boolean",
            "description": "Whether to gift wrap the order"
        },
        "express_shipping": {
            "type": "boolean",
            "description": "Use express shipping"
        }
    }
}
```

### Array Parameters

```python
parameters={
    "type": "object",
    "properties": {
        "items": {
            "type": "array",
            "description": "List of menu items to order",
            "items": {
                "type": "string"
            }
        },
        "tags": {
            "type": "array",
            "description": "Tags to apply",
            "items": {
                "type": "string",
                "enum": ["urgent", "vip", "callback"]
            }
        }
    },
    "required": ["items"]
}
```

### Object Parameters

```python
parameters={
    "type": "object",
    "properties": {
        "address": {
            "type": "object",
            "description": "Delivery address",
            "properties": {
                "street": {"type": "string"},
                "city": {"type": "string"},
                "zip": {"type": "string"}
            },
            "required": ["street", "city", "zip"]
        }
    },
    "required": ["address"]
}
```

### Optional vs Required Parameters

```python
parameters={
    "type": "object",
    "properties": {
        # Required - AI must extract this
        "order_number": {
            "type": "string",
            "description": "Order number (required)"
        },
        # Optional - AI will include if mentioned
        "include_tracking": {
            "type": "boolean",
            "description": "Include tracking details"
        },
        # Optional with default handling
        "format": {
            "type": "string",
            "description": "Output format",
            "enum": ["brief", "detailed"],
            "default": "brief"
        }
    },
    "required": ["order_number"]  # Only order_number is required
}
```

### Default Values

Handle missing optional parameters in your handler:

```python
def search_products(self, args, raw_data):
    # Get required parameter
    query = args.get("query")

    # Get optional parameters with defaults
    category = args.get("category", "all")
    max_results = args.get("max_results", 5)
    sort_by = args.get("sort_by", "relevance")

    # Use parameters
    results = self.db.search(
        query=query,
        category=category,
        limit=max_results,
        sort=sort_by
    )

    return SwaigFunctionResult(f"Found {len(results)} products")
```

### Parameter Descriptions

Good descriptions help the AI extract parameters correctly:

```python
parameters={
    "type": "object",
    "properties": {
        # Good - specific format guidance
        "order_number": {
            "type": "string",
            "description": "Order number, usually starts with ORD- followed by digits"
        },

        # Good - examples help
        "date": {
            "type": "string",
            "description": "Date in MM/DD/YYYY format, e.g., 12/25/2024"
        },

        # Good - clarifies ambiguity
        "amount": {
            "type": "number",
            "description": "Dollar amount without currency symbol, e.g., 29.99"
        },

        # Bad - too vague
        "info": {
            "type": "string",
            "description": "Information"  # Don't do this
        }
    }
}
```

### Complex Example

```python
from signalwire_agents import AgentBase, SwaigFunctionResult


class TravelAgent(AgentBase):
    def __init__(self):
        super().__init__(name="travel-agent")
        self.add_language("English", "en-US", "rime.spore")

        self.define_tool(
            name="search_flights",
            description="Search for available flights between cities",
            parameters={
                "type": "object",
                "properties": {
                    "from_city": {
                        "type": "string",
                        "description": "Departure city or airport code"
                    },
                    "to_city": {
                        "type": "string",
                        "description": "Destination city or airport code"
                    },
                    "departure_date": {
                        "type": "string",
                        "description": "Departure date in YYYY-MM-DD format"
                    },
                    "return_date": {
                        "type": "string",
                        "description": "Return date in YYYY-MM-DD format (optional for one-way)"
                    },
                    "passengers": {
                        "type": "integer",
                        "description": "Number of passengers",
                        "minimum": 1,
                        "maximum": 9
                    },
                    "cabin_class": {
                        "type": "string",
                        "description": "Preferred cabin class",
                        "enum": ["economy", "premium_economy", "business", "first"]
                    },
                    "preferences": {
                        "type": "object",
                        "description": "Travel preferences",
                        "properties": {
                            "nonstop_only": {
                                "type": "boolean",
                                "description": "Only show nonstop flights"
                            },
                            "flexible_dates": {
                                "type": "boolean",
                                "description": "Search nearby dates for better prices"
                            }
                        }
                    }
                },
                "required": ["from_city", "to_city", "departure_date"]
            },
            handler=self.search_flights
        )

    def search_flights(self, args, raw_data):
        from_city = args.get("from_city")
        to_city = args.get("to_city")
        date = args.get("departure_date")
        passengers = args.get("passengers", 1)
        cabin = args.get("cabin_class", "economy")
        prefs = args.get("preferences", {})

        nonstop = prefs.get("nonstop_only", False)

        # Your flight search logic here
        return SwaigFunctionResult(
            f"Found 3 flights from {from_city} to {to_city} on {date}. "
            f"Cheapest: $299 {cabin} class"
        )
```

### Validating Parameters

Add validation in your handler:

```python
def process_payment(self, args, raw_data):
    amount = args.get("amount")
    card_last_four = args.get("card_last_four")

    # Validate amount
    if amount is None or amount <= 0:
        return SwaigFunctionResult(
            "Invalid amount. Please specify a positive dollar amount."
        )

    # Validate card
    if not card_last_four or len(card_last_four) != 4:
        return SwaigFunctionResult(
            "Please provide the last 4 digits of your card."
        )

    # Process payment
    return SwaigFunctionResult(f"Processing ${amount:.2f} on card ending {card_last_four}")
```

### Parameter Best Practices

**DO:**
- Use clear, descriptive names (order_number not num)
- Provide detailed descriptions with examples
- Use enum for fixed choices
- Mark truly required parameters as required
- Handle missing optional parameters with defaults

**DON'T:**
- Require parameters the caller might not know
- Use ambiguous descriptions
- Expect perfect formatting (be flexible in handlers)
- Create too many required parameters



---

## Results & Actions

> **Summary**: SwaigFunctionResult is the return type for all SWAIG functions. It contains response text for the AI to speak and optional actions like transfers, SMS, or context changes.

### Basic Results

Return a simple response:

```python
from signalwire_agents import SwaigFunctionResult


def check_order(self, args, raw_data):
    order_number = args.get("order_number")
    return SwaigFunctionResult(f"Order {order_number} shipped yesterday")
```

### SwaigFunctionResult Components

| Component | Description |
|-----------|-------------|
| `response` | Text the AI will speak to the caller |
| `action` | List of actions to execute (transfers, SMS, context changes, etc.) |
| `post_process` | If `True`, AI speaks once more before actions execute (useful for confirmations) |

### Method Chaining

SwaigFunctionResult methods return self for chaining:

```python
def transfer_to_support(self, args, raw_data):
    department = args.get("department", "support")

    return (
        SwaigFunctionResult("I'll transfer you now")
        .connect("+15551234567", final=True)
    )
```

### Call Transfer

Transfer to another number:

```python
def transfer_call(self, args, raw_data):
    department = args.get("department")

    numbers = {
        "sales": "+15551111111",
        "support": "+15552222222",
        "billing": "+15553333333"
    }

    dest = numbers.get(department, "+15550000000")

    return (
        SwaigFunctionResult(f"Transferring you to {department}")
        .connect(dest, final=True)
    )
```

**Transfer options:**

```python
## Permanent transfer - call leaves agent completely
.connect("+15551234567", final=True)

## Temporary transfer - returns to agent if far end hangs up
.connect("+15551234567", final=False)

## With custom caller ID
.connect("+15551234567", final=True, from_addr="+15559876543")

## Transfer to SIP address
.connect("support@company.com", final=True)
```

**SIP REFER transfer:**

Use SIP REFER for attended transfers:

```python
def transfer_to_extension(self, args, raw_data):
    extension = args.get("extension")

    return (
        SwaigFunctionResult(f"Transferring to extension {extension}")
        .sip_refer(f"sip:{extension}@pbx.example.com")
    )
```

**SWML-specific transfer:**

Transfer with AI response for context handoff:

```python
def transfer_with_context(self, args, raw_data):
    department = args.get("department")

    return (
        SwaigFunctionResult("Let me connect you")
        .swml_transfer(
            dest="+15551234567",
            ai_response=f"Customer needs help with {department}",
            final=True
        )
    )
```

### Send SMS

Send a text message during the call:

```python
def send_confirmation(self, args, raw_data):
    phone = args.get("phone_number")
    order_id = args.get("order_id")

    return (
        SwaigFunctionResult("I've sent you a confirmation text")
        .send_sms(
            to_number=phone,
            from_number="+15559876543",
            body=f"Your order {order_id} has been confirmed!"
        )
    )
```

**SMS with media:**

```python
def send_receipt(self, args, raw_data):
    phone = args.get("phone_number")
    receipt_url = args.get("receipt_url")

    return (
        SwaigFunctionResult("I've sent your receipt")
        .send_sms(
            to_number=phone,
            from_number="+15559876543",
            body="Here's your receipt:",
            media=[receipt_url]
        )
    )
```

### Payment Processing

Process credit card payments during the call:

```python
def collect_payment(self, args, raw_data):
    amount = args.get("amount")
    description = args.get("description", "Purchase")

    return (
        SwaigFunctionResult("I'll collect your payment information now")
        .pay(
            payment_connector_url="https://api.example.com/payment",
            charge_amount=amount,
            description=description,
            input_method="dtmf",
            security_code=True,
            postal_code=True
        )
    )
```

**Payment with custom prompts:**

```python
def subscription_payment(self, args, raw_data):
    return (
        SwaigFunctionResult("Let's set up your monthly subscription")
        .pay(
            payment_connector_url="https://api.example.com/subscribe",
            charge_amount="29.99",
            description="Monthly Subscription",
            token_type="reusable",
            prompts=[
                {
                    "say": "Please enter your credit card number",
                    "type": "card_number"
                },
                {
                    "say": "Enter the expiration month and year",
                    "type": "expiration"
                }
            ]
        )
    )
```

### Call Recording

Start and stop call recording:

```python
def start_recording(self, args, raw_data):
    return (
        SwaigFunctionResult("Starting call recording")
        .record_call(
            control_id="my_recording",
            stereo=True,
            format="mp3",
            direction="both"
        )
    )


def stop_recording(self, args, raw_data):
    return (
        SwaigFunctionResult("Recording stopped")
        .stop_record_call(control_id="my_recording")
    )
```

**Record with auto-stop:**

```python
def record_with_timeout(self, args, raw_data):
    return (
        SwaigFunctionResult("Recording your message")
        .record_call(
            control_id="voicemail",
            max_length=120.0,  # Stop after 2 minutes
            end_silence_timeout=3.0,  # Stop after 3s silence
            beep=True
        )
    )
```

### Audio Tapping

Tap audio to external endpoint for monitoring or transcription. Supports WebSocket (`wss://`) or RTP (`rtp://`) URIs:

**WebSocket tap:**

```python
def start_websocket_monitoring(self, args, raw_data):
    return (
        SwaigFunctionResult("Call monitoring started")
        .tap(
            uri="wss://monitor.example.com/audio",
            control_id="supervisor_tap",
            direction="both",
            codec="PCMU"
        )
    )
```

**RTP tap:**

```python
def start_rtp_tap(self, args, raw_data):
    return (
        SwaigFunctionResult("Recording to RTP endpoint")
        .tap(
            uri="rtp://192.168.1.100:5004",
            control_id="rtp_tap",
            direction="both",
            codec="PCMU",
            rtp_ptime=20
        )
    )


def stop_monitoring(self, args, raw_data):
    return (
        SwaigFunctionResult("Monitoring stopped")
        .stop_tap(control_id="supervisor_tap")
    )
```

### Call Control

**Hold:**

Put caller on hold:

```python
def hold_for_agent(self, args, raw_data):
    return (
        SwaigFunctionResult("Please hold while I find an available agent")
        .hold(timeout=60)  # Hold for up to 60 seconds
    )
```

### Hang Up

End the call:

```python
def end_call(self, args, raw_data):
    return (
        SwaigFunctionResult("Thank you for calling. Goodbye!")
        .hangup()
    )
```

### Speech Control

**Direct speech with .say():**

Make the AI speak specific text immediately:

```python
def announce_status(self, args, raw_data):
    order_status = args.get("status")

    return (
        SwaigFunctionResult()
        .say(f"Your order status is: {order_status}")
    )
```

**Stop AI from speaking:**

```python
def interrupt_speech(self, args, raw_data):
    return (
        SwaigFunctionResult()
        .stop()  # Immediately stop AI speech
        .say("Let me start over")
    )
```

**Wait for user input:**

Pause and wait for the user to speak:

```python
def wait_for_confirmation(self, args, raw_data):
    return (
        SwaigFunctionResult("I'll wait for your response")
        .wait_for_user(enabled=True, timeout=10)
    )
```

**Simulate user input:**

Inject text as if the user spoke it:

```python
def auto_confirm(self, args, raw_data):
    return (
        SwaigFunctionResult()
        .simulate_user_input("yes, I confirm")
    )
```

### Background Audio

Play audio files in the background during conversation:

```python
def play_hold_music(self, args, raw_data):
    return (
        SwaigFunctionResult("Please hold")
        .play_background_file(
            filename="https://example.com/hold-music.mp3",
            wait=False
        )
    )


def stop_hold_music(self, args, raw_data):
    return (
        SwaigFunctionResult("I'm back")
        .stop_background_file()
    )
```

### Update Global Data

Store data accessible throughout the call:

```python
def save_customer_info(self, args, raw_data):
    customer_id = args.get("customer_id")
    customer_name = args.get("name")

    return (
        SwaigFunctionResult(f"I've noted your information, {customer_name}")
        .update_global_data({
            "customer_id": customer_id,
            "customer_name": customer_name,
            "verified": True
        })
    )
```

**Remove global data:**

```python
def clear_session_data(self, args, raw_data):
    return (
        SwaigFunctionResult("Session data cleared")
        .remove_global_data(["customer_id", "verified"])
    )
```

### Metadata Management

Store function-specific metadata (separate from global data):

```python
def track_function_usage(self, args, raw_data):
    return (
        SwaigFunctionResult("Usage tracked")
        .set_metadata({
            "function_called": "check_order",
            "timestamp": "2024-01-15T10:30:00Z",
            "user_id": args.get("user_id")
        })
    )
```

**Remove metadata:**

```python
def clear_function_metadata(self, args, raw_data):
    return (
        SwaigFunctionResult("Metadata cleared")
        .remove_metadata(["timestamp", "user_id"])
    )
```

### Context Switching

**Advanced context switch:**

Change the agent's prompt/context with new system and user prompts:

```python
def switch_to_technical(self, args, raw_data):
    return (
        SwaigFunctionResult("Switching to technical support mode")
        .switch_context(
            system_prompt="You are now a technical support specialist. "
                         "Help the customer with their technical issue.",
            user_prompt="The customer needs help with their account"
        )
    )
```

**SWML context switch:**

Switch to a named SWML context:

```python
def switch_to_billing(self, args, raw_data):
    return (
        SwaigFunctionResult("Let me connect you with billing")
        .swml_change_context("billing_context")
    )
```

**SWML step change:**

Change to a specific workflow step:

```python
def move_to_checkout(self, args, raw_data):
    return (
        SwaigFunctionResult("Moving to checkout")
        .swml_change_step("checkout_step")
    )
```

### Function Control

Dynamically enable or disable functions during the call:

```python
def enable_payment_functions(self, args, raw_data):
    return (
        SwaigFunctionResult("Payment functions are now available")
        .toggle_functions([
            {"function": "collect_payment", "active": True},
            {"function": "refund_payment", "active": True},
            {"function": "check_balance", "active": False}
        ])
    )
```

**Enable functions on timeout:**

```python
def enable_escalation_on_timeout(self, args, raw_data):
    return (
        SwaigFunctionResult("I'll help you with that")
        .enable_functions_on_timeout(enabled=True)
    )
```

**Update AI settings:**

```python
def adjust_speech_timing(self, args, raw_data):
    return (
        SwaigFunctionResult("Adjusting response timing")
        .update_settings({
            "end_of_speech_timeout": 1000,
            "attention_timeout": 30000
        })
    )
```

**Set speech timeouts:**

```python
def configure_timeouts(self, args, raw_data):
    return (
        SwaigFunctionResult()
        .set_end_of_speech_timeout(800)  # 800ms
        .set_speech_event_timeout(5000)  # 5s
    )
```

### Conference & Rooms

**Join a conference:**

```python
def join_team_conference(self, args, raw_data):
    conf_name = args.get("conference_name")

    return (
        SwaigFunctionResult(f"Joining {conf_name}")
        .join_conference(
            name=conf_name,
            muted=False,
            beep="true",
            start_conference_on_enter=True
        )
    )
```

**Join a SignalWire room:**

```python
def join_support_room(self, args, raw_data):
    return (
        SwaigFunctionResult("Connecting to support room")
        .join_room(name="support-room-1")
    )
```

### Post-Processing

Let AI speak once more before executing actions:

```python
def transfer_with_confirmation(self, args, raw_data):
    return (
        SwaigFunctionResult(
            "I'll transfer you to billing. Is there anything else first?",
            post_process=True  # AI can respond to follow-up before transfer
        )
        .connect("+15551234567", final=True)
    )
```

### Multiple Actions

Chain multiple actions together:

```python
def complete_interaction(self, args, raw_data):
    customer_phone = args.get("phone")

    return (
        SwaigFunctionResult("I've completed your request")
        .update_global_data({"interaction_complete": True})
        .send_sms(
            to_number=customer_phone,
            from_number="+15559876543",
            body="Thank you for calling!"
        )
    )
```

### Advanced: Execute Raw SWML

For advanced use cases, execute raw SWML documents directly:

```python
def execute_custom_swml(self, args, raw_data):
    swml_doc = {
        "version": "1.0.0",
        "sections": {
            "main": [
                {"play": {"url": "https://example.com/announcement.mp3"}},
                {"hangup": {}}
            ]
        }
    }

    return (
        SwaigFunctionResult()
        .execute_swml(swml_doc, transfer=False)
    )
```

**Note:** Most use cases are covered by the convenience methods above. Use `execute_swml()` only when you need SWML features not available through other action methods.

### Action Reference

#### Call Control Actions

| Method | Description |
|--------|-------------|
| `.connect(dest, final, from_addr)` | Transfer call to another number or SIP URI |
| `.swml_transfer(dest, ai_response, final)` | SWML-specific transfer with AI response |
| `.sip_refer(to_uri)` | SIP REFER transfer |
| `.hangup()` | End the call |
| `.hold(timeout)` | Put caller on hold (default 300s, max 900s) |
| `.send_sms(to, from, body, media)` | Send SMS message |
| `.record_call(control_id, stereo, ...)` | Start call recording |
| `.stop_record_call(control_id)` | Stop call recording |
| `.tap(uri, control_id, direction, ...)` | Tap call audio to external URI |
| `.stop_tap(control_id)` | Stop call tapping |
| `.pay(payment_connector_url, ...)` | Process payment |
| `.execute_swml(doc, transfer)` | Execute raw SWML document |
| `.join_room(name)` | Join a SignalWire room |
| `.join_conference(name, muted, ...)` | Join a conference |

#### Speech & Audio Actions

| Method | Description |
|--------|-------------|
| `.say(text)` | Have AI speak specific text |
| `.stop()` | Stop AI from speaking |
| `.play_background_file(url, wait)` | Play background audio |
| `.stop_background_file()` | Stop background audio |
| `.simulate_user_input(text)` | Inject text as user speech |
| `.wait_for_user(enabled, timeout, answer_first)` | Wait for user to speak |

#### Context & Workflow Actions

| Method | Description |
|--------|-------------|
| `.switch_context(system_prompt, user_prompt)` | Advanced context switch with new prompts |
| `.swml_change_context(ctx)` | Switch to named context |
| `.swml_change_step(step)` | Change to specific workflow step |

#### Data Management Actions

| Method | Description |
|--------|-------------|
| `.update_global_data(data)` | Set global session data |
| `.remove_global_data(keys)` | Remove keys from global data |
| `.set_metadata(data)` | Set function-specific metadata |
| `.remove_metadata(keys)` | Remove function metadata keys |

#### AI Behavior Actions

| Method | Description |
|--------|-------------|
| `.toggle_functions(funcs)` | Enable/disable specific functions |
| `.enable_functions_on_timeout(enabled)` | Enable functions when timeout occurs |
| `.update_settings(config)` | Modify AI settings dynamically |
| `.set_end_of_speech_timeout(ms)` | Adjust speech timeout |
| `.set_speech_event_timeout(ms)` | Adjust speech event timeout |
| `.enable_extensive_data(enabled)` | Enable extended data in webhooks |

#### Events

| Method | Description |
|--------|-------------|
| `.swml_user_event(data)` | Fire custom user event |



---

## DataMap

> **Summary**: DataMap provides serverless API integration - define functions that call REST APIs directly from SignalWire's infrastructure without running code on your server.

### When to Use DataMap

| Use Handler Functions When | Use DataMap When |
|----------------------------|------------------|
| Complex business logic | Simple REST API calls |
| Database access needed | No custom logic required |
| Multi-step processing | Want serverless deployment |
| External service integration with custom handling | Pattern-based responses |
| | Variable substitution only |

### DataMap Flow

**DataMap Execution Steps:**

1. **AI decides to call function**
   - Function: `get_weather`
   - Args: `{"city": "Seattle"}`

2. **SignalWire executes DataMap** (no webhook to your server!)
   - `GET https://api.weather.com?city=Seattle`

3. **API response processed**
   - Response: `{"temp": 65, "condition": "cloudy"}`

4. **Output template filled**
   - Result: "Weather in Seattle: 65 degrees, cloudy"

### Basic DataMap

```python
from signalwire_agents import AgentBase
from signalwire_agents.core.data_map import DataMap
from signalwire_agents.core.function_result import SwaigFunctionResult


class WeatherAgent(AgentBase):
    def __init__(self):
        super().__init__(name="weather-agent")
        self.add_language("English", "en-US", "rime.spore")

        # Create DataMap
        weather_dm = (
            DataMap("get_weather")
            .description("Get current weather for a city")
            .parameter("city", "string", "City name", required=True)
            .webhook("GET", "https://api.weather.com/v1/current?key=API_KEY&q=${enc:args.city}")
            .output(SwaigFunctionResult(
                "The weather in ${args.city} is ${response.current.condition.text}, "
                "${response.current.temp_f} degrees Fahrenheit"
            ))
        )

        # Register it
        self.register_swaig_function(weather_dm.to_swaig_function())
```

### Variable Substitution

DataMap supports these variable patterns:

| Pattern | Description |
|---------|-------------|
| `${args.param}` | Function argument value |
| `${enc:args.param}` | URL-encoded argument (use in webhook URLs) |
| `${lc:args.param}` | Lowercase argument value |
| `${fmt_ph:args.phone}` | Format as phone number |
| `${response.field}` | API response field |
| `${response.arr[0]}` | Array element in response |
| `${global_data.key}` | Global session data |
| `${meta_data.key}` | Call metadata |

#### Chained Modifiers

Modifiers are applied right-to-left:

| Pattern | Result |
|---------|--------|
| `${enc:lc:args.param}` | First lowercase, then URL encode |
| `${lc:enc:args.param}` | First URL encode, then lowercase |

#### Examples

| Pattern | Result |
|---------|--------|
| `${args.city}` | "Seattle" (in body/output) |
| `${enc:args.city}` | "Seattle" URL-encoded (in URLs) |
| `${lc:args.city}` | "seattle" (lowercase) |
| `${enc:lc:args.city}` | "seattle" lowercased then URL-encoded |
| `${fmt_ph:args.phone}` | "+1 (555) 123-4567" |
| `${response.temp}` | "65" |
| `${response.items[0].name}` | "First item" |
| `${global_data.user_id}` | "user123" |

### DataMap Builder Methods

#### description() / purpose()

Set the function description:

```python
DataMap("my_function")
    .description("Look up product information by SKU")
```

#### parameter()

Add a function parameter:

```python
.parameter("sku", "string", "Product SKU code", required=True)
.parameter("include_price", "boolean", "Include pricing info", required=False)
.parameter("category", "string", "Filter by category", enum=["electronics", "clothing", "food"])
```

#### webhook()

Add an API call:

```python
## GET request
.webhook("GET", "https://api.example.com/products?sku=${enc:args.sku}")

## POST request
.webhook("POST", "https://api.example.com/search")

## With headers
.webhook("GET", "https://api.example.com/data",
         headers={"Authorization": "Bearer ${global_data.api_key}"})
```

#### body()

Set request body for POST/PUT:

```python
.webhook("POST", "https://api.example.com/search")
.body({
    "query": "${args.search_term}",
    "limit": 5
})
```

#### output()

Set the response for a webhook:

```python
.output(SwaigFunctionResult(
    "Found product: ${response.name}. Price: $${response.price}"
))
```

#### fallback_output()

Set fallback if all webhooks fail:

```python
.fallback_output(SwaigFunctionResult(
    "Sorry, the service is currently unavailable"
))
```

### Complete Example

```python
#!/usr/bin/env python3
## weather_datamap_agent.py - Weather agent using DataMap
from signalwire_agents import AgentBase
from signalwire_agents.core.data_map import DataMap
from signalwire_agents.core.function_result import SwaigFunctionResult


class WeatherAgent(AgentBase):
    def __init__(self):
        super().__init__(name="weather-agent")
        self.add_language("English", "en-US", "rime.spore")

        self.prompt_add_section("Role", "You help users check the weather.")

        weather_dm = (
            DataMap("get_weather")
            .description("Get current weather conditions for a city")
            .parameter("city", "string", "City name", required=True)
            .webhook(
                "GET",
                "https://api.weatherapi.com/v1/current.json"
                "?key=YOUR_API_KEY&q=${enc:args.city}"
            )
            .output(SwaigFunctionResult(
                "Current weather in ${args.city}: "
                "${response.current.condition.text}, "
                "${response.current.temp_f} degrees Fahrenheit"
            ))
            .fallback_output(SwaigFunctionResult(
                "Sorry, I couldn't get weather data for ${args.city}"
            ))
        )

        self.register_swaig_function(weather_dm.to_swaig_function())


if __name__ == "__main__":
    agent = WeatherAgent()
    agent.run()
```

### DataMap Best Practices

**DO:**
- Use for simple API integrations
- Set fallback_output for resilience
- Use error_keys to detect API errors
- Test with swaig-test before deploying

**DON'T:**
- Put API keys directly in URLs (use secure storage)
- Use for complex multi-step logic
- Forget to handle all error cases
- Assume API responses will always have expected structure



---

## Native Functions

> **Summary**: Native functions are built-in SignalWire capabilities that can be enabled without writing code. They provide common operations like web search and debugging.

### What Are Native Functions?

Native functions run directly on SignalWire's platform. Enable them to give the AI access to built-in capabilities without creating handlers.

| Handler Function | Native Function |
|------------------|-----------------|
| You define handler | SignalWire provides |
| Runs on your server | Runs on SignalWire |
| Custom logic | Pre-built behavior |

**Available Native Functions:**

- `web_search` - Search the web
- `debug` - Debug mode for testing

### Enabling Native Functions

Enable native functions in the constructor:

```python
from signalwire_agents import AgentBase


class MyAgent(AgentBase):
    def __init__(self):
        super().__init__(
            name="my-agent",
            native_functions=["web_search"]  # Enable web search
        )
        self.add_language("English", "en-US", "rime.spore")
```

### Web Search Function

Enable web search to let the AI look up information:

```python
class ResearchAgent(AgentBase):
    def __init__(self):
        super().__init__(
            name="research-agent",
            native_functions=["web_search"]
        )
        self.add_language("English", "en-US", "rime.spore")

        self.prompt_add_section(
            "Role",
            "You are a research assistant. Search the web to answer questions."
        )
```

The AI can now search the web to find answers to caller questions.

### Debug Function

Enable debug mode for development and testing:

```python
class DebugAgent(AgentBase):
    def __init__(self):
        super().__init__(
            name="debug-agent",
            native_functions=["debug"]
        )
        self.add_language("English", "en-US", "rime.spore")
```

The debug function provides diagnostic information during testing.

### Call Transfers

For call transfers, use `SwaigFunctionResult.connect()` in a custom handler function - there is no native transfer function:

```python
from signalwire_agents import AgentBase, SwaigFunctionResult


class TransferAgent(AgentBase):
    DEPARTMENTS = {
        "sales": "+15551111111",
        "support": "+15552222222",
        "billing": "+15553333333"
    }

    def __init__(self):
        super().__init__(name="transfer-agent")
        self.add_language("English", "en-US", "rime.spore")

        self.prompt_add_section(
            "Role",
            "You are a receptionist. Transfer callers to the appropriate department."
        )

        self.define_tool(
            name="transfer_call",
            description="Transfer the call to a department",
            parameters={
                "type": "object",
                "properties": {
                    "department": {
                        "type": "string",
                        "description": "Department to transfer to",
                        "enum": ["sales", "support", "billing"]
                    }
                },
                "required": ["department"]
            },
            handler=self.transfer_call
        )

    def transfer_call(self, args, raw_data):
        department = args.get("department")
        number = self.DEPARTMENTS.get(department)

        if not number:
            return SwaigFunctionResult("Invalid department")

        return (
            SwaigFunctionResult(f"Transferring you to {department}")
            .connect(number, final=True)
        )
```

### Combining Native and Custom Functions

Use native functions alongside your custom handlers:

```python
from signalwire_agents import AgentBase, SwaigFunctionResult


class HybridAgent(AgentBase):
    def __init__(self):
        super().__init__(
            name="hybrid-agent",
            native_functions=["web_search"]  # Native
        )
        self.add_language("English", "en-US", "rime.spore")

        # Custom function alongside native ones
        self.define_tool(
            name="check_account",
            description="Look up customer account information",
            parameters={
                "type": "object",
                "properties": {
                    "account_id": {
                        "type": "string",
                        "description": "Account ID"
                    }
                },
                "required": ["account_id"]
            },
            handler=self.check_account
        )

        self.prompt_add_section(
            "Role",
            "You are a customer service agent. "
            "You can check accounts and search the web for information."
        )

    def check_account(self, args, raw_data):
        account_id = args.get("account_id")
        return SwaigFunctionResult(f"Account {account_id} is active")
```

### When to Use Native vs Custom Functions

| Scenario | Recommendation |
|----------|----------------|
| Web search capability | Use `web_search` native function |
| Development testing | Use `debug` native function |
| Transfer to phone number | Use SwaigFunctionResult.connect() in custom handler |
| Transfer to SIP address | Use SwaigFunctionResult.connect() in custom handler |
| Custom business logic | Use define_tool() with handler |
| Database lookups | Use define_tool() with handler |

### Native Functions Reference

| Function | Description | Use Case |
|----------|-------------|----------|
| `web_search` | Search the web | Answer general questions |
| `debug` | Debug information | Development/testing |

### Next Steps

You've now learned all about SWAIG functions. Next, explore Skills to add pre-built capabilities to your agents.



# Part: Skills

---

# Skills

> **Summary**: Skills are modular, reusable capabilities that add functions, prompts, and integrations to your agents without custom code.

## What You'll Learn

This chapter covers the skills system:

1. **Understanding Skills** - What skills are and how they work
2. **Built-in Skills** - Pre-built skills available in the SDK
3. **Adding Skills** - How to add skills to your agents
4. **Custom Skills** - Creating your own skills
5. **Skill Configuration** - Parameters and advanced options

## What Are Skills?

Skills are pre-packaged capabilities that add:

- **Functions** - SWAIG tools the AI can call
- **Prompts** - Instructions for how to use the skill
- **Hints** - Speech recognition keywords
- **Global Data** - Variables available throughout the call

| Without Skills | With Skills |
|----------------|-------------|
| Write weather function | `self.add_skill("weather")` |
| Add API integration | |
| Write prompts | Done! |
| Add speech hints | |
| Handle errors | |

## Quick Start

Add a skill in one line:

```python
from signalwire_agents import AgentBase

class MyAgent(AgentBase):
    def __init__(self):
        super().__init__(name="my-agent")
        self.add_language("English", "en-US", "rime.spore")

        # Add datetime capability
        self.add_skill("datetime")

        # Add math capability
        self.add_skill("math")

        self.prompt_add_section(
            "Role",
            "You are a helpful assistant that can tell time and do math."
        )
```

## Available Built-in Skills

| Skill | Description |
|-------|-------------|
| `datetime` | Get current date and time |
| `math` | Perform calculations |
| `web_search` | Search the web (requires API key) |
| `wikipedia_search` | Search Wikipedia |
| `weather_api` | Get weather information |
| `joke` | Tell jokes |
| `play_background_file` | Play audio files |
| `swml_transfer` | Transfer calls to SWML endpoints |
| `datasphere` | Search DataSphere documents |
| `native_vector_search` | Local vector search |

## Chapter Contents

| Section | Description |
|---------|-------------|
| [Understanding Skills](05_01_understanding-skills.md) | How skills work internally |
| [Built-in Skills](05_02_builtin-skills.md) | Reference for included skills |
| [Adding Skills](05_03_adding-skills.md) | How to use skills in your agents |
| [Custom Skills](05_04_custom-skills.md) | Creating your own skills |
| [Skill Configuration](05_05_skill-config.md) | Parameters and advanced options |

## Skills vs Functions

| Aspect | SWAIG Function | Skill |
|--------|----------------|-------|
| **Scope** | Single function | Multiple functions + prompts + hints |
| **Reusability** | Per-agent | Across all agents |
| **Setup** | define_tool() | add_skill() |
| **Customization** | Full control | Parameters only |
| **Maintenance** | You maintain | SDK maintains |

## When to Use Skills

### Use Built-in Skills When:

- Standard capability needed (datetime, search, etc.)
- Want quick setup without custom code
- Need tested, maintained functionality

### Create Custom Skills When:

- Reusing capability across multiple agents
- Want to share functionality with team/community
- Packaging complex integrations

### Use SWAIG Functions When:

- One-off custom logic
- Agent-specific business rules
- Need full control over implementation

## Complete Example

```python
#!/usr/bin/env python3
# assistant_agent.py - Agent with multiple skills
from signalwire_agents import AgentBase

class AssistantAgent(AgentBase):
    def __init__(self):
        super().__init__(name="assistant")
        self.add_language("English", "en-US", "rime.spore")

        # Add multiple skills
        self.add_skill("datetime")
        self.add_skill("math")

        self.prompt_add_section(
            "Role",
            "You are a helpful assistant named Alex."
        )

        self.prompt_add_section(
            "Capabilities",
            body="You can help with:",
            bullets=[
                "Telling the current date and time",
                "Performing math calculations"
            ]
        )

if __name__ == "__main__":
    agent = AssistantAgent()
    agent.run()
```

Let's start by understanding how skills work internally.

## Skill Architecture

### SkillBase (Abstract Base Class)

**Required Methods:**
- `setup()` - Initialize the skill
- `register_tools()` - Register SWAIG functions

**Optional Methods:**
- `get_hints()` - Speech recognition hints
- `get_global_data()` - Session data
- `get_prompt_sections()` - Prompt additions
- `cleanup()` - Resource cleanup

### SkillRegistry (Discovery & Loading)

- Discovers skills from directories
- Loads skills on-demand (lazy loading)
- Validates requirements (packages, env vars)
- Supports external skill paths

## How Skills Work

When you call `add_skill()`:

```diagram
┌─────────────────────────────────────────────────────────────────────────────┐
│                      Skill Loading Process                                  │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  1. Agent calls add_skill("datetime")                                       │
│              │                                                              │
│              ▼                                                              │
│  2. SkillRegistry looks up skill class                                      │
│     • Checks already loaded skills                                          │
│     • Searches built-in skills directory                                    │
│     • Searches external paths                                               │
│              │                                                              │
│              ▼                                                              │
│  3. SkillManager instantiates skill                                         │
│     • Creates skill instance with agent reference                           │
│     • Passes configuration parameters                                       │
│              │                                                              │
│              ▼                                                              │
│  4. Skill setup() is called                                                 │
│     • Validates required packages                                           │
│     • Validates environment variables                                       │
│     • Initializes APIs/connections                                          │
│              │                                                              │
│              ▼                                                              │
│  5. Skill register_tools() is called                                        │
│     • Registers SWAIG functions with agent                                  │
│              │                                                              │
│              ▼                                                              │
│  6. Skill contributions applied                                             │
│     • Prompts added to agent                                                │
│     • Hints added for speech recognition                                    │
│     • Global data merged                                                    │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

## Skill Directory Structure

Built-in skills live in the SDK:

```
signalwire_agents/
└── skills/
    ├── datetime/
    │   ├── __init__.py
    │   └── skill.py
    ├── math/
    │   ├── __init__.py
    │   └── skill.py
    ├── web_search/
    │   ├── __init__.py
    │   ├── skill.py
    │   └── requirements.txt
    └── ...
```

Each skill directory contains:

| File | Purpose |
|------|---------|
| `skill.py` | Skill class implementation |
| `__init__.py` | Python package marker |
| `requirements.txt` | Optional extra dependencies |

## SkillBase Class

All skills inherit from `SkillBase`:

```python
from signalwire_agents.core.skill_base import SkillBase
from signalwire_agents.core.function_result import SwaigFunctionResult


class MySkill(SkillBase):
    # Required class attributes
    SKILL_NAME = "my_skill"
    SKILL_DESCRIPTION = "Does something useful"
    SKILL_VERSION = "1.0.0"

    # Optional requirements
    REQUIRED_PACKAGES = []      # Python packages needed
    REQUIRED_ENV_VARS = []      # Environment variables needed

    # Multi-instance support
    SUPPORTS_MULTIPLE_INSTANCES = False

    def setup(self) -> bool:
        """Initialize the skill. Return True if successful."""
        return True

    def register_tools(self) -> None:
        """Register SWAIG tools with the agent."""
        self.define_tool(
            name="my_function",
            description="Does something",
            parameters={},
            handler=self.my_handler
        )

    def my_handler(self, args, raw_data):
        """Handle function calls."""
        return SwaigFunctionResult("Result")
```

## Skill Lifecycle

```
Discover → Load → Setup → Register → Active → Cleanup
```

| Stage | Description |
|-------|-------------|
| **Discover** | Registry finds skill class in directory |
| **Load** | Skill class is imported and validated |
| **Setup** | `setup()` validates requirements, initializes resources |
| **Register** | `register_tools()` adds functions to agent |
| **Active** | Skill is ready, functions can be called |
| **Cleanup** | `cleanup()` releases resources on shutdown |

## Skill Contributions

Skills can contribute to the agent in multiple ways:

### 1. Tools (Functions)

```python
def register_tools(self) -> None:
    self.define_tool(
        name="get_time",
        description="Get current time",
        parameters={
            "timezone": {
                "type": "string",
                "description": "Timezone name"
            }
        },
        handler=self.get_time_handler
    )
```

### 2. Prompt Sections

```python
def get_prompt_sections(self):
    return [
        {
            "title": "Time Information",
            "body": "You can tell users the current time.",
            "bullets": [
                "Use get_time for time queries",
                "Support multiple timezones"
            ]
        }
    ]
```

### 3. Speech Hints

```python
def get_hints(self):
    return ["time", "date", "clock", "timezone"]
```

### 4. Global Data

```python
def get_global_data(self):
    return {
        "datetime_enabled": True,
        "default_timezone": "UTC"
    }
```

## Skill Discovery Paths

Skills are discovered from multiple locations in priority order:

| Priority | Source | Example |
|----------|--------|---------|
| 1 | Already registered skills (in memory) | - |
| 2 | Entry points (pip installed packages) | `entry_points={'signalwire_agents.skills': ['my_skill = pkg:Skill']}` |
| 3 | Built-in skills directory | `signalwire_agents/skills/` |
| 4 | External paths | `skill_registry.add_skill_directory('/opt/custom_skills')` |
| 5 | Environment variable paths | `SIGNALWIRE_SKILL_PATHS=/path1:/path2` |

## Lazy Loading

Skills are loaded on-demand to minimize startup time:

```python
# Skill NOT loaded yet
agent = MyAgent()

# Skill loaded when first referenced
agent.add_skill("datetime")  # datetime skill loaded here

# Already loaded, reused
agent.add_skill("datetime")  # Uses cached class
```

## Multi-Instance Skills

Some skills support multiple instances with different configurations:

```python
class MySkill(SkillBase):
    SUPPORTS_MULTIPLE_INSTANCES = True

    def get_instance_key(self) -> str:
        # Unique key for this instance
        tool_name = self.params.get('tool_name', self.SKILL_NAME)
        return f"{self.SKILL_NAME}_{tool_name}"
```

Usage:

```python
# Add two instances with different configs
agent.add_skill("web_search", {
    "tool_name": "search_news",
    "search_engine_id": "NEWS_ENGINE_ID",
    "api_key": "KEY"
})

agent.add_skill("web_search", {
    "tool_name": "search_docs",
    "search_engine_id": "DOCS_ENGINE_ID",
    "api_key": "KEY"
})
```



---

## Built-in Skills

> **Summary**: The SDK includes ready-to-use skills for common tasks like datetime, math, web search, and more. Each skill adds specific capabilities to your agents.

### Available Skills

| Skill | Description | Requirements |
|-------|-------------|--------------|
| `datetime` | Date/time information | pytz |
| `math` | Mathematical calculations | (none) |
| `web_search` | Web search via Google API | API key |
| `wikipedia_search` | Wikipedia lookups | (none) |
| `weather_api` | Weather information | API key |
| `joke` | Tell jokes | (none) |
| `play_background_file` | Play audio files | (none) |
| `swml_transfer` | Transfer to SWML endpoint | (none) |
| `datasphere` | DataSphere document search | API credentials |
| `native_vector_search` | Local vector search | search extras |

### datetime

Get current date (today) and time information with timezone support.

**Functions:**
- `get_current_time` - Get current time in a timezone
- `get_current_date` - Get today's date

**Requirements:** `pytz` package

```python
from signalwire_agents import AgentBase


class TimeAgent(AgentBase):
    def __init__(self):
        super().__init__(name="time-agent")
        self.add_language("English", "en-US", "rime.spore")

        self.add_skill("datetime")

        self.prompt_add_section(
            "Role",
            "You help users with date and time information."
        )
```

### math

Perform mathematical calculations.

**Functions:**
- `calculate` - Evaluate mathematical expressions

**Requirements:** None

```python
from signalwire_agents import AgentBase


class CalculatorAgent(AgentBase):
    def __init__(self):
        super().__init__(name="calculator")
        self.add_language("English", "en-US", "rime.spore")

        self.add_skill("math")

        self.prompt_add_section(
            "Role",
            "You are a calculator that helps with math."
        )
```

### web_search

Search the web using Google Custom Search API with quality filtering.

**Functions:**
- `web_search` - Search the web

**Requirements:**
- Google Custom Search API key
- Search Engine ID

```python
from signalwire_agents import AgentBase


class SearchAgent(AgentBase):
    def __init__(self):
        super().__init__(name="search-agent")
        self.add_language("English", "en-US", "rime.spore")

        self.add_skill("web_search", {
            "api_key": "YOUR_GOOGLE_API_KEY",
            "search_engine_id": "YOUR_SEARCH_ENGINE_ID",
            "num_results": 3
        })

        self.prompt_add_section(
            "Role",
            "You search the web to answer questions."
        )
```

**Parameters:**

| Parameter | Type | Description | Default |
|-----------|------|-------------|---------|
| `api_key` | string | Google API key | Required |
| `search_engine_id` | string | Search engine ID | Required |
| `num_results` | integer | Results to return | 3 |
| `min_quality_score` | number | Quality threshold | 0.3 |

### wikipedia_search

Search Wikipedia for information.

**Functions:**
- `search_wikipedia` - Search Wikipedia articles

**Requirements:** None

```python
from signalwire_agents import AgentBase


class WikiAgent(AgentBase):
    def __init__(self):
        super().__init__(name="wiki-agent")
        self.add_language("English", "en-US", "rime.spore")

        self.add_skill("wikipedia_search")

        self.prompt_add_section(
            "Role",
            "You look up information on Wikipedia."
        )
```

### weather_api

Get weather information for locations.

**Functions:**
- `get_weather` - Get current weather

**Requirements:** Weather API key

```python
from signalwire_agents import AgentBase


class WeatherAgent(AgentBase):
    def __init__(self):
        super().__init__(name="weather-agent")
        self.add_language("English", "en-US", "rime.spore")

        self.add_skill("weather_api", {
            "api_key": "YOUR_WEATHER_API_KEY"
        })

        self.prompt_add_section(
            "Role",
            "You provide weather information."
        )
```

### joke

Tell jokes to users.

**Functions:**
- `tell_joke` - Get a random joke

**Requirements:** None

```python
from signalwire_agents import AgentBase


class FunAgent(AgentBase):
    def __init__(self):
        super().__init__(name="fun-agent")
        self.add_language("English", "en-US", "rime.spore")

        self.add_skill("joke")

        self.prompt_add_section(
            "Role",
            "You are a fun assistant that tells jokes."
        )
```

### play_background_file

Play audio files during the call.

**Functions:**
- `play_background_file` - Start playing audio
- `stop_background_file` - Stop playing audio

**Requirements:** None

```python
from signalwire_agents import AgentBase


class MusicAgent(AgentBase):
    def __init__(self):
        super().__init__(name="music-agent")
        self.add_language("English", "en-US", "rime.spore")

        self.add_skill("play_background_file", {
            "audio_url": "https://example.com/music.mp3"
        })
```

### swml_transfer

Transfer calls to another SWML endpoint.

**Functions:**
- `transfer_to_swml` - Transfer to SWML URL

**Requirements:** None

```python
from signalwire_agents import AgentBase


class TransferAgent(AgentBase):
    def __init__(self):
        super().__init__(name="transfer-agent")
        self.add_language("English", "en-US", "rime.spore")

        self.add_skill("swml_transfer", {
            "swml_url": "https://your-server.com/other-agent",
            "description": "Transfer to specialist"
        })
```

### datasphere

Search SignalWire DataSphere documents.

**Functions:**
- `search_datasphere` - Search uploaded documents

**Requirements:** DataSphere API credentials

```python
from signalwire_agents import AgentBase


class KnowledgeAgent(AgentBase):
    def __init__(self):
        super().__init__(name="knowledge-agent")
        self.add_language("English", "en-US", "rime.spore")

        self.add_skill("datasphere", {
            "space_name": "your-space",
            "project_id": "YOUR_PROJECT_ID",
            "api_token": "YOUR_API_TOKEN"
        })
```

### native_vector_search

Local vector search using .swsearch index files.

**Functions:**
- `search_knowledge` - Search local vector index

**Requirements:** Search extras installed (`pip install signalwire-agents[search]`)

```python
from signalwire_agents import AgentBase


class LocalSearchAgent(AgentBase):
    def __init__(self):
        super().__init__(name="local-search")
        self.add_language("English", "en-US", "rime.spore")

        self.add_skill("native_vector_search", {
            "index_path": "/path/to/knowledge.swsearch",
            "tool_name": "search_docs"
        })
```

### Skills Summary Table

| Skill | Functions | API Required | Multi-Instance |
|-------|-----------|--------------|----------------|
| `datetime` | 2 | No | No |
| `math` | 1 | No | No |
| `web_search` | 1 | Yes | Yes |
| `wikipedia_search` | 1 | No | No |
| `weather_api` | 1 | Yes | No |
| `joke` | 1 | No | No |
| `play_background_file` | 2 | No | No |
| `swml_transfer` | 1 | No | Yes |
| `datasphere` | 1 | Yes | Yes |
| `native_vector_search` | 1 | No | Yes |



---

## Adding Skills

> **Summary**: Add skills to your agents with `add_skill()`. Pass configuration parameters to customize behavior.

### Basic Usage

Add a skill with no configuration:

```python
from signalwire_agents import AgentBase


class MyAgent(AgentBase):
    def __init__(self):
        super().__init__(name="my-agent")
        self.add_language("English", "en-US", "rime.spore")

        # Add skill with default settings
        self.add_skill("datetime")
```

### With Configuration

Pass parameters as a dictionary:

```python
from signalwire_agents import AgentBase


class MyAgent(AgentBase):
    def __init__(self):
        super().__init__(name="my-agent")
        self.add_language("English", "en-US", "rime.spore")

        # Add skill with configuration
        self.add_skill("web_search", {
            "api_key": "YOUR_API_KEY",
            "search_engine_id": "YOUR_ENGINE_ID",
            "num_results": 5
        })
```

### Method Chaining

`add_skill()` returns `self` for chaining:

```python
from signalwire_agents import AgentBase


class MyAgent(AgentBase):
    def __init__(self):
        super().__init__(name="my-agent")
        self.add_language("English", "en-US", "rime.spore")

        # Chain multiple skills
        (self
            .add_skill("datetime")
            .add_skill("math")
            .add_skill("joke"))
```

### Multiple Skills

Add as many skills as needed:

```python
from signalwire_agents import AgentBase


class AssistantAgent(AgentBase):
    def __init__(self):
        super().__init__(name="assistant")
        self.add_language("English", "en-US", "rime.spore")

        # Add multiple capabilities
        self.add_skill("datetime")
        self.add_skill("math")
        self.add_skill("wikipedia_search")

        self.prompt_add_section(
            "Role",
            "You are a helpful assistant."
        )

        self.prompt_add_section(
            "Capabilities",
            body="You can help with:",
            bullets=[
                "Date and time information",
                "Math calculations",
                "Wikipedia lookups"
            ]
        )
```

### Checking Loaded Skills

```python
## Check if skill is loaded
if agent.has_skill("datetime"):
    print("Datetime skill is active")

## List all loaded skills
skills = agent.list_skills()
print(f"Loaded skills: {skills}")
```

### Removing Skills

```python
## Remove a skill
agent.remove_skill("datetime")
```

### Multi-Instance Skills

Some skills support multiple instances:

```python
from signalwire_agents import AgentBase


class MultiSearchAgent(AgentBase):
    def __init__(self):
        super().__init__(name="multi-search")
        self.add_language("English", "en-US", "rime.spore")

        # First search instance for news
        self.add_skill("web_search", {
            "tool_name": "search_news",
            "api_key": "YOUR_API_KEY",
            "search_engine_id": "NEWS_ENGINE_ID"
        })

        # Second search instance for documentation
        self.add_skill("web_search", {
            "tool_name": "search_docs",
            "api_key": "YOUR_API_KEY",
            "search_engine_id": "DOCS_ENGINE_ID"
        })

        self.prompt_add_section(
            "Role",
            "You can search news and documentation separately."
        )
```

### SWAIG Fields

Add extra SWAIG metadata to skill functions:

```python
self.add_skill("datetime", {
    "swaig_fields": {
        "fillers": {
            "en-US": ["Let me check the time..."]
        }
    }
})
```

### Error Handling

Skills may fail to load:

```python
try:
    agent.add_skill("web_search", {
        "api_key": "invalid"
    })
except ValueError as e:
    print(f"Skill failed to load: {e}")
```

Common errors:

| Error | Cause | Solution |
|-------|-------|----------|
| Skill not found | Invalid skill name | Check spelling |
| Missing parameters | Required config not provided | Add required params |
| Package not installed | Missing Python dependency | Install with pip |
| Env var missing | Required environment variable | Set the variable |

### Skills with Environment Variables

Some skills read from environment variables:

```python
import os

## Set API key via environment
os.environ["GOOGLE_SEARCH_API_KEY"] = "your-key"

## Skill can read from env
self.add_skill("web_search", {
    "api_key": os.environ["GOOGLE_SEARCH_API_KEY"],
    "search_engine_id": "your-engine-id"
})
```

### Complete Example

```python
#!/usr/bin/env python3
## full_featured_agent.py - Agent with multiple configured skills
from signalwire_agents import AgentBase


class FullFeaturedAgent(AgentBase):
    def __init__(self):
        super().__init__(name="full-featured")
        self.add_language("English", "en-US", "rime.spore")

        # Simple skills (no config needed)
        self.add_skill("datetime")
        self.add_skill("math")

        self.prompt_add_section(
            "Role",
            "You are a versatile assistant named Alex."
        )

        self.prompt_add_section(
            "Capabilities",
            body="You can help with:",
            bullets=[
                "Current date and time",
                "Math calculations"
            ]
        )


if __name__ == "__main__":
    agent = FullFeaturedAgent()
    agent.run()
```

> **Note**: Skills like `web_search` and `joke` require additional configuration or API keys. See the [Built-in Skills](05_02_builtin-skills.md) section for details on each skill's requirements.

### Best Practices

**DO:**
- Add skills in __init__ before prompt configuration
- Use environment variables for API keys
- Check skill availability with has_skill() if conditional
- Update prompts to mention skill capabilities

**DON'T:**
- Hardcode API keys in source code
- Add duplicate skills (unless multi-instance)
- Assume skills are available without checking
- Forget to handle skill loading errors



---

## Custom Skills

> **Summary**: Create your own skills by inheriting from `SkillBase`. Custom skills can be reused across agents and shared with others.

### Skill Structure

Create a directory with these files:

```
my_custom_skill/
     __init__.py          # Empty or exports
     skill.py             # Skill implementation
     requirements.txt     # Optional dependencies
```

### Basic Custom Skill

```python
## my_custom_skill/skill.py

from typing import List, Dict, Any
from signalwire_agents.core.skill_base import SkillBase
from signalwire_agents.core.function_result import SwaigFunctionResult


class GreetingSkill(SkillBase):
    """A skill that provides personalized greetings"""

    # Required class attributes
    SKILL_NAME = "greeting"
    SKILL_DESCRIPTION = "Provides personalized greetings"
    SKILL_VERSION = "1.0.0"

    # Optional requirements
    REQUIRED_PACKAGES = []
    REQUIRED_ENV_VARS = []

    def setup(self) -> bool:
        """Initialize the skill. Return True if successful."""
        # Get configuration parameter with default
        self.greeting_style = self.params.get("style", "friendly")
        return True

    def register_tools(self) -> None:
        """Register SWAIG tools with the agent."""
        self.define_tool(
            name="greet_user",
            description="Generate a personalized greeting",
            parameters={
                "name": {
                    "type": "string",
                    "description": "Name of the person to greet"
                }
            },
            handler=self.greet_handler
        )

    def greet_handler(self, args, raw_data):
        """Handle greeting requests."""
        name = args.get("name", "friend")

        if self.greeting_style == "formal":
            greeting = f"Good day, {name}. How may I assist you?"
        else:
            greeting = f"Hey {name}! Great to hear from you!"

        return SwaigFunctionResult(greeting)
```

### Required Class Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `SKILL_NAME` | `str` | Unique identifier for the skill |
| `SKILL_DESCRIPTION` | `str` | Human-readable description |
| `SKILL_VERSION` | `str` | Semantic version (default: "1.0.0") |

**Optional Attributes:**

| Attribute | Type | Description |
|-----------|------|-------------|
| `REQUIRED_PACKAGES` | `List[str]` | Python packages needed |
| `REQUIRED_ENV_VARS` | `List[str]` | Environment variables needed |
| `SUPPORTS_MULTIPLE` | `bool` | Allow multiple instances |

### Required Methods

#### setup()

Initialize the skill and validate requirements:

```python
def setup(self) -> bool:
    """
    Initialize the skill.

    Returns:
        True if setup successful, False otherwise
    """
    # Validate packages are installed
    if not self.validate_packages():
        return False

    # Validate environment variables
    if not self.validate_env_vars():
        return False

    # Initialize from parameters
    self.api_url = self.params.get("api_url", "https://api.example.com")
    self.timeout = self.params.get("timeout", 30)

    # Any other initialization
    return True
```

#### register_tools()

Register SWAIG functions:

```python
def register_tools(self) -> None:
    """Register all tools this skill provides."""

    self.define_tool(
        name="my_function",
        description="Does something useful",
        parameters={
            "param1": {
                "type": "string",
                "description": "First parameter"
            },
            "param2": {
                "type": "integer",
                "description": "Second parameter"
            }
        },
        handler=self.my_handler
    )

    # Register multiple tools if needed
    self.define_tool(
        name="another_function",
        description="Does something else",
        parameters={},
        handler=self.another_handler
    )
```

### Optional Methods

#### get_hints()

Provide speech recognition hints:

```python
def get_hints(self) -> List[str]:
    """Return words to improve speech recognition."""
    return ["greeting", "hello", "hi", "welcome"]
```

#### get_prompt_sections()

Add sections to the agent's prompt:

```python
def get_prompt_sections(self) -> List[Dict[str, Any]]:
    """Return prompt sections for the agent."""
    return [
        {
            "title": "Greeting Capability",
            "body": "You can greet users by name.",
            "bullets": [
                "Use greet_user when someone introduces themselves",
                "Match the greeting style to the conversation tone"
            ]
        }
    ]
```

#### get_global_data()

Provide data for the agent's global context:

```python
def get_global_data(self) -> Dict[str, Any]:
    """Return data to add to global context."""
    return {
        "greeting_skill_enabled": True,
        "greeting_style": self.greeting_style
    }
```

#### cleanup()

Release resources when skill is unloaded:

```python
def cleanup(self) -> None:
    """Clean up when skill is removed."""
    # Close connections, release resources
    if hasattr(self, "connection"):
        self.connection.close()
```

### Parameter Schema

Define parameters your skill accepts:

```python
@classmethod
def get_parameter_schema(cls) -> Dict[str, Dict[str, Any]]:
    """Define the parameters this skill accepts."""
    # Start with base schema
    schema = super().get_parameter_schema()

    # Add skill-specific parameters
    schema.update({
        "style": {
            "type": "string",
            "description": "Greeting style",
            "default": "friendly",
            "enum": ["friendly", "formal", "casual"],
            "required": False
        },
        "api_key": {
            "type": "string",
            "description": "API key for external service",
            "required": True,
            "hidden": True,
            "env_var": "MY_SKILL_API_KEY"
        }
    })

    return schema
```

### Multi-Instance Skills

Support multiple instances with different configurations:

```python
class MultiInstanceSkill(SkillBase):
    SKILL_NAME = "multi_search"
    SKILL_DESCRIPTION = "Searchable with multiple instances"
    SKILL_VERSION = "1.0.0"

    # Enable multiple instances
    SUPPORTS_MULTIPLE_INSTANCES = True

    def get_instance_key(self) -> str:
        """Return unique key for this instance."""
        tool_name = self.params.get("tool_name", self.SKILL_NAME)
        return f"{self.SKILL_NAME}_{tool_name}"

    def setup(self) -> bool:
        self.tool_name = self.params.get("tool_name", "search")
        return True

    def register_tools(self) -> None:
        # Use custom tool name
        self.define_tool(
            name=self.tool_name,
            description="Search function",
            parameters={
                "query": {"type": "string", "description": "Search query"}
            },
            handler=self.search_handler
        )
```

### Complete Example

```python
#!/usr/bin/env python3
## product_search_skill.py - Custom skill for product search
from typing import List, Dict, Any
import requests

from signalwire_agents.core.skill_base import SkillBase
from signalwire_agents.core.function_result import SwaigFunctionResult


class ProductSearchSkill(SkillBase):
    """Search product catalog"""

    SKILL_NAME = "product_search"
    SKILL_DESCRIPTION = "Search and lookup products in catalog"
    SKILL_VERSION = "1.0.0"
    REQUIRED_PACKAGES = ["requests"]
    REQUIRED_ENV_VARS = []
    SUPPORTS_MULTIPLE_INSTANCES = False

    def setup(self) -> bool:
        if not self.validate_packages():
            return False

        self.api_url = self.params.get("api_url")
        self.api_key = self.params.get("api_key")

        if not self.api_url or not self.api_key:
            self.logger.error("api_url and api_key are required")
            return False

        return True

    def register_tools(self) -> None:
        self.define_tool(
            name="search_products",
            description="Search for products by name or category",
            parameters={
                "query": {
                    "type": "string",
                    "description": "Search term"
                },
                "category": {
                    "type": "string",
                    "description": "Product category filter",
                    "enum": ["electronics", "clothing", "home", "all"]
                }
            },
            handler=self.search_handler
        )

        self.define_tool(
            name="get_product_details",
            description="Get details for a specific product",
            parameters={
                "product_id": {
                    "type": "string",
                    "description": "Product ID"
                }
            },
            handler=self.details_handler
        )

    def search_handler(self, args, raw_data):
        query = args.get("query", "")
        category = args.get("category", "all")

        try:
            response = requests.get(
                f"{self.api_url}/search",
                params={"q": query, "cat": category},
                headers={"Authorization": f"Bearer {self.api_key}"},
                timeout=10
            )
            response.raise_for_status()
            data = response.json()

            products = data.get("products", [])
            if not products:
                return SwaigFunctionResult(f"No products found for '{query}'")

            result = f"Found {len(products)} products:\n"
            for p in products[:5]:
                result += f"- {p['name']} (${p['price']})\n"

            return SwaigFunctionResult(result)

        except Exception as e:
            self.logger.error(f"Search failed: {e}")
            return SwaigFunctionResult("Product search is temporarily unavailable")

    def details_handler(self, args, raw_data):
        product_id = args.get("product_id")

        try:
            response = requests.get(
                f"{self.api_url}/products/{product_id}",
                headers={"Authorization": f"Bearer {self.api_key}"},
                timeout=10
            )
            response.raise_for_status()
            product = response.json()

            return SwaigFunctionResult(
                f"{product['name']}: {product['description']}. "
                f"Price: ${product['price']}. In stock: {product['stock']}"
            )

        except Exception as e:
            self.logger.error(f"Details lookup failed: {e}")
            return SwaigFunctionResult("Could not retrieve product details")

    def get_hints(self) -> List[str]:
        return ["product", "search", "find", "lookup", "catalog"]

    def get_prompt_sections(self) -> List[Dict[str, Any]]:
        return [
            {
                "title": "Product Search",
                "body": "You can search the product catalog.",
                "bullets": [
                    "Use search_products to find products",
                    "Use get_product_details for specific items"
                ]
            }
        ]

    @classmethod
    def get_parameter_schema(cls) -> Dict[str, Dict[str, Any]]:
        schema = super().get_parameter_schema()
        schema.update({
            "api_url": {
                "type": "string",
                "description": "Product catalog API URL",
                "required": True
            },
            "api_key": {
                "type": "string",
                "description": "API authentication key",
                "required": True,
                "hidden": True
            }
        })
        return schema
```

### Using Custom Skills

Register the skill directory:

```python
from signalwire_agents.skills.registry import skill_registry

## Add your skills directory
skill_registry.add_skill_directory("/path/to/my_skills")

## Now use in agent
class MyAgent(AgentBase):
    def __init__(self):
        super().__init__(name="my-agent")
        self.add_language("English", "en-US", "rime.spore")

        self.add_skill("product_search", {
            "api_url": "https://api.mystore.com",
            "api_key": "secret"
        })
```



---

## Skill Configuration

> **Summary**: Configure skills with parameters, environment variables, and SWAIG field overrides. Understand the parameter schema and discovery options.

### Configuration Methods

| Method | Description |
|--------|-------------|
| Parameters dict | Pass config when calling `add_skill()` |
| Environment variables | Set via OS environment |
| SWAIG fields | Customize tool metadata |
| External directories | Register custom skill paths |

### Parameter Dictionary

Pass configuration when adding a skill:

```python
self.add_skill("web_search", {
    "api_key": "your-api-key",
    "search_engine_id": "your-engine-id",
    "num_results": 5,
    "min_quality_score": 0.4
})
```

### Parameter Schema

Skills define their parameters via `get_parameter_schema()`:

```python
{
    "api_key": {
        "type": "string",
        "description": "Google API key",
        "required": True,
        "hidden": True,
        "env_var": "GOOGLE_API_KEY"
    },
    "num_results": {
        "type": "integer",
        "description": "Number of results",
        "default": 3,
        "min": 1,
        "max": 10
    },
    "style": {
        "type": "string",
        "description": "Output style",
        "enum": ["brief", "detailed"],
        "default": "brief"
    }
}
```

### Parameter Properties

| Property | Type | Description |
|----------|------|-------------|
| `type` | string | Data type: string, integer, number, boolean, object, array |
| `description` | string | Human-readable description |
| `default` | any | Default value if not provided |
| `required` | bool | Whether parameter is required |
| `hidden` | bool | Hide in UIs (for secrets) |
| `env_var` | string | Environment variable source |
| `enum` | array | Allowed values |
| `min`/`max` | number | Value range for numbers |

### Environment Variables

Skills can read from environment variables:

```python
import os

## Set environment variable
os.environ["GOOGLE_API_KEY"] = "your-key"

## Skill reads from params or falls back to env
self.add_skill("web_search", {
    "api_key": os.getenv("GOOGLE_API_KEY"),
    "search_engine_id": os.getenv("SEARCH_ENGINE_ID")
})
```

### SWAIG Fields

Override SWAIG function metadata for skill tools:

```python
self.add_skill("datetime", {
    "swaig_fields": {
        # Add filler phrases while function executes
        "fillers": {
            "en-US": [
                "Let me check the time...",
                "One moment..."
            ]
        },
        # Disable security for testing
        "secure": False
    }
})
```

Available SWAIG fields:

| Field | Description |
|-------|-------------|
| `fillers` | Language-specific filler phrases |
| `secure` | Enable/disable token validation |
| `webhook_url` | Override webhook URL |

### External Skill Directories

Register custom skill directories:

```python
from signalwire_agents.skills.registry import skill_registry

## Add directory at runtime
skill_registry.add_skill_directory("/opt/custom_skills")

## Environment variable (colon-separated paths)
## SIGNALWIRE_SKILL_PATHS=/path1:/path2:/path3
```

### Entry Points

Install skills via pip packages:

```python
## In setup.py
setup(
    name="my-skills-package",
    entry_points={
        "signalwire_agents.skills": [
            "weather = my_package.skills:WeatherSkill",
            "stock = my_package.skills:StockSkill"
        ]
    }
)
```

### Listing Available Skills

```python
from signalwire_agents.skills.registry import skill_registry

## List all available skills
skills = skill_registry.list_skills()
for skill in skills:
    print(f"{skill['name']}: {skill['description']}")

## Get complete schema for all skills
schema = skill_registry.get_all_skills_schema()
print(schema)
```

### Multi-Instance Configuration

Skills supporting multiple instances need unique tool names:

```python
## Instance 1: News search
self.add_skill("web_search", {
    "tool_name": "search_news",      # Unique function name
    "api_key": "KEY",
    "search_engine_id": "NEWS_ENGINE"
})

## Instance 2: Documentation search
self.add_skill("web_search", {
    "tool_name": "search_docs",      # Different function name
    "api_key": "KEY",
    "search_engine_id": "DOCS_ENGINE"
})
```

### Configuration Validation

Skills validate configuration in `setup()`:

```diagram
┌─────────────────────────────────────────────────────────────────────────────┐
│                      Validation Flow                                        │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  1. add_skill() called with params                                          │
│              │                                                              │
│              ▼                                                              │
│  2. Skill instantiated                                                      │
│     • params stored in self.params                                          │
│     • swaig_fields extracted                                                │
│              │                                                              │
│              ▼                                                              │
│  3. setup() called                                                          │
│     • validate_packages() - check Python packages                           │
│     • validate_env_vars() - check environment                               │
│     • Custom validation                                                     │
│              │                                                              │
│              ▼                                                              │
│  4. Success: register_tools() called                                        │
│     Failure: ValueError raised                                              │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Complete Configuration Example

```python
from signalwire_agents import AgentBase
from signalwire_agents.skills.registry import skill_registry
import os


## Register external skills
skill_registry.add_skill_directory("/opt/my_company/skills")


class ConfiguredAgent(AgentBase):
    def __init__(self):
        super().__init__(name="configured-agent")
        self.add_language("English", "en-US", "rime.spore")

        # Simple skill - no config
        self.add_skill("datetime")

        # Skill with parameters
        self.add_skill("web_search", {
            "api_key": os.getenv("GOOGLE_API_KEY"),
            "search_engine_id": os.getenv("SEARCH_ENGINE_ID"),
            "num_results": 5,
            "min_quality_score": 0.4
        })

        # Skill with SWAIG field overrides
        self.add_skill("math", {
            "swaig_fields": {
                "fillers": {
                    "en-US": ["Calculating..."]
                }
            }
        })

        # Multi-instance skill
        self.add_skill("native_vector_search", {
            "tool_name": "search_products",
            "index_path": "/data/products.swsearch"
        })

        self.add_skill("native_vector_search", {
            "tool_name": "search_faqs",
            "index_path": "/data/faqs.swsearch"
        })

        self.prompt_add_section(
            "Role",
            "You are a customer service agent."
        )


if __name__ == "__main__":
    agent = ConfiguredAgent()
    agent.run()
```

### Configuration Best Practices

#### Security
- Store API keys in environment variables
- Never commit secrets to version control
- Use hidden: true for sensitive parameters

#### Organization
- Group related configuration
- Use descriptive tool_name for multi-instance
- Document required configuration

#### Validation
- Check has_skill() before using conditionally
- Handle ValueError from add_skill()
- Validate parameters early in setup()

### Next Steps

You've learned the complete skills system. Next, explore advanced topics like contexts, workflows, and state management.



# Part: Advanced Topics

---

# Advanced Features

> **Summary**: This chapter covers advanced SDK features including multi-step workflows with contexts, state management, call recording, call transfers, multi-agent servers, and knowledge search integration.

## What You'll Learn

This chapter covers advanced capabilities:

1. **Contexts & Workflows** - Multi-step conversation flows with branching logic
2. **State Management** - Session data, global state, and metadata handling
3. **Call Recording** - Record calls with various formats and options
4. **Call Transfer** - Transfer calls to other destinations
5. **Multi-Agent Servers** - Run multiple agents on a single server
6. **Search & Knowledge** - Vector search for RAG-style knowledge integration

## Feature Overview

### Contexts & Workflows
- Multi-step conversations
- Branching logic
- Context switching
- Step validation

### State Management
- global_data dictionary
- metadata per call
- Tool-specific tokens
- Post-prompt data injection

### Call Recording
- Stereo/mono recording
- Multiple formats (mp3, wav, mp4 for video)
- Pause/resume control
- Transcription support

### Call Transfer
- Blind transfers
- Announced transfers
- SIP destinations
- PSTN destinations

### Multi-Agent Servers
- Multiple agents per server
- Path-based routing
- SIP username routing
- Shared configuration

### Search & Knowledge
- Vector similarity search
- SQLite/pgvector backends
- Document processing
- RAG integration

## When to Use These Features

| Feature | Use Case |
|---------|----------|
| Contexts | Multi-step forms, wizards, guided flows |
| State Management | Persisting data across function calls |
| Call Recording | Compliance, training, quality assurance |
| Call Transfer | Escalation, routing to humans |
| Multi-Agent | Different agents for different purposes |
| Search | Knowledge bases, FAQ lookup, documentation |

## Prerequisites

Before diving into advanced features:

- Understand basic agent creation (Chapter 3)
- Know how SWAIG functions work (Chapter 4)
- Be comfortable with skills (Chapter 5)

## Chapter Contents

| Section | Description |
|---------|-------------|
| [Contexts & Workflows](06_01_contexts-workflows.md) | Build multi-step conversation flows |
| [State Management](06_02_state-management.md) | Manage session and call state |
| [Call Recording](06_03_call-recording.md) | Record calls with various options |
| [Call Transfer](06_04_call-transfer.md) | Transfer calls to destinations |
| [Multi-Agent](06_05_multi-agent.md) | Run multiple agents on one server |
| [Search & Knowledge](06_06_search-knowledge.md) | Vector search integration |

## When to Use Contexts

| Regular Prompts | Contexts |
|-----------------|----------|
| Free-form conversations | Structured workflows |
| Simple Q&A agents | Multi-step data collection |
| Single-purpose tasks | Wizard-style flows |
| No defined sequence | Branching conversations |
| | Multiple personas |

**Use contexts when you need:**
- Guaranteed step completion
- Controlled navigation
- Step-specific function access
- Context-dependent personas
- Department transfers
- Isolated conversation segments

## Context Architecture

```diagram
┌─────────────────────────────────────────────────────────────────────────────┐
│                        Context Structure                                    │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  ┌─────────────────────────────────────────────────────────────────────┐    │
│  │                         ContextBuilder                              │    │
│  │  ┌─────────────────────────────────────────────────────────────┐    │    │
│  │  │                      Context "sales"                        │    │    │
│  │  │  ┌────────────┐ ┌────────────┐ ┌────────────┐               │    │    │
│  │  │  │  Step 1    │→│  Step 2    │→│  Step 3    │               │    │    │
│  │  │  │ get_info   │ │ confirm    │ │ process    │               │    │    │
│  │  │  └────────────┘ └────────────┘ └────────────┘               │    │    │
│  │  └─────────────────────────────────────────────────────────────┘    │    │
│  │                              ↕                                      │    │
│  │  ┌─────────────────────────────────────────────────────────────┐    │    │
│  │  │                    Context "support"                        │    │    │
│  │  │  ┌────────────┐                                             │    │    │
│  │  │  │  Step 1    │                                             │    │    │
│  │  │  │ help       │                                             │    │    │
│  │  │  └────────────┘                                             │    │    │
│  │  └─────────────────────────────────────────────────────────────┘    │    │
│  └─────────────────────────────────────────────────────────────────────┘    │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

## Basic Context Example

```python
from signalwire_agents import AgentBase


class OrderAgent(AgentBase):
    def __init__(self):
        super().__init__(name="order-agent")
        self.add_language("English", "en-US", "rime.spore")

        # Base prompt (required even with contexts)
        self.prompt_add_section(
            "Role",
            "You help customers place orders."
        )

        # Define contexts after setting base prompt
        contexts = self.define_contexts()

        # Add a context with steps
        order = contexts.add_context("default")

        order.add_step("get_item") \
            .set_text("Ask what item they want to order.") \
            .set_step_criteria("Customer has specified an item") \
            .set_valid_steps(["get_quantity"])

        order.add_step("get_quantity") \
            .set_text("Ask how many they want.") \
            .set_step_criteria("Customer has specified a quantity") \
            .set_valid_steps(["confirm"])

        order.add_step("confirm") \
            .set_text("Confirm the order details and thank them.") \
            .set_step_criteria("Order has been confirmed")


if __name__ == "__main__":
    agent = OrderAgent()
    agent.run()
```

## Step Configuration

### set_text()

Simple text prompt for the step:

```python
step.set_text("What item would you like to order?")
```

### add_section() / add_bullets()

POM-style structured prompts:

```python
step.add_section("Task", "Collect customer information") \
    .add_bullets("Required Information", [
        "Full name",
        "Phone number",
        "Email address"
    ])
```

### set_step_criteria()

Define when the step is complete:

```python
step.set_step_criteria("Customer has provided their full name and phone number")
```

### set_valid_steps()

Control step navigation:

```python
# Can go to specific steps
step.set_valid_steps(["confirm", "cancel"])

# Use "next" for sequential flow
step.set_valid_steps(["next"])
```

### set_functions()

Restrict available functions per step:

```python
# Disable all functions
step.set_functions("none")

# Allow specific functions only
step.set_functions(["check_inventory", "get_price"])
```

### set_valid_contexts()

Allow navigation to other contexts:

```python
step.set_valid_contexts(["support", "manager"])
```

## Context Configuration

### set_isolated()

Truncate conversation history when entering:

```python
context.set_isolated(True)
```

### set_system_prompt()

New system prompt when entering context:

```python
context.set_system_prompt("You are now a technical support specialist.")
```

### set_user_prompt()

Inject a user message when entering:

```python
context.set_user_prompt("I need help with a technical issue.")
```

### set_consolidate()

Summarize previous conversation when switching:

```python
context.set_consolidate(True)
```

### set_full_reset()

Completely reset conversation state:

```python
context.set_full_reset(True)
```

### add_enter_filler() / add_exit_filler()

Add transition phrases:

```python
context.add_enter_filler("en-US", [
    "Let me connect you with our support team...",
    "Transferring you to a specialist..."
])

context.add_exit_filler("en-US", [
    "Returning you to the main menu...",
    "Back to the sales department..."
])
```

## Multi-Context Example

```python
from signalwire_agents import AgentBase


class MultiDepartmentAgent(AgentBase):
    def __init__(self):
        super().__init__(name="multi-dept-agent")
        self.add_language("English-Sales", "en-US", "rime.spore")
        self.add_language("English-Support", "en-US", "rime.cove")
        self.add_language("English-Manager", "en-US", "rime.marsh")

        self.prompt_add_section(
            "Instructions",
            "Guide customers through sales or transfer to appropriate departments."
        )

        contexts = self.define_contexts()

        # Sales context
        sales = contexts.add_context("sales") \
            .set_isolated(True) \
            .add_section("Role", "You are Alex, a sales representative.")

        sales.add_step("qualify") \
            .add_section("Task", "Determine customer needs") \
            .set_step_criteria("Customer needs are understood") \
            .set_valid_steps(["recommend"]) \
            .set_valid_contexts(["support", "manager"])

        sales.add_step("recommend") \
            .add_section("Task", "Make product recommendations") \
            .set_step_criteria("Recommendation provided") \
            .set_valid_contexts(["support", "manager"])

        # Support context
        support = contexts.add_context("support") \
            .set_isolated(True) \
            .add_section("Role", "You are Sam, technical support.") \
            .add_enter_filler("en-US", [
                "Connecting you with technical support...",
                "Let me transfer you to our tech team..."
            ])

        support.add_step("assist") \
            .add_section("Task", "Help with technical questions") \
            .set_step_criteria("Technical issue resolved") \
            .set_valid_contexts(["sales", "manager"])

        # Manager context
        manager = contexts.add_context("manager") \
            .set_isolated(True) \
            .add_section("Role", "You are Morgan, the store manager.") \
            .add_enter_filler("en-US", [
                "Let me get the manager for you...",
                "One moment, connecting you with management..."
            ])

        manager.add_step("escalate") \
            .add_section("Task", "Handle escalated issues") \
            .set_step_criteria("Issue resolved by manager") \
            .set_valid_contexts(["sales", "support"])


if __name__ == "__main__":
    agent = MultiDepartmentAgent()
    agent.run()
```

## Navigation Flow

### Within Context (Steps)
- `set_valid_steps(["next"])` - Go to next sequential step
- `set_valid_steps(["step_name"])` - Go to specific step
- `set_valid_steps(["a", "b"])` - Multiple options

### Between Contexts
- `set_valid_contexts(["other_context"])` - Allow context switch
- AI calls `change_context("context_name")` automatically
- Enter/exit fillers provide smooth transitions

### Context Entry Behavior
- `isolated=True` - Clear conversation history
- `consolidate=True` - Summarize previous conversation
- `full_reset=True` - Complete prompt replacement

## Validation Rules

The ContextBuilder validates your configuration:

- Single context must be named "default"
- Every context must have at least one step
- `valid_steps` must reference existing steps (or "next")
- `valid_contexts` must reference existing contexts
- Cannot mix `set_text()` with `add_section()` on same step
- Cannot mix `set_prompt()` with `add_section()` on same context

## Step and Context Methods Summary

| Method | Level | Purpose |
|--------|-------|---------|
| `set_text()` | Step | Simple text prompt |
| `add_section()` | Both | POM-style section |
| `add_bullets()` | Both | Bulleted list section |
| `set_step_criteria()` | Step | Completion criteria |
| `set_functions()` | Step | Restrict available functions |
| `set_valid_steps()` | Step | Allowed step navigation |
| `set_valid_contexts()` | Both | Allowed context navigation |
| `set_isolated()` | Context | Clear history on entry |
| `set_consolidate()` | Context | Summarize on entry |
| `set_full_reset()` | Context | Complete reset on entry |
| `set_system_prompt()` | Context | New system prompt |
| `set_user_prompt()` | Context | Inject user message |
| `add_enter_filler()` | Context | Entry transition phrases |
| `add_exit_filler()` | Context | Exit transition phrases |

## Best Practices

**DO:**
- Set clear step_criteria for each step
- Use isolated=True for persona changes
- Add enter_fillers for smooth transitions
- Define valid_contexts to enable department transfers
- Test navigation paths thoroughly

**DON'T:**
- Create circular navigation without exit paths
- Skip setting a base prompt before define_contexts()
- Mix set_text() with add_section() on the same step
- Forget to validate step/context references


---

## State Management

> **Summary**: Manage data throughout call sessions using global_data for persistent state, metadata for function-scoped data, and post_prompt for call summaries.

### State Types Overview

| State Type | Scope | Key Features |
|------------|-------|--------------|
| **global_data** | Entire session | Persists entire session, available to all functions, accessible in prompts, set at init or runtime |
| **metadata** | Function-scoped | Scoped to function's token, private to specific function, isolated per `meta_data_token`, set via function results |
| **post_prompt** | After call | Executes after call ends, generates summaries, extracts structured data, webhook delivery |
| **call_info** | Read-only | Read-only call metadata, caller ID, call ID, available in `raw_data`, SignalWire-provided |

### Global Data

Global data persists throughout the entire call session and is available to all functions and prompts.

#### Setting Initial Global Data

```python
from signalwire_agents import AgentBase


class CustomerAgent(AgentBase):
    def __init__(self):
        super().__init__(name="customer-agent")
        self.add_language("English", "en-US", "rime.spore")

        # Set initial global data at agent creation
        self.set_global_data({
            "business_name": "Acme Corp",
            "support_hours": "9 AM - 5 PM EST",
            "current_promo": "20% off first order"
        })

        self.prompt_add_section(
            "Role",
            "You are a customer service agent for ${global_data.business_name}."
        )


if __name__ == "__main__":
    agent = CustomerAgent()
    agent.run()
```

#### Updating Global Data at Runtime

```python
self.update_global_data({
    "customer_tier": "premium",
    "account_balance": 150.00
})
```

#### Updating Global Data from Functions

```python
from signalwire_agents import AgentBase
from signalwire_agents.core.function_result import SwaigFunctionResult


class StateAgent(AgentBase):
    def __init__(self):
        super().__init__(name="state-agent")
        self.add_language("English", "en-US", "rime.spore")

        self.define_tool(
            name="set_customer_name",
            description="Store the customer's name",
            parameters={
                "type": "object",
                "properties": {
                    "name": {"type": "string", "description": "Customer name"}
                },
                "required": ["name"]
            },
            handler=self.set_customer_name
        )

    def set_customer_name(self, args, raw_data):
        name = args.get("name", "")

        return (
            SwaigFunctionResult(f"Stored name: {name}")
            .update_global_data({"customer_name": name})
        )


if __name__ == "__main__":
    agent = StateAgent()
    agent.run()
```

#### Accessing Global Data in Prompts

Use `${global_data.key}` syntax in prompts:

```python
self.prompt_add_section(
    "Customer Info",
    """
    Customer Name: ${global_data.customer_name}
    Account Tier: ${global_data.customer_tier}
    Current Balance: ${global_data.account_balance}
    """
)
```

### Metadata

Metadata is scoped to a specific function's `meta_data_token`, providing isolated storage per function.

#### Setting Metadata

```python
def process_order(self, args, raw_data):
    order_id = create_order()

    return (
        SwaigFunctionResult(f"Created order {order_id}")
        .set_metadata({"order_id": order_id, "status": "pending"})
    )
```

#### Removing Metadata

```python
def cancel_order(self, args, raw_data):
    return (
        SwaigFunctionResult("Order cancelled")
        .remove_metadata(["order_id", "status"])
    )
```

### Post-Prompt Data

The post-prompt runs after the call ends and generates structured data from the conversation.

#### Setting Post-Prompt

```python
from signalwire_agents import AgentBase


class SurveyAgent(AgentBase):
    def __init__(self):
        super().__init__(name="survey-agent")
        self.add_language("English", "en-US", "rime.spore")

        self.prompt_add_section(
            "Role",
            "Conduct a customer satisfaction survey."
        )

        # Post-prompt extracts structured data after call
        self.set_post_prompt("""
            Summarize the survey results as JSON:
            {
                "satisfaction_score": <1-10>,
                "main_feedback": "<summary>",
                "would_recommend": <true/false>,
                "issues_mentioned": ["<issue1>", "<issue2>"]
            }
        """)

        # Optionally set where to send the data
        self.set_post_prompt_url("https://example.com/survey-results")


if __name__ == "__main__":
    agent = SurveyAgent()
    agent.run()
```

#### Post-Prompt LLM Parameters

Configure a different model for post-prompt processing:

```python
self.set_post_prompt_llm_params(
    model="gpt-4o-mini",
    temperature=0.3  # Lower for consistent extraction
)
```

### Accessing Call Information

The `raw_data` parameter contains call metadata:

```python
def my_handler(self, args, raw_data):
    # Available call information
    call_id = raw_data.get("call_id")
    caller_id_number = raw_data.get("caller_id_number")
    caller_id_name = raw_data.get("caller_id_name")
    call_direction = raw_data.get("call_direction")  # "inbound" or "outbound"

    # Current AI interaction state
    ai_session_id = raw_data.get("ai_session_id")

    self.log.info(f"Call from {caller_id_number}")

    return SwaigFunctionResult("Processing...")
```

### State Flow Diagram

```diagram
┌─────────────────────────────────────────────────────────────────────────────┐
│                        State Flow                                           │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  Call Start                                                                 │
│      │                                                                      │
│      ▼                                                                      │
│  ┌─────────────────────┐                                                    │
│  │  set_global_data()  │  Initial state from agent config                   │
│  └─────────────────────┘                                                    │
│      │                                                                      │
│      ▼                                                                      │
│  ┌─────────────────────┐                                                    │
│  │  Conversation       │  AI uses ${global_data.key} in prompts             │
│  └─────────────────────┘                                                    │
│      │                                                                      │
│      ▼                                                                      │
│  ┌─────────────────────┐                                                    │
│  │  Function Call      │  Handler receives raw_data with call info          │
│  └─────────────────────┘                                                    │
│      │                                                                      │
│      ▼                                                                      │
│  ┌─────────────────────────────────────────────────────────┐                │
│  │  SwaigFunctionResult                                    │                │
│  │    .update_global_data()  → Updates session state       │                │
│  │    .set_metadata()        → Updates function-scoped     │                │
│  └─────────────────────────────────────────────────────────┘                │
│      │                                                                      │
│      ▼                                                                      │
│  ┌─────────────────────┐                                                    │
│  │  Call Ends          │                                                    │
│  └─────────────────────┘                                                    │
│      │                                                                      │
│      ▼                                                                      │
│  ┌─────────────────────┐                                                    │
│  │  Post-Prompt        │  Extracts structured data from conversation        │
│  └─────────────────────┘                                                    │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Complete Example

```python
#!/usr/bin/env python3
## order_agent.py - Order management with state
from signalwire_agents import AgentBase
from signalwire_agents.core.function_result import SwaigFunctionResult


class OrderAgent(AgentBase):
    def __init__(self):
        super().__init__(name="order-agent")
        self.add_language("English", "en-US", "rime.spore")

        # Initial global state
        self.set_global_data({
            "store_name": "Pizza Palace",
            "order_items": [],
            "order_total": 0.0
        })

        self.prompt_add_section(
            "Role",
            "You are an order assistant for ${global_data.store_name}. "
            "Help customers place their order."
        )

        self.prompt_add_section(
            "Current Order",
            "Items: ${global_data.order_items}\n"
            "Total: $${global_data.order_total}"
        )

        # Post-prompt for order summary
        self.set_post_prompt("""
            Extract the final order as JSON:
            {
                "items": [{"name": "", "quantity": 0, "price": 0.00}],
                "total": 0.00,
                "customer_name": "",
                "special_instructions": ""
            }
        """)

        self._register_functions()

    def _register_functions(self):
        self.define_tool(
            name="add_item",
            description="Add an item to the order",
            parameters={
                "type": "object",
                "properties": {
                    "item": {"type": "string", "description": "Item name"},
                    "price": {"type": "number", "description": "Item price"}
                },
                "required": ["item", "price"]
            },
            handler=self.add_item
        )

    def add_item(self, args, raw_data):
        item = args.get("item")
        price = args.get("price", 0.0)

        # Note: In real implementation, maintain state server-side
        # This example shows the pattern
        return (
            SwaigFunctionResult(f"Added {item} (${price}) to your order")
            .update_global_data({
                "last_item_added": item,
                "last_item_price": price
            })
        )


if __name__ == "__main__":
    agent = OrderAgent()
    agent.run()
```

### DataMap Variable Access

In DataMap functions, use variable substitution:

```python
from signalwire_agents.core.data_map import DataMap
from signalwire_agents.core.function_result import SwaigFunctionResult

lookup_dm = (
    DataMap("lookup_customer")
    .description("Look up customer by ID")
    .parameter("customer_id", "string", "Customer ID", required=True)
    .webhook(
        "GET",
        "https://api.example.com/customers/${enc:args.customer_id}"
        "?store=${enc:global_data.store_id}"
    )
    .output(SwaigFunctionResult(
        "Customer: ${response.name}, Tier: ${response.tier}"
    ))
)
```

### State Methods Summary

| Method | Scope | Purpose |
|--------|-------|---------|
| `set_global_data()` | Agent | Set initial global state |
| `update_global_data()` | Agent | Update global state at runtime |
| `SwaigFunctionResult.update_global_data()` | Function | Update state from function |
| `SwaigFunctionResult.set_metadata()` | Function | Set function-scoped data |
| `SwaigFunctionResult.remove_metadata()` | Function | Remove function-scoped data |
| `set_post_prompt()` | Agent | Set post-call data extraction |
| `set_post_prompt_url()` | Agent | Set webhook for post-prompt data |
| `set_post_prompt_llm_params()` | Agent | Configure post-prompt model |

### Best Practices

**DO:**
- Use global_data for data needed across functions
- Use metadata for function-specific isolated data
- Set initial state in __init__ for predictable behavior
- Use post_prompt to extract structured call summaries
- Log state changes for debugging

**DON'T:**
- Store sensitive data (passwords, API keys) in global_data
- Rely on global_data for complex state machines (use server-side)
- Assume metadata persists across function boundaries
- Forget that state resets between calls


---

## Call Recording

> **Summary**: Record calls using `record_call()` and `stop_record_call()` methods on SwaigFunctionResult. Supports stereo/mono, multiple formats, and webhook notifications.

### Recording Overview

**`record_call()`**
- Starts background recording
- Continues while conversation proceeds
- Supports stereo (separate channels) or mono
- Output formats: WAV, MP3, or MP4
- Direction: speak only, listen only, or both

**`stop_record_call()`**
- Stops an active recording
- Uses control_id to target specific recording
- Recording is automatically stopped on call end

### Basic Recording

```python
from signalwire_agents import AgentBase
from signalwire_agents.core.function_result import SwaigFunctionResult


class RecordingAgent(AgentBase):
    def __init__(self):
        super().__init__(name="recording-agent")
        self.add_language("English", "en-US", "rime.spore")

        self.prompt_add_section(
            "Role",
            "You are a customer service agent. "
            "Start recording when the customer agrees."
        )

        self.define_tool(
            name="start_recording",
            description="Start recording the call with customer consent",
            parameters={"type": "object", "properties": {}},
            handler=self.start_recording
        )

    def start_recording(self, args, raw_data):
        return (
            SwaigFunctionResult("Recording has started.")
            .record_call(
                control_id="main_recording",
                stereo=True,
                format="wav"
            )
        )


if __name__ == "__main__":
    agent = RecordingAgent()
    agent.run()
```

### Recording Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `control_id` | str | None | Identifier to stop specific recording |
| `stereo` | bool | False | True for separate L/R channels |
| `format` | str | `"wav"` | Output format: "wav", "mp3", or "mp4" |
| `direction` | str | `"both"` | "speak", "listen", or "both" |
| `terminators` | str | None | DTMF digits that stop recording |
| `beep` | bool | False | Play beep before recording |
| `input_sensitivity` | float | `44.0` | Audio sensitivity threshold |
| `initial_timeout` | float | `0.0` | Seconds to wait for speech |
| `end_silence_timeout` | float | `0.0` | Silence duration to auto-stop |
| `max_length` | float | None | Maximum recording seconds |
| `status_url` | str | None | Webhook for recording events |

### Stereo Recording

Record caller and agent on separate channels:

```python
def start_stereo_recording(self, args, raw_data):
    return (
        SwaigFunctionResult("Recording in stereo mode")
        .record_call(
            control_id="stereo_rec",
            stereo=True,  # Caller on left, agent on right
            format="wav"
        )
    )
```

### Direction Options

```python
## Record only what the AI/agent speaks
def record_agent_only(self, args, raw_data):
    return (
        SwaigFunctionResult("Recording agent audio")
        .record_call(direction="speak")
    )

## Record only what the caller says
def record_caller_only(self, args, raw_data):
    return (
        SwaigFunctionResult("Recording caller audio")
        .record_call(direction="listen")
    )

## Record both sides (default)
def record_both(self, args, raw_data):
    return (
        SwaigFunctionResult("Recording full conversation")
        .record_call(direction="both")
    )
```

### Recording with Webhook

Receive notifications when recording completes:

```python
def start_recording_with_callback(self, args, raw_data):
    return (
        SwaigFunctionResult("Recording started")
        .record_call(
            control_id="webhook_rec",
            status_url="https://example.com/recording-complete"
        )
    )
```

The webhook receives recording metadata including the URL to download the file.

### Auto-Stop Recording

Configure automatic stop conditions:

```python
def start_auto_stop_recording(self, args, raw_data):
    return (
        SwaigFunctionResult("Recording with auto-stop")
        .record_call(
            max_length=300.0,        # Stop after 5 minutes
            end_silence_timeout=5.0, # Stop after 5 seconds of silence
            terminators="#"          # Stop if user presses #
        )
    )
```

### Stop Recording

Stop a recording by control_id:

```python
from signalwire_agents import AgentBase
from signalwire_agents.core.function_result import SwaigFunctionResult


class ControlledRecordingAgent(AgentBase):
    def __init__(self):
        super().__init__(name="controlled-recording-agent")
        self.add_language("English", "en-US", "rime.spore")

        self.prompt_add_section(
            "Role",
            "You handle call recordings. You can start and stop recording."
        )

        self._register_functions()

    def _register_functions(self):
        self.define_tool(
            name="start_recording",
            description="Start recording the call",
            parameters={"type": "object", "properties": {}},
            handler=self.start_recording
        )

        self.define_tool(
            name="stop_recording",
            description="Stop recording the call",
            parameters={"type": "object", "properties": {}},
            handler=self.stop_recording
        )

    def start_recording(self, args, raw_data):
        return (
            SwaigFunctionResult("Recording has started")
            .record_call(control_id="main")
        )

    def stop_recording(self, args, raw_data):
        return (
            SwaigFunctionResult("Recording has stopped")
            .stop_record_call(control_id="main")
        )


if __name__ == "__main__":
    agent = ControlledRecordingAgent()
    agent.run()
```

### Recording with Beep

Alert the caller that recording is starting:

```python
def start_recording_with_beep(self, args, raw_data):
    return (
        SwaigFunctionResult("This call will be recorded")
        .record_call(
            beep=True,  # Plays a beep before recording starts
            format="mp3"
        )
    )
```

### Complete Example

```python
#!/usr/bin/env python3
## compliance_agent.py - Agent with recording compliance features
from signalwire_agents import AgentBase
from signalwire_agents.core.function_result import SwaigFunctionResult


class ComplianceAgent(AgentBase):
    """Agent with full recording compliance features"""

    def __init__(self):
        super().__init__(name="compliance-agent")
        self.add_language("English", "en-US", "rime.spore")

        self.prompt_add_section(
            "Role",
            "You are a customer service agent. Before recording, you must "
            "inform the customer and get their verbal consent."
        )

        self.prompt_add_section(
            "Recording Policy",
            """
            1. Always inform customer: "This call may be recorded for quality purposes."
            2. Ask for consent: "Do you agree to the recording?"
            3. Only start recording after explicit "yes" or agreement.
            4. If customer declines, proceed without recording.
            """
        )

        self._register_functions()

    def _register_functions(self):
        self.define_tool(
            name="start_compliant_recording",
            description="Start recording after customer consent is obtained",
            parameters={"type": "object", "properties": {}},
            handler=self.start_compliant_recording
        )

        self.define_tool(
            name="pause_recording",
            description="Pause recording for sensitive information",
            parameters={"type": "object", "properties": {}},
            handler=self.pause_recording
        )

        self.define_tool(
            name="resume_recording",
            description="Resume recording after sensitive section",
            parameters={"type": "object", "properties": {}},
            handler=self.resume_recording
        )

    def start_compliant_recording(self, args, raw_data):
        call_id = raw_data.get("call_id", "unknown")

        return (
            SwaigFunctionResult("Recording has begun. Thank you for your consent.")
            .record_call(
                control_id=f"compliance_{call_id}",
                stereo=True,
                format="wav",
                beep=True,
                status_url="https://example.com/recordings/status"
            )
            .update_global_data({"recording_active": True})
        )

    def pause_recording(self, args, raw_data):
        call_id = raw_data.get("call_id", "unknown")

        return (
            SwaigFunctionResult(
                "Recording paused. You may now provide sensitive information."
            )
            .stop_record_call(control_id=f"compliance_{call_id}")
            .update_global_data({"recording_active": False})
        )

    def resume_recording(self, args, raw_data):
        call_id = raw_data.get("call_id", "unknown")

        return (
            SwaigFunctionResult("Recording resumed.")
            .record_call(
                control_id=f"compliance_{call_id}",
                stereo=True,
                format="wav"
            )
            .update_global_data({"recording_active": True})
        )


if __name__ == "__main__":
    agent = ComplianceAgent()
    agent.run()
```

### Recording Best Practices

#### Compliance
- Always inform callers before recording
- Obtain consent where legally required
- Provide option to decline recording
- Document consent in call logs

#### Technical
- Use control_id for multiple recordings
- Use stereo=True for transcription accuracy
- Use status_url to track recording completion
- Set max_length to prevent oversized files

#### Storage
- Use WAV for quality, MP3 for size, MP4 for video
- Implement retention policies
- Secure storage with encryption


---

## Call Transfer

> **Summary**: Transfer calls to other destinations using `connect()` for phone numbers/SIP and `swml_transfer()` for SWML endpoints. Support for both permanent and temporary transfers.

### Transfer Types

#### Permanent Transfer (`final=True`)
- Call exits the agent completely
- Caller connected directly to destination
- Agent conversation ends
- **Use for:** Handoff to human, transfer to another system

#### Temporary Transfer (`final=False`)
- Call returns to agent when far end hangs up
- Agent can continue conversation after transfer
- **Use for:** Conferencing, brief consultations

### Basic Phone Transfer

```python
from signalwire_agents import AgentBase
from signalwire_agents.core.function_result import SwaigFunctionResult


class TransferAgent(AgentBase):
    def __init__(self):
        super().__init__(name="transfer-agent")
        self.add_language("English", "en-US", "rime.spore")

        self.prompt_add_section(
            "Role",
            "You are a receptionist who can transfer calls to different departments."
        )

        self.define_tool(
            name="transfer_to_sales",
            description="Transfer the caller to the sales department",
            parameters={"type": "object", "properties": {}},
            handler=self.transfer_to_sales
        )

    def transfer_to_sales(self, args, raw_data):
        return (
            SwaigFunctionResult("Transferring you to sales now.")
            .connect("+15551234567", final=True)
        )


if __name__ == "__main__":
    agent = TransferAgent()
    agent.run()
```

### Connect Method Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `destination` | str | required | Phone number, SIP address, or URI |
| `final` | bool | True | Permanent (True) or temporary (False) |
| `from_addr` | str | None | Override caller ID for outbound leg |

### Permanent vs Temporary Transfer

```python
from signalwire_agents import AgentBase
from signalwire_agents.core.function_result import SwaigFunctionResult


class SmartTransferAgent(AgentBase):
    def __init__(self):
        super().__init__(name="smart-transfer-agent")
        self.add_language("English", "en-US", "rime.spore")

        self.prompt_add_section(
            "Role",
            "You can transfer calls permanently or temporarily."
        )

        self._register_functions()

    def _register_functions(self):
        self.define_tool(
            name="transfer_permanent",
            description="Permanently transfer to support (call ends with agent)",
            parameters={
                "type": "object",
                "properties": {
                    "number": {"type": "string", "description": "Phone number"}
                },
                "required": ["number"]
            },
            handler=self.transfer_permanent
        )

        self.define_tool(
            name="transfer_temporary",
            description="Temporarily connect to expert, then return to agent",
            parameters={
                "type": "object",
                "properties": {
                    "number": {"type": "string", "description": "Phone number"}
                },
                "required": ["number"]
            },
            handler=self.transfer_temporary
        )

    def transfer_permanent(self, args, raw_data):
        number = args.get("number")
        return (
            SwaigFunctionResult(f"Transferring you now. Goodbye!")
            .connect(number, final=True)
        )

    def transfer_temporary(self, args, raw_data):
        number = args.get("number")
        return (
            SwaigFunctionResult("Connecting you briefly. I'll be here when you're done.")
            .connect(number, final=False)
        )


if __name__ == "__main__":
    agent = SmartTransferAgent()
    agent.run()
```

### SIP Transfer

Transfer to SIP endpoints:

```python
def transfer_to_sip(self, args, raw_data):
    return (
        SwaigFunctionResult("Connecting to internal support")
        .connect("sip:support@company.com", final=True)
    )
```

### Transfer with Caller ID Override

```python
def transfer_with_custom_callerid(self, args, raw_data):
    return (
        SwaigFunctionResult("Connecting you now")
        .connect(
            "+15551234567",
            final=True,
            from_addr="+15559876543"  # Custom caller ID
        )
    )
```

### SWML Transfer

Transfer to another SWML endpoint (another agent):

```python
from signalwire_agents import AgentBase
from signalwire_agents.core.function_result import SwaigFunctionResult


class MultiAgentTransfer(AgentBase):
    def __init__(self):
        super().__init__(name="multi-agent-transfer")
        self.add_language("English", "en-US", "rime.spore")

        self.prompt_add_section("Role", "You route calls to specialized agents.")

        self.define_tool(
            name="transfer_to_billing",
            description="Transfer to the billing specialist agent",
            parameters={"type": "object", "properties": {}},
            handler=self.transfer_to_billing
        )

    def transfer_to_billing(self, args, raw_data):
        return (
            SwaigFunctionResult(
                "I'm transferring you to our billing specialist.",
                post_process=True  # Speak message before transfer
            )
            .swml_transfer(
                dest="https://agents.example.com/billing",
                ai_response="How else can I help?",  # Used if final=False
                final=True
            )
        )


if __name__ == "__main__":
    agent = MultiAgentTransfer()
    agent.run()
```

### Transfer Flow

```diagram
┌─────────────────────────────────────────────────────────────────────────────┐
│                    Transfer Flow Diagram                                    │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  Permanent Transfer (final=True):                                           │
│                                                                             │
│  Caller ──→ Agent ──→ "Transferring..." ──→ Destination                     │
│                                │                    │                       │
│                                └── Agent exits ─────┘                       │
│                                                                             │
│  Temporary Transfer (final=False):                                          │
│                                                                             │
│  Caller ──→ Agent ──→ "Connecting..." ──→ Destination                       │
│                │                               │                            │
│                │                               ▼                            │
│                │                        Destination hangs up                │
│                │                               │                            │
│                └───────────── Returns ─────────┘                            │
│                                    │                                        │
│                                    ▼                                        │
│                          Agent continues conversation                       │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Department Transfer Example

```python
from signalwire_agents import AgentBase
from signalwire_agents.core.function_result import SwaigFunctionResult


class ReceptionistAgent(AgentBase):
    """Receptionist that routes calls to departments"""

    DEPARTMENTS = {
        "sales": "+15551111111",
        "support": "+15552222222",
        "billing": "+15553333333",
        "hr": "+15554444444"
    }

    def __init__(self):
        super().__init__(name="receptionist-agent")
        self.add_language("English", "en-US", "rime.spore")

        self.prompt_add_section(
            "Role",
            "You are the company receptionist. Help callers reach the right department."
        )

        self.prompt_add_section(
            "Available Departments",
            "Sales, Support, Billing, Human Resources (HR)"
        )

        self.define_tool(
            name="transfer_to_department",
            description="Transfer caller to a specific department",
            parameters={
                "type": "object",
                "properties": {
                    "department": {
                        "type": "string",
                        "description": "Department name",
                        "enum": ["sales", "support", "billing", "hr"]
                    }
                },
                "required": ["department"]
            },
            handler=self.transfer_to_department
        )

    def transfer_to_department(self, args, raw_data):
        dept = args.get("department", "").lower()

        if dept not in self.DEPARTMENTS:
            return SwaigFunctionResult(
                f"I don't recognize the department '{dept}'. "
                "Available departments are: Sales, Support, Billing, and HR."
            )

        number = self.DEPARTMENTS[dept]
        dept_name = dept.upper() if dept == "hr" else dept.capitalize()

        return (
            SwaigFunctionResult(f"Transferring you to {dept_name} now. Have a great day!")
            .connect(number, final=True)
        )


if __name__ == "__main__":
    agent = ReceptionistAgent()
    agent.run()
```

### Sending SMS During Transfer

Notify the user via SMS before transfer:

```python
def transfer_with_sms(self, args, raw_data):
    caller_number = raw_data.get("caller_id_number")

    return (
        SwaigFunctionResult("I'm transferring you and sending a confirmation text.")
        .send_sms(
            to_number=caller_number,
            from_number="+15559876543",
            body="You're being transferred to our support team. Reference #12345"
        )
        .connect("+15551234567", final=True)
    )
```

### Post-Process Transfer

Use `post_process=True` to have the AI speak before executing the transfer:

```python
def announced_transfer(self, args, raw_data):
    return (
        SwaigFunctionResult(
            "Please hold while I transfer you to our specialist. "
            "This should only take a moment.",
            post_process=True  # AI speaks this before transfer executes
        )
        .connect("+15551234567", final=True)
    )
```

### Transfer Methods Summary

| Method | Use Case | Destination Types |
|--------|----------|-------------------|
| `connect()` | Direct call transfer | Phone numbers, SIP URIs |
| `swml_transfer()` | Transfer to another agent | SWML endpoint URLs |

### Best Practices

**DO:**
- Use post_process=True to announce transfers
- Validate destination numbers before transfer
- Log transfers for tracking and compliance
- Use final=False for consultation/return flows
- Provide clear confirmation to the caller

**DON'T:**
- Transfer without informing the caller
- Use hard-coded numbers without validation
- Forget to handle transfer failures gracefully
- Use final=True when you need the call to return


---

## Multi-Agent Servers

> **Summary**: Run multiple agents on a single server using `AgentServer`. Each agent gets its own route, and you can configure SIP-based routing for username-to-agent mapping.

### When to Use AgentServer

| Single Agent (`agent.run()`) | AgentServer |
|------------------------------|-------------|
| One agent per process | Multiple agents per process |
| Simple deployment | Shared resources |
| Separate ports per agent | Single port, multiple routes |
| | SIP username routing |
| | Unified health checks |

### Basic AgentServer

```python
from signalwire_agents import AgentBase, AgentServer


class SalesAgent(AgentBase):
    def __init__(self):
        super().__init__(name="sales-agent")
        self.add_language("English", "en-US", "rime.spore")
        self.prompt_add_section("Role", "You are a sales representative.")


class SupportAgent(AgentBase):
    def __init__(self):
        super().__init__(name="support-agent")
        self.add_language("English", "en-US", "rime.spore")
        self.prompt_add_section("Role", "You are a support specialist.")


if __name__ == "__main__":
    server = AgentServer(host="0.0.0.0", port=3000)

    server.register(SalesAgent(), "/sales")
    server.register(SupportAgent(), "/support")

    server.run()
```

Agents are available at:

| Endpoint | Description |
|----------|-------------|
| `http://localhost:3000/sales` | Sales agent |
| `http://localhost:3000/support` | Support agent |
| `http://localhost:3000/health` | Built-in health check |

### AgentServer Configuration

```python
server = AgentServer(
    host="0.0.0.0",     # Bind address
    port=3000,          # Listen port
    log_level="info"    # debug, info, warning, error, critical
)
```

### Registering Agents

#### With Explicit Route

```python
server.register(SalesAgent(), "/sales")
```

#### Using Agent's Default Route

```python
class BillingAgent(AgentBase):
    def __init__(self):
        super().__init__(
            name="billing-agent",
            route="/billing"  # Default route
        )

server.register(BillingAgent())  # Uses "/billing"
```

### Server Architecture

```diagram
┌─────────────────────────────────────────────────────────────────────────────┐
│                        AgentServer Architecture                             │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│                          AgentServer                                        │
│                     (FastAPI Application)                                   │
│                              │                                              │
│         ┌────────────────────┼────────────────────┐                         │
│         │                    │                    │                         │
│         ▼                    ▼                    ▼                         │
│    ┌─────────┐         ┌─────────┐         ┌─────────┐                      │
│    │ /sales  │         │/support │         │/billing │                      │
│    │         │         │         │         │         │                      │
│    │ Sales   │         │ Support │         │ Billing │                      │
│    │ Agent   │         │ Agent   │         │ Agent   │                      │
│    └─────────┘         └─────────┘         └─────────┘                      │
│                                                                             │
│  Each agent has:                                                            │
│  • GET/POST /route         → SWML document                                  │
│  • POST /route/swaig       → Function calls                                 │
│  • POST /route/post_prompt → Post-prompt handling                           │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Managing Agents

#### Get All Agents

```python
agents = server.get_agents()
for route, agent in agents:
    print(f"{route}: {agent.get_name()}")
```

#### Get Specific Agent

```python
sales_agent = server.get_agent("/sales")
```

#### Unregister Agent

```python
server.unregister("/sales")
```

### SIP Routing

Route SIP calls to specific agents based on username:

```python
from signalwire_agents import AgentBase, AgentServer


class SalesAgent(AgentBase):
    def __init__(self):
        super().__init__(name="sales-agent")
        self.add_language("English", "en-US", "rime.spore")
        self.prompt_add_section("Role", "You are a sales representative.")


class SupportAgent(AgentBase):
    def __init__(self):
        super().__init__(name="support-agent")
        self.add_language("English", "en-US", "rime.spore")
        self.prompt_add_section("Role", "You are a support specialist.")


if __name__ == "__main__":
    server = AgentServer()

    server.register(SalesAgent(), "/sales")
    server.register(SupportAgent(), "/support")

    # Enable SIP routing
    server.setup_sip_routing("/sip", auto_map=True)

    # Manual SIP username mapping
    server.register_sip_username("sales-team", "/sales")
    server.register_sip_username("help-desk", "/support")

    server.run()
```

When `auto_map=True`, the server automatically creates mappings:

- Agent name → route (e.g., "salesagent" → "/sales")
- Route path → route (e.g., "sales" → "/sales")

### SIP Routing Flow

```diagram
┌─────────────────────────────────────────────────────────────────────────────┐
│                        SIP Routing Flow                                     │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  SIP Call to: sip:sales-team@example.com                                    │
│                        │                                                    │
│                        ▼                                                    │
│            ┌──────────────────────┐                                         │
│            │  POST /sip           │                                         │
│            │  (routing endpoint)  │                                         │
│            └──────────────────────┘                                         │
│                        │                                                    │
│                        ▼                                                    │
│            ┌──────────────────────┐                                         │
│            │ Extract username:    │                                         │
│            │ "sales-team"         │                                         │
│            └──────────────────────┘                                         │
│                        │                                                    │
│                        ▼                                                    │
│            ┌──────────────────────┐                                         │
│            │ Lookup route:        │                                         │
│            │ "/sales"             │                                         │
│            └──────────────────────┘                                         │
│                        │                                                    │
│                        ▼                                                    │
│            ┌──────────────────────┐                                         │
│            │ Return SWML from     │                                         │
│            │ Sales Agent          │                                         │
│            └──────────────────────┘                                         │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Health Check Endpoint

AgentServer provides a built-in health check:

```bash
curl http://localhost:3000/health
```

Response:

```json
{
    "status": "ok",
    "agents": 2,
    "routes": ["/sales", "/support"]
}
```

### Serverless Deployment

AgentServer supports serverless environments automatically:

```python
from signalwire_agents import AgentBase, AgentServer


class MyAgent(AgentBase):
    def __init__(self):
        super().__init__(name="my-agent")
        self.add_language("English", "en-US", "rime.spore")


server = AgentServer()
server.register(MyAgent(), "/agent")


## AWS Lambda handler
def lambda_handler(event, context):
    return server.run(event, context)


## CGI mode (auto-detected)
if __name__ == "__main__":
    server.run()
```

### Complete Example

```python
#!/usr/bin/env python3
## multi_agent_server.py - Server with multiple specialized agents
from signalwire_agents import AgentBase, AgentServer
from signalwire_agents.core.function_result import SwaigFunctionResult


class SalesAgent(AgentBase):
    def __init__(self):
        super().__init__(name="sales-agent")
        self.add_language("English", "en-US", "rime.spore")

        self.prompt_add_section(
            "Role",
            "You are a sales representative for Acme Corp."
        )

        self.define_tool(
            name="get_pricing",
            description="Get product pricing",
            parameters={
                "type": "object",
                "properties": {
                    "product": {"type": "string", "description": "Product name"}
                },
                "required": ["product"]
            },
            handler=self.get_pricing
        )

    def get_pricing(self, args, raw_data):
        product = args.get("product", "")
        # Pricing lookup logic
        return SwaigFunctionResult(f"The price for {product} is $99.99")


class SupportAgent(AgentBase):
    def __init__(self):
        super().__init__(name="support-agent")
        self.add_language("English", "en-US", "rime.spore")

        self.prompt_add_section(
            "Role",
            "You are a technical support specialist."
        )

        self.define_tool(
            name="create_ticket",
            description="Create a support ticket",
            parameters={
                "type": "object",
                "properties": {
                    "issue": {"type": "string", "description": "Issue description"}
                },
                "required": ["issue"]
            },
            handler=self.create_ticket
        )

    def create_ticket(self, args, raw_data):
        issue = args.get("issue", "")
        # Ticket creation logic
        return SwaigFunctionResult(f"Created ticket #12345 for: {issue}")


class BillingAgent(AgentBase):
    def __init__(self):
        super().__init__(name="billing-agent")
        self.add_language("English", "en-US", "rime.spore")

        self.prompt_add_section(
            "Role",
            "You help customers with billing questions."
        )


if __name__ == "__main__":
    # Create server
    server = AgentServer(host="0.0.0.0", port=3000)

    # Register agents
    server.register(SalesAgent(), "/sales")
    server.register(SupportAgent(), "/support")
    server.register(BillingAgent(), "/billing")

    # Enable SIP routing
    server.setup_sip_routing("/sip", auto_map=True)

    # Custom SIP mappings
    server.register_sip_username("sales", "/sales")
    server.register_sip_username("help", "/support")
    server.register_sip_username("accounts", "/billing")

    print("Agents available:")
    for route, agent in server.get_agents():
        print(f"  {route}: {agent.get_name()}")

    server.run()
```

### AgentServer Methods Summary

| Method | Purpose |
|--------|---------|
| `register(agent, route)` | Register an agent at a route |
| `unregister(route)` | Remove an agent |
| `get_agents()` | Get all registered agents |
| `get_agent(route)` | Get agent by route |
| `setup_sip_routing(route, auto_map)` | Enable SIP-based routing |
| `register_sip_username(username, route)` | Map SIP username to route |
| `run()` | Start the server |

### Best Practices

**DO:**
- Use meaningful route names (/sales, /support, /billing)
- Enable SIP routing for SIP-based deployments
- Monitor /health endpoint for availability
- Use consistent naming between routes and SIP usernames

**DON'T:**
- Register duplicate routes
- Forget to handle routing conflicts
- Mix agent.run() and AgentServer for the same agent


---

## Search & Knowledge

> **Summary**: Add RAG-style knowledge search to your agents using local vector indexes (.swsearch files) or PostgreSQL with pgvector. Build indexes with `sw-search` CLI and integrate using the `native_vector_search` skill.

### Search System Overview

**Build Time:**
```
Documents → sw-search CLI → .swsearch file (SQLite + vectors)
```

**Runtime:**
```
Agent → native_vector_search skill → SearchEngine → Results
```

**Backends:**

| Backend | Description |
|---------|-------------|
| SQLite | `.swsearch` files - Local, portable, no infrastructure |
| pgvector | PostgreSQL extension for production deployments |
| Remote | Network mode for centralized search servers |

### Building Search Indexes

Use the `sw-search` CLI to create search indexes:

```bash
## Basic usage - index a directory
sw-search ./docs --output knowledge.swsearch

## Multiple directories
sw-search ./docs ./examples --file-types md,txt,py

## Specific files
sw-search README.md ./docs/guide.md

## Mixed sources
sw-search ./docs README.md ./examples --file-types md,txt
```

### Chunking Strategies

| Strategy | Best For | Parameters |
|----------|----------|------------|
| `sentence` | General text | `--max-sentences-per-chunk 5` |
| `paragraph` | Structured docs | (default) |
| `sliding` | Dense text | `--chunk-size 100 --overlap-size 20` |
| `page` | PDFs | (uses page boundaries) |
| `markdown` | Documentation | (header-aware, code detection) |
| `semantic` | Topic clustering | `--semantic-threshold 0.6` |
| `topic` | Long documents | `--topic-threshold 0.2` |
| `qa` | Q&A applications | (optimized for questions) |

#### Markdown Chunking (Recommended for Docs)

```bash
sw-search ./docs \
  --chunking-strategy markdown \
  --file-types md \
  --output docs.swsearch
```

This strategy:

- Chunks at header boundaries
- Detects code blocks and extracts language
- Adds "code" tags to chunks containing code
- Preserves section hierarchy in metadata

#### Sentence Chunking

```bash
sw-search ./docs \
  --chunking-strategy sentence \
  --max-sentences-per-chunk 10 \
  --output knowledge.swsearch
```

### Installing Search Dependencies

```bash
## Query-only (smallest footprint)
pip install signalwire-agents[search-queryonly]

## Build indexes + vector search
pip install signalwire-agents[search]

## Full features (PDF, DOCX processing)
pip install signalwire-agents[search-full]

## All features including NLP
pip install signalwire-agents[search-all]

## PostgreSQL pgvector support
pip install signalwire-agents[pgvector]
```

### Using Search in Agents

Add the `native_vector_search` skill to enable search:

```python
from signalwire_agents import AgentBase


class KnowledgeAgent(AgentBase):
    def __init__(self):
        super().__init__(name="knowledge-agent")
        self.add_language("English", "en-US", "rime.spore")

        self.prompt_add_section(
            "Role",
            "You are a helpful assistant with access to company documentation. "
            "Use the search_documents function to find relevant information."
        )

        # Add search skill with local index
        self.add_skill(
            "native_vector_search",
            index_file="./knowledge.swsearch",
            count=5,  # Number of results
            tool_name="search_documents",
            tool_description="Search the company documentation"
        )


if __name__ == "__main__":
    agent = KnowledgeAgent()
    agent.run()
```

### Skill Configuration Options

```python
self.add_skill(
    "native_vector_search",
    # Index source (choose one)
    index_file="./knowledge.swsearch",       # Local SQLite index
    # OR
    # remote_url="http://search-server:8001", # Remote search server
    # index_name="default",

    # Search parameters
    count=5,                    # Results to return (1-20)
    similarity_threshold=0.0,   # Min score (0.0-1.0)
    tags=["docs", "api"],       # Filter by tags

    # Tool configuration
    tool_name="search_knowledge",
    tool_description="Search the knowledge base for information"
)
```

### pgvector Backend

For production deployments, use PostgreSQL with pgvector:

```python
self.add_skill(
    "native_vector_search",
    backend="pgvector",
    connection_string="postgresql://user:pass@localhost/db",
    collection_name="knowledge_base",
    count=5,
    tool_name="search_docs"
)
```

### Search Flow

```diagram
┌─────────────────────────────────────────────────────────────────────────────┐
│                        Search Flow                                          │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  User: "What is the return policy?"                                         │
│                     │                                                       │
│                     ▼                                                       │
│  ┌────────────────────────────────────────┐                                 │
│  │ AI decides to call search_documents()  │                                 │
│  │ with query: "return policy"            │                                 │
│  └────────────────────────────────────────┘                                 │
│                     │                                                       │
│                     ▼                                                       │
│  ┌────────────────────────────────────────┐                                 │
│  │ SearchEngine performs:                 │                                 │
│  │  • Vector similarity search            │                                 │
│  │  • Keyword matching                    │                                 │
│  │  • Metadata filtering                  │                                 │
│  │  • Result ranking                      │                                 │
│  └────────────────────────────────────────┘                                 │
│                     │                                                       │
│                     ▼                                                       │
│  ┌────────────────────────────────────────┐                                 │
│  │ Returns top results:                   │                                 │
│  │  1. returns.md - "30-day return..."    │                                 │
│  │  2. faq.md - "Return shipping..."      │                                 │
│  │  3. policies.md - "Refund process..."  │                                 │
│  └────────────────────────────────────────┘                                 │
│                     │                                                       │
│                     ▼                                                       │
│  ┌────────────────────────────────────────┐                                 │
│  │ AI synthesizes response using results  │                                 │
│  └────────────────────────────────────────┘                                 │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### CLI Commands

#### Build Index

```bash
## Basic build
sw-search ./docs --output knowledge.swsearch

## With specific file types
sw-search ./docs --file-types md,txt,rst --output knowledge.swsearch

## With chunking strategy
sw-search ./docs --chunking-strategy markdown --output knowledge.swsearch

## With tags
sw-search ./docs --tags documentation,api --output knowledge.swsearch
```

#### Validate Index

```bash
sw-search validate knowledge.swsearch
```

#### Search Index

```bash
sw-search search knowledge.swsearch "how do I configure auth"
```

### Complete Example

```python
#!/usr/bin/env python3
## documentation_agent.py - Agent that searches documentation
from signalwire_agents import AgentBase
from signalwire_agents.core.function_result import SwaigFunctionResult


class DocumentationAgent(AgentBase):
    """Agent that searches documentation to answer questions"""

    def __init__(self):
        super().__init__(name="docs-agent")
        self.add_language("English", "en-US", "rime.spore")

        self.prompt_add_section(
            "Role",
            "You are a documentation assistant. When users ask questions, "
            "search the documentation to find accurate answers. Always cite "
            "the source document when providing information."
        )

        self.prompt_add_section(
            "Instructions",
            """
            1. When asked a question, use search_docs to find relevant information
            2. Review the search results carefully
            3. Synthesize an answer from the results
            4. Mention which document the information came from
            5. If nothing relevant is found, say so honestly
            """
        )

        # Add a simple search function for demonstration
        # In production, use native_vector_search skill with a .swsearch index:
        # self.add_skill("native_vector_search", index_file="./docs.swsearch")
        self.define_tool(
            name="search_docs",
            description="Search the documentation for information",
            parameters={
                "type": "object",
                "properties": {
                    "query": {"type": "string", "description": "Search query"}
                },
                "required": ["query"]
            },
            handler=self.search_docs
        )

    def search_docs(self, args, raw_data):
        """Stub search function for demonstration"""
        query = args.get("query", "")
        return SwaigFunctionResult(
            f"Search results for '{query}': This is a demonstration. "
            "In production, use native_vector_search skill with a .swsearch index file."
        )


if __name__ == "__main__":
    agent = DocumentationAgent()
    agent.run()
```

> **Note**: This example uses a stub function for demonstration. In production, use the `native_vector_search` skill with a `.swsearch` index file built using `sw-search`.

### Multiple Knowledge Bases

Add multiple search instances for different topics:

```python
## Product documentation
self.add_skill(
    "native_vector_search",
    index_file="./products.swsearch",
    tool_name="search_products",
    tool_description="Search product catalog and specifications"
)

## Support articles
self.add_skill(
    "native_vector_search",
    index_file="./support.swsearch",
    tool_name="search_support",
    tool_description="Search support articles and troubleshooting guides"
)

## API documentation
self.add_skill(
    "native_vector_search",
    index_file="./api-docs.swsearch",
    tool_name="search_api",
    tool_description="Search API reference documentation"
)
```

### Search Best Practices

#### Index Building
- Use markdown chunking for documentation
- Keep chunks reasonably sized (5-10 sentences)
- Add meaningful tags for filtering
- Rebuild indexes when source docs change

#### Agent Configuration
- Set count=3-5 for most use cases
- Use similarity_threshold to filter noise
- Give descriptive tool_name and tool_description
- Tell AI when/how to use search in the prompt

#### Production
- Use pgvector for high-volume deployments
- Consider remote search server for shared indexes
- Monitor search latency and result quality



# Part: Deployment

---

# Deployment

> **Summary**: Deploy your agents as local servers, production services, or serverless functions. This chapter covers all deployment options from development to production.

## What You'll Learn

This chapter covers deployment options:

1. **Local Development** - Running agents during development
2. **Production** - Deploying to production servers
3. **Serverless** - AWS Lambda, Google Cloud Functions, Azure Functions
4. **Docker & Kubernetes** - Container-based deployment
5. **CGI Mode** - Traditional web server deployment

## Deployment Options Overview

| Environment | Options |
|-------------|---------|
| **Development** | `agent.run()` on localhost, ngrok for public testing, auto-reload on changes |
| **Production** | Uvicorn with workers, HTTPS with certificates, load balancing, health monitoring |
| **Serverless** | AWS Lambda, Google Cloud Functions, Azure Functions, auto-scaling, pay per invocation |
| **Container** | Docker, Kubernetes, auto-scaling, rolling updates, service mesh |
| **Traditional** | CGI mode, Apache/nginx integration, shared hosting compatible |

## Environment Detection

The SDK automatically detects your deployment environment:

| Environment Variable | Detected Mode |
|---------------------|---------------|
| `GATEWAY_INTERFACE` | CGI mode |
| `AWS_LAMBDA_FUNCTION_NAME` | AWS Lambda |
| `LAMBDA_TASK_ROOT` | AWS Lambda |
| `FUNCTION_TARGET` | Google Cloud Functions |
| `K_SERVICE` | Google Cloud Functions |
| `GOOGLE_CLOUD_PROJECT` | Google Cloud Functions |
| `AZURE_FUNCTIONS_ENVIRONMENT` | Azure Functions |
| `FUNCTIONS_WORKER_RUNTIME` | Azure Functions |
| (none of above) | Server mode (default) |

## Chapter Contents

| Section | Description |
|---------|-------------|
| [Local Development](07_01_local-development.md) | Development server and testing |
| [Production](07_02_production.md) | Production server deployment |
| [Serverless](07_03_serverless.md) | Lambda, Cloud Functions, Azure |
| [Docker & Kubernetes](07_04_docker-kubernetes.md) | Container deployment |
| [CGI Mode](07_05_cgi-mode.md) | Traditional CGI deployment |

## Quick Start

```python
from signalwire_agents import AgentBase

class MyAgent(AgentBase):
    def __init__(self):
        super().__init__(name="my-agent")
        self.add_language("English", "en-US", "rime.spore")
        self.prompt_add_section("Role", "You are a helpful assistant.")

if __name__ == "__main__":
    agent = MyAgent()
    agent.run()  # Automatically detects environment
```

The `run()` method automatically:

- Detects serverless environments (Lambda, Cloud Functions, Azure)
- Starts a development server on localhost for local development
- Handles CGI mode when deployed to traditional web servers

## Starting the Development Server

The simplest way to run your agent locally:

```python
from signalwire_agents import AgentBase


class MyAgent(AgentBase):
    def __init__(self):
        super().__init__(name="my-agent")
        self.add_language("English", "en-US", "rime.spore")
        self.prompt_add_section("Role", "You are a helpful assistant.")


if __name__ == "__main__":
    agent = MyAgent()
    agent.run()  # Starts on http://localhost:3000
```

## Server Configuration

### Custom Host and Port

```python
agent.run(host="0.0.0.0", port=8080)
```

### Using serve() Directly

For more control, use `serve()` instead of `run()`:

```python
# Development server
agent.serve(host="127.0.0.1", port=3000)

# Listen on all interfaces
agent.serve(host="0.0.0.0", port=3000)
```

## Development Endpoints

| Endpoint | Method | Purpose |
|----------|--------|---------|
| `/` | GET/POST | SWML document |
| `/swaig` | POST | SWAIG function calls |
| `/post_prompt` | POST | Post-prompt handling |
| `/debug` | GET/POST | Debug information |
| `/health` | GET | Health check (AgentServer only) |

## Testing Your Agent

### View SWML Output

```bash
# Get the SWML document
curl http://localhost:3000/

# Pretty print with jq
curl http://localhost:3000/ | jq .
```

### Using swaig-test CLI

```bash
# List available functions
swaig-test my_agent.py --list-tools

# Test a specific function
swaig-test my_agent.py --exec get_weather --city "Seattle"

# Dump SWML output
swaig-test my_agent.py --dump-swml
```

## Exposing Local Server

SignalWire needs to reach your agent via a public URL. Use ngrok or similar:

**Connection Flow:** SignalWire Cloud → ngrok tunnel → localhost:3000

**Steps:**
1. Start your agent: `python my_agent.py`
2. Start ngrok: `ngrok http 3000`
3. Use ngrok URL in SignalWire: `https://abc123.ngrok.io`

### Using ngrok

```bash
# Start your agent
python my_agent.py

# In another terminal, start ngrok
ngrok http 3000
```

ngrok provides a public URL like `https://abc123.ngrok.io` that forwards to your local server.

### Using localtunnel

```bash
# Install
npm install -g localtunnel

# Start tunnel
lt --port 3000
```

## Environment Variables for Development

```bash
# Disable authentication for local testing
export SWML_BASIC_AUTH_USER=""
export SWML_BASIC_AUTH_PASSWORD=""

# Or set custom credentials
export SWML_BASIC_AUTH_USER="dev"
export SWML_BASIC_AUTH_PASSWORD="test123"

# Override proxy URL if behind ngrok
export SWML_PROXY_URL_BASE="https://abc123.ngrok.io"
```

## Proxy URL Configuration

When behind ngrok or another proxy, the SDK needs to know the public URL:

```python
import os

# Option 1: Environment variable
os.environ['SWML_PROXY_URL_BASE'] = 'https://abc123.ngrok.io'

# Option 2: Auto-detection from X-Forwarded headers
# The SDK automatically detects proxy from request headers
```

## Development Workflow

**1. Code**

Write/modify your agent code.

**2. Test Locally**
- `swaig-test my_agent.py --dump-swml`
- `swaig-test my_agent.py --exec function_name --param value`

**3. Run Server**

`python my_agent.py`

**4. Expose Publicly**

`ngrok http 3000`

**5. Test with SignalWire**

Point phone number to ngrok URL and make test call.

## Debug Mode

Enable debug logging:

```python
import logging
logging.basicConfig(level=logging.DEBUG)

agent = MyAgent()
agent.run()
```

Or via environment variable:

```bash
export SIGNALWIRE_LOG_MODE=default
python my_agent.py
```

## Hot Reloading

For automatic reloading during development, use uvicorn directly:

```bash
# Install uvicorn with reload support
pip install uvicorn[standard]

# Run with auto-reload
uvicorn my_agent:agent._app --reload --host 0.0.0.0 --port 3000
```

Or create a development script:

```python
# dev.py
from my_agent import MyAgent

agent = MyAgent()
app = agent._app  # Expose the ASGI app for uvicorn
```

Then run:

```bash
uvicorn dev:app --reload --port 3000
```

## Serving Static Files

Use `AgentServer.serve_static_files()` to serve static files alongside your agents. This is useful for web dashboards, documentation, or any static content:

```python
from signalwire_agents import AgentServer
from pathlib import Path

# Create your agents
from my_agents import SupportAgent, SalesAgent

HOST = "0.0.0.0"
PORT = 3000

server = AgentServer(host=HOST, port=PORT)
server.register(SupportAgent(), "/support")
server.register(SalesAgent(), "/sales")

# Serve static files from web directory
web_dir = Path(__file__).parent / "web"
if web_dir.exists():
    server.serve_static_files(str(web_dir))

server.run()
```

**Directory Structure:**

```
my_project/
├── server.py
├── my_agents.py
└── web/
    ├── index.html
    ├── styles.css
    └── app.js
```

**Key Points:**

- Use `server.serve_static_files(directory)` to serve static files
- Agent routes always take priority over static files
- Requests to `/` serve `index.html` from the static directory
- Both `/support` and `/support/` work correctly with agents

**Route Priority:**

| Route | Handler |
|-------|---------|
| `/support` | SupportAgent |
| `/sales` | SalesAgent |
| `/health` | AgentServer health check |
| `/*` | Static files (fallback) |

## Common Development Issues

| Issue | Solution |
|-------|----------|
| Port already in use | Use different port: `agent.run(port=8080)` |
| 401 Unauthorized | Check `SWML_BASIC_AUTH_*` env vars |
| Functions not found | Verify function registration |
| SWML URL wrong | Set `SWML_PROXY_URL_BASE` for ngrok |
| Connection refused | Ensure agent is running on correct port |
| Static files not found | Check `web_dir.exists()` and path is correct |



---

## Production Deployment

> **Summary**: Deploy agents to production with proper SSL, authentication, monitoring, and scaling. Use uvicorn workers, nginx reverse proxy, and systemd for process management.

### Production Checklist

#### Security
- [ ] HTTPS enabled with valid certificates
- [ ] Basic authentication configured
- [ ] Firewall rules in place
- [ ] No secrets in code or logs

#### Reliability
- [ ] Process manager (systemd/supervisor)
- [ ] Health checks configured
- [ ] Logging to persistent storage
- [ ] Error monitoring/alerting

#### Performance
- [ ] Multiple workers for concurrency
- [ ] Reverse proxy (nginx) for SSL termination
- [ ] Load balancing if needed

### Environment Variables

```bash
## Authentication (required for production)
export SWML_BASIC_AUTH_USER="your-username"
export SWML_BASIC_AUTH_PASSWORD="your-secure-password"

## SSL Configuration
export SWML_SSL_ENABLED="true"
export SWML_SSL_CERT_PATH="/etc/ssl/certs/agent.crt"
export SWML_SSL_KEY_PATH="/etc/ssl/private/agent.key"

## Domain configuration
export SWML_DOMAIN="agent.example.com"

## Proxy URL (if behind load balancer/reverse proxy)
export SWML_PROXY_URL_BASE="https://agent.example.com"
```

### Running with Uvicorn Workers

For production, run with multiple workers:

```bash
## Run with 4 workers
uvicorn my_agent:app --host 0.0.0.0 --port 3000 --workers 4
```

Create an entry point module:

```python
## app.py
from my_agent import MyAgent

agent = MyAgent()
app = agent._app
```

### Systemd Service

Create `/etc/systemd/system/signalwire-agent.service`:

```ini
[Unit]
Description=SignalWire AI Agent
After=network.target

[Service]
Type=simple
User=www-data
Group=www-data
WorkingDirectory=/opt/agent
Environment="PATH=/opt/agent/venv/bin"
Environment="SWML_BASIC_AUTH_USER=your-username"
Environment="SWML_BASIC_AUTH_PASSWORD=your-password"
ExecStart=/opt/agent/venv/bin/uvicorn app:app --host 127.0.0.1 --port 3000 --workers 4
Restart=always
RestartSec=5

[Install]
WantedBy=multi-user.target
```

Enable and start:

```bash
sudo systemctl enable signalwire-agent
sudo systemctl start signalwire-agent
sudo systemctl status signalwire-agent
```

### Nginx Reverse Proxy

```nginx
## /etc/nginx/sites-available/agent
server {
    listen 443 ssl http2;
    server_name agent.example.com;

    ssl_certificate /etc/ssl/certs/agent.crt;
    ssl_certificate_key /etc/ssl/private/agent.key;

    location / {
        proxy_pass http://127.0.0.1:3000;
        proxy_http_version 1.1;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_set_header X-Forwarded-Host $host;
        proxy_read_timeout 300s;
        proxy_connect_timeout 75s;
    }
}

server {
    listen 80;
    server_name agent.example.com;
    return 301 https://$server_name$request_uri;
}
```

Enable the site:

```bash
sudo ln -s /etc/nginx/sites-available/agent /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl reload nginx
```

### Production Architecture

```diagram
┌─────────────────────────────────────────────────────────────────────────────┐
│                     Production Architecture                                 │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  Internet                                                                   │
│      │                                                                      │
│      ▼                                                                      │
│  ┌──────────────────┐                                                       │
│  │   Load Balancer  │  (optional, for high availability)                    │
│  └──────────────────┘                                                       │
│      │                                                                      │
│      ▼                                                                      │
│  ┌──────────────────┐                                                       │
│  │   Nginx          │  SSL termination, rate limiting                       │
│  │   (reverse proxy)│                                                       │
│  └──────────────────┘                                                       │
│      │                                                                      │
│      ▼                                                                      │
│  ┌──────────────────┐                                                       │
│  │   Uvicorn        │  Multiple workers (--workers 4)                       │
│  │   + Agent        │                                                       │
│  └──────────────────┘                                                       │
│      │                                                                      │
│      ▼                                                                      │
│  ┌──────────────────┐                                                       │
│  │   External APIs  │  Databases, services, etc.                            │
│  └──────────────────┘                                                       │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### SSL Configuration

#### Using Environment Variables

```bash
export SWML_SSL_ENABLED="true"
export SWML_SSL_CERT_PATH="/path/to/cert.pem"
export SWML_SSL_KEY_PATH="/path/to/key.pem"
```

#### Let's Encrypt with Certbot

```bash
## Install certbot
sudo apt install certbot python3-certbot-nginx

## Get certificate
sudo certbot --nginx -d agent.example.com

## Auto-renewal is configured automatically
```

### Health Checks

For AgentServer deployments:

```bash
## Health check endpoint
curl https://agent.example.com/health
```

Response:

```json
{
    "status": "ok",
    "agents": 1,
    "routes": ["/"]
}
```

For load balancers, use this endpoint to verify agent availability.

### Logging Configuration

```python
import logging

## Configure logging for production
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('/var/log/agent/agent.log'),
        logging.StreamHandler()
    ]
)
```

Or use environment variable:

```bash
export SIGNALWIRE_LOG_MODE=default
```

### Monitoring

#### Prometheus Metrics

Add custom metrics to your agent:

```python
from prometheus_client import Counter, Histogram, start_http_server

## Start metrics server on port 9090
start_http_server(9090)

## Define metrics
call_counter = Counter('agent_calls_total', 'Total calls handled')
call_duration = Histogram('agent_call_duration_seconds', 'Call duration')
```

#### External Monitoring

- **Uptime monitoring**: Monitor the health endpoint
- **Log aggregation**: Ship logs to ELK, Datadog, or similar
- **APM**: Use Application Performance Monitoring tools

### Scaling Considerations

#### Vertical Scaling
- Increase uvicorn workers (`--workers N`)
- Use larger server instances
- Optimize agent code and external calls

#### Horizontal Scaling
- Multiple server instances behind load balancer
- Stateless agent design
- Shared session storage (Redis) if needed

#### Serverless
- Auto-scaling with Lambda/Cloud Functions
- Pay per invocation
- No server management

### Security Best Practices

**DO:**
- Use HTTPS everywhere
- Set strong basic auth credentials
- Use environment variables for secrets
- Enable firewall and limit access
- Regularly update dependencies
- Monitor for suspicious activity

**DON'T:**
- Expose debug endpoints in production
- Log sensitive data
- Use default credentials
- Disable SSL verification
- Run as root user



---

## Serverless Deployment

> **Summary**: Deploy agents to AWS Lambda, Google Cloud Functions, or Azure Functions. The SDK automatically detects serverless environments and adapts accordingly.

### Serverless Overview

| Platform | Detection | Handler |
|----------|-----------|---------|
| AWS Lambda | `AWS_LAMBDA_FUNCTION_NAME` | `agent.run(event, ctx)` |
| Google Cloud Functions | `FUNCTION_TARGET` | `agent.run(request)` |
| Azure Functions | `AZURE_FUNCTIONS_ENV` | `agent.run(req)` |

**Benefits:**
- Auto-scaling
- Pay per invocation
- No server management
- High availability

### AWS Lambda

#### Basic Lambda Handler

```python
from signalwire_agents import AgentBase


class MyAgent(AgentBase):
    def __init__(self):
        super().__init__(name="my-agent")
        self.add_language("English", "en-US", "rime.spore")
        self.prompt_add_section("Role", "You are a helpful assistant.")


## Create agent instance
agent = MyAgent()


def lambda_handler(event, context):
    """AWS Lambda entry point"""
    return agent.run(event, context)
```

#### Lambda with API Gateway

Configure API Gateway to pass requests to your Lambda:

```yaml
## serverless.yml (Serverless Framework)
service: signalwire-agent

provider:
  name: aws
  runtime: python3.11
  region: us-east-1

functions:
  agent:
    handler: handler.lambda_handler
    events:
      - http:
          path: /
          method: any
      - http:
          path: /{proxy+}
          method: any
```

#### Lambda Environment Variables

```yaml
## In serverless.yml
provider:
  environment:
    SWML_BASIC_AUTH_USER: ${env:SWML_BASIC_AUTH_USER}
    SWML_BASIC_AUTH_PASSWORD: ${env:SWML_BASIC_AUTH_PASSWORD}
```

#### Lambda Request Flow

```diagram
┌─────────────────────────────────────────────────────────────────────────────┐
│                     Lambda Request Flow                                     │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  SignalWire                                                                 │
│      │                                                                      │
│      ▼                                                                      │
│  ┌──────────────────┐                                                       │
│  │   API Gateway    │  HTTPS endpoint                                       │
│  └──────────────────┘                                                       │
│      │                                                                      │
│      ▼                                                                      │
│  ┌──────────────────┐                                                       │
│  │   Lambda         │  agent.run(event, context)                            │
│  │   Function       │                                                       │
│  └──────────────────┘                                                       │
│      │                                                                      │
│      │  Path: /           → Return SWML document                            │
│      │  Path: /swaig      → Execute SWAIG function                          │
│      │                                                                      │
│      ▼                                                                      │
│  ┌──────────────────┐                                                       │
│  │   Response       │  JSON response to SignalWire                          │
│  └──────────────────┘                                                       │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Google Cloud Functions

#### Cloud Functions Handler

```python
from signalwire_agents import AgentBase


class MyAgent(AgentBase):
    def __init__(self):
        super().__init__(name="my-agent")
        self.add_language("English", "en-US", "rime.spore")
        self.prompt_add_section("Role", "You are a helpful assistant.")


## Create agent instance
agent = MyAgent()


def main(request):
    """Google Cloud Functions entry point"""
    return agent.run(request)
```

#### Deploying to Cloud Functions

```bash
gcloud functions deploy signalwire-agent \
  --runtime python311 \
  --trigger-http \
  --allow-unauthenticated \
  --entry-point main \
  --set-env-vars SWML_BASIC_AUTH_USER=user,SWML_BASIC_AUTH_PASSWORD=pass
```

#### requirements.txt

```
signalwire-agents>=1.0.4
```

### Azure Functions

#### Azure Functions Handler

```python
import azure.functions as func
from signalwire_agents import AgentBase


class MyAgent(AgentBase):
    def __init__(self):
        super().__init__(name="my-agent")
        self.add_language("English", "en-US", "rime.spore")
        self.prompt_add_section("Role", "You are a helpful assistant.")


## Create agent instance
agent = MyAgent()


def main(req: func.HttpRequest) -> func.HttpResponse:
    """Azure Functions entry point"""
    return agent.run(req)
```

#### function.json

```json
{
    "scriptFile": "__init__.py",
    "bindings": [
        {
            "authLevel": "anonymous",
            "type": "httpTrigger",
            "direction": "in",
            "name": "req",
            "methods": ["get", "post"],
            "route": "{*path}"
        },
        {
            "type": "http",
            "direction": "out",
            "name": "$return"
        }
    ]
}
```

### Testing Serverless Locally

Use `swaig-test` to simulate serverless environments:

```bash
## Simulate AWS Lambda
swaig-test my_agent.py --simulate-serverless lambda --dump-swml

## Simulate Google Cloud Functions
swaig-test my_agent.py --simulate-serverless cloud_function --dump-swml

## Simulate Azure Functions
swaig-test my_agent.py --simulate-serverless azure_function --dump-swml
```

### Force Mode Override

For testing, you can force a specific execution mode:

```python
## Force Lambda mode
agent.run(event={}, context=None, force_mode='lambda')

## Force Cloud Functions mode
agent.run(request, force_mode='google_cloud_function')

## Force Azure mode
agent.run(req, force_mode='azure_function')
```

### Serverless Best Practices

#### Cold Starts
- Keep dependencies minimal
- Initialize agent outside handler function
- Use provisioned concurrency for low latency

#### Timeouts
- Set appropriate timeout (Lambda: up to 15 min)
- Account for external API calls
- Monitor and optimize slow functions

#### Memory
- Allocate sufficient memory
- More memory = more CPU in Lambda
- Monitor memory usage

#### State
- Design for statelessness
- Use external storage for persistent data
- Don't rely on local filesystem

### Multi-Agent Serverless

Deploy multiple agents with AgentServer:

```python
from signalwire_agents import AgentBase, AgentServer


class SalesAgent(AgentBase):
    def __init__(self):
        super().__init__(name="sales-agent")
        self.add_language("English", "en-US", "rime.spore")


class SupportAgent(AgentBase):
    def __init__(self):
        super().__init__(name="support-agent")
        self.add_language("English", "en-US", "rime.spore")


server = AgentServer()
server.register(SalesAgent(), "/sales")
server.register(SupportAgent(), "/support")


def lambda_handler(event, context):
    """Lambda handler for multi-agent server"""
    return server.run(event, context)
```

### Environment Detection

The SDK detects serverless environments automatically:

| Environment Variable | Platform |
|---------------------|----------|
| `AWS_LAMBDA_FUNCTION_NAME` | AWS Lambda |
| `LAMBDA_TASK_ROOT` | AWS Lambda |
| `FUNCTION_TARGET` | Google Cloud Functions |
| `K_SERVICE` | Google Cloud Functions |
| `GOOGLE_CLOUD_PROJECT` | Google Cloud Functions |
| `AZURE_FUNCTIONS_ENVIRONMENT` | Azure Functions |
| `FUNCTIONS_WORKER_RUNTIME` | Azure Functions |



---

## Docker & Kubernetes

> **Summary**: Containerize your agents with Docker and deploy to Kubernetes for scalable, manageable production deployments.

### Dockerfile

```dockerfile
FROM python:3.11-slim

WORKDIR /app

## Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

## Copy application
COPY . .

## Create non-root user
RUN useradd -m appuser && chown -R appuser:appuser /app
USER appuser

## Expose port
EXPOSE 3000

## Run with uvicorn
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "3000", "--workers", "4"]
```

### requirements.txt

```
signalwire-agents>=1.0.4
uvicorn[standard]>=0.20.0
```

### Application Entry Point

```python
## app.py
from signalwire_agents import AgentBase


class MyAgent(AgentBase):
    def __init__(self):
        super().__init__(name="my-agent")
        self.add_language("English", "en-US", "rime.spore")
        self.prompt_add_section("Role", "You are a helpful assistant.")


agent = MyAgent()
app = agent._app
```

### Building and Running

```bash
## Build image
docker build -t signalwire-agent .

## Run container
docker run -d \
  -p 3000:3000 \
  -e SWML_BASIC_AUTH_USER=myuser \
  -e SWML_BASIC_AUTH_PASSWORD=mypassword \
  --name agent \
  signalwire-agent

## View logs
docker logs -f agent

## Stop container
docker stop agent
```

### Docker Compose

```yaml
## docker-compose.yml
version: '3.8'

services:
  agent:
    build: .
    ports:
      - "3000:3000"
    environment:
      - SWML_BASIC_AUTH_USER=${SWML_BASIC_AUTH_USER}
      - SWML_BASIC_AUTH_PASSWORD=${SWML_BASIC_AUTH_PASSWORD}
      - SWML_PROXY_URL_BASE=${SWML_PROXY_URL_BASE}
    restart: unless-stopped
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:3000/health"]
      interval: 30s
      timeout: 10s
      retries: 3

  nginx:
    image: nginx:alpine
    ports:
      - "443:443"
      - "80:80"
    volumes:
      - ./nginx.conf:/etc/nginx/nginx.conf:ro
      - ./certs:/etc/ssl/certs:ro
    depends_on:
      - agent
    restart: unless-stopped
```

Run with:

```bash
docker-compose up -d
```

### Kubernetes Deployment

#### Deployment Manifest

```yaml
## deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: signalwire-agent
  labels:
    app: signalwire-agent
spec:
  replicas: 3
  selector:
    matchLabels:
      app: signalwire-agent
  template:
    metadata:
      labels:
        app: signalwire-agent
    spec:
      containers:
      - name: agent
        image: your-registry/signalwire-agent:latest
        ports:
        - containerPort: 3000
        env:
        - name: SWML_BASIC_AUTH_USER
          valueFrom:
            secretKeyRef:
              name: agent-secrets
              key: auth-user
        - name: SWML_BASIC_AUTH_PASSWORD
          valueFrom:
            secretKeyRef:
              name: agent-secrets
              key: auth-password
        resources:
          requests:
            memory: "256Mi"
            cpu: "250m"
          limits:
            memory: "512Mi"
            cpu: "500m"
        livenessProbe:
          httpGet:
            path: /health
            port: 3000
          initialDelaySeconds: 10
          periodSeconds: 30
        readinessProbe:
          httpGet:
            path: /health
            port: 3000
          initialDelaySeconds: 5
          periodSeconds: 10
```

#### Service Manifest

```yaml
## service.yaml
apiVersion: v1
kind: Service
metadata:
  name: signalwire-agent
spec:
  selector:
    app: signalwire-agent
  ports:
  - protocol: TCP
    port: 80
    targetPort: 3000
  type: ClusterIP
```

#### Ingress Manifest

```yaml
## ingress.yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: signalwire-agent
  annotations:
    nginx.ingress.kubernetes.io/ssl-redirect: "true"
    cert-manager.io/cluster-issuer: "letsencrypt-prod"
spec:
  ingressClassName: nginx
  tls:
  - hosts:
    - agent.example.com
    secretName: agent-tls
  rules:
  - host: agent.example.com
    http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: signalwire-agent
            port:
              number: 80
```

#### Secrets

```yaml
## secrets.yaml
apiVersion: v1
kind: Secret
metadata:
  name: agent-secrets
type: Opaque
stringData:
  auth-user: your-username
  auth-password: your-secure-password
```

### Kubernetes Architecture

```diagram
┌─────────────────────────────────────────────────────────────────────────────┐
│                     Kubernetes Architecture                                 │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  Internet                                                                   │
│      │                                                                      │
│      ▼                                                                      │
│  ┌──────────────────┐                                                       │
│  │     Ingress      │  SSL termination, routing                             │
│  │   (nginx/traefik)│                                                       │
│  └──────────────────┘                                                       │
│      │                                                                      │
│      ▼                                                                      │
│  ┌──────────────────┐                                                       │
│  │     Service      │  Load balancing across pods                           │
│  │  (ClusterIP)     │                                                       │
│  └──────────────────┘                                                       │
│      │                                                                      │
│      ├──────────────┬──────────────┐                                        │
│      ▼              ▼              ▼                                        │
│  ┌────────┐    ┌────────┐    ┌────────┐                                     │
│  │  Pod   │    │  Pod   │    │  Pod   │  replicas: 3                        │
│  │ Agent  │    │ Agent  │    │ Agent  │                                     │
│  └────────┘    └────────┘    └────────┘                                     │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Deploying to Kubernetes

```bash
## Create secrets
kubectl apply -f secrets.yaml

## Deploy application
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
kubectl apply -f ingress.yaml

## Check status
kubectl get pods -l app=signalwire-agent
kubectl get svc signalwire-agent
kubectl get ingress signalwire-agent

## View logs
kubectl logs -f -l app=signalwire-agent

## Scale deployment
kubectl scale deployment signalwire-agent --replicas=5
```

### Horizontal Pod Autoscaler

```yaml
## hpa.yaml
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: signalwire-agent
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: signalwire-agent
  minReplicas: 2
  maxReplicas: 10
  metrics:
  - type: Resource
    resource:
      name: cpu
      target:
        type: Utilization
        averageUtilization: 70
```

### Multi-Architecture Builds

```dockerfile
## Build for multiple architectures
FROM --platform=$TARGETPLATFORM python:3.11-slim

## ... rest of Dockerfile
```

Build with:

```bash
docker buildx build --platform linux/amd64,linux/arm64 -t your-registry/agent:latest --push .
```

### Container Best Practices

#### Security
- Run as non-root user
- Use minimal base images (slim, alpine)
- Scan images for vulnerabilities
- Don't store secrets in images

#### Performance
- Use multi-stage builds to reduce image size
- Layer dependencies efficiently
- Set appropriate resource limits

#### Reliability
- Add health checks
- Use restart policies
- Configure proper logging
- Set graceful shutdown handling



---

## CGI Mode

> **Summary**: Deploy agents as CGI scripts on traditional web servers like Apache or nginx. The SDK automatically detects CGI environments and handles requests appropriately.

### CGI Overview

CGI (Common Gateway Interface) allows web servers to execute scripts and return their output as HTTP responses.

**Benefits:**
- Works with shared hosting
- Simple deployment - just upload files
- No separate process management
- Compatible with Apache, nginx

**Drawbacks:**
- New process per request (slower)
- No persistent connections
- Limited scalability

### CGI Detection

The SDK detects CGI mode via the `GATEWAY_INTERFACE` environment variable:

```python
## Automatic detection
if os.getenv('GATEWAY_INTERFACE'):
    # CGI mode detected
    mode = 'cgi'
```

### Basic CGI Script

```python
#!/usr/bin/env python3
## agent.py - Basic CGI agent script
from signalwire_agents import AgentBase


class MyAgent(AgentBase):
    def __init__(self):
        super().__init__(name="my-agent")
        self.add_language("English", "en-US", "rime.spore")
        self.prompt_add_section("Role", "You are a helpful assistant.")


if __name__ == "__main__":
    agent = MyAgent()
    agent.run()  # Automatically detects CGI mode
```

Make it executable:

```bash
chmod +x agent.py
```

### CGI Request Flow

```diagram
┌─────────────────────────────────────────────────────────────────────────────┐
│                     CGI Request Flow                                        │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  SignalWire                                                                 │
│      │                                                                      │
│      ▼                                                                      │
│  ┌──────────────────┐                                                       │
│  │   Web Server     │  Apache/nginx                                         │
│  │   (httpd)        │                                                       │
│  └──────────────────┘                                                       │
│      │                                                                      │
│      │  Sets environment variables:                                         │
│      │  • GATEWAY_INTERFACE=CGI/1.1                                         │
│      │  • PATH_INFO=/swaig                                                  │
│      │  • CONTENT_LENGTH=...                                                │
│      │                                                                      │
│      ▼                                                                      │
│  ┌──────────────────┐                                                       │
│  │   Python CGI     │  agent.py                                             │
│  │   Script         │                                                       │
│  └──────────────────┘                                                       │
│      │                                                                      │
│      │  PATH_INFO=""     → Return SWML document                             │
│      │  PATH_INFO=/swaig → Execute SWAIG function                           │
│      │                                                                      │
│      ▼                                                                      │
│  ┌──────────────────┐                                                       │
│  │   stdout         │  JSON response to web server                          │
│  └──────────────────┘                                                       │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Apache Configuration

#### Enable CGI

```apache
## Enable CGI module
LoadModule cgi_module modules/mod_cgi.so

## Configure CGI directory
<Directory "/var/www/cgi-bin">
    Options +ExecCGI
    AddHandler cgi-script .py
    Require all granted
</Directory>
```

#### Virtual Host Configuration

```apache
<VirtualHost *:443>
    ServerName agent.example.com

    SSLEngine on
    SSLCertificateFile /etc/ssl/certs/agent.crt
    SSLCertificateKeyFile /etc/ssl/private/agent.key

    ScriptAlias / /var/www/cgi-bin/agent.py

    <Directory "/var/www/cgi-bin">
        Options +ExecCGI
        SetHandler cgi-script
        Require all granted
    </Directory>

    # Set environment variables
    SetEnv SWML_BASIC_AUTH_USER "myuser"
    SetEnv SWML_BASIC_AUTH_PASSWORD "mypassword"
</VirtualHost>
```

### nginx Configuration

nginx doesn't natively support CGI, but you can use FastCGI with `fcgiwrap`:

```nginx
server {
    listen 443 ssl;
    server_name agent.example.com;

    ssl_certificate /etc/ssl/certs/agent.crt;
    ssl_certificate_key /etc/ssl/private/agent.key;

    location / {
        fastcgi_pass unix:/var/run/fcgiwrap.socket;
        fastcgi_param SCRIPT_FILENAME /var/www/cgi-bin/agent.py;
        fastcgi_param GATEWAY_INTERFACE CGI/1.1;
        fastcgi_param PATH_INFO $uri;
        fastcgi_param SWML_BASIC_AUTH_USER "myuser";
        fastcgi_param SWML_BASIC_AUTH_PASSWORD "mypassword";
        include fastcgi_params;
    }
}
```

### CGI Host Configuration

In CGI mode, the SDK needs to know the external hostname for generating URLs:

```bash
## Using swaig-test to simulate CGI mode
swaig-test my_agent.py --simulate-serverless cgi --cgi-host agent.example.com
```

Or set environment variable:

```apache
SetEnv SWML_PROXY_URL_BASE "https://agent.example.com"
```

### Testing CGI Locally

Use `swaig-test` to simulate CGI environment:

```bash
## Test SWML generation in CGI mode
swaig-test my_agent.py --simulate-serverless cgi --dump-swml

## With custom host
swaig-test my_agent.py --simulate-serverless cgi --cgi-host mysite.com --dump-swml

## Test a function
swaig-test my_agent.py --simulate-serverless cgi --exec function_name --param value
```

### Authentication in CGI Mode

The SDK checks basic auth in CGI mode:

```python
## Authentication is automatic when these are set
## SWML_BASIC_AUTH_USER
## SWML_BASIC_AUTH_PASSWORD

## The SDK reads Authorization header and validates
```

If authentication fails, returns 401 with WWW-Authenticate header.

### Directory Structure

```
/var/www/cgi-bin/
├── agent.py              # Main CGI script
├── requirements.txt      # Dependencies
└── venv/                 # Virtual environment (optional)
```

### Shared Hosting Deployment

For shared hosting where you can't install system packages:

```python
#!/usr/bin/env python3
## agent_shared.py - CGI agent for shared hosting
import sys
import os

## Add local packages directory
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'packages'))

from signalwire_agents import AgentBase


class MyAgent(AgentBase):
    def __init__(self):
        super().__init__(name="my-agent")
        self.add_language("English", "en-US", "rime.spore")


if __name__ == "__main__":
    agent = MyAgent()
    agent.run()
```

Install packages locally:

```bash
pip install --target=./packages signalwire-agents
```

### CGI Best Practices

#### Performance
- Keep imports minimal - each request starts fresh
- Consider FastCGI for better performance
- Cache what you can (but remember process dies)

#### Security
- Set proper file permissions (750 or 755)
- Don't expose .py files directly if possible
- Use HTTPS always
- Set auth credentials as environment variables

#### Debugging
- Check web server error logs
- Verify shebang line (#!/usr/bin/env python3)
- Test script from command line first
- Ensure proper line endings (LF, not CRLF)

### Common CGI Issues

| Issue | Solution |
|-------|----------|
| 500 Internal Server Error | Check error logs, verify permissions |
| Permission denied | `chmod +x agent.py` |
| Module not found | Check `sys.path`, install dependencies |
| Wrong Python version | Update shebang to correct Python |
| Malformed headers | Ensure proper Content-Type output |
| Timeout | Optimize code, increase server timeout |

### Migration from CGI

When you outgrow CGI:

#### CGI → FastCGI
Keep same code, use fcgiwrap or gunicorn. Better performance, persistent processes.

#### CGI → Server Mode
Same code works - just run differently (`python agent.py` instead of CGI). Add systemd service, nginx reverse proxy.

#### CGI → Serverless
Same code works with minor changes. Add Lambda handler wrapper. Deploy to AWS/GCP/Azure.




# Part: SignalWire Integration

---

# SignalWire Integration

> **Summary**: Connect your agents to phone numbers through SignalWire. This chapter covers account setup, phone number configuration, and testing your voice agents.

## What You'll Learn

This chapter covers SignalWire integration:

1. **Account Setup** - Create and configure your SignalWire account
2. **Phone Numbers** - Purchase and manage phone numbers
3. **Mapping Numbers** - Connect phone numbers to your agents
4. **Testing** - Test your agents before going live
5. **Troubleshooting** - Common issues and solutions

## Integration Overview

```diagram
┌─────────────────────────────────────────────────────────────────────────────┐
│                      SignalWire Integration                                 │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  ┌─────────┐    ┌─────────────┐    ┌─────────────┐    ┌─────────────┐       │
│  │ Caller  │ →  │ SignalWire  │ →  │ Your Server │ →  │    Agent    │       │
│  │  Phone  │    │   Network   │    │   (SWML)    │    │    Logic    │       │
│  └─────────┘    └─────────────┘    └─────────────┘    └─────────────┘       │
│                                                                             │
│  1. Caller dials your phone number                                          │
│  2. SignalWire receives the call                                            │
│  3. SignalWire requests SWML from your server                               │
│  4. Your agent handles the conversation                                     │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

## Prerequisites

Before connecting to SignalWire:

- Working agent (tested locally)
- Publicly accessible server
- SignalWire account

## Chapter Contents

| Section | Description |
|---------|-------------|
| [Account Setup](08_01_account-setup.md) | Create SignalWire account and project |
| [Phone Numbers](08_02_phone-numbers.md) | Purchase and manage numbers |
| [Mapping Numbers](08_03_mapping-numbers.md) | Connect numbers to agents |
| [Testing](08_04_testing.md) | Test calls and debugging |
| [Troubleshooting](08_05_troubleshooting.md) | Common issues and fixes |

## Quick Integration Steps

### Step 1: Account Setup
- Create SignalWire account
- Create a project
- Note your Space Name

### Step 2: Phone Number
- Purchase a phone number
- Or use a SIP endpoint

### Step 3: Deploy Agent
- Deploy agent to public URL
- Verify HTTPS is working
- Test SWML endpoint responds

### Step 4: Connect
- Point phone number to agent URL
- Make test call
- Verify agent responds

## Architecture

```diagram
┌─────────────────────────────────────────────────────────────────────────────┐
│                      Call Flow Architecture                                 │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  ┌───────────────────────────────────────────────────────────────────────┐  │
│  │                        SignalWire Cloud                               │  │
│  │  ┌─────────────────────────────────────────────────────────────────┐  │  │
│  │  │ Inbound Call          SWML Processor                            │  │  │
│  │  │              →                                                  │  │  │
│  │  │                    • Fetches SWML from your server              │  │  │
│  │  │                    • Executes AI verbs                          │  │  │
│  │  │                    • Handles speech                             │  │  │
│  │  │                    • Calls SWAIG funcs                          │  │  │
│  │  │                              │                                  │  │  │
│  │  └──────────────────────────────┼──────────────────────────────────┘  │  │
│  └─────────────────────────────────┼─────────────────────────────────────┘  │
│                                    │                                        │
│                                    ▼ HTTPS                                  │
│                                                                             │
│  ┌───────────────────────────────────────────────────────────────────────┐  │
│  │                          Your Server                                  │  │
│  │  ┌─────────────────────────────────────────────────────────────────┐  │  │
│  │  │                      Agent (SWML)                               │  │  │
│  │  │                                                                 │  │  │
│  │  │                    • Returns SWML doc                           │  │  │
│  │  │                    • Handles functions                          │  │  │
│  │  │                    • Business logic                             │  │  │
│  │  │                                                                 │  │  │
│  │  └─────────────────────────────────────────────────────────────────┘  │  │
│  └───────────────────────────────────────────────────────────────────────┘  │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

## Required URLs

Your agent needs to be accessible at these endpoints:

| Endpoint | Method | Purpose |
|----------|--------|---------|
| `/` | POST | Main SWML document |
| `/swaig` | POST | SWAIG function calls |

## Security Considerations

- Always use HTTPS for production
- Enable basic auth for SWML endpoints
- Use secure tokens for SWAIG functions
- Don't expose sensitive data in prompts
- Monitor for unusual call patterns

Let's start with setting up your SignalWire account.

## Create Account

1. Go to [signalwire.com](https://signalwire.com)
2. Click [Sign Up](https://id.signalwire.com/onboarding) or [Login](https://id.signalwire.com/login/session/new)
3. Complete registration with email and password
4. Verify your email address

**Note:** If you have problems verifying your account, email support@signalwire.com

## Create a Project

After logging in:

1. Navigate to Projects in the dashboard
2. Click "Create New Project"
3. Enter a project name (e.g., "Voice Agents")
4. Select your use case

## Space Name

Your Space Name is your unique SignalWire identifier.

**URL Format:** `https://YOUR-SPACE-NAME.signalwire.com`

**Example:** `https://mycompany.signalwire.com`

**You'll need this for:**
- API authentication
- Dashboard access
- SWML webhook configuration

## API Credentials

Get your API credentials from the project:

1. Go to [API Credentials](https://my.signalwire.com/?page=/credentials)
2. Note your Project ID
3. Create an API Token if needed

| Credential | Format |
|------------|--------|
| Project ID | `xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx` |
| API Token | `PTxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx` |
| Space Name | `your-space` |

**Keep these secure - don't commit to version control!**

## Environment Variables

Set these for your agent:

```bash
export SIGNALWIRE_PROJECT_ID="your-project-id"
export SIGNALWIRE_API_TOKEN="your-api-token"
export SIGNALWIRE_SPACE_NAME="your-space"
```

## Dashboard Overview

| Section | Purpose |
|---------|---------|
| **[Phone Numbers](https://my.signalwire.com/?page=/phone_numbers)** | Purchase and manage phone numbers |
| **[SWML](https://my.signalwire.com/?page=/resources/scripts)** | Configure SWML scripts and webhooks |
| **[Logs](https://my.signalwire.com/?/logs/voices)** | View call history and debugging info |
| **[API Credentials](https://my.signalwire.com/?page=/credentials)** | Credentials and API explorer |
| **[Billing](https://my.signalwire.com/?page=/payment_methods)** | Account balance and usage |

## Add Credit

Before making calls:

1. Go to [Billing](https://my.signalwire.com/?page=/payment_methods)
2. Add payment method
3. Add credit to your account

Trial accounts may have limited credit for testing.

## Account Verification

Some features require account verification:

- Phone number purchases
- Outbound calling
- Certain number types

Complete verification in Account Settings if prompted.

## Next Steps

With your account ready:

1. [Purchase a phone number](https://my.signalwire.com/?page=/phone_numbers)
2. Deploy your agent
3. Connect the number to your agent



---

## Phone Numbers

> **Summary**: Purchase and configure phone numbers to receive calls for your agents.

### Purchasing Numbers

1. Go to [Phone Numbers](https://my.signalwire.com/?page=/phone_numbers) in dashboard
2. Click "Buy a New Phone Number"
3. Search by area code or location
4. Select a number and purchase

### Number Types

| Type | Description | Use Case |
|------|-------------|----------|
| Local | Standard local numbers | General business use |
| Toll-Free | 800/888/877/866 numbers | Customer service |
| Short Code | 5-6 digit numbers | SMS campaigns |

### Number Features

Each number can support:

| Feature | Description |
|---------|-------------|
| Voice | Inbound/outbound calls |
| SMS | Text messaging |
| MMS | Picture messaging |
| Fax | Fax transmission |

### Managing Numbers

View your numbers in [Phone Numbers](https://my.signalwire.com/?page=/phone_numbers) section. Each number shows:

| Field | Example |
|-------|---------|
| Number | +1 (555) 123-4567 |
| Type | Local |
| Capabilities | Voice, SMS |
| Status | Active |
| Voice Handler | https://your-server.com/agent |

**Available Actions:**
- Edit Settings
- View [Logs](https://my.signalwire.com/?/logs/voices)
- Release Number

### Number Settings

Configure each number:

**Voice Settings:**
- Accept Incoming: Enable/disable
- Voice URL: Your agent's SWML endpoint
- Fallback URL: Backup if primary fails

**SMS Settings:**
- Accept Incoming: Enable/disable
- Message URL: Webhook for SMS

### SIP Endpoints

Alternative to phone numbers - use SIP for testing.

**SIP Address Format:** `sip:username@your-space.signalwire.com`

**Use with:**
- Software phones (Zoiper, Linphone)
- SIP-enabled devices
- Testing without PSTN charges

### Number Porting

Bring existing numbers to SignalWire:

1. Go to [Phone Numbers](https://my.signalwire.com/?page=/phone_numbers) > [Porting Request](https://my.signalwire.com/?port_requests/new)
2. Submit porting request
3. Provide current carrier info
4. Wait for port completion (~1 week in most cases)

### Costs

**Phone Number Costs:**
- Monthly rental fee per number
- Varies by number type and country

**Voice Usage:**
- Per-minute charges for calls
- Inbound vs outbound rates differ
- See [Voice Pricing](https://signalwire.com/pricing/voice)

**AI Agent Usage:**
- Per-minute AI processing costs
- Includes STT, TTS, and LLM usage
- See [AI Agent Pricing](https://signalwire.com/pricing/ai-agent-pricing)

**Questions?** Contact sales@signalwire.com for custom pricing and volume discounts.

### Multiple Numbers

You can have multiple numbers pointing to:

- Same agent (multiple entry points)
- Different agents (department routing)
- Different configurations per number

```python
## Agent can check which number was called
def my_handler(self, args, raw_data):
    called_number = raw_data.get("called_id_num")

    if called_number == "+15551234567":
        return SwaigFunctionResult("Sales line")
    else:
        return SwaigFunctionResult("Support line")
```



---

## Mapping Numbers

> **Summary**: Connect phone numbers to your agent's SWML endpoint so calls are handled by your agent.

### Overview

```diagram
┌─────────────────────────────────────────────────────────────────────────────┐
│                      Number to Agent Mapping                                │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  Phone Number          →    Voice URL           →    Agent                  │
│  +1 (555) 123-4567          https://server/          SupportAgent           │
│  +1 (555) 987-6543          https://server/sales     SalesAgent             │
│                                                                             │
│  When a call comes in:                                                      │
│  1. SignalWire receives call on your number                                 │
│  2. SignalWire makes POST request to Voice URL                              │
│  3. Your server returns SWML document                                       │
│  4. SignalWire executes the SWML (runs your agent)                          │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Configure Voice URL

1. Go to Phone Numbers in dashboard
2. Click on your number
3. Set Voice URL to your agent endpoint
4. Save changes

### URL Format

Your agent URL structure:

**Single Agent:**
```
https://your-server.com/
```

**Multiple Agents:**
```
https://your-server.com/support
https://your-server.com/sales
https://your-server.com/billing
```

**With Authentication:**
```
https://user:pass@your-server.com/
```

### HTTPS Requirements

**Production:**
- HTTPS required
- Valid SSL certificate
- Properly configured domain

**Development:**
- Use ngrok or similar tunnel
- ngrok provides HTTPS automatically
- Update URL when tunnel restarts

### Using ngrok for Development

```bash
## Start your agent locally
python my_agent.py

## In another terminal, start ngrok
ngrok http 3000

## Use the ngrok HTTPS URL in SignalWire
## https://abc123.ngrok.io
```

### Basic Authentication

Set authentication credentials:

```python
from signalwire_agents import AgentBase


class SecureAgent(AgentBase):
    def __init__(self):
        super().__init__(
            name="secure-agent",
            # Basic auth credentials
            # Also configurable via environment variables:
            # SWML_BASIC_AUTH_USER, SWML_BASIC_AUTH_PASSWORD
        )
```

In SignalWire, use URL with credentials:

```
https://username:password@your-server.com/
```

### Multi-Agent Server

Run multiple agents on one server:

```python
from signalwire_agents import AgentServer

server = AgentServer()

## Register agents at different paths
server.register(SupportAgent(), "/support")
server.register(SalesAgent(), "/sales")
server.register(BillingAgent(), "/billing")

server.run(host="0.0.0.0", port=3000)
```

Map each number to its agent:

| Number | Voice URL |
|--------|-----------|
| +1 (555) 111-1111 | https://server.com/support |
| +1 (555) 222-2222 | https://server.com/sales |
| +1 (555) 333-3333 | https://server.com/billing |

### SWML Scripts

Alternative: Use SWML scripts directly in SignalWire:

```json
{
    "version": "1.0.0",
    "sections": {
        "main": [
            {
                "ai": {
                    "prompt": {
                        "text": "You are a helpful assistant."
                    },
                    "SWAIG": {
                        "defaults": {
                            "web_hook_url": "https://your-server.com/swaig"
                        }
                    }
                }
            }
        ]
    }
}
```

### Fallback URL

Configure a fallback for errors:

| Setting | Value |
|---------|-------|
| Primary URL | `https://your-server.com/agent` |
| Fallback URL | `https://backup-server.com/agent` |

**Fallback triggers on:**
- Connection timeout
- HTTP 5xx errors
- Invalid SWML response

### Status Callbacks

Receive notifications about call events:

```
Status Callback URL: https://your-server.com/status

Events:
• Call started
• Call answered
• Call completed
• Call failed
```

### Verification Checklist

Before going live:

- [ ] Agent is deployed and running
- [ ] HTTPS URL is accessible
- [ ] URL returns valid SWML on POST request
- [ ] Basic auth is configured (if used)
- [ ] Phone number Voice URL is set
- [ ] Fallback URL is configured (recommended)
- [ ] Test call completes successfully



---

## Testing

> **Summary**: Test your agent thoroughly before production. Use local testing, swaig-test CLI, and test calls.

### Testing Stages

#### 1. Local Testing
- Run agent locally
- Test with swaig-test CLI
- Verify SWML output

#### 2. Tunnel Testing
- Expose via ngrok
- Make real calls
- Test end-to-end

#### 3. Production Testing
- Deploy to production server
- Test with real phone
- Monitor call logs

### swaig-test CLI

Test agents without making calls:

```bash
## List available functions
swaig-test my_agent.py --list-tools

## View SWML output
swaig-test my_agent.py --dump-swml

## Execute a function
swaig-test my_agent.py --exec get_weather --city Seattle

## Raw JSON output
swaig-test my_agent.py --dump-swml --raw
```

### Local Server Testing

Run your agent locally:

```bash
## Start the agent
python my_agent.py

## In another terminal, test the endpoint
curl -X POST http://localhost:3000/ \
  -H "Content-Type: application/json" \
  -d '{"call_id": "test-123"}'
```

### Using ngrok

Expose local server for real calls:

```bash
## Terminal 1: Run agent
python my_agent.py

## Terminal 2: Start ngrok
ngrok http 3000
```

Copy the ngrok HTTPS URL and configure in SignalWire.

### Test Call Checklist

#### Basic Functionality
- [ ] Call connects successfully
- [ ] Agent greeting plays
- [ ] Speech recognition works
- [ ] Agent responds appropriately

#### Function Calls
- [ ] Functions execute correctly
- [ ] Results returned to AI
- [ ] AI summarizes results properly

#### Edge Cases
- [ ] Silence handling
- [ ] Interruption handling
- [ ] Long responses
- [ ] Multiple function calls

#### Error Handling
- [ ] Invalid input handled
- [ ] Function errors handled gracefully
- [ ] Timeout behavior correct

### Viewing Logs

In SignalWire dashboard:

1. Go to [Logs](https://my.signalwire.com/?/logs/voices)
2. Find your test call
3. View details:
   - Call duration
   - SWML executed
   - Function calls
   - Errors

### Debugging with Logs

Add logging to your agent:

```python
import logging

logging.basicConfig(level=logging.DEBUG)


class MyAgent(AgentBase):
    def __init__(self):
        super().__init__(name="my-agent")
        self.log.info("Agent initialized")

    def my_handler(self, args, raw_data):
        self.log.debug(f"Function called with args: {args}")
        self.log.debug(f"Raw data: {raw_data}")

        result = "Some result"
        self.log.info(f"Returning: {result}")

        return SwaigFunctionResult(result)
```

### Testing Transfers

Test call transfers carefully:

```python
def test_transfer(self, args, raw_data):
    # Use a test number you control
    test_number = "+15551234567"

    return (
        SwaigFunctionResult("Transferring now")
        .connect(test_number, final=True)
    )
```

### Testing SMS

Test SMS sending:

```python
def test_sms(self, args, raw_data):
    # Send to your own phone for testing
    return (
        SwaigFunctionResult("Sent test SMS")
        .send_sms(
            to_number="+15551234567",  # Your test phone
            from_number="+15559876543", # Your SignalWire number
            body="Test message from agent"
        )
    )
```

### Load Testing

For production readiness:

- Test concurrent call handling
- Monitor server resources
- Check response times under load
- Verify function execution at scale
- Test database/API connection pooling

### Common Test Scenarios

| Scenario | What to Test |
|----------|--------------|
| Happy path | Normal conversation flow |
| No speech | Silence and timeout handling |
| Background noise | Speech recognition accuracy |
| Rapid speech | Interruption handling |
| Invalid requests | Error handling |
| Function errors | Graceful degradation |
| Long calls | Memory and stability |

### Automated Testing

Create test scripts:

```python
import requests


def test_swml_endpoint():
    """Test that SWML endpoint returns valid response"""
    response = requests.post(
        "http://localhost:3000/",
        json={"call_id": "test-123"},
        headers={"Content-Type": "application/json"}
    )

    assert response.status_code == 200
    data = response.json()
    assert "version" in data
    assert data["version"] == "1.0.0"


def test_function_execution():
    """Test that functions execute correctly"""
    response = requests.post(
        "http://localhost:3000/swaig",
        json={
            "function": "get_weather",
            "argument": {"parsed": [{"city": "Seattle"}]},
            "call_id": "test-123"
        }
    )

    assert response.status_code == 200
```



---

## Troubleshooting

> **Summary**: Common issues and solutions when integrating agents with SignalWire.

### Connection Issues

**Problem:** Call doesn't connect to agent

**Check:**
- Is the server running?
- Is the URL correct in SignalWire?
- Is HTTPS configured properly?
- Is the firewall allowing connections?
- Can you access the URL from browser?

**Test:**
```bash
curl -X POST https://your-server.com/ -H "Content-Type: application/json"
```

### Authentication Errors

**Problem:** 401 Unauthorized

**Check:**
- Is basic auth enabled on the server?
- Are credentials in the URL correct?
- Are credentials URL-encoded if special chars?

**URL Format:**
```
https://username:password@your-server.com/
```

**Special characters in password need encoding:**

| Character | Encoded |
|-----------|---------|
| `@` | `%40` |
| `:` | `%3A` |
| `/` | `%2F` |

### SWML Errors

**Problem:** Invalid SWML response

**Verify with swaig-test:**
```bash
swaig-test my_agent.py --dump-swml --raw
```

**Common issues:**
- Missing `"version": "1.0.0"`
- Invalid JSON format
- Missing required sections
- Syntax errors in SWML verbs

### No Speech Response

**Problem:** Agent doesn't speak

**Check:**
- Is a language configured? `self.add_language("English", "en-US", "rime.spore")`
- Is there a prompt? `self.prompt_add_section("Role", "You are...")`
- Is the AI model specified? Check SWML output for `ai.params`

### Function Not Called

**Problem:** AI doesn't call your function

**Check:**
- Is the function registered? Run `swaig-test my_agent.py --list-tools`
- Is the description clear? AI needs to understand when to use it
- Is the prompt mentioning the capability? Example: "You can check the weather using get_weather"

### Function Errors

**Problem:** Function returns error

**Test locally:**
```bash
swaig-test my_agent.py --exec function_name --param value
```

**Check:**
- Are all required parameters provided?
- Is the handler returning SwaigFunctionResult?
- Are there exceptions in the handler?

**Add error handling:**
```python
try:
    result = do_something()
    return SwaigFunctionResult(result)
except Exception as e:
    self.log.error(f"Error: {e}")
    return SwaigFunctionResult("Sorry, an error occurred")
```

### SSL Certificate Issues

**Problem:** SSL handshake failed

**Check:**
- Is certificate valid and not expired?
- Is the full certificate chain provided?
- Is the domain correct on the certificate?

**Test:**
```bash
openssl s_client -connect your-server.com:443
```

For development, use ngrok (handles SSL automatically).

### Timeout Issues

**Problem:** Requests timing out

**SWML Request Timeout:**
- SignalWire waits ~5 seconds for SWML
- Make sure server responds quickly

**Function Timeout:**
- SWAIG functions should complete in <30 seconds
- Use async operations for slow tasks
- Consider background processing for long tasks

### Quick Diagnostic Steps

| Issue | First Check | Command |
|-------|-------------|---------|
| Server down | Process running | `ps aux \| grep python` |
| Bad URL | Test endpoint | `curl -X POST https://url/` |
| Bad SWML | View output | `swaig-test agent.py --dump-swml` |
| Function error | Execute directly | `swaig-test agent.py --exec func` |
| Auth error | Check credentials | Verify URL format |

### Getting Help

If issues persist:

1. Check SignalWire documentation
2. Review call logs in dashboard
3. Enable debug logging in your agent
4. Contact SignalWire support

### Common Error Messages

| Error | Meaning | Solution |
|-------|---------|----------|
| "No route to host" | Server unreachable | Check network/firewall |
| "Connection refused" | Server not listening | Start the server |
| "Invalid SWML" | Bad response format | Check swaig-test output |
| "Function not found" | Missing function | Register the function |
| "Unauthorized" | Auth failed | Check credentials |

### Logging for Debugging

Enable detailed logging:

```python
import logging
import structlog

## Enable debug logging
logging.basicConfig(level=logging.DEBUG)

## The agent uses structlog
structlog.configure(
    wrapper_class=structlog.make_filtering_bound_logger(logging.DEBUG)
)
```



# Part: Prefab Agents

---

# Prefab Agents

> **Summary**: Prefabs are pre-built agent archetypes for common use cases. Use them directly or extend them to quickly build information gatherers, FAQ bots, surveys, receptionists, and concierges.

## What Are Prefabs?

Prefabs are ready-to-use agent classes that implement common conversational patterns:

| Prefab | Description |
|--------|-------------|
| **InfoGatherer** | Collect answers to a series of questions |
| **FAQBot** | Answer questions from a knowledge base |
| **Survey** | Conduct automated surveys with validation |
| **Receptionist** | Greet callers and transfer to departments |
| **Concierge** | Provide information and booking assistance |

## Why Use Prefabs?

- **Faster Development:** Pre-built conversation flows
- **Best Practices:** Proven patterns for common scenarios
- **Extensible:** Inherit and customize as needed
- **Production-Ready:** Includes validation, error handling, summaries

## Quick Examples

### InfoGatherer

```python
from signalwire_agents.prefabs import InfoGathererAgent

agent = InfoGathererAgent(
    questions=[
        {"key_name": "name", "question_text": "What is your name?"},
        {"key_name": "email", "question_text": "What is your email?", "confirm": True},
        {"key_name": "reason", "question_text": "How can I help you?"}
    ]
)
agent.run()
```

### FAQBot

```python
from signalwire_agents.prefabs import FAQBotAgent

agent = FAQBotAgent(
    faqs=[
        {"question": "What are your hours?", "answer": "We're open 9 AM to 5 PM."},
        {"question": "Where are you located?", "answer": "123 Main Street, Downtown."}
    ]
)
agent.run()
```

### Survey

```python
from signalwire_agents.prefabs import SurveyAgent

agent = SurveyAgent(
    survey_name="Customer Satisfaction",
    questions=[
        {"id": "rating", "text": "Rate your experience?", "type": "rating", "scale": 5},
        {"id": "feedback", "text": "Any comments?", "type": "open_ended", "required": False}
    ]
)
agent.run()
```

### Receptionist

```python
from signalwire_agents.prefabs import ReceptionistAgent

agent = ReceptionistAgent(
    departments=[
        {"name": "sales", "description": "Product inquiries", "number": "+15551234567"},
        {"name": "support", "description": "Technical help", "number": "+15551234568"}
    ]
)
agent.run()
```

### Concierge

```python
from signalwire_agents.prefabs import ConciergeAgent

agent = ConciergeAgent(
    venue_name="Grand Hotel",
    services=["room service", "spa", "restaurant"],
    amenities={
        "pool": {"hours": "7 AM - 10 PM", "location": "2nd Floor"},
        "gym": {"hours": "24 hours", "location": "3rd Floor"}
    }
)
agent.run()
```

## Chapter Contents

| Section | Description |
|---------|-------------|
| [InfoGatherer](09_01_info-gatherer.md) | Collect information through questions |
| [FAQBot](09_02_faq-bot.md) | Answer frequently asked questions |
| [Survey](09_03_survey.md) | Conduct automated surveys |
| [Receptionist](09_04_receptionist.md) | Greet and transfer callers |
| [Concierge](09_05_concierge.md) | Provide venue information and services |

## Importing Prefabs

```python
# Import individual prefabs
from signalwire_agents.prefabs import InfoGathererAgent
from signalwire_agents.prefabs import FAQBotAgent
from signalwire_agents.prefabs import SurveyAgent
from signalwire_agents.prefabs import ReceptionistAgent
from signalwire_agents.prefabs import ConciergeAgent

# Or import all
from signalwire_agents.prefabs import (
    InfoGathererAgent,
    FAQBotAgent,
    SurveyAgent,
    ReceptionistAgent,
    ConciergeAgent
)
```

## Extending Prefabs

All prefabs inherit from `AgentBase`, so you can extend them:

```python
from signalwire_agents.prefabs import FAQBotAgent
from signalwire_agents.core.function_result import SwaigFunctionResult

class MyFAQBot(FAQBotAgent):
    def __init__(self):
        super().__init__(
            faqs=[
                {"question": "What is your return policy?", "answer": "30-day returns."}
            ]
        )

        # Add custom prompt sections
        self.prompt_add_section("Brand", "You represent Acme Corp.")

        # Add custom functions
        self.define_tool(
            name="escalate",
            description="Escalate to human agent",
            parameters={"type": "object", "properties": {}},
            handler=self.escalate
        )

    def escalate(self, args, raw_data):
        return SwaigFunctionResult("Transferring to agent...").connect("+15551234567")
```

## Basic Usage

```python
from signalwire_agents.prefabs import InfoGathererAgent

agent = InfoGathererAgent(
    questions=[
        {"key_name": "full_name", "question_text": "What is your full name?"},
        {"key_name": "email", "question_text": "What is your email address?", "confirm": True},
        {"key_name": "reason", "question_text": "How can I help you today?"}
    ]
)

if __name__ == "__main__":
    agent.run()
```

## Question Format

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `key_name` | string | Yes | Identifier for storing the answer |
| `question_text` | string | Yes | The question to ask the user |
| `confirm` | boolean | No | If true, confirm answer before next |

## Constructor Parameters

```python
InfoGathererAgent(
    questions=None,           # List of question dictionaries
    name="info_gatherer",     # Agent name
    route="/info_gatherer",   # HTTP route
    **kwargs                  # Additional AgentBase arguments
)
```

## Flow Diagram

```diagram
┌─────────────────────────────────────────────────────────────────────────────┐
│                     InfoGatherer Flow                                       │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  1. Agent asks if user is ready                                             │
│      │                                                                      │
│      ▼                                                                      │
│  2. User confirms → AI calls start_questions()                              │
│      │                                                                      │
│      ▼                                                                      │
│  3. Agent asks first question                                               │
│      │                                                                      │
│      ▼                                                                      │
│  4. User answers → AI calls submit_answer()                                 │
│      │                                                                      │
│      ├── If confirm=true → Verify with user                                 │
│      │                                                                      │
│      ▼                                                                      │
│  5. Repeat for each question                                                │
│      │                                                                      │
│      ▼                                                                      │
│  6. All questions answered → Summary                                        │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

## Built-in Functions

InfoGatherer provides these SWAIG functions automatically:

| Function | Description |
|----------|-------------|
| `start_questions` | Begin the question sequence |
| `submit_answer` | Submit answer and get next question |

## Dynamic Questions

Instead of static questions, use a callback to determine questions at runtime:

```python
from signalwire_agents.prefabs import InfoGathererAgent


def get_questions(query_params, body_params, headers):
    """Dynamically determine questions based on request"""
    question_set = query_params.get('type', 'default')

    if question_set == 'support':
        return [
            {"key_name": "name", "question_text": "What is your name?"},
            {"key_name": "issue", "question_text": "Describe your issue."},
            {"key_name": "urgency", "question_text": "How urgent is this?"}
        ]
    else:
        return [
            {"key_name": "name", "question_text": "What is your name?"},
            {"key_name": "message", "question_text": "How can I help?"}
        ]


# Create agent without static questions
agent = InfoGathererAgent()

# Set the callback for dynamic questions
agent.set_question_callback(get_questions)

if __name__ == "__main__":
    agent.run()
```

## Accessing Collected Data

The collected answers are stored in `global_data`:

```python
# In a SWAIG function or callback:
global_data = raw_data.get("global_data", {})
answers = global_data.get("answers", [])

# answers is a list like:
# [
#     {"key_name": "full_name", "answer": "John Doe"},
#     {"key_name": "email", "answer": "john@example.com"},
#     {"key_name": "reason", "answer": "Product inquiry"}
# ]
```

## Complete Example

```python
#!/usr/bin/env python3
# appointment_scheduler.py - Info gatherer for scheduling appointments
from signalwire_agents.prefabs import InfoGathererAgent


agent = InfoGathererAgent(
    questions=[
        {"key_name": "name", "question_text": "What is your name?"},
        {"key_name": "phone", "question_text": "What is your phone number?", "confirm": True},
        {"key_name": "date", "question_text": "What date would you like to schedule?"},
        {"key_name": "time", "question_text": "What time works best for you?"},
        {"key_name": "notes", "question_text": "Any special notes or requests?"}
    ],
    name="appointment-scheduler"
)

# Add custom language
agent.add_language("English", "en-US", "rime.spore")

# Customize prompt
agent.prompt_add_section(
    "Brand",
    "You are scheduling appointments for Dr. Smith's office."
)

if __name__ == "__main__":
    agent.run()
```

## Best Practices

### Questions
- Keep questions clear and specific
- Use confirm=true for critical data (email, phone)
- Limit to 5-7 questions max per session
- Order from simple to complex

### key_name Values
- Use descriptive, unique identifiers
- snake_case convention recommended
- Match your backend/database field names

### Dynamic Questions
- Use callbacks for multi-purpose agents
- Validate questions in callback
- Handle errors gracefully



---

## FAQBot

> **Summary**: FAQBotAgent answers frequently asked questions from a provided knowledge base. It matches user questions to FAQs and optionally suggests related questions.

### Basic Usage

```python
from signalwire_agents.prefabs import FAQBotAgent

agent = FAQBotAgent(
    faqs=[
        {
            "question": "What are your business hours?",
            "answer": "We're open Monday through Friday, 9 AM to 5 PM."
        },
        {
            "question": "Where are you located?",
            "answer": "Our main office is at 123 Main Street, Downtown."
        },
        {
            "question": "How do I contact support?",
            "answer": "Email support@example.com or call 555-1234."
        }
    ]
)

if __name__ == "__main__":
    agent.run()
```

### FAQ Format

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `question` | string | Yes | The FAQ question |
| `answer` | string | Yes | The answer to provide |
| `categories` | list[string] | No | Category tags for filtering |

### Constructor Parameters

```python
FAQBotAgent(
    faqs=[...],                # List of FAQ dictionaries (required)
    suggest_related=True,      # Suggest related questions
    persona=None,              # Custom personality description
    name="faq_bot",            # Agent name
    route="/faq",              # HTTP route
    **kwargs                   # Additional AgentBase arguments
)
```

### With Categories

Use categories to organize FAQs:

```python
from signalwire_agents.prefabs import FAQBotAgent

agent = FAQBotAgent(
    faqs=[
        {
            "question": "How do I reset my password?",
            "answer": "Click 'Forgot Password' on the login page.",
            "categories": ["account", "security"]
        },
        {
            "question": "How do I update my email?",
            "answer": "Go to Settings > Account > Email.",
            "categories": ["account", "settings"]
        },
        {
            "question": "What payment methods do you accept?",
            "answer": "We accept Visa, Mastercard, and PayPal.",
            "categories": ["billing", "payments"]
        }
    ]
)
```

### Built-in Functions

FAQBot provides this SWAIG function automatically:

| Function | Description |
|----------|-------------|
| `search_faqs` | Search FAQs by query or category |

### Custom Persona

Customize the bot's personality:

```python
agent = FAQBotAgent(
    faqs=[...],
    persona="You are a friendly and knowledgeable support agent for Acme Corp. "
            "You speak in a warm, professional tone and always try to be helpful."
)
```

### Complete Example

```python
#!/usr/bin/env python3
## product_faq_bot.py - FAQ bot for product questions
from signalwire_agents.prefabs import FAQBotAgent


agent = FAQBotAgent(
    faqs=[
        {
            "question": "What is the warranty period?",
            "answer": "All products come with a 2-year warranty.",
            "categories": ["warranty", "products"]
        },
        {
            "question": "How do I return a product?",
            "answer": "Start a return within 30 days at returns.example.com.",
            "categories": ["returns", "products"]
        },
        {
            "question": "Do you ship internationally?",
            "answer": "Yes, we ship to over 50 countries.",
            "categories": ["shipping"]
        }
    ],
    suggest_related=True,
    persona="You are a helpful product specialist for TechGadgets Inc.",
    name="product-faq"
)

## Add language
agent.add_language("English", "en-US", "rime.spore")

if __name__ == "__main__":
    agent.run()
```

### Best Practices

#### FAQ Content
- Write questions as users would ask them
- Keep answers concise but complete
- Include variations of common questions
- Update FAQs based on actual user queries

#### Categories
- Use consistent category naming
- Limit to 2-3 categories per FAQ
- Use categories for related question suggestions

#### Scaling
- For large FAQ sets, consider native_vector_search skill
- FAQBot works best with 50 or fewer FAQs
- Use categories to help matching



---

## Survey

> **Summary**: SurveyAgent conducts automated surveys with different question types (rating, multiple choice, yes/no, open-ended), validation, and response logging.

### Basic Usage

```python
from signalwire_agents.prefabs import SurveyAgent

agent = SurveyAgent(
    survey_name="Customer Satisfaction Survey",
    questions=[
        {
            "id": "satisfaction",
            "text": "How satisfied were you with our service?",
            "type": "rating",
            "scale": 5
        },
        {
            "id": "recommend",
            "text": "Would you recommend us to others?",
            "type": "yes_no"
        },
        {
            "id": "comments",
            "text": "Any additional comments?",
            "type": "open_ended",
            "required": False
        }
    ]
)

if __name__ == "__main__":
    agent.run()
```

### Question Types

| Type | Fields | Example |
|------|--------|---------|
| `rating` | scale (1-10) | "Rate 1-5, where 5 is best" |
| `multiple_choice` | options (list) | "Choose: Poor, Fair, Good, Excellent" |
| `yes_no` | (none) | "Would you recommend us?" |
| `open_ended` | (none) | "Any comments?" |

### Question Format

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `id` | string | Yes | Unique identifier for the question |
| `text` | string | Yes | The question to ask |
| `type` | string | Yes | rating, multiple_choice, yes_no, open_ended |
| `options` | list[string] | * | Required for multiple_choice |
| `scale` | integer | No | For rating (default: 5) |
| `required` | boolean | No | Is answer required (default: true) |

### Constructor Parameters

```python
SurveyAgent(
    survey_name="...",         # Name of the survey (required)
    questions=[...],           # List of question dictionaries (required)
    introduction=None,         # Custom intro message
    conclusion=None,           # Custom conclusion message
    brand_name=None,           # Company/brand name
    max_retries=2,             # Retries for invalid answers
    name="survey",             # Agent name
    route="/survey",           # HTTP route
    **kwargs                   # Additional AgentBase arguments
)
```

### Built-in Functions

SurveyAgent provides these SWAIG functions automatically:

| Function | Description |
|----------|-------------|
| `validate_response` | Check if response is valid for question type |
| `log_response` | Record a validated response |

### Survey Flow

```diagram
┌─────────────────────────────────────────────────────────────────────────────┐
│                     Survey Flow                                             │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  1. Introduction                                                            │
│      │                                                                      │
│      ▼                                                                      │
│  2. Ask question                                                            │
│      │                                                                      │
│      ▼                                                                      │
│  3. Get response                                                            │
│      │                                                                      │
│      ├── Valid → Log and continue                                           │
│      │                                                                      │
│      └── Invalid → Retry (up to max_retries)                                │
│              │                                                              │
│              └── Still invalid → Skip or ask again                          │
│      │                                                                      │
│      ▼                                                                      │
│  4. Next question (repeat 2-3)                                              │
│      │                                                                      │
│      ▼                                                                      │
│  5. Conclusion                                                              │
│      │                                                                      │
│      ▼                                                                      │
│  6. Generate summary                                                        │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Complete Example

```python
#!/usr/bin/env python3
## product_survey.py - Product feedback survey agent
from signalwire_agents.prefabs import SurveyAgent


agent = SurveyAgent(
    survey_name="Product Feedback Survey",
    brand_name="TechGadgets Inc.",
    introduction="Thank you for purchasing our product. We'd love your feedback!",
    conclusion="Thank you for completing our survey. Your input helps us improve.",
    questions=[
        {
            "id": "overall_rating",
            "text": "How would you rate the product overall?",
            "type": "rating",
            "scale": 5,
            "required": True
        },
        {
            "id": "quality",
            "text": "How would you rate the build quality?",
            "type": "multiple_choice",
            "options": ["Poor", "Fair", "Good", "Excellent"],
            "required": True
        },
        {
            "id": "purchase_again",
            "text": "Would you purchase from us again?",
            "type": "yes_no",
            "required": True
        },
        {
            "id": "improvements",
            "text": "What could we improve?",
            "type": "open_ended",
            "required": False
        }
    ],
    max_retries=2
)

if __name__ == "__main__":
    agent.add_language("English", "en-US", "rime.spore")
    agent.run()
```

### Best Practices

#### Question Design
- Keep surveys short (5-7 questions max)
- Start with easy questions
- Put open-ended questions at the end
- Make non-essential questions optional

#### Question Types
- Use rating for satisfaction metrics (NPS, CSAT)
- Use multiple_choice for specific options
- Use yes_no for simple binary questions
- Use open_ended sparingly - harder to analyze

#### Validation
- Set appropriate max_retries (2-3)
- Use clear scale descriptions
- List all options for multiple choice



---

## Receptionist

> **Summary**: ReceptionistAgent greets callers, collects their information, and transfers them to the appropriate department based on their needs.

### Basic Usage

```python
from signalwire_agents.prefabs import ReceptionistAgent

agent = ReceptionistAgent(
    departments=[
        {
            "name": "sales",
            "description": "Product inquiries, pricing, and purchasing",
            "number": "+15551234567"
        },
        {
            "name": "support",
            "description": "Technical help and troubleshooting",
            "number": "+15551234568"
        },
        {
            "name": "billing",
            "description": "Payment questions and account issues",
            "number": "+15551234569"
        }
    ]
)

if __name__ == "__main__":
    agent.run()
```

### Department Format

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `name` | string | Yes | Department identifier (e.g., "sales") |
| `description` | string | Yes | What the department handles |
| `number` | string | Yes | Phone number for transfer |

### Constructor Parameters

```python
ReceptionistAgent(
    departments=[...],                              # List of department dicts (required)
    name="receptionist",                            # Agent name
    route="/receptionist",                          # HTTP route
    greeting="Thank you for calling. How can I help you today?",
    voice="rime.spore",                             # Voice ID
    **kwargs                                        # Additional AgentBase arguments
)
```

### Built-in Functions

ReceptionistAgent provides these SWAIG functions automatically:

| Function | Description |
|----------|-------------|
| `collect_caller_info` | Collect caller's name and reason for calling |
| `transfer_call` | Transfer to a specific department |

### Call Flow

```diagram
┌─────────────────────────────────────────────────────────────────────────────┐
│                     Receptionist Flow                                       │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  1. Greeting                                                                │
│      │  "Thank you for calling. How can I help you today?"                  │
│      │                                                                      │
│      ▼                                                                      │
│  2. Collect Information                                                     │
│      │  • Caller's name                                                     │
│      │  • Reason for calling                                                │
│      │                                                                      │
│      ▼                                                                      │
│  3. AI calls collect_caller_info()                                          │
│      │  Stores info in global_data                                          │
│      │                                                                      │
│      ▼                                                                      │
│  4. Determine Department                                                    │
│      │  AI matches reason to department                                     │
│      │                                                                      │
│      ▼                                                                      │
│  5. Confirm Transfer                                                        │
│      │  "I'll transfer you to sales. Is that correct?"                      │
│      │                                                                      │
│      ▼                                                                      │
│  6. AI calls transfer_call()                                                │
│      │  Connects to department number                                       │
│      │                                                                      │
│      ▼                                                                      │
│  7. Call Transferred                                                        │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Complete Example

```python
#!/usr/bin/env python3
## company_receptionist.py - Custom receptionist agent
from signalwire_agents.prefabs import ReceptionistAgent


agent = ReceptionistAgent(
    departments=[
        {
            "name": "sales",
            "description": "New orders, pricing, quotes, and product information",
            "number": "+15551001001"
        },
        {
            "name": "support",
            "description": "Technical issues, troubleshooting, and product help",
            "number": "+15551001002"
        },
        {
            "name": "billing",
            "description": "Invoices, payments, refunds, and account questions",
            "number": "+15551001003"
        },
        {
            "name": "hr",
            "description": "Employment, careers, and benefits",
            "number": "+15551001004"
        }
    ],
    greeting="Thank you for calling Acme Corporation. How may I direct your call?",
    voice="rime.spore",
    name="acme-receptionist"
)

## Add custom prompt section
agent.prompt_add_section(
    "Company",
    "You are the receptionist for Acme Corporation, a leading technology company."
)

if __name__ == "__main__":
    agent.run()
```

### Best Practices

#### Departments
- Use clear, distinct department names
- Write descriptions that help AI route correctly
- Include common reasons in descriptions
- Verify transfer numbers are correct

#### Greeting
- Keep greeting professional and welcoming
- Include company name if appropriate
- Ask how to help (prompts caller to state need)

#### Transfers
- Always confirm before transferring
- Use final=True for permanent transfers
- Test all transfer numbers



---

## Concierge

> **Summary**: ConciergeAgent provides venue information, answers questions about amenities and services, helps with bookings, and gives directions.

### Basic Usage

```python
from signalwire_agents.prefabs import ConciergeAgent

agent = ConciergeAgent(
    venue_name="Grand Hotel",
    services=["room service", "spa bookings", "restaurant reservations", "tours"],
    amenities={
        "pool": {"hours": "7 AM - 10 PM", "location": "2nd Floor"},
        "gym": {"hours": "24 hours", "location": "3rd Floor"},
        "spa": {"hours": "9 AM - 8 PM", "location": "4th Floor"}
    }
)

if __name__ == "__main__":
    agent.run()
```

### Amenity Format

```python
amenities = {
    "amenity_name": {
        "hours": "Operating hours",
        "location": "Where to find it",
        "description": "Optional description",
        # ... any other key-value pairs
    }
}
```

### Constructor Parameters

```python
ConciergeAgent(
    venue_name="...",                  # Name of venue (required)
    services=[...],                    # List of services offered (required)
    amenities={...},                   # Dict of amenities with details (required)
    hours_of_operation=None,           # Dict of operating hours
    special_instructions=None,         # List of special instructions
    welcome_message=None,              # Custom welcome message
    name="concierge",                  # Agent name
    route="/concierge",                # HTTP route
    **kwargs                           # Additional AgentBase arguments
)
```

### Built-in Functions

ConciergeAgent provides these SWAIG functions automatically:

| Function | Description |
|----------|-------------|
| `check_availability` | Check service availability for date/time |
| `get_directions` | Get directions to an amenity or location |

### Concierge Flow

```diagram
┌─────────────────────────────────────────────────────────────────────────────┐
│                     Concierge Flow                                          │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  Guest: "What time does the pool close?"                                    │
│      │                                                                      │
│      ▼                                                                      │
│  AI looks up pool in amenities                                              │
│      │                                                                      │
│      ▼                                                                      │
│  Response: "The pool is open until 10 PM and located on the 2nd Floor."     │
│                                                                             │
│  ─────────────────────────────────────────────────────────────────────────  │
│                                                                             │
│  Guest: "Can I book a spa appointment for tomorrow at 2 PM?"                │
│      │                                                                      │
│      ▼                                                                      │
│  AI calls check_availability("spa", "2025-01-16", "14:00")                  │
│      │                                                                      │
│      ▼                                                                      │
│  Response: "Yes, the spa is available tomorrow at 2 PM. Shall I book it?"   │
│                                                                             │
│  ─────────────────────────────────────────────────────────────────────────  │
│                                                                             │
│  Guest: "How do I get to the gym?"                                          │
│      │                                                                      │
│      ▼                                                                      │
│  AI calls get_directions("gym")                                             │
│      │                                                                      │
│      ▼                                                                      │
│  Response: "The gym is on Level 2, West Wing. From the lobby..."            │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Complete Example

```python
#!/usr/bin/env python3
## resort_concierge.py - Hotel concierge agent
from signalwire_agents.prefabs import ConciergeAgent


agent = ConciergeAgent(
    venue_name="The Riverside Resort",
    services=[
        "room service",
        "spa treatments",
        "restaurant reservations",
        "golf tee times",
        "airport shuttle",
        "event planning"
    ],
    amenities={
        "swimming pool": {
            "hours": "6 AM - 10 PM",
            "location": "Ground Floor, East Wing",
            "description": "Heated indoor/outdoor pool with poolside bar"
        },
        "fitness center": {
            "hours": "24 hours",
            "location": "Level 2, West Wing",
            "description": "Full gym with personal trainers available"
        },
        "spa": {
            "hours": "9 AM - 9 PM",
            "location": "Level 3, East Wing",
            "description": "Full service spa with massage and facials"
        },
        "restaurant": {
            "hours": "Breakfast 7-10 AM, Lunch 12-3 PM, Dinner 6-10 PM",
            "location": "Lobby Level",
            "description": "Fine dining with panoramic river views"
        }
    },
    hours_of_operation={
        "front desk": "24 hours",
        "concierge": "7 AM - 11 PM",
        "valet": "6 AM - 12 AM"
    },
    special_instructions=[
        "Always offer to make reservations when guests ask about restaurants or spa.",
        "Mention the daily happy hour at the pool bar (4-6 PM)."
    ],
    welcome_message="Welcome to The Riverside Resort! How may I assist you today?"
)

if __name__ == "__main__":
    agent.add_language("English", "en-US", "rime.spore")
    agent.run()
```

### Best Practices

#### Amenities
- Include hours for all amenities
- Provide clear location descriptions
- Add any special requirements or dress codes
- Keep information up to date

#### Services
- List all bookable services
- Connect to real booking system for availability
- Include service descriptions and pricing if possible

#### Special Instructions
- Use for promotions and special offers
- Include upselling opportunities
- Add seasonal information




# Part: Reference

---

# Reference

> **Summary**: Complete API reference for all SignalWire Agents SDK classes, methods, CLI tools, and configuration options.

This chapter provides detailed reference documentation for the SignalWire Agents SDK.

## Reference Overview

### API Reference
- **AgentBase** - Main agent class with all methods
- **SWMLService** - Base service for SWML generation
- **SwaigFunctionResult** - Function return values and actions
- **DataMap** - Serverless REST API integration
- **SkillBase** - Custom skill development
- **ContextBuilder** - Multi-step workflows

### CLI Tools
- **swaig-test** - Test agents and functions locally
- **sw-search** - Build and query search indexes

### Configuration
- **Environment Variables** - Runtime configuration
- **Config Files** - YAML/JSON configuration
- **SWML Schema** - Document structure reference

## Quick Reference

### Creating an Agent
```python
agent = AgentBase(name="my-agent", route="/agent")
agent.add_language("English", "en-US", "rime.spore")
agent.prompt_add_section("Role", "You are a helpful assistant.")
agent.run()
```

### Defining a Function
```python
@agent.tool(description="Search for information")
def search(query: str) -> SwaigFunctionResult:
    return SwaigFunctionResult(f"Found results for: {query}")
```

### Returning Actions
```python
return SwaigFunctionResult("Transferring...").connect("+15551234567")
return SwaigFunctionResult("Goodbye").hangup()
return SwaigFunctionResult().update_global_data({"key": "value"})
```

## Import Patterns

```python
# Main imports
from signalwire_agents import AgentBase
from signalwire_agents.core.function_result import SwaigFunctionResult
from signalwire_agents.core.data_map import DataMap

# Prefab agents
from signalwire_agents.prefabs import (
    InfoGathererAgent,
    FAQBotAgent,
    SurveyAgent,
    ReceptionistAgent,
    ConciergeAgent
)

# Context/workflow system
from signalwire_agents.core.contexts import ContextBuilder

# Skill development
from signalwire_agents.core.skill_base import SkillBase
```

## Chapter Contents

| Section | Description |
|---------|-------------|
| [AgentBase API](10_01_api-agent-base.md) | Main agent class reference |
| [SWMLService API](10_02_api-swml-service.md) | Base service class reference |
| [SWAIG Function API](10_03_api-swaig-function.md) | Function definition reference |
| [SwaigFunctionResult API](10_04_api-function-result.md) | Return value and actions reference |
| [DataMap API](10_05_api-data-map.md) | Serverless API integration reference |
| [SkillBase API](10_06_api-skill-base.md) | Custom skill development reference |
| [ContextBuilder API](10_07_api-contexts.md) | Workflow system reference |
| [swaig-test CLI](10_08_cli-swaig-test.md) | Testing tool reference |
| [sw-search CLI](10_09_cli-sw-search.md) | Search tool reference |
| [Environment Variables](10_10_environment-variables.md) | Environment configuration |
| [Config Files](10_11_config-files.md) | File-based configuration |
| [SWML Schema](10_12_swml-schema.md) | Document structure reference |

## Class Definition

```python
from signalwire_agents import AgentBase

class AgentBase(
    AuthMixin,
    WebMixin,
    SWMLService,
    PromptMixin,
    ToolMixin,
    SkillMixin,
    AIConfigMixin,
    ServerlessMixin,
    StateMixin
)
```

## Constructor

```python
AgentBase(
    name: str,                              # Agent name/identifier (required)
    route: str = "/",                       # HTTP route path
    host: str = "0.0.0.0",                  # Host to bind
    port: int = 3000,                       # Port to bind
    basic_auth: Optional[Tuple[str, str]] = None,  # (username, password)
    use_pom: bool = True,                   # Use POM for prompts
    token_expiry_secs: int = 3600,          # Token expiration time
    auto_answer: bool = True,               # Auto-answer calls
    record_call: bool = False,              # Enable recording
    record_format: str = "mp4",             # Recording format
    record_stereo: bool = True,             # Stereo recording
    default_webhook_url: Optional[str] = None,  # Default webhook URL
    agent_id: Optional[str] = None,         # Unique agent ID
    native_functions: Optional[List[str]] = None,  # Native function list
    schema_path: Optional[str] = None,      # SWML schema path
    suppress_logs: bool = False,            # Suppress structured logs
    enable_post_prompt_override: bool = False,  # Enable post-prompt override
    check_for_input_override: bool = False, # Enable input override
    config_file: Optional[str] = None       # Path to config file
)
```

## Constructor Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `name` | str | required | Agent identifier |
| `route` | str | `"/"` | HTTP endpoint path |
| `host` | str | `"0.0.0.0"` | Bind address |
| `port` | int | `3000` | Bind port |
| `basic_auth` | Tuple[str, str] | None | Auth credentials |
| `use_pom` | bool | True | Use POM prompts |
| `token_expiry_secs` | int | `3600` | Token TTL |
| `auto_answer` | bool | True | Auto-answer calls |
| `record_call` | bool | False | Record calls |
| `record_format` | str | `"mp4"` | Recording format |
| `record_stereo` | bool | True | Stereo recording |
| `native_functions` | List[str] | None | Native functions |

## Prompt Methods

### prompt_add_section

```python
def prompt_add_section(
    self,
    section: str,              # Section title
    body: str,                 # Section content
    bullets: List[str] = None  # Optional bullet points
) -> 'AgentBase'
```

Add a section to the agent's prompt.

### prompt_add_text

```python
def prompt_add_text(
    self,
    text: str  # Text to add
) -> 'AgentBase'
```

Add raw text to the prompt.

### get_prompt

```python
def get_prompt(self) -> Union[str, List[Dict]]
```

Get the complete prompt. Returns POM structure if `use_pom=True`, otherwise plain text.

## Language and Voice Methods

### add_language

```python
def add_language(
    self,
    name: str,           # Language name (e.g., "English")
    code: str,           # Language code (e.g., "en-US")
    voice: str,          # Voice ID (e.g., "rime.spore")
    speech_fillers: Optional[List[str]] = None,  # Filler words
    function_fillers: Optional[List[str]] = None, # Processing phrases
    language_order: int = 0  # Priority order
) -> 'AgentBase'
```

Add a supported language with voice configuration.

### set_voice

```python
def set_voice(
    self,
    voice: str  # Voice ID
) -> 'AgentBase'
```

Set the default voice for the agent.

## Tool Definition Methods

### tool (decorator)

```python
@agent.tool(
    name: str = None,           # Function name (default: function name)
    description: str = "",      # Function description
    secure: bool = False,       # Require token authentication
    fillers: List[str] = None,  # Processing phrases
    wait_file: str = None       # Audio file URL for hold
)
def my_function(args...) -> SwaigFunctionResult:
    ...
```

Decorator to register a SWAIG function.

### define_tool

```python
def define_tool(
    self,
    name: str,                          # Function name
    description: str,                   # Function description
    handler: Callable,                  # Function handler
    parameters: Dict[str, Any] = None,  # Parameter schema
    secure: bool = False,               # Require authentication
    fillers: List[str] = None,          # Processing phrases
    wait_file: str = None               # Hold audio URL
) -> 'AgentBase'
```

Programmatically define a SWAIG function.

## Skill Methods

### add_skill

```python
def add_skill(
    self,
    skill_name: str,               # Skill identifier
    params: Dict[str, Any] = None  # Skill configuration
) -> 'AgentBase'
```

Add a skill to the agent.

### list_available_skills

```python
def list_available_skills(self) -> List[str]
```

List all available skills.

## AI Configuration Methods

### set_params

```python
def set_params(
    self,
    params: Dict[str, Any]  # AI parameters
) -> 'AgentBase'
```

Set AI model parameters (temperature, top_p, etc.).

### add_hints

```python
def add_hints(
    self,
    hints: List[str]  # Speech recognition hints
) -> 'AgentBase'
```

Add speech recognition hints.

### add_pronounce

```python
def add_pronounce(
    self,
    patterns: List[Dict[str, str]]  # Pronunciation rules
) -> 'AgentBase'
```

Add pronunciation rules.

## State Methods

### set_global_data

```python
def set_global_data(
    self,
    data: Dict[str, Any]  # Data to store
) -> 'AgentBase'
```

Set initial global data for the agent session.

## URL Methods

### get_full_url

```python
def get_full_url(
    self,
    include_auth: bool = False  # Include credentials in URL
) -> str
```

Get the full URL for the agent endpoint.

### set_web_hook_url

```python
def set_web_hook_url(
    self,
    url: str  # Webhook URL
) -> 'AgentBase'
```

Override the default webhook URL.

### set_post_prompt_url

```python
def set_post_prompt_url(
    self,
    url: str  # Post-prompt URL
) -> 'AgentBase'
```

Override the post-prompt summary URL.

## Server Methods

### run

```python
def run(
    self,
    host: str = None,  # Override host
    port: int = None   # Override port
) -> None
```

Start the development server.

### get_app

```python
def get_app(self) -> FastAPI
```

Get the FastAPI application instance.

## Serverless Methods

### serverless_handler

```python
def serverless_handler(
    self,
    event: Dict[str, Any],  # Lambda event
    context: Any            # Lambda context
) -> Dict[str, Any]
```

Handle AWS Lambda invocations.

### cloud_function_handler

```python
def cloud_function_handler(
    self,
    request  # Flask request
) -> Response
```

Handle Google Cloud Function invocations.

### azure_function_handler

```python
def azure_function_handler(
    self,
    req  # Azure HttpRequest
) -> HttpResponse
```

Handle Azure Function invocations.

## Callback Methods

### on_summary

```python
def on_summary(
    self,
    summary: Optional[Dict[str, Any]],  # Summary data
    raw_data: Optional[Dict[str, Any]] = None  # Raw POST data
) -> None
```

Override to handle post-prompt summaries.

### set_dynamic_config_callback

```python
def set_dynamic_config_callback(
    self,
    callback: Callable  # Config callback
) -> 'AgentBase'
```

Set a callback for dynamic configuration.

## SIP Routing Methods

### enable_sip_routing

```python
def enable_sip_routing(
    self,
    auto_map: bool = True,  # Auto-map usernames
    path: str = "/sip"      # Routing endpoint path
) -> 'AgentBase'
```

Enable SIP-based routing.

### register_sip_username

```python
def register_sip_username(
    self,
    sip_username: str  # SIP username
) -> 'AgentBase'
```

Register a SIP username for routing.

## Method Chaining

All setter methods return `self` for method chaining:

```python
from signalwire_agents import AgentBase
from signalwire_agents.core.function_result import SwaigFunctionResult

agent = (
    AgentBase(name="assistant", route="/assistant")
    .add_language("English", "en-US", "rime.spore")
    .add_hints(["SignalWire", "SWML", "SWAIG"])
    .set_params({"temperature": 0.7})
    .set_global_data({"user_tier": "standard"})
)

@agent.tool(description="Get help")
def get_help(topic: str) -> SwaigFunctionResult:
    return SwaigFunctionResult(f"Help for {topic}")

if __name__ == "__main__":
    agent.run()
```

## Class Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `PROMPT_SECTIONS` | List[Dict] | Declarative prompt sections |
| `name` | str | Agent name |
| `route` | str | HTTP route path |
| `host` | str | Bind host |
| `port` | int | Bind port |
| `agent_id` | str | Unique agent identifier |
| `pom` | PromptObject | POM instance (if use_pom=True) |
| `skill_manager` | SkillManager | Skill manager instance |



---

## SWMLService API

> **Summary**: API reference for SWMLService, the base class for creating and serving SWML documents.

### Class Definition

```python
from signalwire_agents.core.swml_service import SWMLService

class SWMLService:
    """Base class for creating and serving SWML documents."""
```

### Constructor

```python
SWMLService(
    name: str,                              # Service name (required)
    route: str = "/",                       # HTTP route path
    host: str = "0.0.0.0",                  # Host to bind
    port: int = 3000,                       # Port to bind
    basic_auth: Optional[Tuple[str, str]] = None,  # (username, password)
    schema_path: Optional[str] = None,      # SWML schema path
    config_file: Optional[str] = None       # Config file path
)
```

### Core Responsibilities

**SWML Generation:**
- Create and validate SWML documents
- Add verbs to document sections
- Render complete SWML JSON output

**Web Server:**
- Serve SWML documents via FastAPI
- Handle SWAIG webhook callbacks
- Manage authentication

**Schema Validation:**
- Load and validate SWML schema
- Auto-generate verb methods from schema
- Validate document structure

### Document Methods

#### reset_document

```python
def reset_document(self) -> None
```

Reset the SWML document to a clean state.

#### add_verb

```python
def add_verb(
    self,
    verb_name: str,           # Verb name (e.g., "ai", "play")
    params: Dict[str, Any]    # Verb parameters
) -> 'SWMLService'
```

Add a verb to the current document section.

#### get_document

```python
def get_document(self) -> Dict[str, Any]
```

Get the current SWML document as a dictionary.

#### render

```python
def render(self) -> str
```

Render the SWML document as a JSON string.

### Auto-Generated Verb Methods

SWMLService automatically generates methods for all SWML verbs defined in the schema:

```python
## These methods are auto-generated from schema
service.ai(...)          # AI verb
service.play(...)        # Play audio
service.record(...)      # Record audio
service.connect(...)     # Connect call
service.transfer(...)    # Transfer call
service.hangup(...)      # End call
service.sleep(...)       # Pause execution
## ... many more
```

### Server Methods

#### run

```python
def run(
    self,
    host: str = None,  # Override host
    port: int = None   # Override port
) -> None
```

Start the development server.

#### get_app

```python
def get_app(self) -> FastAPI
```

Get the FastAPI application instance.

### Authentication Methods

#### get_basic_auth_credentials

```python
def get_basic_auth_credentials(self) -> Tuple[str, str]
```

Get the current basic auth credentials.

### URL Building Methods

#### _build_full_url

```python
def _build_full_url(
    self,
    endpoint: str = "",           # Endpoint path
    include_auth: bool = False    # Include credentials
) -> str
```

Build a full URL for an endpoint.

#### _build_webhook_url

```python
def _build_webhook_url(
    self,
    endpoint: str,                    # Endpoint path
    query_params: Dict[str, str] = None  # Query parameters
) -> str
```

Build a webhook URL with authentication.

### Routing Methods

#### register_routing_callback

```python
def register_routing_callback(
    self,
    callback: Callable,   # Routing callback
    path: str = "/"       # Path to register
) -> None
```

Register a routing callback for dynamic request handling.

### Security Configuration

| Attribute | Type | Description |
|-----------|------|-------------|
| `ssl_enabled` | bool | Whether SSL is enabled |
| `domain` | str | Domain for SSL certificates |
| `ssl_cert_path` | str | Path to SSL certificate |
| `ssl_key_path` | str | Path to SSL private key |
| `security` | SecurityConfig | Unified security configuration |

### Schema Utils

The `schema_utils` attribute provides access to SWML schema validation:

```python
## Access schema utilities
service.schema_utils.validate(document)
service.schema_utils.get_all_verb_names()
service.schema_utils.get_verb_schema("ai")
```

### Verb Registry

The `verb_registry` manages SWML verb handlers:

```python
## Access verb registry
service.verb_registry.register_handler("custom_verb", handler)
service.verb_registry.get_handler("ai")
```

### Instance Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `name` | str | Service name |
| `route` | str | HTTP route path |
| `host` | str | Bind host |
| `port` | int | Bind port |
| `schema_utils` | SchemaUtils | Schema validation utilities |
| `verb_registry` | VerbRegistry | Verb handler registry |
| `log` | Logger | Structured logger |

### Usage Example

```python
from signalwire_agents.core.swml_service import SWMLService


## Create a basic SWML service
service = SWMLService(
    name="my-service",
    route="/swml",
    port=8080
)

## Add verbs to build a document
service.reset_document()
service.play(url="https://example.com/welcome.mp3")
service.ai(
    prompt={"text": "You are a helpful assistant"},
    SWAIG={"functions": []}
)

## Get the rendered SWML
swml_json = service.render()
print(swml_json)
```

### Relationship to AgentBase

AgentBase extends SWMLService with higher-level abstractions:

**SWMLService provides:**
- SWML document generation
- Schema validation
- Basic web server
- Authentication

**AgentBase adds:**
- Prompt management (POM)
- Tool/function definitions
- Skills system
- AI configuration
- Serverless support
- State management



---

## SWAIG Function API

> **Summary**: API reference for defining SWAIG functions using decorators and programmatic methods.

### Overview

SWAIG (SignalWire AI Gateway) functions are the primary way for AI agents to perform actions and retrieve information during conversations.

**SWAIG Function Flow:**

```
User speaks → AI decides to call function → Webhook invoked → Result
```

1. AI determines a function should be called based on conversation
2. SignalWire invokes the webhook with function arguments
3. Function executes and returns SwaigFunctionResult
4. AI uses the result to continue the conversation

### Decorator Syntax

#### Basic Usage

```python
from signalwire_agents import AgentBase
from signalwire_agents.core.function_result import SwaigFunctionResult

agent = AgentBase(name="my-agent")

@agent.tool(description="Search for information")
def search(query: str) -> SwaigFunctionResult:
    results = perform_search(query)
    return SwaigFunctionResult(f"Found: {results}")
```

#### Decorator Parameters

```python
@agent.tool(
    name: str = None,           # Function name (default: function name)
    description: str = "",      # Function description (required)
    secure: bool = False,       # Require token authentication
    fillers: List[str] = None,  # Phrases to say while processing
    wait_file: str = None,      # Audio URL to play while processing
    meta_data: Dict = None,     # Custom metadata
    meta_data_token: str = None # Token for metadata access
)
```

### Decorator Parameter Details

| Parameter | Type | Description |
|-----------|------|-------------|
| `name` | str | Override function name |
| `description` | str | What the function does (shown to AI) |
| `secure` | bool | Require per-call token authentication |
| `fillers` | List[str] | Phrases like "Let me check on that..." |
| `wait_file` | str | Hold music URL during processing |
| `meta_data` | Dict | Static metadata for the function |
| `meta_data_token` | str | Token scope for metadata access |

### Parameter Types

Function parameters are automatically converted to JSON Schema:

```python
@agent.tool(description="Book a reservation")
def book_reservation(
    name: str,                    # Required string
    party_size: int,              # Required integer
    date: str,                    # Required string
    time: str = "7:00 PM",        # Optional with default
    special_requests: str = None  # Optional, nullable
) -> SwaigFunctionResult:
    ...
```

Generated parameter schema:

```json
{
  "type": "object",
  "properties": {
    "name": {"type": "string", "description": "name parameter"},
    "party_size": {"type": "integer", "description": "party_size parameter"},
    "date": {"type": "string", "description": "date parameter"},
    "time": {"type": "string", "description": "time parameter"},
    "special_requests": {"type": "string", "description": "special_requests parameter"}
  },
  "required": ["name", "party_size", "date"]
}
```

### Type Mapping

| Python Type | JSON Schema Type | Notes |
|-------------|------------------|-------|
| `str` | string | Basic string |
| `int` | integer | Whole numbers |
| `float` | number | Decimal numbers |
| `bool` | boolean | True/False |
| `list` | array | List of items |
| `dict` | object | Key-value pairs |
| `Optional[T]` | T (nullable) | Optional parameter |

### Programmatic Definition

#### define_tool Method

```python
agent.define_tool(
    name="search",
    description="Search for information",
    parameters={
        "type": "object",
        "properties": {
            "query": {
                "type": "string",
                "description": "Search query"
            },
            "limit": {
                "type": "integer",
                "description": "Maximum results",
                "default": 10
            }
        },
        "required": ["query"]
    },
    handler=search_handler,
    secure=False,
    fillers=["Searching now..."]
)
```

### Handler Function Signature

Handler functions receive parsed arguments and raw data:

```python
def my_handler(
    args: Dict[str, Any],      # Parsed function arguments
    raw_data: Dict[str, Any]   # Complete POST data
) -> SwaigFunctionResult:
    # args contains: {"query": "...", "limit": 10}
    # raw_data contains full request including metadata
    return SwaigFunctionResult("Result")
```

### Raw Data Contents

The `raw_data` parameter contains:

```json
{
    "function": "function_name",
    "argument": {
        "parsed": [{"name": "...", "value": "..."}]
    },
    "call_id": "uuid-call-id",
    "global_data": {"key": "value"},
    "meta_data": {"key": "value"},
    "caller_id_name": "Caller Name",
    "caller_id_number": "+15551234567",
    "ai_session_id": "uuid-session-id"
}
```

### Accessing Raw Data

```python
@agent.tool(description="Process order")
def process_order(order_id: str, args=None, raw_data=None) -> SwaigFunctionResult:
    # Get global data
    global_data = raw_data.get("global_data", {})
    user_id = global_data.get("user_id")

    # Get caller info
    caller_number = raw_data.get("caller_id_number")

    # Get session info
    call_id = raw_data.get("call_id")

    return SwaigFunctionResult(f"Order {order_id} processed")
```

### Secure Functions

Secure functions require token authentication per call:

```python
@agent.tool(
    description="Access sensitive data",
    secure=True
)
def get_account_info(account_id: str) -> SwaigFunctionResult:
    # This function requires a valid token
    return SwaigFunctionResult(f"Account info for {account_id}")
```

### Fillers and Wait Files

Keep users engaged during processing:

```python
## Text fillers - AI speaks these while processing
@agent.tool(
    description="Search database",
    fillers=[
        "Let me search for that...",
        "One moment please...",
        "Checking our records..."
    ]
)
def search_database(query: str) -> SwaigFunctionResult:
    ...

## Wait file - Play audio while processing
@agent.tool(
    description="Long operation",
    wait_file="https://example.com/hold_music.mp3"
)
def long_operation(data: str) -> SwaigFunctionResult:
    ...
```

### Return Value Requirements

**IMPORTANT**: All SWAIG functions MUST return `SwaigFunctionResult`:

```python
## Correct
@agent.tool(description="Get info")
def get_info(id: str) -> SwaigFunctionResult:
    return SwaigFunctionResult("Information retrieved")

## WRONG - Never return plain strings
@agent.tool(description="Get info")
def get_info(id: str) -> str:
    return "Information retrieved"  # This will fail!
```

### Complete Example

```python
#!/usr/bin/env python3
## order_functions_agent.py - Agent with various SWAIG function patterns
from signalwire_agents import AgentBase
from signalwire_agents.core.function_result import SwaigFunctionResult

agent = AgentBase(name="order-agent", route="/orders")

## Simple function
@agent.tool(description="Get order status")
def get_order_status(order_id: str) -> SwaigFunctionResult:
    status = lookup_order(order_id)
    return SwaigFunctionResult(f"Order {order_id} is {status}")

## Function with multiple parameters
@agent.tool(description="Place a new order")
def place_order(
    product: str,
    quantity: int = 1,
    shipping: str = "standard"
) -> SwaigFunctionResult:
    order_id = create_order(product, quantity, shipping)
    return SwaigFunctionResult(f"Order {order_id} placed successfully")

## Secure function with fillers
@agent.tool(
    description="Cancel an order",
    secure=True,
    fillers=["Let me process that cancellation..."]
)
def cancel_order(order_id: str, reason: str = None) -> SwaigFunctionResult:
    cancel_result = do_cancel(order_id, reason)
    return SwaigFunctionResult(f"Order {order_id} has been cancelled")

## Function that returns actions
@agent.tool(description="Transfer to support")
def transfer_to_support(issue_type: str) -> SwaigFunctionResult:
    return (
        SwaigFunctionResult("I'll transfer you to our support team")
        .connect("+15551234567", final=True)
    )

if __name__ == "__main__":
    agent.run()
```



---

## SwaigFunctionResult API

> **Summary**: Complete API reference for SwaigFunctionResult, the class for returning responses and actions from SWAIG functions.

### Class Definition

```python
from signalwire_agents.core.function_result import SwaigFunctionResult

class SwaigFunctionResult:
    """Wrapper around SWAIG function responses."""
```

### Constructor

```python
SwaigFunctionResult(
    response: Optional[str] = None,  # Text for AI to speak
    post_process: bool = False       # Let AI respond before actions
)
```

### Core Concept

| Component | Purpose |
|-----------|---------|
| `response` | Text the AI should say back to the user |
| `action` | List of structured actions to execute |
| `post_process` | Let AI respond once more before executing actions |

**Post-Processing Behavior:**

- `post_process=False` (default): Execute actions immediately
- `post_process=True`: AI responds first, then actions execute

### Basic Methods

#### set_response

```python
def set_response(self, response: str) -> 'SwaigFunctionResult'
```

Set the response text.

#### set_post_process

```python
def set_post_process(self, post_process: bool) -> 'SwaigFunctionResult'
```

Set post-processing behavior.

#### add_action

```python
def add_action(self, name: str, data: Any) -> 'SwaigFunctionResult'
```

Add a single action.

#### add_actions

```python
def add_actions(self, actions: List[Dict[str, Any]]) -> 'SwaigFunctionResult'
```

Add multiple actions.

### Call Control Actions

#### connect

```python
def connect(
    self,
    destination: str,              # Phone number or SIP address
    final: bool = True,            # Permanent (True) or temporary (False)
    from_addr: Optional[str] = None  # Caller ID override
) -> 'SwaigFunctionResult'
```

Transfer the call to another destination.

```python
## Permanent transfer
return SwaigFunctionResult("Transferring you now").connect("+15551234567")

## Temporary transfer (returns to agent when far end hangs up)
return SwaigFunctionResult("Connecting you").connect("+15551234567", final=False)

## With custom caller ID
return SwaigFunctionResult("Transferring").connect(
    "support@company.com",
    final=True,
    from_addr="+15559876543"
)
```

#### hangup

```python
def hangup(self) -> 'SwaigFunctionResult'
```

End the call.

```python
return SwaigFunctionResult("Goodbye!").hangup()
```

#### hold

```python
def hold(self, timeout: int = 300) -> 'SwaigFunctionResult'
```

Put the call on hold (max 900 seconds).

```python
return SwaigFunctionResult("Please hold").hold(timeout=120)
```

#### stop

```python
def stop(self) -> 'SwaigFunctionResult'
```

Stop agent execution.

```python
return SwaigFunctionResult("Stopping now").stop()
```

### Speech Actions

#### say

```python
def say(self, text: str) -> 'SwaigFunctionResult'
```

Make the agent speak specific text.

```python
return SwaigFunctionResult().say("Important announcement!")
```

#### wait_for_user

```python
def wait_for_user(
    self,
    enabled: Optional[bool] = None,  # Enable/disable
    timeout: Optional[int] = None,   # Seconds to wait
    answer_first: bool = False       # Special mode
) -> 'SwaigFunctionResult'
```

Control how agent waits for user input.

```python
return SwaigFunctionResult("Take your time").wait_for_user(timeout=30)
```

### Data Actions

#### update_global_data

```python
def update_global_data(self, data: Dict[str, Any]) -> 'SwaigFunctionResult'
```

Update global session data.

```python
return SwaigFunctionResult("Account verified").update_global_data({
    "verified": True,
    "user_id": "12345"
})
```

#### remove_global_data

```python
def remove_global_data(self, keys: Union[str, List[str]]) -> 'SwaigFunctionResult'
```

Remove keys from global data.

```python
return SwaigFunctionResult("Cleared").remove_global_data(["temp_data", "cache"])
```

#### set_metadata

```python
def set_metadata(self, data: Dict[str, Any]) -> 'SwaigFunctionResult'
```

Set metadata scoped to the function's token.

```python
return SwaigFunctionResult("Saved").set_metadata({"last_action": "search"})
```

#### remove_metadata

```python
def remove_metadata(self, keys: Union[str, List[str]]) -> 'SwaigFunctionResult'
```

Remove metadata keys.

### Media Actions

#### play_background_file

```python
def play_background_file(
    self,
    filename: str,       # Audio/video URL
    wait: bool = False   # Suppress attention-getting
) -> 'SwaigFunctionResult'
```

Play background audio.

```python
return SwaigFunctionResult().play_background_file(
    "https://example.com/music.mp3",
    wait=True
)
```

#### stop_background_file

```python
def stop_background_file(self) -> 'SwaigFunctionResult'
```

Stop background playback.

### Recording Actions

#### record_call

```python
def record_call(
    self,
    control_id: Optional[str] = None,  # Recording identifier
    stereo: bool = False,              # Stereo recording
    format: str = "wav",               # "wav", "mp3", or "mp4"
    direction: str = "both",           # "speak", "listen", or "both"
    terminators: Optional[str] = None, # Digits to stop recording
    beep: bool = False,                # Play beep before recording
    input_sensitivity: float = 44.0,   # Input sensitivity
    initial_timeout: float = 0.0,      # Wait for speech start
    end_silence_timeout: float = 0.0,  # Silence before ending
    max_length: Optional[float] = None,  # Max duration
    status_url: Optional[str] = None   # Status webhook URL
) -> 'SwaigFunctionResult'
```

Start call recording.

```python
return SwaigFunctionResult("Recording started").record_call(
    control_id="main_recording",
    stereo=True,
    format="mp3"
)
```

#### stop_record_call

```python
def stop_record_call(
    self,
    control_id: Optional[str] = None  # Recording to stop
) -> 'SwaigFunctionResult'
```

Stop recording.

### Messaging Actions

#### send_sms

```python
def send_sms(
    self,
    to_number: str,                    # Destination (E.164)
    from_number: str,                  # Sender (E.164)
    body: Optional[str] = None,        # Message text
    media: Optional[List[str]] = None, # Media URLs
    tags: Optional[List[str]] = None,  # Tags for searching
    region: Optional[str] = None       # Origin region
) -> 'SwaigFunctionResult'
```

Send SMS message.

```python
return SwaigFunctionResult("Confirmation sent").send_sms(
    to_number="+15551234567",
    from_number="+15559876543",
    body="Your order has been confirmed!"
)
```

### Payment Actions

#### pay

```python
def pay(
    self,
    payment_connector_url: str,        # Payment endpoint (required)
    input_method: str = "dtmf",        # "dtmf" or "voice"
    payment_method: str = "credit-card",
    timeout: int = 5,                  # Digit timeout
    max_attempts: int = 1,             # Retry attempts
    security_code: bool = True,        # Prompt for CVV
    postal_code: Union[bool, str] = True,  # Prompt for zip
    charge_amount: Optional[str] = None,   # Amount to charge
    currency: str = "usd",
    language: str = "en-US",
    voice: str = "woman",
    valid_card_types: str = "visa mastercard amex",
    ai_response: Optional[str] = None  # Post-payment response
) -> 'SwaigFunctionResult'
```

Process payment.

```python
return SwaigFunctionResult("Processing payment").pay(
    payment_connector_url="https://pay.example.com/process",
    charge_amount="49.99",
    currency="usd"
)
```

### Context Actions

#### swml_change_step

```python
def swml_change_step(self, step_name: str) -> 'SwaigFunctionResult'
```

Change conversation step.

```python
return SwaigFunctionResult("Moving to confirmation").swml_change_step("confirm")
```

#### swml_change_context

```python
def swml_change_context(self, context_name: str) -> 'SwaigFunctionResult'
```

Change conversation context.

```python
return SwaigFunctionResult("Switching to support").swml_change_context("support")
```

#### switch_context

```python
def switch_context(
    self,
    system_prompt: Optional[str] = None,  # New system prompt
    user_prompt: Optional[str] = None,    # User message to add
    consolidate: bool = False,            # Summarize conversation
    full_reset: bool = False              # Complete reset
) -> 'SwaigFunctionResult'
```

Advanced context switching.

### Conference Actions

#### join_room

```python
def join_room(self, name: str) -> 'SwaigFunctionResult'
```

Join a RELAY room.

#### join_conference

```python
def join_conference(
    self,
    name: str,                    # Conference name (required)
    muted: bool = False,          # Join muted
    beep: str = "true",           # Beep config
    start_on_enter: bool = True,  # Start when joining
    end_on_exit: bool = False,    # End when leaving
    max_participants: int = 250,  # Max attendees
    record: str = "do-not-record" # Recording mode
) -> 'SwaigFunctionResult'
```

Join audio conference.

### Tap/Stream Actions

#### tap

```python
def tap(
    self,
    uri: str,                        # Destination URI (required)
    control_id: Optional[str] = None,
    direction: str = "both",         # "speak", "hear", "both"
    codec: str = "PCMU",             # "PCMU" or "PCMA"
    rtp_ptime: int = 20
) -> 'SwaigFunctionResult'
```

Start media tap/stream.

#### stop_tap

```python
def stop_tap(self, control_id: Optional[str] = None) -> 'SwaigFunctionResult'
```

Stop media tap.

### SIP Actions

#### sip_refer

```python
def sip_refer(self, to_uri: str) -> 'SwaigFunctionResult'
```

Send SIP REFER for call transfer.

### Advanced Actions

#### execute_swml

```python
def execute_swml(
    self,
    swml_content,           # String, Dict, or SWML object
    transfer: bool = False  # Exit agent after execution
) -> 'SwaigFunctionResult'
```

Execute raw SWML.

```python
swml_doc = {
    "version": "1.0.0",
    "sections": {
        "main": [{"play": {"url": "https://example.com/audio.mp3"}}]
    }
}
return SwaigFunctionResult().execute_swml(swml_doc)
```

#### toggle_functions

```python
def toggle_functions(
    self,
    function_toggles: List[Dict[str, Any]]
) -> 'SwaigFunctionResult'
```

Enable/disable specific functions.

```python
return SwaigFunctionResult("Functions updated").toggle_functions([
    {"function": "transfer_call", "active": True},
    {"function": "cancel_order", "active": False}
])
```

### Settings Actions

#### update_settings

```python
def update_settings(self, settings: Dict[str, Any]) -> 'SwaigFunctionResult'
```

Update AI runtime settings.

```python
return SwaigFunctionResult().update_settings({
    "temperature": 0.5,
    "confidence": 0.8
})
```

#### set_end_of_speech_timeout

```python
def set_end_of_speech_timeout(self, milliseconds: int) -> 'SwaigFunctionResult'
```

Adjust speech detection timeout.

### Method Chaining

All methods return `self` for chaining:

```python
return (
    SwaigFunctionResult("Processing your order")
    .update_global_data({"order_id": "12345"})
    .send_sms(
        to_number="+15551234567",
        from_number="+15559876543",
        body="Order confirmed!"
    )
    .swml_change_step("confirmation")
)
```

### to_dict Method

```python
def to_dict(self) -> Dict[str, Any]
```

Convert to SWAIG response format. Called automatically when returning from functions.



---

## DataMap API

> **Summary**: API reference for DataMap, enabling serverless REST API integration without webhooks.

### Class Definition

```python
from signalwire_agents.core.data_map import DataMap

class DataMap:
    """Builder class for creating SWAIG data_map configurations."""
```

### Overview

DataMap enables SWAIG functions that execute on SignalWire servers without requiring your own webhook endpoints.

**Use Cases:**
- Call external APIs directly from SWML
- Pattern-based responses without API calls
- Reduce infrastructure requirements
- Serverless function execution

### Constructor

```python
DataMap(function_name: str)
```

Create a new DataMap builder.

### Core Methods

#### purpose / description

```python
def purpose(self, description: str) -> 'DataMap'
def description(self, description: str) -> 'DataMap'  # Alias
```

Set the function description shown to the AI.

```python
data_map = DataMap("get_weather").purpose("Get current weather for a city")
```

#### parameter

```python
def parameter(
    self,
    name: str,                      # Parameter name
    param_type: str,                # JSON schema type
    description: str,               # Parameter description
    required: bool = False,         # Is required
    enum: Optional[List[str]] = None  # Allowed values
) -> 'DataMap'
```

Add a function parameter.

```python
data_map = (
    DataMap("search")
    .purpose("Search for items")
    .parameter("query", "string", "Search query", required=True)
    .parameter("limit", "integer", "Max results", required=False)
    .parameter("category", "string", "Category filter",
               enum=["electronics", "clothing", "food"])
)
```

### Parameter Types

| Type | JSON Schema | Description |
|------|-------------|-------------|
| string | string | Text values |
| integer | integer | Whole numbers |
| number | number | Decimal numbers |
| boolean | boolean | True/False |
| array | array | List of items |
| object | object | Key-value pairs |

### Webhook Methods

#### webhook

```python
def webhook(
    self,
    method: str,                          # HTTP method
    url: str,                             # API endpoint
    headers: Optional[Dict[str, str]] = None,  # HTTP headers
    form_param: Optional[str] = None,     # Form parameter name
    input_args_as_params: bool = False,   # Merge args to params
    require_args: Optional[List[str]] = None  # Required args
) -> 'DataMap'
```

Add an API call.

```python
data_map = (
    DataMap("get_weather")
    .purpose("Get weather information")
    .parameter("city", "string", "City name", required=True)
    .webhook("GET", "https://api.weather.com/v1/current?q=${enc:args.city}&key=API_KEY")
)
```

#### body

```python
def body(self, data: Dict[str, Any]) -> 'DataMap'
```

Set request body for POST/PUT.

```python
data_map = (
    DataMap("create_ticket")
    .purpose("Create support ticket")
    .parameter("subject", "string", "Ticket subject", required=True)
    .parameter("message", "string", "Ticket message", required=True)
    .webhook("POST", "https://api.support.com/tickets",
             headers={"Authorization": "Bearer TOKEN"})
    .body({
        "subject": "${args.subject}",
        "body": "${args.message}",
        "priority": "normal"
    })
)
```

#### params

```python
def params(self, data: Dict[str, Any]) -> 'DataMap'
```

Set request parameters (alias for body).

### Output Methods

#### output

```python
def output(self, result: SwaigFunctionResult) -> 'DataMap'
```

Set the output for the most recent webhook.

```python
from signalwire_agents.core.function_result import SwaigFunctionResult

data_map = (
    DataMap("get_weather")
    .purpose("Get weather")
    .parameter("city", "string", "City", required=True)
    .webhook("GET", "https://api.weather.com/current?q=${enc:args.city}")
    .output(SwaigFunctionResult(
        "The weather in ${args.city} is ${response.condition} with a temperature of ${response.temp}°F"
    ))
)
```

#### fallback_output

```python
def fallback_output(self, result: SwaigFunctionResult) -> 'DataMap'
```

Set output when all webhooks fail.

```python
data_map = (
    DataMap("search")
    .purpose("Search multiple sources")
    .webhook("GET", "https://api.primary.com/search?q=${enc:args.query}")
    .output(SwaigFunctionResult("Found: ${response.title}"))
    .webhook("GET", "https://api.backup.com/search?q=${enc:args.query}")
    .output(SwaigFunctionResult("Backup result: ${response.title}"))
    .fallback_output(SwaigFunctionResult("Sorry, search is unavailable"))
)
```

### Variable Patterns

| Pattern | Description |
|---------|-------------|
| `${args.param}` | Function argument value |
| `${enc:args.param}` | URL-encoded argument (use in webhook URLs) |
| `${lc:args.param}` | Lowercase argument value |
| `${fmt_ph:args.phone}` | Format as phone number |
| `${response.field}` | API response field |
| `${response.arr[0]}` | Array element in response |
| `${global_data.key}` | Global session data |
| `${meta_data.key}` | Call metadata |
| `${this.field}` | Current item in foreach |

#### Chained Modifiers

Modifiers are applied right-to-left:

| Pattern | Result |
|---------|--------|
| `${enc:lc:args.param}` | First lowercase, then URL encode |
| `${lc:enc:args.param}` | First URL encode, then lowercase |

#### Examples

| Pattern | Result |
|---------|--------|
| `${args.city}` | "Seattle" (in body/output) |
| `${enc:args.city}` | "Seattle" URL-encoded (in URLs) |
| `${lc:args.city}` | "seattle" (lowercase) |
| `${enc:lc:args.city}` | "seattle" lowercased then URL-encoded |
| `${fmt_ph:args.phone}` | "+1 (555) 123-4567" |
| `${response.temp}` | "65" |
| `${response.items[0].name}` | "First item" |
| `${global_data.user_id}` | "user123" |

### Expression Methods

#### expression

```python
def expression(
    self,
    test_value: str,                        # Template to test
    pattern: Union[str, Pattern],           # Regex pattern
    output: SwaigFunctionResult,            # Match output
    nomatch_output: Optional[SwaigFunctionResult] = None  # No-match output
) -> 'DataMap'
```

Add pattern-based response (no API call needed).

```python
data_map = (
    DataMap("control_playback")
    .purpose("Control media playback")
    .parameter("command", "string", "Playback command", required=True)
    .expression(
        "${args.command}",
        r"play|start",
        SwaigFunctionResult("Starting playback").add_action("playback_bg", "music.mp3")
    )
    .expression(
        "${args.command}",
        r"stop|pause",
        SwaigFunctionResult("Stopping playback").add_action("stop_playback_bg", True)
    )
)
```

### Array Processing

#### foreach

```python
def foreach(self, foreach_config: Dict[str, Any]) -> 'DataMap'
```

Process array from API response.

```python
data_map = (
    DataMap("search_products")
    .purpose("Search product catalog")
    .parameter("query", "string", "Search query", required=True)
    .webhook("GET", "https://api.store.com/products?q=${enc:args.query}")
    .foreach({
        "input_key": "products",
        "output_key": "product_list",
        "max": 3,
        "append": "- ${this.name}: $${this.price}\n"
    })
    .output(SwaigFunctionResult("Found products:\n${product_list}"))
)
```

### Foreach Configuration

| Key | Type | Description |
|-----|------|-------------|
| `input_key` | string | Key in response containing array |
| `output_key` | string | Variable name for built string |
| `max` | integer | Maximum items to process (optional) |
| `append` | string | Template for each item |

### Webhook Expressions

#### webhook_expressions

```python
def webhook_expressions(
    self,
    expressions: List[Dict[str, Any]]
) -> 'DataMap'
```

Add expressions to run after webhook completes.

### Registering with Agent

```python
from signalwire_agents import AgentBase
from signalwire_agents.core.data_map import DataMap
from signalwire_agents.core.function_result import SwaigFunctionResult

agent = AgentBase(name="weather-agent")

## Create DataMap
weather_map = (
    DataMap("get_weather")
    .purpose("Get current weather for a location")
    .parameter("city", "string", "City name", required=True)
    .webhook("GET", "https://api.weather.com/v1/current?q=${enc:args.city}&key=YOUR_KEY")
    .output(SwaigFunctionResult(
        "The weather in ${args.city} is ${response.current.condition.text} "
        "with ${response.current.temp_f}°F"
    ))
)

## Register with agent - convert DataMap to SWAIG function dictionary
agent.register_swaig_function(weather_map.to_swaig_function())
```

### Complete Example

```python
#!/usr/bin/env python3
## datamap_api_agent.py - Agent using DataMap for API calls
from signalwire_agents import AgentBase
from signalwire_agents.core.data_map import DataMap
from signalwire_agents.core.function_result import SwaigFunctionResult

agent = AgentBase(name="api-agent", route="/api")
agent.add_language("English", "en-US", "rime.spore")

## Weather lookup
weather = (
    DataMap("check_weather")
    .purpose("Check weather conditions")
    .parameter("location", "string", "City or zip code", required=True)
    .webhook("GET", "https://api.weather.com/v1/current?q=${enc:args.location}")
    .output(SwaigFunctionResult(
        "Current conditions in ${args.location}: ${response.condition}, ${response.temp}°F"
    ))
    .fallback_output(SwaigFunctionResult("Weather service is currently unavailable"))
)

## Order status lookup
order_status = (
    DataMap("check_order")
    .purpose("Check order status")
    .parameter("order_id", "string", "Order number", required=True)
    .webhook("GET", "https://api.orders.com/status/${enc:args.order_id}",
             headers={"Authorization": "Bearer ${env.API_KEY}"})
    .output(SwaigFunctionResult(
        "Order ${args.order_id}: ${response.status}. "
        "Expected delivery: ${response.delivery_date}"
    ))
)

## Expression-based control
volume_control = (
    DataMap("set_volume")
    .purpose("Control audio volume")
    .parameter("level", "string", "Volume level", required=True)
    .expression("${args.level}", r"high|loud|up",
                SwaigFunctionResult("Volume increased").add_action("volume", 100))
    .expression("${args.level}", r"low|quiet|down",
                SwaigFunctionResult("Volume decreased").add_action("volume", 30))
    .expression("${args.level}", r"mute|off",
                SwaigFunctionResult("Audio muted").add_action("mute", True))
)

## Register all - convert DataMap to SWAIG function dictionary
agent.register_swaig_function(weather.to_swaig_function())
agent.register_swaig_function(order_status.to_swaig_function())
agent.register_swaig_function(volume_control.to_swaig_function())

if __name__ == "__main__":
    agent.run()
```



---

## SkillBase API

> **Summary**: API reference for SkillBase, the abstract base class for creating custom agent skills.

### Class Definition

```python
from signalwire_agents.core.skill_base import SkillBase

class SkillBase(ABC):
    """Abstract base class for all agent skills."""
```

### Overview

Skills are modular, reusable capabilities that can be added to agents.

**Features:**
- Auto-discovered from skill directories
- Automatic dependency validation
- Configuration via parameters
- Can add tools, prompts, hints, and global data

### Class Attributes

```python
class MySkill(SkillBase):
    # Required attributes
    SKILL_NAME: str = "my_skill"           # Unique identifier
    SKILL_DESCRIPTION: str = "Description" # Human-readable description

    # Optional attributes
    SKILL_VERSION: str = "1.0.0"           # Semantic version
    REQUIRED_PACKAGES: List[str] = []      # Python packages needed
    REQUIRED_ENV_VARS: List[str] = []      # Environment variables needed
    SUPPORTS_MULTIPLE_INSTANCES: bool = False  # Allow multiple instances
```

### Class Attributes Reference

| Attribute | Type | Required | Description |
|-----------|------|----------|-------------|
| `SKILL_NAME` | str | Yes | Unique identifier |
| `SKILL_DESCRIPTION` | str | Yes | Description |
| `SKILL_VERSION` | str | No | Version string |
| `REQUIRED_PACKAGES` | List[str] | No | Package dependencies |
| `REQUIRED_ENV_VARS` | List[str] | No | Required env vars |
| `SUPPORTS_MULTIPLE_INSTANCES` | bool | No | Multiple instances |

### Constructor

```python
def __init__(
    self,
    agent: 'AgentBase',                    # Parent agent
    params: Optional[Dict[str, Any]] = None  # Skill configuration
)
```

### Instance Attributes

```python
self.agent      # Reference to parent AgentBase
self.params     # Configuration parameters dict
self.logger     # Skill-specific logger
self.swaig_fields  # SWAIG metadata to merge into tools
```

### Abstract Methods (Must Implement)

#### setup

```python
@abstractmethod
def setup(self) -> bool:
    """
    Setup the skill.

    Returns:
        True if setup successful, False otherwise
    """
    pass
```

Validate environment, initialize APIs, prepare resources.

#### register_tools

```python
@abstractmethod
def register_tools(self) -> None:
    """Register SWAIG tools with the agent."""
    pass
```

Register functions that the skill provides.

### Helper Methods

#### define_tool

```python
def define_tool(self, **kwargs) -> None
```

Register a tool with automatic `swaig_fields` merging.

```python
def register_tools(self):
    self.define_tool(
        name="my_search",
        description="Search functionality",
        handler=self._handle_search,
        parameters={
            "type": "object",
            "properties": {
                "query": {"type": "string", "description": "Search query"}
            },
            "required": ["query"]
        }
    )
```

#### validate_env_vars

```python
def validate_env_vars(self) -> bool
```

Check if all required environment variables are set.

#### validate_packages

```python
def validate_packages(self) -> bool
```

Check if all required Python packages are available.

### Optional Override Methods

#### get_hints

```python
def get_hints(self) -> List[str]:
    """Return speech recognition hints for this skill."""
    return []
```

#### get_global_data

```python
def get_global_data(self) -> Dict[str, Any]:
    """Return data to add to agent's global context."""
    return {}
```

#### get_prompt_sections

```python
def get_prompt_sections(self) -> List[Dict[str, Any]]:
    """Return prompt sections to add to agent."""
    return []
```

#### cleanup

```python
def cleanup(self) -> None:
    """Cleanup when skill is removed or agent shuts down."""
    pass
```

#### get_instance_key

```python
def get_instance_key(self) -> str:
    """Get unique key for this skill instance."""
    pass
```

### Parameter Schema

#### get_parameter_schema

```python
@classmethod
def get_parameter_schema(cls) -> Dict[str, Dict[str, Any]]:
    """Get parameter schema for this skill."""
    pass
```

Define configuration parameters:

```python
@classmethod
def get_parameter_schema(cls):
    schema = super().get_parameter_schema()
    schema.update({
        "api_key": {
            "type": "string",
            "description": "API key for service",
            "required": True,
            "hidden": True,
            "env_var": "MY_API_KEY"
        },
        "max_results": {
            "type": "integer",
            "description": "Maximum results to return",
            "default": 10,
            "min": 1,
            "max": 100
        }
    })
    return schema
```

### Parameter Schema Fields

| Field | Type | Description |
|-------|------|-------------|
| `type` | string | Parameter type (string, integer, number, etc.) |
| `description` | string | Human-readable description |
| `default` | any | Default value if not provided |
| `required` | bool | Whether parameter is required |
| `hidden` | bool | Hide in UIs (for secrets) |
| `env_var` | string | Environment variable alternative |
| `enum` | list | List of allowed values |
| `min/max` | number | Min/max for numeric types |

### Complete Skill Example

```python
from signalwire_agents.core.skill_base import SkillBase
from signalwire_agents.core.function_result import SwaigFunctionResult
from typing import Dict, Any, List
import os


class WeatherSkill(SkillBase):
    """Skill for weather lookups."""

    SKILL_NAME = "weather"
    SKILL_DESCRIPTION = "Provides weather information"
    SKILL_VERSION = "1.0.0"
    REQUIRED_PACKAGES = ["requests"]
    REQUIRED_ENV_VARS = ["WEATHER_API_KEY"]

    def setup(self) -> bool:
        """Initialize the weather skill."""
        # Validate dependencies
        if not self.validate_packages():
            return False
        if not self.validate_env_vars():
            return False

        # Store API key
        self.api_key = os.getenv("WEATHER_API_KEY")
        return True

    def register_tools(self) -> None:
        """Register weather tools."""
        self.define_tool(
            name="get_weather",
            description="Get current weather for a location",
            handler=self._get_weather,
            parameters={
                "type": "object",
                "properties": {
                    "location": {
                        "type": "string",
                        "description": "City name or zip code"
                    }
                },
                "required": ["location"]
            }
        )

    def _get_weather(self, args: Dict, raw_data: Dict) -> SwaigFunctionResult:
        """Handle weather lookup."""
        import requests

        location = args.get("location")
        url = f"https://api.weather.com/v1/current?q={location}&key={self.api_key}"

        try:
            response = requests.get(url)
            data = response.json()
            return SwaigFunctionResult(
                f"Weather in {location}: {data['condition']}, {data['temp']}°F"
            )
        except Exception as e:
            return SwaigFunctionResult(f"Unable to get weather: {str(e)}")

    def get_hints(self) -> List[str]:
        """Speech recognition hints."""
        return ["weather", "temperature", "forecast", "sunny", "rainy"]

    def get_prompt_sections(self) -> List[Dict[str, Any]]:
        """Add weather instructions to prompt."""
        return [{
            "title": "Weather Information",
            "body": "You can check weather for any location using the get_weather function."
        }]

    @classmethod
    def get_parameter_schema(cls):
        schema = super().get_parameter_schema()
        schema.update({
            "units": {
                "type": "string",
                "description": "Temperature units",
                "default": "fahrenheit",
                "enum": ["fahrenheit", "celsius"]
            }
        })
        return schema
```

### Using Skills

```python
from signalwire_agents import AgentBase

agent = AgentBase(name="weather-agent")

## Add skill with default configuration
agent.add_skill("weather")

## Add skill with custom configuration
agent.add_skill("weather", {
    "units": "celsius"
})

## List available skills
print(agent.list_available_skills())
```

### Skill Directory Structure

```
signalwire_agents/skills/
   weather/
      __init__.py
      skill.py          # WeatherSkill class
      requirements.txt  # Skill-specific dependencies
   calendar/
      __init__.py
      skill.py
      requirements.txt
   ...
```



---

## ContextBuilder API

> **Summary**: API reference for ContextBuilder and Step classes, enabling multi-step conversation workflows.

### Class Definitions

```python
from signalwire_agents.core.contexts import ContextBuilder, Step
```

### Overview

Contexts define structured conversation workflows with multiple steps.

**Context Structure:**
- **Context** - A named conversation workflow
  - **Steps** - Sequential conversation phases
    - Prompt text or POM sections
    - Completion criteria
    - Available functions
    - Navigation rules

### Step Class

#### Constructor

```python
Step(name: str)  # Step name/identifier
```

#### set_text

```python
def set_text(self, text: str) -> 'Step'
```

Set the step's prompt text directly.

```python
step = Step("greeting")
step.set_text("Welcome the caller and ask how you can help.")
```

#### add_section

```python
def add_section(self, title: str, body: str) -> 'Step'
```

Add a POM section to the step.

```python
step = Step("collect_info")
step.add_section("Task", "Collect the caller's name and phone number.")
step.add_section("Guidelines", "Be polite and patient.")
```

#### add_bullets

```python
def add_bullets(self, title: str, bullets: List[str]) -> 'Step'
```

Add a section with bullet points.

```python
step.add_bullets("Requirements", [
    "Get full legal name",
    "Verify phone number",
    "Confirm email address"
])
```

#### set_step_criteria

```python
def set_step_criteria(self, criteria: str) -> 'Step'
```

Define when this step is complete.

```python
step.set_step_criteria(
    "Step is complete when caller has provided their name and phone number."
)
```

#### set_functions

```python
def set_functions(self, functions: Union[str, List[str]]) -> 'Step'
```

Set which functions are available in this step.

```python
## Disable all functions
step.set_functions("none")

## Allow specific functions
step.set_functions(["lookup_account", "verify_identity"])
```

#### set_valid_steps

```python
def set_valid_steps(self, steps: List[str]) -> 'Step'
```

Set which steps can be navigated to.

```python
step.set_valid_steps(["confirmation", "error_handling"])
```

#### set_valid_contexts

```python
def set_valid_contexts(self, contexts: List[str]) -> 'Step'
```

Set which contexts can be navigated to.

```python
step.set_valid_contexts(["support", "billing"])
```

### Step Context Switch Methods

#### set_reset_system_prompt

```python
def set_reset_system_prompt(self, system_prompt: str) -> 'Step'
```

Set system prompt for context switching.

#### set_reset_user_prompt

```python
def set_reset_user_prompt(self, user_prompt: str) -> 'Step'
```

Set user prompt for context switching.

#### set_reset_consolidate

```python
def set_reset_consolidate(self, consolidate: bool) -> 'Step'
```

Set whether to consolidate conversation on context switch.

#### set_reset_full_reset

```python
def set_reset_full_reset(self, full_reset: bool) -> 'Step'
```

Set whether to do full reset on context switch.

### ContextBuilder Class

#### Constructor

```python
ContextBuilder()
```

Create a new context builder.

#### add_context

```python
def add_context(
    self,
    name: str,           # Context name
    steps: List[Step]    # List of steps
) -> 'ContextBuilder'
```

Add a context with its steps.

```python
builder = ContextBuilder()
builder.add_context("main", [
    Step("greeting").set_text("Greet the caller"),
    Step("collect").set_text("Collect information"),
    Step("confirm").set_text("Confirm details")
])
```

#### set_default_context

```python
def set_default_context(self, name: str) -> 'ContextBuilder'
```

Set the default starting context.

```python
builder.set_default_context("main")
```

#### build

```python
def build(self) -> Dict[str, Any]
```

Build the contexts structure for SWML.

### Using with AgentBase

```python
from signalwire_agents import AgentBase
from signalwire_agents.core.contexts import ContextBuilder, Step

agent = AgentBase(name="workflow-agent")

## Create context builder
builder = ContextBuilder()

## Define steps for main context
greeting = (
    Step("greeting")
    .set_text("Welcome the caller and ask how you can help today.")
    .set_functions("none")
    .set_valid_steps(["collect_info"])
)

collect = (
    Step("collect_info")
    .add_section("Task", "Collect the caller's information.")
    .add_bullets("Required Information", [
        "Full name",
        "Account number",
        "Reason for calling"
    ])
    .set_step_criteria("Complete when all information is collected.")
    .set_functions(["lookup_account"])
    .set_valid_steps(["process", "error"])
)

process = (
    Step("process")
    .set_text("Process the caller's request based on collected information.")
    .set_valid_steps(["farewell"])
)

farewell = (
    Step("farewell")
    .set_text("Thank the caller and end the conversation.")
    .set_functions("none")
)

## Add context
builder.add_context("main", [greeting, collect, process, farewell])
builder.set_default_context("main")

## Apply to agent
agent.set_contexts(builder)
```

### Multiple Contexts Example

```python
builder = ContextBuilder()

## Main menu context
main_steps = [
    Step("menu")
    .set_text("Present options: sales, support, or billing.")
    .set_valid_contexts(["sales", "support", "billing"])
]
builder.add_context("main", main_steps)

## Sales context
sales_steps = [
    Step("qualify")
    .set_text("Understand what product the caller is interested in.")
    .set_functions(["check_inventory", "get_pricing"])
    .set_valid_steps(["quote"]),

    Step("quote")
    .set_text("Provide pricing and availability.")
    .set_valid_steps(["close"]),

    Step("close")
    .set_text("Close the sale or schedule follow-up.")
    .set_valid_contexts(["main"])
]
builder.add_context("sales", sales_steps)

## Support context
support_steps = [
    Step("diagnose")
    .set_text("Understand the customer's issue.")
    .set_functions(["lookup_account", "check_status"])
    .set_valid_steps(["resolve"]),

    Step("resolve")
    .set_text("Resolve the issue or escalate.")
    .set_functions(["create_ticket", "transfer_call"])
    .set_valid_contexts(["main"])
]
builder.add_context("support", support_steps)

builder.set_default_context("main")
```

### Step Flow Diagram

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                        Step Navigation                                      │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  Context: main                                                              │
│                                                                             │
│  ┌──────────┐   ┌──────────┐   ┌──────────┐   ┌──────────┐                  │
│  │ greeting │ → │ collect  │ → │ process  │ → │ farewell │                  │
│  └──────────┘   └──────────┘   └──────────┘   └──────────┘                  │
│                      │                                                      │
│                      ▼                                                      │
│                 ┌──────────┐                                                │
│                 │  error   │                                                │
│                 └──────────┘                                                │
│                                                                             │
│  Navigation:                                                                │
│  • set_valid_steps: Control which steps can be reached                      │
│  • set_valid_contexts: Control which contexts can be reached                │
│  • AI uses swml_change_step() or swml_change_context() to navigate          │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Generated SWML Structure

The contexts system generates SWML with this structure:

```json
{
  "version": "1.0.0",
  "sections": {
    "main": [{
      "ai": {
        "contexts": {
          "default": "main",
          "main": {
            "steps": [
              {
                "name": "greeting",
                "text": "Welcome the caller...",
                "functions": "none",
                "valid_steps": ["collect_info"]
              },
              {
                "name": "collect_info",
                "text": "## Task\nCollect information...",
                "step_criteria": "Complete when...",
                "functions": ["lookup_account"],
                "valid_steps": ["process", "error"]
              }
            ]
          }
        }
      }
    }]
  }
}
```



---

## swaig-test CLI

> **Summary**: Command-line tool for testing agents and SWAIG functions locally without deploying to production.

### Overview

The `swaig-test` tool loads agent files and allows you to:

- Generate and inspect SWML output
- Test SWAIG functions with arguments
- Simulate serverless environments (Lambda, CGI, Cloud Functions, Azure)
- Debug agent configuration and dynamic behavior
- Test DataMap functions with live webhook calls
- Execute functions with mock call data

### Command Syntax

```bash
swaig-test <agent_path> [options]
```

### Quick Reference

| Command | Purpose |
|---------|---------|
| `swaig-test agent.py` | List available tools |
| `swaig-test agent.py --dump-swml` | Generate SWML document |
| `swaig-test agent.py --list-tools` | List all SWAIG functions |
| `swaig-test agent.py --list-agents` | List agents in multi-agent file |
| `swaig-test agent.py --exec fn --arg val` | Execute a function |
| `swaig-test agent.py --help-examples` | Show comprehensive examples |
| `swaig-test agent.py --help-platforms` | Show serverless platform options |

### Basic Usage

```bash
## Generate SWML document (pretty printed)
swaig-test agent.py --dump-swml

## Generate raw JSON for piping to jq
swaig-test agent.py --dump-swml --raw | jq '.'

## List all SWAIG functions
swaig-test agent.py --list-tools

## Execute a function with CLI-style arguments
swaig-test agent.py --exec search --query "AI agents" --limit 5

## Execute with verbose output
swaig-test agent.py --verbose --exec search --query "test"
```

### Actions

Choose one action per command:

| Action | Description |
|--------|-------------|
| `--list-agents` | List all agents in the file |
| `--list-tools` | List all SWAIG functions in the agent |
| `--dump-swml` | Generate and output SWML document |
| `--exec FUNCTION` | Execute a function with CLI arguments |
| (default) | If no action specified, defaults to `--list-tools` |

### Common Options

| Option | Description |
|--------|-------------|
| `-v, --verbose` | Enable verbose output with debug information |
| `--raw` | Output raw JSON only (for piping to jq) |
| `--agent-class NAME` | Specify agent class for multi-agent files |
| `--route PATH` | Specify agent by route (e.g., /healthcare) |

### SWML Generation

#### Basic Generation

```bash
## Pretty-printed SWML
swaig-test agent.py --dump-swml

## Raw JSON for processing
swaig-test agent.py --dump-swml --raw

## Pretty-print with jq
swaig-test agent.py --dump-swml --raw | jq '.'
```

#### Extract Specific Fields

```bash
## Extract SWAIG functions
swaig-test agent.py --dump-swml --raw | jq '.sections.main[1].ai.SWAIG.functions'

## Extract prompt
swaig-test agent.py --dump-swml --raw | jq '.sections.main[1].ai.prompt'

## Extract languages
swaig-test agent.py --dump-swml --raw | jq '.sections.main[1].ai.languages'
```

#### Generate with Fake Call Data

```bash
## With comprehensive fake call data (call_id, from, to, etc.)
swaig-test agent.py --dump-swml --fake-full-data

## Customize call configuration
swaig-test agent.py --dump-swml --call-type sip --from-number +15551234567
```

### SWML Generation Options

| Option | Default | Description |
|--------|---------|-------------|
| `--call-type` | webrtc | Call type: sip or webrtc |
| `--call-direction` | inbound | Call direction: inbound or outbound |
| `--call-state` | created | Call state value |
| `--from-number` | (none) | Override from/caller number |
| `--to-extension` | (none) | Override to/extension number |
| `--fake-full-data` | false | Use comprehensive fake post_data |

### Function Execution

#### CLI-Style Arguments (Recommended)

```bash
## Simple function call
swaig-test agent.py --exec search --query "AI agents"

## Multiple arguments
swaig-test agent.py --exec book_reservation \
  --name "John Doe" \
  --date "2025-01-20" \
  --party_size 4

## With verbose output
swaig-test agent.py --verbose --exec search --query "test"
```

#### Type Conversion

Arguments are automatically converted:

| Type | Example | Notes |
|------|---------|-------|
| String | `--name "John Doe"` | Quoted or unquoted |
| Integer | `--count 5` | Numeric values |
| Float | `--threshold 0.75` | Decimal values |
| Boolean | `--active true` | true/false |

#### Legacy JSON Syntax

Still supported for backwards compatibility:

```bash
swaig-test agent.py search '{"query": "AI agents", "limit": 5}'
```

### Function Execution Options

| Option | Description |
|--------|-------------|
| `--minimal` | Use minimal post_data (function args only) |
| `--fake-full-data` | Use comprehensive fake call data |
| `--custom-data` | JSON string with custom post_data overrides |

### Multi-Agent Files

When a file contains multiple agent classes:

```bash
## List all agents in file
swaig-test multi_agent.py --list-agents

## Use specific agent by class name
swaig-test multi_agent.py --agent-class SalesAgent --list-tools
swaig-test multi_agent.py --agent-class SalesAgent --dump-swml

## Use specific agent by route
swaig-test multi_agent.py --route /sales --list-tools
swaig-test multi_agent.py --route /support --exec create_ticket --issue "Login problem"
```

### Dynamic Agent Testing

Test agents that configure themselves based on request data:

```bash
## Test with query parameters
swaig-test dynamic_agent.py --dump-swml --query-params '{"tier":"premium"}'

## Test with custom headers
swaig-test dynamic_agent.py --dump-swml --header "Authorization=Bearer token123"
swaig-test dynamic_agent.py --dump-swml --header "X-Customer-ID=12345"

## Test with custom request body
swaig-test dynamic_agent.py --dump-swml --method POST --body '{"custom":"data"}'

## Test with user variables
swaig-test dynamic_agent.py --dump-swml --user-vars '{"preferences":{"language":"es"}}'

## Combined dynamic configuration
swaig-test dynamic_agent.py --dump-swml \
  --query-params '{"tier":"premium","region":"eu"}' \
  --header "X-Customer-ID=12345" \
  --user-vars '{"preferences":{"language":"es"}}'
```

### Data Customization Options

| Option | Description |
|--------|-------------|
| `--user-vars` | JSON string for userVariables |
| `--query-params` | JSON string for query parameters |
| `--header` | Add HTTP header (KEY=VALUE format) |
| `--override` | Override specific value (path.to.key=value) |
| `--override-json` | Override with JSON value (path.to.key='{"nested":true}') |

### Advanced Data Overrides

```bash
## Override specific values
swaig-test agent.py --dump-swml \
  --override call.state=answered \
  --override call.timeout=60

## Override with JSON values
swaig-test agent.py --dump-swml \
  --override-json vars.custom='{"key":"value","nested":{"data":true}}'

## Combine multiple override types
swaig-test agent.py --dump-swml \
  --call-type sip \
  --user-vars '{"vip":"true"}' \
  --header "X-Source=test" \
  --override call.project_id=my-project \
  --verbose
```

### Serverless Simulation

Test agents in simulated serverless environments:

| Platform | Value | Description |
|----------|-------|-------------|
| AWS Lambda | `lambda` | Simulates Lambda environment |
| CGI | `cgi` | Simulates CGI deployment |
| Cloud Functions | `cloud_function` | Simulates Google Cloud Functions |
| Azure Functions | `azure_function` | Simulates Azure Functions |

#### AWS Lambda Simulation

```bash
## Basic Lambda simulation
swaig-test agent.py --simulate-serverless lambda --dump-swml

## With custom Lambda configuration
swaig-test agent.py --simulate-serverless lambda \
  --aws-function-name prod-agent \
  --aws-region us-west-2 \
  --dump-swml

## With Lambda function URL
swaig-test agent.py --simulate-serverless lambda \
  --aws-function-name my-agent \
  --aws-function-url https://xxx.lambda-url.us-west-2.on.aws \
  --dump-swml

## With API Gateway
swaig-test agent.py --simulate-serverless lambda \
  --aws-api-gateway-id abc123 \
  --aws-stage prod \
  --dump-swml
```

#### AWS Lambda Options

| Option | Description |
|--------|-------------|
| `--aws-function-name` | Lambda function name |
| `--aws-function-url` | Lambda function URL |
| `--aws-region` | AWS region |
| `--aws-api-gateway-id` | API Gateway ID for API Gateway URLs |
| `--aws-stage` | API Gateway stage (default: prod) |

#### CGI Simulation

```bash
## Basic CGI (host required)
swaig-test agent.py --simulate-serverless cgi \
  --cgi-host example.com \
  --dump-swml

## CGI with HTTPS
swaig-test agent.py --simulate-serverless cgi \
  --cgi-host example.com \
  --cgi-https \
  --dump-swml

## CGI with custom script path
swaig-test agent.py --simulate-serverless cgi \
  --cgi-host example.com \
  --cgi-script-name /cgi-bin/agent.py \
  --cgi-path-info /custom/path \
  --dump-swml
```

#### CGI Options

| Option | Description |
|--------|-------------|
| `--cgi-host` | CGI server hostname (REQUIRED for CGI simulation) |
| `--cgi-script-name` | CGI script name/path |
| `--cgi-https` | Use HTTPS for CGI URLs |
| `--cgi-path-info` | CGI PATH_INFO value |

#### Google Cloud Functions Simulation

```bash
## Basic Cloud Functions
swaig-test agent.py --simulate-serverless cloud_function --dump-swml

## With project configuration
swaig-test agent.py --simulate-serverless cloud_function \
  --gcp-project my-project \
  --gcp-region us-central1 \
  --dump-swml

## With custom function URL
swaig-test agent.py --simulate-serverless cloud_function \
  --gcp-function-url https://us-central1-myproject.cloudfunctions.net/agent \
  --dump-swml
```

#### GCP Options

| Option | Description |
|--------|-------------|
| `--gcp-project` | Google Cloud project ID |
| `--gcp-function-url` | Google Cloud Function URL |
| `--gcp-region` | Google Cloud region |
| `--gcp-service` | Google Cloud service name |

#### Azure Functions Simulation

```bash
## Basic Azure Functions
swaig-test agent.py --simulate-serverless azure_function --dump-swml

## With environment
swaig-test agent.py --simulate-serverless azure_function \
  --azure-env production \
  --dump-swml

## With custom function URL
swaig-test agent.py --simulate-serverless azure_function \
  --azure-function-url https://myapp.azurewebsites.net/api/agent \
  --dump-swml
```

#### Azure Options

| Option | Description |
|--------|-------------|
| `--azure-env` | Azure Functions environment |
| `--azure-function-url` | Azure Function URL |

### Environment Variables

Set environment variables for testing:

```bash
## Set individual variables
swaig-test agent.py --simulate-serverless lambda \
  --env API_KEY=secret123 \
  --env DEBUG=1 \
  --exec my_function

## Load from environment file
swaig-test agent.py --simulate-serverless lambda \
  --env-file production.env \
  --dump-swml

## Combine both
swaig-test agent.py --simulate-serverless lambda \
  --env-file .env \
  --env API_KEY=override_key \
  --dump-swml
```

### DataMap Function Testing

DataMap functions execute their configured webhooks:

```bash
## Test DataMap function (makes actual HTTP requests)
swaig-test agent.py --exec get_weather --city "New York"

## With verbose output to see webhook details
swaig-test agent.py --verbose --exec get_weather --city "New York"
```

### Cross-Platform Testing

Compare agent behavior across serverless platforms:

```bash
## Test across all platforms
for platform in lambda cgi cloud_function azure_function; do
  echo "Testing $platform..."
  if [ "$platform" = "cgi" ]; then
    swaig-test agent.py --simulate-serverless $platform \
      --cgi-host example.com --exec my_function --param value
  else
    swaig-test agent.py --simulate-serverless $platform \
      --exec my_function --param value
  fi
done

## Compare webhook URLs across platforms
swaig-test agent.py --simulate-serverless lambda --dump-swml --raw | \
  jq '.sections.main[1].ai.SWAIG.functions[].web_hook_url'

swaig-test agent.py --simulate-serverless cgi --cgi-host example.com \
  --dump-swml --raw | jq '.sections.main[1].ai.SWAIG.functions[].web_hook_url'
```

### Output Options

| Option | Description |
|--------|-------------|
| `--raw` | Machine-readable JSON output (suppresses logs) |
| `--verbose` | Include debug information and detailed output |

### Extended Help

```bash
## Show platform-specific serverless options
swaig-test agent.py --help-platforms

## Show comprehensive usage examples
swaig-test agent.py --help-examples
```

### Complete Workflow Examples

#### Development Workflow

```bash
## 1. Inspect generated SWML
swaig-test agent.py --dump-swml --raw | jq '.'

## 2. List available functions
swaig-test agent.py --list-tools

## 3. Test a specific function
swaig-test agent.py --exec search --query "test" --verbose

## 4. Test with fake call data
swaig-test agent.py --exec book_appointment \
  --name "John" --date "2025-01-20" \
  --fake-full-data --verbose
```

#### Serverless Deployment Testing

```bash
## Test Lambda configuration
swaig-test agent.py --simulate-serverless lambda \
  --aws-function-name my-agent \
  --aws-region us-east-1 \
  --dump-swml --raw > swml.json

## Verify webhook URLs are correct
cat swml.json | jq '.sections.main[1].ai.SWAIG.functions[].web_hook_url'

## Test function execution in Lambda environment
swaig-test agent.py --simulate-serverless lambda \
  --aws-function-name my-agent \
  --exec process_order --order_id "12345" --verbose
```

#### Multi-Agent Testing

```bash
## Discover agents
swaig-test multi_agent.py --list-agents

## Test each agent
swaig-test multi_agent.py --agent-class RouterAgent --dump-swml
swaig-test multi_agent.py --agent-class SalesAgent --list-tools
swaig-test multi_agent.py --agent-class SupportAgent \
  --exec create_ticket --issue "Cannot login"
```

### Exit Codes

| Code | Meaning |
|------|---------|
| 0 | Success |
| 1 | General error (file not found, invalid args, execution error) |

### Troubleshooting

| Issue | Solution |
|-------|----------|
| Agent file not found | Check path is correct |
| Multiple agents found | Use `--agent-class` or `--route` to specify |
| Function not found | Use `--list-tools` to see available functions |
| CGI host required | Add `--cgi-host` for CGI simulation |
| Invalid JSON | Check `--query-params` and `--body` syntax |
| Import errors | Ensure all dependencies are installed |



---

## sw-search CLI

> **Summary**: Command-line tool for building, searching, and managing vector search indexes for AI agent knowledge bases.

### Overview

The `sw-search` tool builds vector search indexes from documents for use with the native_vector_search skill.

**Capabilities:**

- Build indexes from documents (MD, TXT, PDF, DOCX, RST, PY)
- Multiple chunking strategies for different content types
- SQLite and PostgreSQL/pgvector storage backends
- Interactive search shell for index exploration
- Export chunks to JSON for review or external processing
- Migrate indexes between backends
- Search via remote API endpoints

### Architecture

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   Documents     │───▶│   Index Builder  │───▶│  .swsearch DB   │
│ (MD, PDF, etc.) │    │                  │    │                 │
└─────────────────┘    └──────────────────┘    └─────────────────┘
                                                        │
                                                        ▼
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│     Agent       │───▶│  Search Skill    │───▶│  Search Engine  │
│                 │    │                  │    │                 │
└─────────────────┘    └──────────────────┘    └─────────────────┘
```

The system provides:

- **Offline Search**: No external API calls or internet required
- **Hybrid Search**: Combines vector similarity and keyword search
- **Smart Chunking**: Intelligent document segmentation with context preservation
- **Advanced Query Processing**: NLP-enhanced query understanding
- **Flexible Deployment**: Local embedded mode or remote server mode
- **SQLite Storage**: Portable `.swsearch` index files

### Command Modes

sw-search operates in five modes:

| Mode | Syntax | Purpose |
|------|--------|---------|
| build | `sw-search ./docs` | Build search index |
| search | `sw-search search FILE QUERY` | Search existing index |
| validate | `sw-search validate FILE` | Validate index integrity |
| migrate | `sw-search migrate FILE` | Migrate between backends |
| remote | `sw-search remote URL QUERY` | Search via remote API |

### Quick Start

```bash
## Build index from documentation
sw-search ./docs --output knowledge.swsearch

## Search the index
sw-search search knowledge.swsearch "how to create an agent"

## Interactive search shell
sw-search search knowledge.swsearch --shell

## Validate index
sw-search validate knowledge.swsearch
```

### Building Indexes

#### Index Structure

Each `.swsearch` file is a SQLite database containing:

- **Document chunks** with embeddings and metadata
- **Full-text search index** (SQLite FTS5) for keyword search
- **Configuration** and model information
- **Synonym cache** for query expansion

This portable format allows you to build indexes once and distribute them with your agents.

#### Basic Usage

```bash
## Build from single directory
sw-search ./docs

## Build from multiple directories
sw-search ./docs ./examples --file-types md,txt,py

## Build from individual files
sw-search README.md ./docs/guide.md ./src/main.py

## Mixed sources (directories and files)
sw-search ./docs README.md ./examples specific_file.txt

## Specify output file
sw-search ./docs --output ./knowledge.swsearch
```

#### Build Options

| Option | Default | Description |
|--------|---------|-------------|
| `--output FILE` | sources.swsearch | Output file or collection |
| `--output-dir DIR` | (none) | Output directory |
| `--output-format` | index | Output: index or json |
| `--backend` | sqlite | Storage: sqlite or pgvector |
| `--file-types` | md,txt,rst | Comma-separated extensions |
| `--exclude` | (none) | Glob patterns to exclude |
| `--languages` | en | Language codes |
| `--tags` | (none) | Tags for all chunks |
| `--validate` | false | Validate after building |
| `--verbose` | false | Detailed output |

### Chunking Strategies

Choose the right strategy for your content:

| Strategy | Best For | Key Options |
|----------|----------|-------------|
| sentence | General prose, articles | `--max-sentences-per-chunk` |
| sliding | Code, technical documentation | `--chunk-size`, `--overlap-size` |
| paragraph | Structured documents | (none) |
| page | PDFs with distinct pages | (none) |
| semantic | Coherent topic grouping | `--semantic-threshold` |
| topic | Long documents by subject | `--topic-threshold` |
| qa | Question-answering apps | (none) |
| markdown | Documentation with code blocks | (preserves structure) |
| json | Pre-chunked content | (none) |

#### Sentence Chunking (Default)

Groups sentences together:

```bash
## Default: 5 sentences per chunk
sw-search ./docs --chunking-strategy sentence

## Custom sentence count
sw-search ./docs \
  --chunking-strategy sentence \
  --max-sentences-per-chunk 10

## Split on multiple newlines
sw-search ./docs \
  --chunking-strategy sentence \
  --max-sentences-per-chunk 8 \
  --split-newlines 2
```

#### Sliding Window Chunking

Fixed-size chunks with overlap:

```bash
sw-search ./docs \
  --chunking-strategy sliding \
  --chunk-size 100 \
  --overlap-size 20
```

#### Paragraph Chunking

Splits on double newlines:

```bash
sw-search ./docs \
  --chunking-strategy paragraph \
  --file-types md,txt,rst
```

#### Page Chunking

Best for PDFs:

```bash
sw-search ./docs \
  --chunking-strategy page \
  --file-types pdf
```

#### Semantic Chunking

Groups semantically similar sentences:

```bash
sw-search ./docs \
  --chunking-strategy semantic \
  --semantic-threshold 0.6
```

#### Topic Chunking

Detects topic changes:

```bash
sw-search ./docs \
  --chunking-strategy topic \
  --topic-threshold 0.2
```

#### QA Chunking

Optimized for question-answering:

```bash
sw-search ./docs --chunking-strategy qa
```

#### Markdown Chunking

The `markdown` strategy is specifically designed for documentation that contains code examples. It understands markdown structure and adds rich metadata for better search results.

```bash
sw-search ./docs \
  --chunking-strategy markdown \
  --file-types md
```

**Features:**

- **Header-based chunking**: Splits at markdown headers (h1, h2, h3...) for natural boundaries
- **Code block detection**: Identifies fenced code blocks and extracts language (```python, ```bash, etc.)
- **Smart tagging**: Adds `"code"` tags to chunks with code, plus language-specific tags
- **Section hierarchy**: Preserves full path (e.g., "API Reference > AgentBase > Methods")
- **Code protection**: Never splits inside code blocks
- **Metadata enrichment**: Header levels stored as searchable metadata

**Example Metadata:**

```json
{
  "chunk_type": "markdown",
  "h1": "API Reference",
  "h2": "AgentBase",
  "h3": "add_skill Method",
  "has_code": true,
  "code_languages": ["python", "bash"],
  "tags": ["code", "code:python", "code:bash", "depth:3"]
}
```

**Search Benefits:**

When users search for "example code Python":

- Chunks with code blocks get automatic 20% boost
- Python-specific code gets language match bonus
- Vector similarity provides primary semantic ranking
- Metadata tags provide confirmation signals
- Results blend semantic + structural relevance

**Best Used With:**

- API documentation with code examples
- Tutorial content with inline code
- Technical guides with multiple languages
- README files with usage examples

**Usage with pgvector:**

```bash
sw-search ./docs \
  --backend pgvector \
  --connection-string "postgresql://user:pass@localhost:5432/db" \
  --output docs_collection \
  --chunking-strategy markdown
```

#### JSON Chunking

The `json` strategy allows you to provide pre-chunked content in a structured format. This is useful when you need custom control over how documents are split and indexed.

**Expected JSON Format:**

```json
{
  "chunks": [
    {
      "chunk_id": "unique_id",
      "type": "content",
      "content": "The actual text content",
      "metadata": {
        "section": "Introduction",
        "url": "https://example.com/docs/intro",
        "custom_field": "any_value"
      },
      "tags": ["intro", "getting-started"]
    }
  ]
}
```

**Usage:**

```bash
## First preprocess your documents into JSON chunks
python your_preprocessor.py input.txt -o chunks.json

## Then build the index using JSON strategy
sw-search chunks.json --chunking-strategy json --file-types json
```

**Best Used For:**

- API documentation with complex structure
- Documents that need custom parsing logic
- Preserving specific metadata relationships
- Integration with external preprocessing tools

### Model Selection

Choose embedding model based on speed vs quality:

| Alias | Model | Dims | Speed | Quality |
|-------|-------|------|-------|---------|
| mini | all-MiniLM-L6-v2 | 384 | ~5x | Good |
| base | all-mpnet-base-v2 | 768 | 1x | High |
| large | all-mpnet-base-v2 | 768 | 1x | Highest |

```bash
## Fast model (default, recommended for most cases)
sw-search ./docs --model mini

## Balanced model
sw-search ./docs --model base

## Best quality
sw-search ./docs --model large

## Full model name
sw-search ./docs --model sentence-transformers/all-mpnet-base-v2
```

### File Filtering

```bash
## Specific file types
sw-search ./docs --file-types md,txt,rst,py

## Exclude patterns
sw-search ./docs --exclude "**/test/**,**/__pycache__/**,**/.git/**"

## Language filtering
sw-search ./docs --languages en,es,fr
```

### Tags and Metadata

Add tags during build for filtered searching:

```bash
## Add tags to all chunks
sw-search ./docs --tags documentation,api,v2

## Filter by tags when searching
sw-search search index.swsearch "query" --tags documentation
```

### Searching Indexes

#### Basic Search

```bash
## Search with query
sw-search search knowledge.swsearch "how to create an agent"

## Limit results
sw-search search knowledge.swsearch "API reference" --count 3

## Verbose output with scores
sw-search search knowledge.swsearch "configuration" --verbose
```

#### Search Options

| Option | Default | Description |
|--------|---------|-------------|
| `--count` | 5 | Number of results |
| `--distance-threshold` | 0.0 | Minimum similarity score |
| `--tags` | (none) | Filter by tags |
| `--query-nlp-backend` | nltk | NLP backend: nltk or spacy |
| `--keyword-weight` | (auto) | Manual keyword weight (0.0-1.0) |
| `--model` | (index) | Override embedding model |
| `--json` | false | Output as JSON |
| `--no-content` | false | Hide content, show metadata only |
| `--verbose` | false | Detailed output |

#### Output Formats

```bash
## Human-readable (default)
sw-search search knowledge.swsearch "query"

## JSON output
sw-search search knowledge.swsearch "query" --json

## Metadata only
sw-search search knowledge.swsearch "query" --no-content

## Full verbose output
sw-search search knowledge.swsearch "query" --verbose
```

#### Filter by Tags

```bash
## Single tag
sw-search search knowledge.swsearch "functions" --tags documentation

## Multiple tags
sw-search search knowledge.swsearch "API" --tags api,reference
```

### Interactive Search Shell

Load index once and search multiple times:

```bash
sw-search search knowledge.swsearch --shell
```

Shell commands:

| Command | Description |
|---------|-------------|
| `help` | Show help |
| `exit`/`quit`/`q` | Exit shell |
| `count=N` | Set result count |
| `tags=tag1,tag2` | Set tag filter |
| `verbose` | Toggle verbose output |
| `<query>` | Search for query |

Example session:
```
$ sw-search search knowledge.swsearch --shell
Search Shell - Index: knowledge.swsearch
Backend: sqlite
Index contains 1523 chunks from 47 files
Model: sentence-transformers/all-MiniLM-L6-v2
Type 'exit' or 'quit' to leave, 'help' for options
------------------------------------------------------------

search> how to create an agent
Found 5 result(s) for 'how to create an agent' (0.034s):
...

search> count=3
Result count set to: 3

search> SWAIG functions
Found 3 result(s) for 'SWAIG functions' (0.028s):
...

search> exit
Goodbye!
```

### PostgreSQL/pgvector Backend

The search system supports multiple storage backends. Choose based on your deployment needs:

#### Backend Comparison

| Feature | SQLite | pgvector |
|---------|--------|----------|
| Setup complexity | None | Requires PostgreSQL |
| Scalability | Limited | Excellent |
| Concurrent access | Poor | Excellent |
| Update capability | Rebuild required | Real-time |
| Performance (small datasets) | Excellent | Good |
| Performance (large datasets) | Poor | Excellent |
| Deployment | File copy | Database connection |
| Multi-agent support | Separate copies | Shared knowledge base |

**SQLite Backend (Default):**
- File-based `.swsearch` indexes
- Portable single-file format
- No external dependencies
- Best for: Single-agent deployments, development, small to medium datasets

**pgvector Backend:**
- Server-based PostgreSQL storage
- Efficient similarity search with IVFFlat/HNSW indexes
- Multiple agents can share the same knowledge base
- Real-time updates without rebuilding
- Best for: Production deployments, multi-agent systems, large datasets

#### Building with pgvector

```bash
## Build to pgvector
sw-search ./docs \
  --backend pgvector \
  --connection-string "postgresql://user:pass@localhost:5432/knowledge" \
  --output docs_collection

## With markdown strategy
sw-search ./docs \
  --backend pgvector \
  --connection-string "postgresql://user:pass@localhost:5432/knowledge" \
  --output docs_collection \
  --chunking-strategy markdown

## Overwrite existing collection
sw-search ./docs \
  --backend pgvector \
  --connection-string "postgresql://user:pass@localhost:5432/knowledge" \
  --output docs_collection \
  --overwrite
```

#### Search pgvector Collection

```bash
sw-search search docs_collection "how to create an agent" \
  --backend pgvector \
  --connection-string "postgresql://user:pass@localhost/knowledge"
```

### Migration

Migrate indexes between backends:

```bash
## Get index information
sw-search migrate --info ./docs.swsearch

## Migrate SQLite to pgvector
sw-search migrate ./docs.swsearch --to-pgvector \
  --connection-string "postgresql://user:pass@localhost/db" \
  --collection-name docs_collection

## Migrate with overwrite
sw-search migrate ./docs.swsearch --to-pgvector \
  --connection-string "postgresql://user:pass@localhost/db" \
  --collection-name docs_collection \
  --overwrite
```

#### Migration Options

| Option | Description |
|--------|-------------|
| `--info` | Show index information |
| `--to-pgvector` | Migrate SQLite to pgvector |
| `--to-sqlite` | Migrate pgvector to SQLite (planned) |
| `--connection-string` | PostgreSQL connection string |
| `--collection-name` | Target collection name |
| `--overwrite` | Overwrite existing collection |
| `--batch-size` | Chunks per batch (default: 100) |

### Local vs Remote Modes

The search skill supports both local and remote operation modes.

#### Local Mode (Default)

Searches are performed directly in the agent process using the embedded search engine.

**Pros:**
- Faster (no network latency)
- Works offline
- Simple deployment
- Lower operational complexity

**Cons:**
- Higher memory usage per agent
- Index files must be distributed with each agent
- Updates require redeploying agents

**Configuration in Agent:**

```python
self.add_skill("native_vector_search", {
    "tool_name": "search_docs",
    "index_file": "docs.swsearch",  # Local file
    "nlp_backend": "nltk"
})
```

#### Remote Mode

Searches are performed via HTTP API to a centralized search server.

**Pros:**
- Lower memory usage per agent
- Centralized index management
- Easy updates without redeploying agents
- Better scalability for multiple agents
- Shared resources

**Cons:**
- Network dependency
- Additional infrastructure complexity
- Potential latency

**Configuration in Agent:**

```python
self.add_skill("native_vector_search", {
    "tool_name": "search_docs",
    "remote_url": "http://localhost:8001",  # Search server
    "index_name": "docs",
    "nlp_backend": "nltk"
})
```

#### Automatic Mode Detection

The skill automatically detects which mode to use:

- If `remote_url` is provided → Remote mode
- If `index_file` is provided → Local mode
- Remote mode takes priority if both are specified

#### Running a Remote Search Server

1. **Start the search server:**

```bash
python examples/search_server_standalone.py
```

2. **The server provides HTTP API:**
   - `POST /search` - Search the indexes
   - `GET /health` - Health check and available indexes
   - `POST /reload_index` - Add or reload an index

3. **Test the API:**

```bash
curl -X POST "http://localhost:8001/search" \
     -H "Content-Type: application/json" \
     -d '{"query": "how to create an agent", "index_name": "docs", "count": 3}'
```

### Remote Search CLI

Search via remote API endpoint from the command line:

```bash
## Basic remote search
sw-search remote http://localhost:8001 "how to create an agent" \
  --index-name docs

## With options
sw-search remote localhost:8001 "API reference" \
  --index-name docs \
  --count 3 \
  --verbose

## JSON output
sw-search remote localhost:8001 "query" \
  --index-name docs \
  --json
```

#### Remote Options

| Option | Default | Description |
|--------|---------|-------------|
| `--index-name` | (required) | Name of the index to search |
| `--count` | 5 | Number of results |
| `--distance-threshold` | 0.0 | Minimum similarity score |
| `--tags` | (none) | Filter by tags |
| `--timeout` | 30 | Request timeout in seconds |
| `--json` | false | Output as JSON |
| `--no-content` | false | Hide content |
| `--verbose` | false | Detailed output |

### Validation

Verify index integrity:

```bash
## Validate index
sw-search validate ./docs.swsearch

## Verbose validation
sw-search validate ./docs.swsearch --verbose
```

Output:
```
✓ Index is valid: ./docs.swsearch
  Chunks: 1523
  Files: 47

Configuration:
  embedding_model: sentence-transformers/all-MiniLM-L6-v2
  embedding_dimensions: 384
  chunking_strategy: markdown
  created_at: 2025-01-15T10:30:00
```

### JSON Export

Export chunks for review or external processing:

```bash
## Export to single JSON file
sw-search ./docs \
  --output-format json \
  --output all_chunks.json

## Export to directory (one file per source)
sw-search ./docs \
  --output-format json \
  --output-dir ./chunks/

## Build index from exported JSON
sw-search ./chunks/ \
  --chunking-strategy json \
  --file-types json \
  --output final.swsearch
```

### NLP Backend Selection

Choose NLP backend for processing:

| Backend | Speed | Quality | Install Size |
|---------|-------|---------|--------------|
| nltk | Fast | Good | Included |
| spacy | Slower | Better | Requires: `pip install signalwire-agents[search-nlp]` |

```bash
## Index with NLTK (default)
sw-search ./docs --index-nlp-backend nltk

## Index with spaCy (better quality)
sw-search ./docs --index-nlp-backend spacy

## Query with NLTK
sw-search search index.swsearch "query" --query-nlp-backend nltk

## Query with spaCy
sw-search search index.swsearch "query" --query-nlp-backend spacy
```

### Complete Configuration Example

```bash
sw-search ./docs ./examples README.md \
  --output ./knowledge.swsearch \
  --chunking-strategy sentence \
  --max-sentences-per-chunk 8 \
  --file-types md,txt,rst,py \
  --exclude "**/test/**,**/__pycache__/**" \
  --languages en,es,fr \
  --model sentence-transformers/all-mpnet-base-v2 \
  --tags documentation,api \
  --index-nlp-backend nltk \
  --validate \
  --verbose
```

### Using with Skills

After building an index, use it with the native_vector_search skill:

```python
from signalwire_agents import AgentBase

agent = AgentBase(name="search-agent")

## Add search skill with built index
agent.add_skill("native_vector_search", {
    "index_path": "./knowledge.swsearch",
    "tool_name": "search_docs",
    "tool_description": "Search the documentation"
})
```

### Output Formats

| Format | Extension | Description |
|--------|-----------|-------------|
| swsearch | .swsearch | SQLite-based portable index (default) |
| json | .json | JSON export of chunks |
| pgvector | (database) | PostgreSQL with pgvector extension |

### Installation Requirements

The search system uses optional dependencies to keep the base SDK lightweight. Choose the installation option that fits your needs:

#### Basic Search (~500MB)

```bash
pip install "signalwire-agents[search]"
```

**Includes:**
- Core search functionality
- Sentence transformers for embeddings
- SQLite FTS5 for keyword search
- Basic document processing (text, markdown)

#### Full Document Processing (~600MB)

```bash
pip install "signalwire-agents[search-full]"
```

**Adds:**
- PDF processing (PyPDF2)
- DOCX processing (python-docx)
- HTML processing (BeautifulSoup4)
- Additional file format support

#### Advanced NLP Features (~700MB)

```bash
pip install "signalwire-agents[search-nlp]"
```

**Adds:**
- spaCy for advanced text processing
- NLTK for linguistic analysis
- Enhanced query preprocessing
- Language detection

**Additional Setup Required:**

```bash
python -m spacy download en_core_web_sm
```

**Performance Note:** Advanced NLP features provide significantly better query understanding, synonym expansion, and search relevance, but are 2-3x slower than basic search. Only recommended if you have sufficient CPU power and can tolerate longer response times.

#### All Search Features (~700MB)

```bash
pip install "signalwire-agents[search-all]"
```

**Includes everything above.**

**Additional Setup Required:**

```bash
python -m spacy download en_core_web_sm
```

#### Query-Only Mode (~400MB)

```bash
pip install "signalwire-agents[search-queryonly]"
```

For agents that only need to query pre-built indexes without building new ones.

#### PostgreSQL Vector Support

```bash
pip install "signalwire-agents[pgvector]"
```

Adds PostgreSQL with pgvector extension support for production deployments.

#### NLP Backend Selection

You can choose which NLP backend to use for query processing:

| Backend | Speed | Quality | Notes |
|---------|-------|---------|-------|
| nltk | Fast (~50-100ms) | Good | Default, good for most use cases |
| spacy | Slower (~150-300ms) | Better | Better POS tagging and entity recognition |

Configure via `--index-nlp-backend` (build) or `--query-nlp-backend` (search) flags.

### API Reference

For programmatic access to the search system, use the Python API directly.

#### SearchEngine Class

```python
from signalwire_agents.search import SearchEngine

## Load an index
engine = SearchEngine("docs.swsearch")

## Perform search
results = engine.search(
    query_vector=[...],  # Optional: pre-computed query vector
    enhanced_text="search query",  # Enhanced query text
    count=5,  # Number of results
    similarity_threshold=0.0,  # Minimum similarity score
    tags=["documentation"]  # Filter by tags
)

## Get index statistics
stats = engine.get_stats()
print(f"Total chunks: {stats['total_chunks']}")
print(f"Total files: {stats['total_files']}")
```

#### IndexBuilder Class

```python
from signalwire_agents.search import IndexBuilder

## Create index builder
builder = IndexBuilder(
    model_name="sentence-transformers/all-mpnet-base-v2",
    chunk_size=500,
    chunk_overlap=50,
    verbose=True
)

## Build index
builder.build_index(
    source_dir="./docs",
    output_file="docs.swsearch",
    file_types=["md", "txt"],
    exclude_patterns=["**/test/**"],
    tags=["documentation"]
)
```

### Troubleshooting

| Issue | Solution |
|-------|----------|
| Search not available | `pip install signalwire-agents[search]` |
| pgvector errors | `pip install signalwire-agents[pgvector]` |
| PDF processing fails | `pip install signalwire-agents[search-full]` |
| spaCy not found | `pip install signalwire-agents[search-nlp]` |
| No results found | Try different chunking strategy |
| Poor search quality | Use `--model base` or larger chunks |
| Index too large | Use `--model mini`, reduce file types |
| Connection refused (remote) | Check search server is running |

### Related Documentation

- [native_vector_search Skill](05_skills/05_02_native-search-skill.md) - Using search indexes in agents
- [Skills Overview](05_skills/05_01_skills-overview.md) - Adding skills to agents
- [DataSphere Integration](08_signalwire-integration/08_05_datasphere.md) - Cloud-based search alternative

---

## Environment Variables

> **Summary**: Complete reference for all environment variables used by the SignalWire Agents SDK.

### Overview

| Category | Purpose |
|----------|---------|
| Authentication | Basic auth credentials |
| SSL/TLS | HTTPS configuration |
| Proxy | Reverse proxy settings |
| Security | Host restrictions, CORS, rate limiting |
| Logging | Log output control |
| Skills | Custom skill paths |
| Serverless | Platform-specific settings |

### Authentication Variables

| Variable | Type | Default | Description |
|----------|------|---------|-------------|
| `SWML_BASIC_AUTH_USER` | string | Auto-generated | Username for HTTP Basic Authentication |
| `SWML_BASIC_AUTH_PASSWORD` | string | Auto-generated | Password for HTTP Basic Authentication |

**Note**: If neither variable is set, credentials are auto-generated and logged at startup.

### SSL/TLS Variables

| Variable | Type | Default | Description |
|----------|------|---------|-------------|
| `SWML_SSL_ENABLED` | boolean | `false` | Enable HTTPS ("true", "1", "yes") |
| `SWML_SSL_CERT_PATH` | string | None | Path to SSL certificate file (.pem/.crt) |
| `SWML_SSL_KEY_PATH` | string | None | Path to SSL private key file (.key) |
| `SWML_DOMAIN` | string | None | Domain for SSL certs and URL generation |
| `SWML_SSL_VERIFY_MODE` | string | `CERT_REQUIRED` | SSL certificate verification mode |

### Proxy Variables

| Variable | Type | Default | Description |
|----------|------|---------|-------------|
| `SWML_PROXY_URL_BASE` | string | None | Base URL when behind reverse proxy |
| `SWML_PROXY_DEBUG` | boolean | `false` | Enable proxy request debug logging |

**Warning**: Setting `SWML_PROXY_URL_BASE` overrides SSL configuration and port settings.

### Security Variables

| Variable | Type | Default | Description |
|----------|------|---------|-------------|
| `SWML_ALLOWED_HOSTS` | string | `*` | Comma-separated allowed hosts |
| `SWML_CORS_ORIGINS` | string | `*` | Comma-separated allowed CORS origins |
| `SWML_MAX_REQUEST_SIZE` | integer | `10485760` | Maximum request size in bytes (10MB) |
| `SWML_RATE_LIMIT` | integer | `60` | Rate limit in requests per minute |
| `SWML_REQUEST_TIMEOUT` | integer | `30` | Request timeout in seconds |
| `SWML_USE_HSTS` | boolean | `true` | Enable HTTP Strict Transport Security |
| `SWML_HSTS_MAX_AGE` | integer | `31536000` | HSTS max-age in seconds (1 year) |

### Logging Variables

| Variable | Type | Default | Description |
|----------|------|---------|-------------|
| `SIGNALWIRE_LOG_MODE` | string | `auto` | Logging mode: "off", "stderr", "default", "auto" |
| `SIGNALWIRE_LOG_LEVEL` | string | `info` | Log level: "debug", "info", "warning", "error", "critical" |

### Skills Variables

| Variable | Type | Default | Description |
|----------|------|---------|-------------|
| `SIGNALWIRE_SKILL_PATHS` | string | `""` | Colon-separated paths for custom skills |

### Serverless Platform Variables

#### AWS Lambda

| Variable | Default | Description |
|----------|---------|-------------|
| `AWS_LAMBDA_FUNCTION_NAME` | `unknown` | Function name (used for URL construction and logging) |
| `AWS_LAMBDA_FUNCTION_URL` | Constructed | Function URL (if not set, constructed from region and function name) |
| `AWS_REGION` | `us-east-1` | AWS region for Lambda execution |
| `LAMBDA_TASK_ROOT` | None | Lambda environment detection variable |

#### Google Cloud Functions

| Variable | Default | Description |
|----------|---------|-------------|
| `GOOGLE_CLOUD_PROJECT` | None | Google Cloud Project ID |
| `GCP_PROJECT` | None | Alternative to `GOOGLE_CLOUD_PROJECT` |
| `GOOGLE_CLOUD_REGION` | `us-central1` | Google Cloud region |
| `FUNCTION_REGION` | Falls back to `GOOGLE_CLOUD_REGION` | Cloud function region |
| `FUNCTION_TARGET` | `unknown` | Cloud function target/entry point name |
| `K_SERVICE` | `unknown` | Knative/Cloud Run service name |
| `FUNCTION_URL` | None | Cloud function URL (used in simulation) |

#### Azure Functions

| Variable | Default | Description |
|----------|---------|-------------|
| `AZURE_FUNCTIONS_ENVIRONMENT` | None | Environment detection variable |
| `WEBSITE_SITE_NAME` | None | Azure App Service site name (used to construct URLs) |
| `AZURE_FUNCTIONS_APP_NAME` | None | Alternative to `WEBSITE_SITE_NAME` |
| `AZURE_FUNCTION_NAME` | `unknown` | Azure Function name |
| `FUNCTIONS_WORKER_RUNTIME` | None | Azure Functions worker runtime detection |
| `AzureWebJobsStorage` | None | Azure Functions storage connection detection |

#### CGI Mode

| Variable | Default | Description |
|----------|---------|-------------|
| `GATEWAY_INTERFACE` | None | CGI environment detection variable |
| `HTTP_HOST` | Falls back to `SERVER_NAME` | HTTP Host header value |
| `SERVER_NAME` | `localhost` | Server hostname |
| `SCRIPT_NAME` | `""` | CGI script path |
| `PATH_INFO` | `""` | Request path info |
| `HTTPS` | None | Set to `on` when using HTTPS |
| `HTTP_AUTHORIZATION` | None | Authorization header value |
| `REMOTE_USER` | None | Authenticated username |
| `CONTENT_LENGTH` | None | Request content length |

### Quick Reference

#### Commonly Configured

| Variable | Use Case |
|----------|----------|
| `SWML_BASIC_AUTH_USER` / `SWML_BASIC_AUTH_PASSWORD` | Set explicit credentials |
| `SWML_PROXY_URL_BASE` | When behind a reverse proxy |
| `SWML_SSL_ENABLED` / `SWML_SSL_CERT_PATH` / `SWML_SSL_KEY_PATH` | For direct HTTPS |
| `SIGNALWIRE_LOG_LEVEL` | Adjust logging verbosity |
| `SIGNALWIRE_SKILL_PATHS` | Load custom skills |

#### Production Security

| Variable | Recommendation |
|----------|----------------|
| `SWML_ALLOWED_HOSTS` | Restrict to your domain(s) |
| `SWML_CORS_ORIGINS` | Restrict to trusted origins |
| `SWML_RATE_LIMIT` | Set appropriate limit |
| `SWML_USE_HSTS` | Keep enabled (default) |

### Example .env File

```bash
## Authentication
SWML_BASIC_AUTH_USER=agent_user
SWML_BASIC_AUTH_PASSWORD=secret_password_123

## SSL Configuration
SWML_SSL_ENABLED=true
SWML_DOMAIN=agent.example.com
SWML_SSL_CERT_PATH=/etc/ssl/certs/agent.crt
SWML_SSL_KEY_PATH=/etc/ssl/private/agent.key

## Security
SWML_ALLOWED_HOSTS=agent.example.com
SWML_CORS_ORIGINS=https://app.example.com
SWML_RATE_LIMIT=100

## Logging
SIGNALWIRE_LOG_MODE=default
SIGNALWIRE_LOG_LEVEL=info

## Custom Skills
SIGNALWIRE_SKILL_PATHS=/opt/custom_skills
```

### Loading Environment Variables

```python
## Using python-dotenv
from dotenv import load_dotenv
load_dotenv()

from signalwire_agents import AgentBase
agent = AgentBase(name="my-agent")
```

```bash
## Using shell
source .env
python agent.py

## Using swaig-test
swaig-test agent.py --env-file .env --dump-swml
```

### Environment Detection

The SDK automatically detects the execution environment:

```python
from signalwire_agents.core.logging_config import get_execution_mode

mode = get_execution_mode()
## Returns: "server", "lambda", "cgi", "google_cloud_function", or "azure_function"
```



---

## Config Files

> **Summary**: Reference for YAML and JSON configuration files used by the SignalWire Agents SDK.

### Overview

The SDK supports YAML and JSON configuration files for:

- Service settings (host, port, route)
- Security configuration (auth, SSL)
- Agent-specific settings

**File Discovery Order:**

1. `{agent_name}.yaml` / `{agent_name}.json`
2. `config.yaml` / `config.json`
3. `swml.yaml` / `swml.json`

### File Formats

Both YAML and JSON are supported:

**YAML (recommended)**:
```yaml
service:
  name: my-agent
  host: 0.0.0.0
  port: 8080
  route: /agent

security:
  basic_auth:
    username: agent_user
    password: secret_password
```

**JSON**:
```json
{
  "service": {
    "name": "my-agent",
    "host": "0.0.0.0",
    "port": 8080,
    "route": "/agent"
  },
  "security": {
    "basic_auth": {
      "username": "agent_user",
      "password": "secret_password"
    }
  }
}
```

### File Discovery

The SDK searches for config files in this order:

1. Explicit path via `config_file` parameter
2. `{agent_name}.yaml` or `{agent_name}.json`
3. `config.yaml` or `config.json`
4. `swml.yaml` or `swml.json`

### Service Section

```yaml
service:
  # Agent name/identifier
  name: my-agent

  # Host to bind (default: 0.0.0.0)
  host: 0.0.0.0

  # Port to bind (default: 3000)
  port: 8080

  # HTTP route path (default: /)
  route: /agent
```

### Security Section

```yaml
security:
  # Basic authentication credentials
  basic_auth:
    username: agent_user
    password: secret_password

  # SSL/TLS configuration
  ssl:
    enabled: true
    domain: agent.example.com
    cert_path: /etc/ssl/certs/agent.crt
    key_path: /etc/ssl/private/agent.key
```

### Configuration Sections

| Section | Purpose |
|---------|---------|
| `service` | Server settings (name, host, port, route) |
| `security` | Authentication and SSL configuration |
| `agent` | Agent-specific settings |
| `skills` | Skill configurations |
| `logging` | Logging configuration |

### Agent Section

```yaml
agent:
  # Auto-answer incoming calls
  auto_answer: true

  # Enable call recording
  record_call: false
  record_format: mp4
  record_stereo: true

  # Token expiration (seconds)
  token_expiry_secs: 3600

  # Use POM for prompts
  use_pom: true
```

### Skills Section

```yaml
skills:
  # Simple skill activation
  - name: datetime

  # Skill with configuration
  - name: native_vector_search
    params:
      index_path: ./knowledge.swsearch
      tool_name: search_docs

  # Multiple instances
  - name: web_search
    params:
      tool_name: search_products
      api_key: ${SEARCH_API_KEY}
```

### Logging Section

```yaml
logging:
  # Log level
  level: info

  # Output format
  format: structured

  # Disable logging
  mode: default  # or "off"
```

### Environment Variable Substitution

Config files support environment variable substitution:

```yaml
security:
  basic_auth:
    username: ${SWML_BASIC_AUTH_USER}
    password: ${SWML_BASIC_AUTH_PASSWORD}

skills:
  - name: weather
    params:
      api_key: ${WEATHER_API_KEY}
```

### Complete Example

```yaml
## config.yaml
service:
  name: support-agent
  host: 0.0.0.0
  port: 8080
  route: /support

security:
  basic_auth:
    username: ${AUTH_USER:-support_agent}
    password: ${AUTH_PASSWORD}
  ssl:
    enabled: true
    domain: support.example.com
    cert_path: /etc/ssl/certs/support.crt
    key_path: /etc/ssl/private/support.key

agent:
  auto_answer: true
  record_call: true
  record_format: mp3
  token_expiry_secs: 7200

skills:
  - name: datetime
  - name: native_vector_search
    params:
      index_path: ./support_docs.swsearch
      tool_name: search_support
      tool_description: Search support documentation

logging:
  level: info
```

### Using Config Files

#### Explicit Path

```python
from signalwire_agents import AgentBase

agent = AgentBase(
    name="my-agent",
    config_file="/path/to/config.yaml"
)
```

#### Auto-Discovery

```python
## Will look for my-agent.yaml, config.yaml, swml.yaml
agent = AgentBase(name="my-agent")
```

### Priority Order

Configuration values are resolved in this order (highest priority first):

1. Constructor parameters
2. Environment variables
3. Config file values
4. Default values

```python
## Constructor parameter takes precedence
agent = AgentBase(
    name="my-agent",
    port=9000,  # Overrides config file
    config_file="config.yaml"
)
```

### Config Validation

The SDK validates config files on load:

- Required fields are present
- Types are correct (port is integer, etc.)
- File paths exist (for SSL certificates)
- Environment variables are defined (if referenced)

### Multiple Configurations

For multi-agent deployments:

```
project/
   agents/
      sales_agent.py
      sales_agent.yaml
      support_agent.py
      support_agent.yaml
   config.yaml  # Shared defaults
```

Each agent will load its own config file based on agent name.



---

## SWML Schema

> **Summary**: Reference for SWML (SignalWire Markup Language) document structure and validation.

### Overview

SWML (SignalWire Markup Language) is a JSON format for defining call flows and AI agent behavior.

**Key Components:**
- `version`: Schema version (always "1.0.0")
- `sections`: Named groups of verbs
- `Verbs`: Actions like ai, play, connect, transfer

### Basic Structure

```json
{
  "version": "1.0.0",
  "sections": {
    "main": [
      { "verb_name": { "param": "value" } }
    ]
  }
}
```

### Required Fields

| Field | Type | Description |
|-------|------|-------------|
| `version` | string | Must be "1.0.0" |
| `sections` | object | Contains named section arrays |
| `main` | array | Default entry section (required) |

### AI Verb

The `ai` verb creates an AI agent:

```json
{
  "version": "1.0.0",
  "sections": {
    "main": [
      {
        "ai": {
          "prompt": {
            "text": "You are a helpful assistant."
          },
          "post_prompt": {
            "text": "Summarize the conversation."
          },
          "post_prompt_url": "https://example.com/summary",
          "params": {
            "temperature": 0.7
          },
          "languages": [
            {
              "name": "English",
              "code": "en-US",
              "voice": "rime.spore"
            }
          ],
          "hints": ["SignalWire", "SWAIG"],
          "SWAIG": {
            "functions": [],
            "native_functions": [],
            "includes": []
          }
        }
      }
    ]
  }
}
```

### AI Verb Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `prompt` | object | Main prompt configuration |
| `post_prompt` | object | Summary/completion prompt |
| `post_prompt_url` | string | URL for summary delivery |
| `params` | object | AI model parameters |
| `languages` | array | Supported languages and voices |
| `hints` | array | Speech recognition hints |
| `SWAIG` | object | Function definitions |
| `pronounce` | array | Pronunciation rules |
| `global_data` | object | Initial session data |

### SWAIG Object

```json
{
  "SWAIG": {
    "functions": [
      {
        "function": "search",
        "description": "Search for information",
        "parameters": {
          "type": "object",
          "properties": {
            "query": {
              "type": "string",
              "description": "Search query"
            }
          },
          "required": ["query"]
        },
        "web_hook_url": "https://example.com/swaig"
      }
    ],
    "native_functions": [
      "check_time"
    ],
    "includes": [
      {
        "url": "https://example.com/shared_functions",
        "functions": ["shared_search", "shared_lookup"]
      }
    ]
  }
}
```

### Function Definition

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `function` | string | Yes | Function name |
| `description` | string | Yes | What the function does |
| `parameters` | object | No | JSON Schema for parameters |
| `web_hook_url` | string | * | Webhook URL (if not data_map) |
| `data_map` | object | * | DataMap definition |
| `meta_data` | object | No | Custom metadata |
| `meta_data_token` | string | No | Token scope for metadata |
| `fillers` | array | No | Processing phrases |
| `wait_file` | string | No | Hold audio URL |

### Common Verbs

#### answer

```json
{ "answer": {} }
```

#### play

```json
{
  "play": {
    "url": "https://example.com/audio.mp3"
  }
}
```

#### connect

```json
{
  "connect": {
    "to": "+15551234567",
    "from": "+15559876543"
  }
}
```

#### transfer

```json
{
  "transfer": {
    "dest": "https://example.com/other_agent"
  }
}
```

#### hangup

```json
{ "hangup": {} }
```

#### record_call

```json
{
  "record_call": {
    "stereo": true,
    "format": "mp3"
  }
}
```

#### record

```json
{
  "record": {
    "format": "mp3"
  }
}
```

### Contexts Structure

```json
{
  "version": "1.0.0",
  "sections": {
    "main": [{
      "ai": {
        "contexts": {
          "default": "main",
          "main": {
            "steps": [
              {
                "name": "greeting",
                "text": "Welcome the caller.",
                "valid_steps": ["collect"]
              },
              {
                "name": "collect",
                "text": "Collect information.",
                "functions": ["lookup_account"],
                "valid_steps": ["confirm"]
              }
            ]
          }
        }
      }
    }]
  }
}
```

### Step Structure

| Field | Type | Description |
|-------|------|-------------|
| `name` | string | Step identifier |
| `text` | string | Step prompt text |
| `step_criteria` | string | Completion criteria |
| `functions` | string \| array | "none" or list of function names |
| `valid_steps` | array | Allowed next steps |
| `valid_contexts` | array | Allowed context switches |

### DataMap Structure

```json
{
  "function": "get_weather",
  "description": "Get weather information",
  "parameters": {
    "type": "object",
    "properties": {
      "city": {
        "type": "string",
        "description": "City name"
      }
    },
    "required": ["city"]
  },
  "data_map": {
    "webhooks": [
      {
        "url": "https://api.weather.com/current?q=${enc:args.city}",
        "method": "GET",
        "output": {
          "response": "Weather: ${response.condition}"
        }
      }
    ]
  }
}
```

### Prompt Object (POM)

```json
{
  "prompt": {
    "pom": [
      {
        "section": "Role",
        "body": "You are a helpful assistant."
      },
      {
        "section": "Guidelines",
        "bullets": [
          "Be concise",
          "Be helpful",
          "Be accurate"
        ]
      }
    ]
  }
}
```

### Language Configuration

```json
{
  "languages": [
    {
      "name": "English",
      "code": "en-US",
      "voice": "rime.spore",
      "speech_fillers": ["um", "uh"],
      "function_fillers": ["Let me check..."]
    },
    {
      "name": "Spanish",
      "code": "es-ES",
      "voice": "rime.spore"
    }
  ]
}
```

### Model Parameters

```json
{
  "params": {
    "temperature": 0.7,
    "top_p": 0.9,
    "max_tokens": 150,
    "frequency_penalty": 0.0,
    "presence_penalty": 0.0,
    "confidence": 0.6,
    "barge_confidence": 0.1
  }
}
```

### Schema Validation

The SDK includes a schema.json file for validation:

```python
from signalwire_agents.utils.schema_utils import SchemaUtils

schema = SchemaUtils()
schema.validate(swml_document)
```

### Full Example

```json
{
  "version": "1.0.0",
  "sections": {
    "main": [
      { "answer": {} },
      {
        "ai": {
          "prompt": {
            "pom": [
              {
                "section": "Role",
                "body": "You are a customer service agent."
              },
              {
                "section": "Guidelines",
                "bullets": [
                  "Be helpful and professional",
                  "Verify customer identity",
                  "Resolve issues efficiently"
                ]
              }
            ]
          },
          "post_prompt": {
            "text": "Summarize the customer interaction."
          },
          "post_prompt_url": "https://example.com/swaig/summary",
          "params": {
            "temperature": 0.7
          },
          "languages": [
            {
              "name": "English",
              "code": "en-US",
              "voice": "rime.spore"
            }
          ],
          "hints": ["account", "billing", "support"],
          "SWAIG": {
            "functions": [
              {
                "function": "lookup_account",
                "description": "Look up customer account",
                "parameters": {
                  "type": "object",
                  "properties": {
                    "account_id": {
                      "type": "string",
                      "description": "Account number"
                    }
                  },
                  "required": ["account_id"]
                },
                "web_hook_url": "https://example.com/swaig"
              }
            ]
          }
        }
      }
    ]
  }
}
```




# Part: Examples

---

# Examples

> **Summary**: Practical examples organized by feature and complexity to help you build voice AI agents.

## How to Use This Chapter

This chapter provides examples organized two ways:

1. **By Feature** - Find examples demonstrating specific SDK features
2. **By Complexity** - Start simple and progressively add features

## Example Categories

### By Feature
- Basic agent setup
- SWAIG functions
- DataMap integration
- Skills usage
- Call transfers
- Context workflows
- Multi-agent servers

### By Complexity
- **Beginner** - Simple agents with basic prompts
- **Intermediate** - Functions, skills, and state management
- **Advanced** - Multi-context workflows, multi-agent systems

## Quick Start Examples

### Minimal Agent

```python
from signalwire_agents import AgentBase

agent = AgentBase(name="hello", route="/hello")
agent.prompt_add_section("Role", "You are a friendly assistant.")
agent.add_language("English", "en-US", "rime.spore")

if __name__ == "__main__":
    agent.run()
```

### Agent with Function

```python
from signalwire_agents import AgentBase
from signalwire_agents.core.function_result import SwaigFunctionResult

agent = AgentBase(name="helper", route="/helper")
agent.prompt_add_section("Role", "You help users look up information.")
agent.add_language("English", "en-US", "rime.spore")

@agent.tool(description="Look up information by ID")
def lookup(id: str) -> SwaigFunctionResult:
    # Your lookup logic here
    return SwaigFunctionResult(f"Found record {id}")

if __name__ == "__main__":
    agent.run()
```

### Agent with Transfer

```python
from signalwire_agents import AgentBase
from signalwire_agents.core.function_result import SwaigFunctionResult

agent = AgentBase(name="receptionist", route="/reception")
agent.prompt_add_section("Role", "You are a receptionist. Help callers reach the right department.")
agent.add_language("English", "en-US", "rime.spore")

@agent.tool(description="Transfer caller to support")
def transfer_to_support() -> SwaigFunctionResult:
    return (
        SwaigFunctionResult("Transferring you to support now.")
        .connect("+15551234567", final=True)
    )

if __name__ == "__main__":
    agent.run()
```

## Running Examples

```bash
# Run directly
python agent.py

# Test with swaig-test
swaig-test agent.py --dump-swml
swaig-test agent.py --list-tools
swaig-test agent.py --exec lookup --id "12345"
```

## Example Structure

Most examples follow this pattern:

```python
# 1. Imports
from signalwire_agents import AgentBase
from signalwire_agents.core.function_result import SwaigFunctionResult

# 2. Create Agent
agent = AgentBase(name="...", route="/...")

# 3. Configure
agent.prompt_add_section(...)
agent.add_language(...)
agent.add_skill(...)

# 4. Define Functions
@agent.tool(...)
def my_function(...) -> SwaigFunctionResult:
    ...

# 5. Run
if __name__ == "__main__":
    agent.run()
```

## Chapter Contents

| Section | Description |
|---------|-------------|
| [By Feature](11_01_by-feature.md) | Examples organized by SDK feature |
| [By Complexity](11_02_by-complexity.md) | Examples from beginner to advanced |

## Basic Agent Setup

### Minimal Agent

```python
from signalwire_agents import AgentBase

agent = AgentBase(name="basic", route="/basic")
agent.prompt_add_section("Role", "You are a helpful assistant.")
agent.add_language("English", "en-US", "rime.spore")

if __name__ == "__main__":
    agent.run()
```

### Class-Based Agent

```python
from signalwire_agents import AgentBase


class MyAgent(AgentBase):
    def __init__(self):
        super().__init__(name="my-agent", route="/my-agent")
        self.prompt_add_section("Role", "You are a customer service agent.")
        self.prompt_add_section("Guidelines", "Be helpful and professional.")
        self.add_language("English", "en-US", "rime.spore")


if __name__ == "__main__":
    agent = MyAgent()
    agent.run()
```

## SWAIG Functions

### Simple Function

```python
from signalwire_agents import AgentBase
from signalwire_agents.core.function_result import SwaigFunctionResult

agent = AgentBase(name="functions", route="/functions")
agent.prompt_add_section("Role", "You help users with account lookups.")
agent.add_language("English", "en-US", "rime.spore")

@agent.tool(description="Look up account information")
def get_account(account_id: str) -> SwaigFunctionResult:
    # Simulated lookup
    return SwaigFunctionResult(f"Account {account_id}: Active, balance $150.00")

if __name__ == "__main__":
    agent.run()
```

### Function with Multiple Parameters

```python
from signalwire_agents import AgentBase
from signalwire_agents.core.function_result import SwaigFunctionResult

agent = AgentBase(name="booking", route="/booking")
agent.prompt_add_section("Role", "You help users book appointments.")
agent.add_language("English", "en-US", "rime.spore")

@agent.tool(description="Book an appointment")
def book_appointment(
    name: str,
    date: str,
    time: str = "10:00 AM",
    service: str = "consultation"
) -> SwaigFunctionResult:
    return SwaigFunctionResult(
        f"Booked {service} for {name} on {date} at {time}. "
        "You will receive a confirmation."
    )

if __name__ == "__main__":
    agent.run()
```

### Secure Function

```python
from signalwire_agents import AgentBase
from signalwire_agents.core.function_result import SwaigFunctionResult

agent = AgentBase(name="secure", route="/secure")
agent.prompt_add_section("Role", "You handle sensitive account operations.")
agent.add_language("English", "en-US", "rime.spore")

@agent.tool(
    description="Update account password",
    secure=True,
    fillers=["Processing your request securely..."]
)
def update_password(
    account_id: str,
    new_password: str
) -> SwaigFunctionResult:
    # Password update logic here
    return SwaigFunctionResult("Password has been updated successfully.")

if __name__ == "__main__":
    agent.run()
```

## DataMap Integration

### Weather Lookup

```python
from signalwire_agents import AgentBase
from signalwire_agents.core.data_map import DataMap
from signalwire_agents.core.function_result import SwaigFunctionResult

agent = AgentBase(name="weather", route="/weather")
agent.prompt_add_section("Role", "You provide weather information.")
agent.add_language("English", "en-US", "rime.spore")

weather_map = (
    DataMap("get_weather")
    .purpose("Get current weather for a city")
    .parameter("city", "string", "City name", required=True)
    .webhook("GET", "https://api.weather.com/current?q=${enc:args.city}&key=YOUR_API_KEY")
    .output(SwaigFunctionResult(
        "Current weather in ${args.city}: ${response.condition}, ${response.temp} degrees F"
    ))
    .fallback_output(SwaigFunctionResult("Weather service unavailable."))
)

agent.register_swaig_function(weather_map.to_swaig_function())

if __name__ == "__main__":
    agent.run()
```

### Expression-Based Control

```python
from signalwire_agents import AgentBase
from signalwire_agents.core.data_map import DataMap
from signalwire_agents.core.function_result import SwaigFunctionResult

agent = AgentBase(name="control", route="/control")
agent.prompt_add_section("Role", "You control media playback.")
agent.add_language("English", "en-US", "rime.spore")

playback_map = (
    DataMap("media_control")
    .purpose("Control media playback")
    .parameter("command", "string", "Command: play, pause, stop", required=True)
    .expression("${args.command}", r"play|start",
        SwaigFunctionResult("Starting playback.")
        .play_background_file("https://example.com/music.mp3"))
    .expression("${args.command}", r"pause|stop",
        SwaigFunctionResult("Stopping playback.")
        .stop_background_file())
)

agent.register_swaig_function(playback_map.to_swaig_function())

if __name__ == "__main__":
    agent.run()
```

## Call Transfers

### Simple Transfer

```python
from signalwire_agents import AgentBase
from signalwire_agents.core.function_result import SwaigFunctionResult

agent = AgentBase(name="transfer", route="/transfer")
agent.prompt_add_section("Role", "You route callers to the right department.")
agent.add_language("English", "en-US", "rime.spore")

@agent.tool(description="Transfer to sales department")
def transfer_sales() -> SwaigFunctionResult:
    return (
        SwaigFunctionResult("Connecting you to our sales team.")
        .connect("+15551234567", final=True)
    )

@agent.tool(description="Transfer to support department")
def transfer_support() -> SwaigFunctionResult:
    return (
        SwaigFunctionResult("Transferring you to technical support.")
        .connect("+15559876543", final=True)
    )

if __name__ == "__main__":
    agent.run()
```

### Temporary Transfer

```python
from signalwire_agents import AgentBase
from signalwire_agents.core.function_result import SwaigFunctionResult

agent = AgentBase(name="consult", route="/consult")
agent.prompt_add_section("Role", "You help with consultations.")
agent.add_language("English", "en-US", "rime.spore")

@agent.tool(description="Connect to specialist for consultation")
def consult_specialist() -> SwaigFunctionResult:
    return (
        SwaigFunctionResult("Connecting you to a specialist. I'll be here when you're done.")
        .connect("+15551234567", final=False)  # Returns to agent after
    )

if __name__ == "__main__":
    agent.run()
```

## Skills Usage

### DateTime Skill

```python
from signalwire_agents import AgentBase

agent = AgentBase(name="datetime", route="/datetime")
agent.prompt_add_section("Role", "You provide time and date information.")
agent.add_language("English", "en-US", "rime.spore")
agent.add_skill("datetime")

if __name__ == "__main__":
    agent.run()
```

### Search Skill

```python
from signalwire_agents import AgentBase

agent = AgentBase(name="search", route="/search")
agent.prompt_add_section("Role", "You search documentation for answers.")
agent.add_language("English", "en-US", "rime.spore")
agent.add_skill("native_vector_search", {
    "index_path": "./docs.swsearch",
    "tool_name": "search_docs",
    "tool_description": "Search the documentation"
})

if __name__ == "__main__":
    agent.run()
```

## Global Data

### Setting Initial State

```python
from signalwire_agents import AgentBase
from signalwire_agents.core.function_result import SwaigFunctionResult

agent = AgentBase(name="state", route="/state")
agent.prompt_add_section("Role", "You track user preferences.")
agent.add_language("English", "en-US", "rime.spore")
agent.set_global_data({
    "user_tier": "standard",
    "preferences": {}
})

@agent.tool(description="Update user preference")
def set_preference(key: str, value: str) -> SwaigFunctionResult:
    return SwaigFunctionResult(f"Set {key} to {value}").update_global_data({
        f"preferences.{key}": value
    })

if __name__ == "__main__":
    agent.run()
```

## Recording

### Enable Call Recording

```python
from signalwire_agents import AgentBase
from signalwire_agents.core.function_result import SwaigFunctionResult

agent = AgentBase(
    name="recording",
    route="/recording",
    record_call=True,
    record_format="mp3",
    record_stereo=True
)
agent.prompt_add_section("Role", "You handle recorded conversations.")
agent.add_language("English", "en-US", "rime.spore")

@agent.tool(description="Start call recording")
def start_recording() -> SwaigFunctionResult:
    return (
        SwaigFunctionResult("Starting recording now.")
        .record_call(control_id="main", stereo=True, format="mp3")
    )

@agent.tool(description="Stop call recording")
def stop_recording() -> SwaigFunctionResult:
    return (
        SwaigFunctionResult("Recording stopped.")
        .stop_record_call(control_id="main")
    )

if __name__ == "__main__":
    agent.run()
```

## SMS Notifications

### Send Confirmation SMS

```python
from signalwire_agents import AgentBase
from signalwire_agents.core.function_result import SwaigFunctionResult

agent = AgentBase(name="sms", route="/sms")
agent.prompt_add_section("Role", "You help with appointments and send confirmations.")
agent.add_language("English", "en-US", "rime.spore")

@agent.tool(description="Send appointment confirmation via SMS")
def send_confirmation(
    phone: str,
    date: str,
    time: str
) -> SwaigFunctionResult:
    return (
        SwaigFunctionResult("Sending confirmation to your phone.")
        .send_sms(
            to_number=phone,
            from_number="+15559876543",
            body=f"Appointment confirmed for {date} at {time}."
        )
    )

if __name__ == "__main__":
    agent.run()
```

## Static Files with AgentServer

### Serving Static Files Alongside Agents

```python
#!/usr/bin/env python3
# static_files_server.py - Serve static files alongside agents
#
# Static files directory layout:
#   This script expects a "web/" directory in the same folder:
#
#   code/11_examples/
#   ├── static_files_server.py
#   └── web/
#       ├── index.html      -> served at /
#       ├── styles.css      -> served at /styles.css
#       └── app.js          -> served at /app.js
#
# Route priority:
#   /support/*  -> SupportAgent
#   /sales/*    -> SalesAgent
#   /health     -> AgentServer health check
#   /*          -> Static files (fallback)

from signalwire_agents import AgentBase, AgentServer
from pathlib import Path

HOST = "0.0.0.0"
PORT = 3000


class SupportAgent(AgentBase):
    def __init__(self):
        super().__init__(name="support", route="/support")
        self.add_language("English", "en-US", "rime.spore")
        self.prompt_add_section("Role", "You are a support agent.")


class SalesAgent(AgentBase):
    def __init__(self):
        super().__init__(name="sales", route="/sales")
        self.add_language("English", "en-US", "rime.spore")
        self.prompt_add_section("Role", "You are a sales agent.")


def create_server():
    """Create AgentServer with static file mounting."""
    server = AgentServer(host=HOST, port=PORT)
    server.register(SupportAgent(), "/support")
    server.register(SalesAgent(), "/sales")

    # Serve static files using SDK's built-in method
    web_dir = Path(__file__).parent / "web"
    if web_dir.exists():
        server.serve_static_files(str(web_dir))

    return server


if __name__ == "__main__":
    server = create_server()
    server.run()
```

## Hints and Pronunciation

### Speech Recognition Hints

```python
from signalwire_agents import AgentBase

agent = AgentBase(name="hints", route="/hints")
agent.prompt_add_section("Role", "You help with technical products.")
agent.add_language("English", "en-US", "rime.spore")
agent.add_hints([
    "SignalWire",
    "SWML",
    "SWAIG",
    "API",
    "SDK"
])

if __name__ == "__main__":
    agent.run()
```

### Pronunciation Rules

```python
from signalwire_agents import AgentBase

agent = AgentBase(name="pronounce", route="/pronounce")
agent.prompt_add_section("Role", "You discuss technical topics.")
agent.add_language("English", "en-US", "rime.spore")
agent.add_pronounce([
    {"replace": "API", "with": "A P I"},
    {"replace": "SQL", "with": "sequel"},
    {"replace": "JSON", "with": "jason"}
])

if __name__ == "__main__":
    agent.run()
```



---

## Examples by Complexity

> **Summary**: Progressive examples from simple to advanced, helping you build increasingly sophisticated agents.

### Beginner Examples

#### Hello World Agent

The simplest possible agent:

```python
#!/usr/bin/env python3
## hello_world_agent.py - Simplest possible agent
from signalwire_agents import AgentBase

agent = AgentBase(name="hello", route="/hello")
agent.prompt_add_section("Role", "Say hello and have a friendly conversation.")
agent.add_language("English", "en-US", "rime.spore")

if __name__ == "__main__":
    agent.run()
```

#### FAQ Agent

Agent that answers questions from a knowledge base:

```python
#!/usr/bin/env python3
## faq_agent.py - Agent with knowledge base
from signalwire_agents import AgentBase

agent = AgentBase(name="faq", route="/faq")
agent.prompt_add_section("Role", "Answer questions about our company.")
agent.prompt_add_section("Information", """
Our hours are Monday to Friday, 9 AM to 5 PM.
We are located at 123 Main Street.
Contact us at support@example.com.
""")
agent.add_language("English", "en-US", "rime.spore")

if __name__ == "__main__":
    agent.run()
```

#### Greeting Agent

Agent with a custom greeting:

```python
#!/usr/bin/env python3
## greeting_agent.py - Agent with custom greeting
from signalwire_agents import AgentBase

agent = AgentBase(name="greeter", route="/greeter")
agent.prompt_add_section("Role", "You are a friendly receptionist.")
agent.prompt_add_section("Greeting", """
Always start by saying: "Thank you for calling Acme Corporation. How may I help you today?"
""")
agent.add_language("English", "en-US", "rime.spore")

if __name__ == "__main__":
    agent.run()
```

### Intermediate Examples

#### Account Lookup Agent

Agent with database lookup:

```python
#!/usr/bin/env python3
## account_lookup_agent.py - Agent with database lookup
from signalwire_agents import AgentBase
from signalwire_agents.core.function_result import SwaigFunctionResult

## Simulated database
ACCOUNTS = {
    "12345": {"name": "John Doe", "balance": 150.00, "status": "active"},
    "67890": {"name": "Jane Smith", "balance": 500.00, "status": "active"},
}

agent = AgentBase(name="accounts", route="/accounts")
agent.prompt_add_section("Role", "You help customers check their account status.")
agent.prompt_add_section("Guidelines", """
- Always verify the account ID before providing information
- Be helpful and professional
- Never share information about other accounts
""")
agent.add_language("English", "en-US", "rime.spore")

@agent.tool(description="Look up account information by ID")
def lookup_account(account_id: str) -> SwaigFunctionResult:
    account = ACCOUNTS.get(account_id)
    if account:
        return SwaigFunctionResult(
            f"Account for {account['name']}: Status is {account['status']}, "
            f"balance is ${account['balance']:.2f}"
        )
    return SwaigFunctionResult("Account not found. Please check the ID and try again.")

if __name__ == "__main__":
    agent.run()
```

#### Appointment Scheduler

Agent that books appointments with confirmation:

```python
#!/usr/bin/env python3
## appointment_scheduler_agent.py - Agent that books appointments
from signalwire_agents import AgentBase
from signalwire_agents.core.function_result import SwaigFunctionResult
from datetime import datetime

appointments = []

agent = AgentBase(name="scheduler", route="/scheduler")
agent.prompt_add_section("Role", "You help customers schedule appointments.")
agent.prompt_add_section("Guidelines", """
- Collect customer name, date, and preferred time
- Confirm all details before booking
- Send SMS confirmation when booking is complete
""")
agent.add_language("English", "en-US", "rime.spore")

@agent.tool(description="Check if a time slot is available")
def check_availability(date: str, time: str) -> SwaigFunctionResult:
    # Check against existing appointments
    for apt in appointments:
        if apt["date"] == date and apt["time"] == time:
            return SwaigFunctionResult(f"Sorry, {date} at {time} is not available.")
    return SwaigFunctionResult(f"{date} at {time} is available.")

@agent.tool(description="Book an appointment")
def book_appointment(
    name: str,
    phone: str,
    date: str,
    time: str
) -> SwaigFunctionResult:
    appointments.append({
        "name": name,
        "phone": phone,
        "date": date,
        "time": time,
        "booked_at": datetime.now().isoformat()
    })
    return (
        SwaigFunctionResult(f"Appointment booked for {name} on {date} at {time}.")
        .send_sms(
            to_number=phone,
            from_number="+15559876543",
            body=f"Your appointment is confirmed for {date} at {time}."
        )
    )

if __name__ == "__main__":
    agent.run()
```

#### Department Router

Agent that routes calls to the right department:

```python
#!/usr/bin/env python3
## department_router_agent.py - Agent that routes calls
from signalwire_agents import AgentBase
from signalwire_agents.core.function_result import SwaigFunctionResult

DEPARTMENTS = {
    "sales": "+15551001001",
    "support": "+15551001002",
    "billing": "+15551001003",
    "hr": "+15551001004"
}

agent = AgentBase(name="router", route="/router")
agent.prompt_add_section("Role", "You are a receptionist routing calls.")
agent.prompt_add_section("Departments", """
Available departments:

- Sales: Product inquiries, pricing, quotes
- Support: Technical help, troubleshooting
- Billing: Payments, invoices, refunds
- HR: Employment, benefits, careers
""")
agent.add_language("English", "en-US", "rime.spore")

@agent.tool(description="Transfer to a specific department")
def transfer_to_department(department: str) -> SwaigFunctionResult:
    dept_lower = department.lower()
    if dept_lower in DEPARTMENTS:
        return (
            SwaigFunctionResult(f"Transferring you to {department} now.")
            .connect(DEPARTMENTS[dept_lower], final=True)
        )
    return SwaigFunctionResult(
        f"I don't have a {department} department. "
        "Available departments are: sales, support, billing, and HR."
    )

if __name__ == "__main__":
    agent.run()
```

### Advanced Examples

#### Multi-Skill Agent

Agent combining multiple skills:

```python
#!/usr/bin/env python3
## multi_skill_agent.py - Agent with multiple skills
from signalwire_agents import AgentBase
from signalwire_agents.core.function_result import SwaigFunctionResult

agent = AgentBase(name="assistant", route="/assistant")
agent.prompt_add_section("Role", "You are a comprehensive assistant.")
agent.prompt_add_section("Capabilities", """
You can:

- Tell the current time and date
- Search our knowledge base
- Look up weather information
- Transfer to support if needed
""")
agent.add_language("English", "en-US", "rime.spore")

## Add built-in skills
agent.add_skill("datetime")
agent.add_skill("native_vector_search", {
    "index_path": "./knowledge.swsearch",
    "tool_name": "search_kb"
})

## Custom function
@agent.tool(description="Transfer to human support")
def transfer_support() -> SwaigFunctionResult:
    return (
        SwaigFunctionResult("Connecting you to a support representative.")
        .connect("+15551234567", final=True)
    )

if __name__ == "__main__":
    agent.run()
```

#### Order Processing Agent

Complete order management system:

```python
#!/usr/bin/env python3
## order_processing_agent.py - Complete order management system
from signalwire_agents import AgentBase
from signalwire_agents.core.function_result import SwaigFunctionResult
from datetime import datetime
import uuid

## Simulated databases
orders = {}
products = {
    "widget": {"price": 29.99, "stock": 100},
    "gadget": {"price": 49.99, "stock": 50},
    "device": {"price": 99.99, "stock": 25}
}

agent = AgentBase(name="orders", route="/orders")
agent.prompt_add_section("Role", "You help customers with orders.")
agent.prompt_add_section("Products", """
Available products:

- Widget: $29.99
- Gadget: $49.99
- Device: $99.99
""")
agent.prompt_add_section("Guidelines", """
- Verify product availability before placing orders
- Collect customer name and phone for orders
- Confirm order details before finalizing
- Provide order ID for tracking
""")
agent.add_language("English", "en-US", "rime.spore")
agent.set_global_data({"current_order": None})

@agent.tool(description="Check product availability")
def check_product(product: str) -> SwaigFunctionResult:
    prod = products.get(product.lower())
    if prod:
        return SwaigFunctionResult(
            f"{product.title()}: ${prod['price']}, {prod['stock']} in stock."
        )
    return SwaigFunctionResult(f"Product '{product}' not found.")

@agent.tool(description="Place an order")
def place_order(
    product: str,
    quantity: int,
    customer_name: str,
    customer_phone: str
) -> SwaigFunctionResult:
    prod = products.get(product.lower())
    if not prod:
        return SwaigFunctionResult(f"Product '{product}' not found.")

    if prod["stock"] < quantity:
        return SwaigFunctionResult(f"Insufficient stock. Only {prod['stock']} available.")

    order_id = str(uuid.uuid4())[:8].upper()
    total = prod["price"] * quantity

    orders[order_id] = {
        "product": product,
        "quantity": quantity,
        "total": total,
        "customer": customer_name,
        "phone": customer_phone,
        "status": "confirmed",
        "created": datetime.now().isoformat()
    }

    prod["stock"] -= quantity

    return (
        SwaigFunctionResult(
            f"Order {order_id} confirmed! {quantity}x {product} for ${total:.2f}."
        )
        .update_global_data({"last_order_id": order_id})
        .send_sms(
            to_number=customer_phone,
            from_number="+15559876543",
            body=f"Order {order_id} confirmed: {quantity}x {product}, ${total:.2f}"
        )
    )

@agent.tool(description="Check order status")
def order_status(order_id: str) -> SwaigFunctionResult:
    order = orders.get(order_id.upper())
    if order:
        return SwaigFunctionResult(
            f"Order {order_id}: {order['quantity']}x {order['product']}, "
            f"${order['total']:.2f}, Status: {order['status']}"
        )
    return SwaigFunctionResult(f"Order {order_id} not found.")

if __name__ == "__main__":
    agent.run()
```

#### Multi-Agent Server

Server hosting multiple specialized agents:

```python
#!/usr/bin/env python3
## multi_agent_server.py - Server hosting multiple agents
from signalwire_agents import AgentBase, AgentServer
from signalwire_agents.core.function_result import SwaigFunctionResult


class SalesAgent(AgentBase):
    def __init__(self):
        super().__init__(name="sales", route="/sales")
        self.prompt_add_section("Role", "You are a sales specialist.")
        self.add_language("English", "en-US", "rime.spore")

    @AgentBase.tool(description="Get product pricing")
    def get_pricing(self, product: str) -> SwaigFunctionResult:
        return SwaigFunctionResult(f"Pricing for {product}: Starting at $99.")


class SupportAgent(AgentBase):
    def __init__(self):
        super().__init__(name="support", route="/support")
        self.prompt_add_section("Role", "You are a support specialist.")
        self.add_language("English", "en-US", "rime.spore")
        self.add_skill("native_vector_search", {
            "index_path": "./support_docs.swsearch"
        })

    @AgentBase.tool(description="Create support ticket")
    def create_ticket(self, issue: str) -> SwaigFunctionResult:
        return SwaigFunctionResult(f"Ticket created for: {issue}")


class RouterAgent(AgentBase):
    def __init__(self):
        super().__init__(name="router", route="/")
        self.prompt_add_section("Role", "Route callers to the right agent.")
        self.add_language("English", "en-US", "rime.spore")

    @AgentBase.tool(description="Transfer to sales")
    def transfer_sales(self) -> SwaigFunctionResult:
        return SwaigFunctionResult("Transferring to sales.").connect(
            "https://agent.example.com/sales", final=True
        )

    @AgentBase.tool(description="Transfer to support")
    def transfer_support(self) -> SwaigFunctionResult:
        return SwaigFunctionResult("Transferring to support.").connect(
            "https://agent.example.com/support", final=True
        )


if __name__ == "__main__":
    server = AgentServer(host="0.0.0.0", port=8080)
    server.register(RouterAgent())
    server.register(SalesAgent())
    server.register(SupportAgent())
    server.run()
```

### Expert Examples

#### Code-Driven LLM Architecture

The most robust agents use **code-driven architecture** where business logic lives in SWAIG functions, not prompts. The LLM becomes a natural language translator while code handles all validation, state, and business rules.

```diagram
┌─────────────────────────────────────────────────────────────┐
│                   Code-Driven Approach                      │
│                                                             │
│   User ──► LLM ──► SWAIG Function ──► Response to LLM       │
│                         │                                   │
│                         ▼                                   │
│                   Code enforces:                            │
│                   • Business rules                          │
│                   • State management                        │
│                   • Calculations                            │
│                   • Validation                              │
│                   • UI updates                              │
│                                                             │
│   Advantage: LLM only translates intent, code does the rest │
└─────────────────────────────────────────────────────────────┘
```

**Core principles:**

| Traditional Approach | Code-Driven Approach |
|---------------------|----------------------|
| Rules in prompts | Rules in functions |
| LLM does math | Code does math |
| LLM tracks state | Global data tracks state |
| Hope LLM follows rules | Code enforces rules |

#### Order-Taking Agent (Code-Driven)

Complete example demonstrating code-driven patterns:

```python
#!/usr/bin/env python3
## code_driven_order_agent.py - Code-driven LLM architecture example
from signalwire_agents import AgentBase
from signalwire_agents.core.function_result import SwaigFunctionResult

## Menu data lives in code, not prompts
MENU = {
    "tacos": {
        "T001": {"name": "Beef Taco", "price": 3.49},
        "T002": {"name": "Chicken Taco", "price": 3.49},
        "T003": {"name": "Fish Taco", "price": 4.29},
    },
    "sides": {
        "S001": {"name": "Chips & Salsa", "price": 2.99},
        "S002": {"name": "Guacamole", "price": 3.49},
    },
    "drinks": {
        "D001": {"name": "Soda", "price": 1.99},
        "D002": {"name": "Iced Tea", "price": 1.99},
    },
    "combos": {
        "C001": {"name": "Taco Combo", "price": 9.99,
                 "includes": ["taco", "chips", "drink"], "savings": 1.97},
    }
}

## Aliases handle natural speech variations
MENU_ALIASES = {
    "D001": ["soda", "coke", "pop", "soft drink"],
    "S001": ["chips", "chips and salsa", "nachos"],
}

TAX_RATE = 0.10
MAX_ITEMS_PER_ADD = 10
MAX_ORDER_VALUE = 500.00


class OrderAgent(AgentBase):
    def __init__(self):
        super().__init__(name="order-agent", route="/order")
        self.add_language("English", "en-US", "rime.spore")

        # Minimal prompt - personality only, not rules
        self.prompt_add_section("Role",
            "You are a friendly drive-thru order taker. "
            "Keep responses brief and natural."
        )

        # State machine controls conversation flow
        self._setup_contexts()

        # Initialize order state
        self.set_global_data({
            "order_state": {
                "items": [],
                "subtotal": 0.00,
                "tax": 0.00,
                "total": 0.00,
                "item_count": 0
            }
        })

    def _setup_contexts(self):
        """Define state machine for conversation flow."""
        contexts = self.define_contexts()
        ctx = contexts.add_context("default")

        # Greeting state - limited actions
        ctx.add_step("greeting") \
            .add_section("Task", "Welcome the customer and take their order.") \
            .set_functions(["add_item"]) \
            .set_valid_steps(["taking_order"])

        # Order state - full ordering capabilities
        ctx.add_step("taking_order") \
            .add_section("Task", "Continue taking the order.") \
            .add_bullets("Info", [
                "Current total: $${global_data.order_state.total}",
                "Items: ${global_data.order_state.item_count}"
            ]) \
            .set_functions(["add_item", "remove_item", "finalize_order"]) \
            .set_valid_steps(["confirming"])

        # Confirmation state
        ctx.add_step("confirming") \
            .add_section("Task", "Confirm the order with the customer.") \
            .set_functions(["confirm_order", "add_item", "remove_item"]) \
            .set_valid_steps(["complete"])

    def _find_menu_item(self, item_name):
        """Find item by name or alias - code handles fuzzy matching."""
        item_lower = item_name.lower().strip()

        # Check exact matches first
        for category, items in MENU.items():
            for sku, data in items.items():
                if item_lower == data["name"].lower():
                    return sku, data, category

        # Check aliases
        for sku, aliases in MENU_ALIASES.items():
            if item_lower in [a.lower() for a in aliases]:
                for category, items in MENU.items():
                    if sku in items:
                        return sku, items[sku], category

        return None, None, None

    def _calculate_totals(self, items):
        """Code does all math - LLM never calculates."""
        subtotal = sum(item["price"] * item["quantity"] for item in items)
        tax = round(subtotal * TAX_RATE, 2)
        total = round(subtotal + tax, 2)
        return subtotal, tax, total

    def _check_combo_opportunity(self, items):
        """Code detects upsells - no prompt rules needed."""
        item_names = [i["name"].lower() for i in items]
        has_taco = any("taco" in n for n in item_names)
        has_chips = any("chip" in n for n in item_names)
        has_drink = any(n in ["soda", "iced tea"] for n in item_names)

        # Check if already has combo
        if any("combo" in n for n in item_names):
            return None

        if has_taco and has_chips and has_drink:
            return "Great news! I can upgrade you to a Taco Combo and save you $1.97!"
        return None

    @AgentBase.tool(
        name="add_item",
        description="Add an item to the order",
        parameters={
            "type": "object",
            "properties": {
                "item_name": {"type": "string", "description": "Name of the menu item"},
                "quantity": {"type": "integer", "description": "How many (default 1)",
                            "minimum": 1, "maximum": 10}
            },
            "required": ["item_name"]
        }
    )
    def add_item(self, args, raw_data):
        """Add item - code enforces all limits and rules."""
        item_name = args.get("item_name", "")
        quantity = args.get("quantity", 1)

        # Code enforces limits (LLM doesn't need to know)
        if quantity > MAX_ITEMS_PER_ADD:
            quantity = MAX_ITEMS_PER_ADD

        # Get order state
        global_data = raw_data.get("global_data", {})
        order_state = global_data.get("order_state", {
            "items": [], "subtotal": 0, "tax": 0, "total": 0, "item_count": 0
        })

        # Find the item (code handles fuzzy matching)
        sku, item_data, category = self._find_menu_item(item_name)
        if not item_data:
            return SwaigFunctionResult(
                f"I couldn't find '{item_name}' on the menu. "
                "We have tacos, chips, guacamole, and drinks."
            )

        # Check order value limit
        potential = order_state["subtotal"] + (item_data["price"] * quantity)
        if potential > MAX_ORDER_VALUE:
            return SwaigFunctionResult(
                f"That would exceed our ${MAX_ORDER_VALUE:.2f} order limit."
            )

        # Add to order
        order_state["items"].append({
            "sku": sku,
            "name": item_data["name"],
            "quantity": quantity,
            "price": item_data["price"]
        })
        order_state["item_count"] += quantity

        # Code calculates totals (LLM never does math)
        subtotal, tax, total = self._calculate_totals(order_state["items"])
        order_state["subtotal"] = subtotal
        order_state["tax"] = tax
        order_state["total"] = total

        # Build response that guides LLM behavior
        response = f"Added {quantity}x {item_data['name']} (${item_data['price']:.2f} each)."

        # Check for upsell (code decides, not LLM)
        combo_suggestion = self._check_combo_opportunity(order_state["items"])
        if combo_suggestion:
            response += f"\n\n{combo_suggestion}"

        # Update state and transition
        global_data["order_state"] = order_state

        result = SwaigFunctionResult(response)
        result.update_global_data(global_data)
        result.swml_change_step("taking_order")

        # Push UI update (frontend stays in sync without LLM)
        result.swml_user_event({
            "type": "item_added",
            "item": {"name": item_data["name"], "quantity": quantity,
                     "price": item_data["price"]},
            "total": total
        })

        return result

    @AgentBase.tool(
        name="remove_item",
        description="Remove an item from the order",
        parameters={
            "type": "object",
            "properties": {
                "item_name": {"type": "string", "description": "Item to remove"},
                "quantity": {"type": "integer", "description": "How many (-1 for all)"}
            },
            "required": ["item_name"]
        }
    )
    def remove_item(self, args, raw_data):
        """Remove item - code handles all edge cases."""
        item_name = args.get("item_name", "").lower()
        quantity = args.get("quantity", 1)

        global_data = raw_data.get("global_data", {})
        order_state = global_data.get("order_state", {"items": []})

        # Find matching item in order
        for i, item in enumerate(order_state["items"]):
            if item_name in item["name"].lower():
                if quantity == -1 or quantity >= item["quantity"]:
                    removed = order_state["items"].pop(i)
                    order_state["item_count"] -= removed["quantity"]
                else:
                    item["quantity"] -= quantity
                    order_state["item_count"] -= quantity

                # Recalculate
                subtotal, tax, total = self._calculate_totals(order_state["items"])
                order_state["subtotal"] = subtotal
                order_state["tax"] = tax
                order_state["total"] = total

                global_data["order_state"] = order_state

                result = SwaigFunctionResult(f"Removed {item_name} from your order.")
                result.update_global_data(global_data)
                return result

        return SwaigFunctionResult(f"I don't see {item_name} in your order.")

    @AgentBase.tool(
        name="finalize_order",
        description="Finalize and review the order",
        parameters={"type": "object", "properties": {}}
    )
    def finalize_order(self, args, raw_data):
        """Finalize - code builds the summary."""
        global_data = raw_data.get("global_data", {})
        order_state = global_data.get("order_state", {})

        if not order_state.get("items"):
            return SwaigFunctionResult("Your order is empty. What can I get you?")

        # Code builds accurate summary (LLM just relays it)
        items_text = ", ".join(
            f"{i['quantity']}x {i['name']}" for i in order_state["items"]
        )

        result = SwaigFunctionResult(
            f"Your order: {items_text}. "
            f"Total is ${order_state['total']:.2f} including tax. "
            "Does that look correct?"
        )
        result.swml_change_step("confirming")
        return result

    @AgentBase.tool(
        name="confirm_order",
        description="Confirm the order is complete",
        parameters={"type": "object", "properties": {}}
    )
    def confirm_order(self, args, raw_data):
        """Confirm - code handles completion."""
        global_data = raw_data.get("global_data", {})
        order_state = global_data.get("order_state", {})

        # Generate order number
        import random
        order_num = random.randint(100, 999)

        result = SwaigFunctionResult(
            f"Order #{order_num} confirmed! "
            f"Your total is ${order_state['total']:.2f}. "
            "Please pull forward. Thank you!"
        )
        result.swml_change_step("complete")

        # Final UI update
        result.swml_user_event({
            "type": "order_complete",
            "order_number": order_num,
            "total": order_state["total"]
        })

        return result


if __name__ == "__main__":
    agent = OrderAgent()
    agent.run()
```

**Key patterns demonstrated:**

1. **Response-guided behavior**: Functions return text that guides LLM responses. The combo upsell suggestion appears in the response, so the LLM naturally offers it.

2. **Code-enforced limits**: `MAX_ITEMS_PER_ADD` and `MAX_ORDER_VALUE` are enforced in code. The LLM cannot bypass them.

3. **State machine control**: `set_functions()` restricts what the LLM can do in each state. Impossible actions are literally unavailable.

4. **Dynamic prompt injection**: `${global_data.order_state.total}` injects current state into prompts without LLM tracking.

5. **UI synchronization**: `swml_user_event()` pushes updates to frontends in real-time.

6. **Fuzzy input handling**: `_find_menu_item()` handles variations like "coke" → "Soda" without prompt rules.

### Complexity Progression

#### Beginner
1. Create basic agent with prompt
2. Add language configuration
3. Test with swaig-test

#### Intermediate
4. Add SWAIG functions
5. Use global data for state
6. Add skills
7. Implement call transfers

#### Advanced
8. Use DataMap for API integration
9. Implement context workflows
10. Build multi-agent systems
11. Deploy to production

#### Expert
12. Code-driven LLM architecture
13. State machine conversation control
14. Response-guided LLM behavior
15. Real-time UI synchronization




# Part: Appendix

---

# Appendix

> **Summary**: Reference materials, patterns, best practices, and troubleshooting guides for the SignalWire Agents SDK.

## About This Chapter

This appendix provides supplementary reference materials to support your development with the SignalWire Agents SDK.

| Section | Description |
|---------|-------------|
| AI Parameters | Complete reference for all AI model parameters |
| Design Patterns | Common architectural patterns and solutions |
| Best Practices | Guidelines for production-quality agents |
| Troubleshooting | Common issues and their solutions |
| Migration Guide | Upgrading between SDK versions |
| Changelog | Version history and release notes |

## Quick Reference

| Task | See Section |
|------|-------------|
| Configure AI model behavior | AI Parameters → LLM Parameters |
| Set speech recognition | AI Parameters → ASR Parameters |
| Adjust timing/timeouts | AI Parameters → Timing Parameters |
| Implement common patterns | Design Patterns |
| Optimize for production | Best Practices |
| Debug agent issues | Troubleshooting |
| Upgrade SDK version | Migration Guide |

## Chapter Contents

| Section | Description |
|---------|-------------|
| [AI Parameters](12_01_ai-parameters.md) | Complete AI parameter reference |
| [Design Patterns](12_02_patterns.md) | Common architectural patterns |
| [Best Practices](12_03_best-practices.md) | Production guidelines |
| [Troubleshooting](12_04_troubleshooting.md) | Common issues and solutions |
| [Migration Guide](12_05_migration.md) | Version upgrade guide |
| [Changelog](12_06_changelog.md) | Version history |

## Overview

| Category | Description | Where to Set |
|----------|-------------|--------------|
| LLM API | Model behavior (temperature, etc.) | prompt/post_prompt |
| ASR | Speech recognition settings | prompt or params |
| Timing | Timeouts and delays | params |
| Behavior | Agent behavior toggles | params |
| Interrupt | Interruption handling | params |
| Audio | Volume and background audio | params |
| Video | Video display options | params |

## Setting Parameters in Python

```python
from signalwire_agents import AgentBase

agent = AgentBase(name="assistant", route="/assistant")

# Set AI parameters
agent.set_params({
    "temperature": 0.7,
    "confidence": 0.6,
    "end_of_speech_timeout": 2000,
    "attention_timeout": 10000
})
```

## LLM API Parameters

These parameters control the AI model's behavior. Set in `prompt` or `post_prompt` sections.

| Parameter | Type | Range | Default | Description |
|-----------|------|-------|---------|-------------|
| temperature | number | 0.0 - 2.0 | 0.3 | Output randomness |
| top_p | number | 0.0 - 1.0 | 1.0 | Nucleus sampling |
| frequency_penalty | number | -2.0 - 2.0 | 0.1 | Repeat penalty |
| presence_penalty | number | -2.0 - 2.0 | 0.1 | New topic bonus |
| max_tokens | integer | 1 - 16385 | 256 | Max response size |
| max_completion_tokens | integer | 1 - 2048 | 256 | For o1-style models |
| reasoning_effort | string | - | "low" | o1 reasoning level |
| verbosity | string | - | "low" | Response length |

### Temperature

Controls randomness in output generation:

- **0.0**: Deterministic, consistent responses
- **0.3** (default): Balanced creativity
- **1.0+**: More creative, less predictable

### Reasoning Effort

For o1-style models only:

- `"low"`: Quick responses
- `"medium"`: Balanced reasoning
- `"high"`: Deep analysis

## ASR (Speech Recognition) Parameters

Control automatic speech recognition behavior.

| Parameter | Type | Range | Default | Description |
|-----------|------|-------|---------|-------------|
| energy_level | number | 0 - 100 | 52 | Minimum audio (dB) |
| asr_smart_format | boolean | - | false | Smart formatting |
| asr_diarize | boolean | - | false | Speaker detection |
| asr_speaker_affinity | boolean | - | false | Speaker tracking |

<!-- HIDDEN PARAMETERS - DO NOT DOCUMENT:
- confidence (number, 0.0-1.0, default 0.75) - ASR confidence threshold
- barge_confidence (number, 0.0-1.0, default 0.75) - Confidence for barge-in
-->

## Timing Parameters

Control various timeouts and timing behaviors.

| Parameter | Type | Range | Default | Description |
|-----------|------|-------|---------|-------------|
| end_of_speech_timeout | integer | 250 - 10000 | 700 | End silence (ms) |
| first_word_timeout | integer | - | 1000 | First word wait (ms) |
| speech_timeout | integer | - | 60000 | Max speech (ms) |
| speech_event_timeout | integer | - | 1400 | Event wait (ms) |
| turn_detection_timeout | integer | - | 250 | Turn detection (ms) |
| attention_timeout | integer | 0 - 600000 | 5000 | Idle prompt (ms) |
| outbound_attention_timeout | integer | 10000 - 600000 | 120000 | Outbound (ms) |
| inactivity_timeout | integer | 10000 - 3600000 | 600000 | Exit delay (ms) |
| digit_timeout | integer | - | 3000 | DTMF wait (ms) |
| initial_sleep_ms | integer | - | 0 | Start delay (ms) |
| transparent_barge_max_time | integer | 0 - 60000 | 3000 | Barge time (ms) |

### Key Timeouts

- **end_of_speech_timeout**: Milliseconds of silence to detect end of speech
- **attention_timeout**: How long to wait before prompting user (0 disables)
- **inactivity_timeout**: How long before auto-hangup (default 10 minutes)

### Hard Stop Time

```python
# Time expression format
agent.set_params({
    "hard_stop_time": "5m",      # 5 minutes
    "hard_stop_time": "1h30m",   # 1 hour 30 minutes
    "hard_stop_prompt": "We need to wrap up now."
})
```

## Behavior Parameters

Control various AI agent behaviors.

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| direction | string | natural | Force inbound/outbound |
| wait_for_user | boolean | false | Wait before speaking |
| conscience | boolean/str | true | Safety enforcement |
| strict_mode | boolean/str | - | Alias for conscience |
| transparent_barge | boolean | true | Transparent barge mode |
| enable_pause | boolean | false | Allow pausing |
| start_paused | boolean | false | Start paused |
| speak_when_spoken_to | boolean | false | Only respond when spoken to |
| enable_turn_detection | boolean | varies | Turn detection |
| enable_vision | boolean | false | Vision/video AI |
| enable_thinking | boolean | false | Complex reasoning |
| save_conversation | boolean | false | Save summary |
| persist_global_data | boolean | true | Persist data |
| transfer_summary | boolean | false | Summary on transfer |

<!-- HIDDEN PARAMETERS - DO NOT DOCUMENT:
- enable_inner_dialog (boolean, default false) - Enable inner dialog mode
- inner_dialog_synced (boolean, default false) - Sync inner dialog with conversation
- llm_diarize_aware (boolean, default false) - Make LLM aware of speaker diarization
- send_single_llm_response (boolean, default false) - Send single LLM response instead of streaming
- back_to_back_functions (boolean/string, default true) - Allow back-to-back function execution
- cache_mode (boolean, varies) - Enable response caching
- enable_accounting (boolean, default false) - Enable accounting/billing tracking
- languages_enabled (boolean, auto) - Enable multi-language support
-->

## SWAIG Control Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| swaig_allow_swml | boolean | true | Allow SWML returns |
| swaig_allow_settings | boolean | true | Allow settings mods |
| swaig_post_conversation | boolean | false | Post conversation |
| swaig_set_global_data | boolean | true | Allow global data |
| hold_on_process | boolean | false | Hold during process |
| barge_functions | boolean | true | Allow function barge |
| function_wait_for_talking | boolean | false | Wait for speech |
| functions_on_no_response | boolean | false | Run on no response |
| functions_on_speaker_timeout | boolean | true | Run on timeout |

## Interrupt Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| acknowledge_interruptions | boolean | false | Acknowledge interrupts |
| interrupt_prompt | string | - | Custom interrupt message |
| interrupt_on_noise | boolean | false | Allow noise interrupts |
| max_interrupts | integer | 0 | Max before interrupt_prompt |
| barge_min_words | integer | 0 | Min words before barge allowed |

## Debug Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| debug_webhook_url | string | - | URL to send debug data |
| debug_webhook_level | integer | 1 | Debug verbosity (0-2) |
| audible_debug | boolean | false | Enable audible debugging |
| audible_latency | boolean | false | Make latency audible |
| verbose_logs | boolean | false | Enable verbose logging |

<!-- HIDDEN PARAMETERS - DO NOT DOCUMENT:
- conversation_sliding_window (integer) - Number of conversation turns to retain
- speech_gen_quick_stops (integer, default 3) - Number of quick stops allowed
- input_poll_freq (integer, default 2000) - Input polling frequency in milliseconds
- max_response_tokens (integer) - Maximum response tokens (1-16384)
- static_greeting_no_barge (boolean, default false) - Disable barge during static greeting
- swaig_post_swml_vars (object) - Variables to include in SWAIG SWML posts
- openai_azure (boolean, default false) - Use Azure OpenAI (developer mode)
- ai_model_62c3bdb19a89 (string, CHEAT CODE) - Override AI model selection
- max_post_bytes_62c3bdb19a89 (integer, CHEAT CODE) - Override max POST bytes limit
-->

## Audio Parameters

| Parameter | Type | Range | Default | Description |
|-----------|------|-------|---------|-------------|
| ai_volume | integer | -50 - 50 | 0 | AI voice volume |
| background_file | string | - | - | Background audio URL |
| background_file_volume | integer | -50 - 50 | 0 | Background volume |
| background_file_loops | integer | - | -1 | Loop count (-1=infinite) |
| hold_music | string | - | - | Hold audio/tone |
| max_emotion | integer | 1 - 30 | 30 | TTS emotion level |

### Hold Music with Tone

```python
# Use tone generator
agent.set_params({
    "hold_music": "tone:440"  # 440Hz tone
})

# Use audio file
agent.set_params({
    "hold_music": "https://example.com/hold-music.mp3"
})
```

## Video Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| video_talking_file | string | Video when AI is talking |
| video_idle_file | string | Video when AI is idle |
| video_listening_file | string | Video when AI is listening |

## String Parameters

| Parameter | Default | Description |
|-----------|---------|-------------|
| local_tz | "US/Central" | Timezone for agent |
| conversation_id | - | ID for cross-call persistence |
| digit_terminators | - | DTMF end characters (e.g., "#") |
| barge_match_string | - | Barge pattern matching |
| tts_number_format | "international" | Phone format: national/intl |
| ai_model | "gpt-4o-mini" | AI model to use |
| thinking_model | - | Model for thinking mode |
| vision_model | - | Model for vision |
| pom_format | "markdown" | Prompt format: markdown/xml |
| attention_timeout_prompt | - | Custom attention prompt |
| hard_stop_prompt | - | Prompt at hard stop time |
| static_greeting | - | Pre-recorded greeting |
| summary_mode | - | string/og/function |

<!-- HIDDEN PARAMETERS - DO NOT DOCUMENT:
- ai_name (string, default "computer") - Name of AI (for pause/wake modes)
- wake_prefix (string) - Wake word prefix for speak mode
- inner_dialog_model (string) - Model for inner dialog
- inner_dialog_prompt (string, built-in) - Custom inner dialog prompt
- developer_prompt (string) - Additional dev instructions
- openai_asr_engine (string) - Override ASR engine
- openai_gcloud_version (string, deprecated) - Use openai_asr_engine instead
-->

## VAD Configuration

Voice Activity Detection uses a string format: `silero_thresh:frame_ms`

```python
agent.set_params({
    "vad_config": "0.5:30"  # threshold 0.5, 30ms frames
})
```

## Post-Prompt Parameter Defaults

Parameters have different defaults in `post_prompt` for more deterministic summaries:

| Parameter | Prompt Default | Post-Prompt Default | Reason |
|-----------|---------------|---------------------|--------|
| temperature | 0.3 | 0.0 | Deterministic |
| frequency_penalty | 0.1 | 0.0 | No penalty |
| presence_penalty | 0.1 | 0.0 | No penalty |

## Model-Specific Overrides

Different models support different parameters:

| Model Type | Supported Parameters |
|------------|---------------------|
| OpenAI | frequency_penalty, presence_penalty, max_tokens, top_p |
| Bedrock Claude | max_completion_tokens instead of max_tokens |
| o1-style | reasoning_effort, max_completion_tokens |

## Complete Example

```python
#!/usr/bin/env python3
# configured_agent.py - Agent with all AI parameters configured
from signalwire_agents import AgentBase

agent = AgentBase(name="configured", route="/configured")
agent.prompt_add_section("Role", "You are a customer service agent.")
agent.add_language("English", "en-US", "rime.spore")

# Configure all parameters
agent.set_params({
    # LLM settings
    "max_tokens": 300,

    # Timing
    "end_of_speech_timeout": 1500,
    "attention_timeout": 8000,
    "inactivity_timeout": 300000,

    # Behavior
    "wait_for_user": False,
    "conscience": True,
    "local_tz": "America/New_York",

    # Audio
    "background_file": "https://example.com/ambient.mp3",
    "background_file_volume": -30
})

if __name__ == "__main__":
    agent.run()
```

## SWML Example

```json
{
  "version": "1.0.0",
  "sections": {
    "main": [{
      "ai": {
        "params": {
          "end_of_speech_timeout": 2000,
          "attention_timeout": 10000,
          "inactivity_timeout": 600000,
          "wait_for_user": false,
          "conscience": true,
          "local_tz": "America/Chicago",
          "background_file": "https://example.com/music.mp3",
          "background_file_volume": -25
        },
        "prompt": {
          "temperature": 0.3,
          "top_p": 1.0,
          "frequency_penalty": 0.1,
          "presence_penalty": 0.1,
          "text": "You are a helpful assistant."
        },
        "post_prompt": {
          "temperature": 0.0,
          "frequency_penalty": 0.0,
          "presence_penalty": 0.0,
          "text": "Summarize the conversation."
        }
      }
    }]
  }
}
```


---

## Design Patterns

> **Summary**: Common architectural patterns and solutions for building SignalWire voice AI agents.

### Overview

| Pattern | Description |
|---------|-------------|
| Decorator Pattern | Add functions with `@agent.tool` decorator |
| Class-Based Agent | Subclass AgentBase for reusable agents |
| Multi-Agent Router | Route calls to specialized agents |
| State Machine | Use contexts for multi-step workflows |
| DataMap Integration | Serverless API integration |
| Skill Composition | Combine built-in skills |
| Dynamic Configuration | Runtime agent customization |

### Decorator Pattern

The simplest way to create an agent with functions:

```python
from signalwire_agents import AgentBase
from signalwire_agents.core.function_result import SwaigFunctionResult

agent = AgentBase(name="helper", route="/helper")
agent.prompt_add_section("Role", "You help users with account information.")
agent.add_language("English", "en-US", "rime.spore")

@agent.tool(description="Look up account by ID")
def lookup_account(account_id: str) -> SwaigFunctionResult:
    # Lookup logic here
    return SwaigFunctionResult(f"Account {account_id} found.")

@agent.tool(description="Update account status")
def update_status(account_id: str, status: str) -> SwaigFunctionResult:
    # Update logic here
    return SwaigFunctionResult(f"Account {account_id} updated to {status}.")

if __name__ == "__main__":
    agent.run()
```

### Class-Based Agent Pattern

For reusable, shareable agent definitions:

```python
from signalwire_agents import AgentBase
from signalwire_agents.core.function_result import SwaigFunctionResult

class SupportAgent(AgentBase):
    def __init__(self):
        super().__init__(name="support", route="/support")
        self.prompt_add_section("Role", "You are a technical support agent.")
        self.prompt_add_section("Guidelines", """
        - Be patient and helpful
        - Gather issue details before troubleshooting
        - Escalate complex issues to human support
        """)
        self.add_language("English", "en-US", "rime.spore")
        self.add_skill("datetime")

    @AgentBase.tool(description="Create support ticket")
    def create_ticket(self, issue: str, priority: str = "normal") -> SwaigFunctionResult:
        ticket_id = f"TKT-{id(self) % 10000:04d}"
        return SwaigFunctionResult(f"Created ticket {ticket_id} for: {issue}")

    @AgentBase.tool(description="Transfer to human support")
    def transfer_to_human(self) -> SwaigFunctionResult:
        return (
            SwaigFunctionResult("Connecting you to a support representative.")
            .connect("+15551234567", final=True)
        )

if __name__ == "__main__":
    agent = SupportAgent()
    agent.run()
```

### Multi-Agent Router Pattern

Route calls to specialized agents based on intent:

```python
from signalwire_agents import AgentBase, AgentServer
from signalwire_agents.core.function_result import SwaigFunctionResult


class RouterAgent(AgentBase):
    def __init__(self, base_url: str):
        super().__init__(name="router", route="/")
        self.base_url = base_url
        self.prompt_add_section("Role", """
        You are a receptionist. Determine what the caller needs and
        route them to the appropriate department.
        """)
        self.prompt_add_section("Departments", """
        - Sales: Product inquiries, pricing, purchases
        - Support: Technical help, troubleshooting
        - Billing: Payments, invoices, account issues
        """)
        self.add_language("English", "en-US", "rime.spore")

    @AgentBase.tool(description="Transfer to sales department")
    def transfer_sales(self) -> SwaigFunctionResult:
        return (
            SwaigFunctionResult("Transferring to sales.")
            .connect(f"{self.base_url}/sales", final=True)
        )

    @AgentBase.tool(description="Transfer to support department")
    def transfer_support(self) -> SwaigFunctionResult:
        return (
            SwaigFunctionResult("Transferring to support.")
            .connect(f"{self.base_url}/support", final=True)
        )


if __name__ == "__main__":
    server = AgentServer(host="0.0.0.0", port=8080)
    server.register(RouterAgent("https://agent.example.com"))
    server.run()
```

### State Machine Pattern (Contexts)

Use contexts for structured multi-step workflows:

```python
from signalwire_agents import AgentBase
from signalwire_agents.core.contexts import ContextBuilder
from signalwire_agents.core.function_result import SwaigFunctionResult


class VerificationAgent(AgentBase):
    def __init__(self):
        super().__init__(name="verify", route="/verify")
        self.add_language("English", "en-US", "rime.spore")
        self._setup_contexts()

    def _setup_contexts(self):
        ctx = ContextBuilder("verification")

        ctx.add_step(
            "greeting",
            "Welcome the caller and ask for their account number.",
            functions=["verify_account"],
            valid_steps=["collect_info"]
        )

        ctx.add_step(
            "collect_info",
            "Verify the caller's identity by asking security questions.",
            functions=["verify_security"],
            valid_steps=["authenticated", "failed"]
        )

        ctx.add_step(
            "authenticated",
            "The caller is verified. Ask how you can help them today.",
            functions=["check_balance", "transfer_funds", "end_call"],
            valid_steps=["end"]
        )

        self.add_context(ctx.build(), default=True)

    @AgentBase.tool(description="Verify account number")
    def verify_account(self, account_number: str) -> SwaigFunctionResult:
        return SwaigFunctionResult(f"Account {account_number} found.")

    @AgentBase.tool(description="Check account balance")
    def check_balance(self, account_id: str) -> SwaigFunctionResult:
        return SwaigFunctionResult("Current balance is $1,234.56")
```

### DataMap Integration Pattern

Use DataMap for serverless API integration:

```python
from signalwire_agents import AgentBase
from signalwire_agents.core.data_map import DataMap

agent = AgentBase(name="weather", route="/weather")
agent.prompt_add_section("Role", "You provide weather information.")
agent.add_language("English", "en-US", "rime.spore")

## Define DataMap tool
weather_map = DataMap(
    name="get_weather",
    description="Get current weather for a city"
)

weather_map.add_parameter("city", "string", "City name", required=True)

weather_map.add_webhook(
    url="https://api.weather.com/v1/current?q=${enc:args.city}&key=API_KEY",
    method="GET",
    output_map={
        "response": "Weather in ${args.city}: ${response.temp}F, ${response.condition}"
    },
    error_map={
        "response": "Could not retrieve weather for ${args.city}"
    }
)

agent.add_data_map_tool(weather_map)

if __name__ == "__main__":
    agent.run()
```

### Skill Composition Pattern

Combine multiple skills for comprehensive functionality:

```python
from signalwire_agents import AgentBase
from signalwire_agents.core.function_result import SwaigFunctionResult

agent = AgentBase(name="assistant", route="/assistant")
agent.prompt_add_section("Role", """
You are a comprehensive assistant that can:

- Tell the current time and date
- Search our knowledge base
- Look up weather information
""")
agent.add_language("English", "en-US", "rime.spore")

## Add built-in skills
agent.add_skill("datetime")
agent.add_skill("native_vector_search", {
    "index_path": "./knowledge.swsearch",
    "tool_name": "search_docs",
    "tool_description": "Search documentation"
})

## Add custom function alongside skills
@agent.tool(description="Escalate to human agent")
def escalate(reason: str) -> SwaigFunctionResult:
    return (
        SwaigFunctionResult(f"Escalating: {reason}")
        .connect("+15551234567", final=True)
    )

if __name__ == "__main__":
    agent.run()
```

### Dynamic Configuration Pattern

Configure agents dynamically at runtime:

```python
from signalwire_agents import AgentBase
from signalwire_agents.core.function_result import SwaigFunctionResult
from typing import Dict, Any


class DynamicAgent(AgentBase):
    def __init__(self):
        super().__init__(name="dynamic", route="/dynamic")
        self.add_language("English", "en-US", "rime.spore")
        self.set_dynamic_config_callback(self.configure_from_call)

    def configure_from_call(
        self,
        query_params: Dict[str, Any],
        body_params: Dict[str, Any],
        headers: Dict[str, str],
        agent: 'AgentBase'
    ) -> None:
        # Get caller's phone number from body
        caller = body_params.get("call", {}).get("from", "")

        # Customize prompt based on caller
        if caller.startswith("+1555"):
            agent.prompt_add_section("Role", "You are a VIP support agent.")
        else:
            agent.prompt_add_section("Role", "You are a standard support agent.")

        # Add caller info to global data
        agent.set_global_data({"caller_number": caller})


if __name__ == "__main__":
    agent = DynamicAgent()
    agent.run()
```

### Pattern Selection Guide

| Scenario | Recommended Pattern |
|----------|---------------------|
| Quick prototype or simple agent | Decorator Pattern |
| Reusable agent for sharing | Class-Based Agent |
| Multiple specialized agents | Multi-Agent Router |
| Step-by-step workflows | State Machine (Contexts) |
| External API integration | DataMap Integration |
| Feature-rich agent | Skill Composition |
| Per-call customization | Dynamic Configuration |



---

## Best Practices

> **Summary**: Guidelines and recommendations for building production-quality SignalWire voice AI agents.

### Overview

| Category | Focus Area |
|----------|------------|
| Prompt Design | Effective prompts and POM structure |
| Function Design | Well-structured SWAIG functions |
| Error Handling | Graceful failure and recovery |
| Security | Authentication and data protection |
| Performance | Optimization and efficiency |
| Testing | Validation and quality assurance |
| Monitoring | Logging and observability |

### Prompt Design

#### Use POM (Prompt Object Model)

Structure prompts with clear sections:

```python
from signalwire_agents import AgentBase

agent = AgentBase(name="service", route="/service")

## Good: Structured sections
agent.prompt_add_section("Role", """
You are a customer service representative for Acme Corp.
""")

agent.prompt_add_section("Guidelines", body="Follow these rules:", bullets=[
    "Be professional and courteous",
    "Verify customer identity before account access",
    "Never share sensitive information",
    "Escalate complex issues to human agents"
])

agent.add_language("English", "en-US", "rime.spore")
```

#### Be Specific About Behavior

```python
## Good: Specific instructions
agent.prompt_add_section("Response Style", """
- Keep responses under 3 sentences for simple questions
- Ask one question at a time
- Confirm understanding before taking action
- Use the customer's name when known
""")
```

### Function Design

#### Clear Descriptions

```python
from signalwire_agents import AgentBase
from signalwire_agents.core.function_result import SwaigFunctionResult

agent = AgentBase(name="accounts", route="/accounts")

## Good: Descriptive with parameter details
@agent.tool(
    description="Look up customer account by account number. "
    "Returns account status, balance, and last activity date."
)
def lookup_account(
    account_number: str  # The 8-digit account number
) -> SwaigFunctionResult:
    pass
```

#### Return Actionable Information

```python
@agent.tool(description="Check product availability")
def check_availability(product_id: str) -> SwaigFunctionResult:
    stock = get_stock(product_id)

    if stock > 10:
        return SwaigFunctionResult(
            f"Product {product_id} is in stock with {stock} units available. "
            "The customer can place an order."
        )
    elif stock > 0:
        return SwaigFunctionResult(
            f"Product {product_id} has limited stock ({stock} units). "
            "Suggest ordering soon."
        )
    else:
        return SwaigFunctionResult(
            f"Product {product_id} is out of stock. "
            "Expected restock date: next week."
        )
```

### Error Handling

#### Graceful Degradation

```python
@agent.tool(description="Look up order status")
def order_status(order_id: str) -> SwaigFunctionResult:
    try:
        order = fetch_order(order_id)
        return SwaigFunctionResult(
            f"Order {order_id}: Status is {order['status']}"
        )
    except OrderNotFoundError:
        return SwaigFunctionResult(
            f"Order {order_id} was not found. "
            "Please verify the order number and try again."
        )
    except ServiceUnavailableError:
        return SwaigFunctionResult(
            "The order system is temporarily unavailable. "
            "Please try again in a few minutes."
        )
```

### Security

#### Use Authentication

```python
import os

agent = AgentBase(
    name="secure",
    route="/secure",
    basic_auth=(
        os.environ.get("AGENT_USER", "agent"),
        os.environ.get("AGENT_PASSWORD")
    )
)
```

#### Secure Function Tokens

```python
## Require token authentication for sensitive functions
@agent.tool(
    description="Process payment",
    secure=True  # Requires valid token
)
def process_payment(amount: float, card_last_four: str) -> SwaigFunctionResult:
    pass
```

#### Environment Variables

| Variable | Purpose |
|----------|---------|
| `SWML_BASIC_AUTH_USER` | Basic auth username |
| `SWML_BASIC_AUTH_PASSWORD` | Basic auth password (required for production) |
| `SWML_SSL_ENABLED` | Enable HTTPS |
| `SWML_SSL_CERT_PATH` | SSL certificate path |
| `SWML_SSL_KEY_PATH` | SSL key path |

### Performance

#### Use DataMap for Simple API Calls

```python
from signalwire_agents.core.data_map import DataMap

## Good: DataMap for simple lookups (no webhook roundtrip)
weather_map = DataMap(
    name="get_weather",
    description="Get weather for a city"
)
weather_map.add_parameter("city", "string", "City name", required=True)
weather_map.add_webhook(
    url="https://api.weather.com/v1/current?q=${enc:args.city}",
    method="GET",
    output_map={"response": "Weather: ${response.temp}F, ${response.condition}"}
)
agent.add_data_map_tool(weather_map)
```

#### Use Fillers for Long Operations

```python
@agent.tool(
    description="Search database",
    fillers=["Searching...", "This may take a moment..."]
)
def search_db(query: str) -> SwaigFunctionResult:
    # Long-running search
    results = search_database(query)
    return SwaigFunctionResult(f"Found {len(results)} matching orders.")
```

### Testing

#### Use swaig-test

```bash
## Validate agent configuration
swaig-test agent.py --dump-swml

## List available functions
swaig-test agent.py --list-tools

## Test specific function
swaig-test agent.py --exec lookup_account --account_number "12345678"
```

### Monitoring

#### Use Structured Logging

```python
import structlog

logger = structlog.get_logger()

@agent.tool(description="Process refund")
def process_refund(order_id: str, amount: float) -> SwaigFunctionResult:
    logger.info(
        "refund_requested",
        order_id=order_id,
        amount=amount
    )
    # Process refund
    return SwaigFunctionResult(f"Refund of ${amount} processed.")
```

### Production Readiness Checklist

- [ ] Authentication configured (basic_auth or environment variables)
- [ ] SSL/HTTPS enabled for production
- [ ] Sensitive functions marked as secure
- [ ] Error handling in all functions
- [ ] Input validation for user-provided data
- [ ] Logging configured (no sensitive data in logs)
- [ ] All functions tested with swaig-test
- [ ] Edge cases and error scenarios tested
- [ ] Prompts reviewed for clarity and completeness
- [ ] Transfer/escalation paths defined
- [ ] Timeout values appropriate for use case
- [ ] Summary handling for call analytics



---

## Troubleshooting

> **Summary**: Common issues and solutions when developing SignalWire voice AI agents.

### Quick Diagnostics

| Command | Purpose |
|---------|---------|
| `swaig-test agent.py --dump-swml` | Verify SWML generation |
| `swaig-test agent.py --list-tools` | List registered functions |
| `swaig-test agent.py --exec func` | Test function execution |
| `python agent.py` | Check for startup errors |
| `curl http://localhost:3000/` | Test agent endpoint |

### Startup Issues

#### Agent Won't Start

**Symptom**: Python script exits immediately or with an error.

**Common Causes**:

1. **Missing dependencies**

```bash
## Check if signalwire-agents is installed
pip show signalwire-agents

## Install if missing
pip install signalwire-agents
```

2. **Port already in use**

```
Error: [Errno 48] Address already in use
```

**Solution**: Use a different port or stop the existing process.

```python
agent = AgentBase(name="myagent", route="/", port=3001)
```

3. **Invalid Python syntax**

```bash
## Check syntax
python -m py_compile agent.py
```

#### Import Errors

**Symptom**: `ModuleNotFoundError` or `ImportError`.

```
ModuleNotFoundError: No module named 'signalwire_agents'
```

**Solutions**:

```bash
## Ensure virtual environment is activated
source venv/bin/activate

## Verify installation
pip list | grep signalwire

## Reinstall if needed
pip install --upgrade signalwire-agents
```

### Function Issues

#### Function Not Appearing

**Symptom**: Function defined but not showing in `--list-tools`.

**Check 1**: Decorator syntax

```python
## Correct
@agent.tool(description="My function")
def my_function(param: str) -> SwaigFunctionResult:
    return SwaigFunctionResult("Done")

## Wrong: Missing parentheses
@agent.tool
def my_function(param: str) -> SwaigFunctionResult:
    pass

## Wrong: Missing description
@agent.tool()
def my_function(param: str) -> SwaigFunctionResult:
    pass
```

**Check 2**: Function defined before agent.run()

```python
from signalwire_agents import AgentBase
from signalwire_agents.core.function_result import SwaigFunctionResult

agent = AgentBase(name="test", route="/")

## Functions must be defined before run()
@agent.tool(description="Test function")
def test_func() -> SwaigFunctionResult:
    return SwaigFunctionResult("Test")

## Then run
if __name__ == "__main__":
    agent.run()
```

#### Function Returns Wrong Response

**Symptom**: AI receives unexpected or empty response.

**Check 1**: Return SwaigFunctionResult

```python
## Correct
@agent.tool(description="Get status")
def get_status() -> SwaigFunctionResult:
    return SwaigFunctionResult("Status is OK")

## Wrong: Returns string instead of SwaigFunctionResult
@agent.tool(description="Get status")
def get_status() -> SwaigFunctionResult:
    return "Status is OK"  # This won't work!
```

### Connection Issues

#### Webhook Not Reached

**Symptom**: Functions not being called, SignalWire can't reach agent.

**Check 1**: Agent is accessible from internet

```bash
## Local testing with ngrok
ngrok http 3000

## Then use ngrok URL in SignalWire
```

**Check 2**: Firewall allows connections

```bash
## Check if port is open
curl -I http://localhost:3000/
```

#### Authentication Failures

**Symptom**: 401 Unauthorized errors.

**Check credentials**:

```bash
## Test with credentials
curl -u username:password http://localhost:3000/
```

**Set in agent**:

```python
agent = AgentBase(
    name="secure",
    route="/",
    basic_auth=("username", "password")
)
```

### Speech Recognition Issues

#### Agent Not Hearing Caller

**Symptom**: AI doesn't respond to speech.

**Adjust confidence threshold**:

```python
agent.set_params({
    "confidence": 0.5,       # Lower = more sensitive
    "energy_level": 40       # Lower = quieter speech detected
})
```

#### Frequent Interruptions

**Symptom**: AI gets interrupted too easily.

```python
agent.set_params({
    "barge_confidence": 0.8,  # Higher = harder to interrupt
    "barge_min_words": 3      # Require 3+ words to barge
})
```

#### Speech Cut Off Too Early

**Symptom**: AI thinks caller finished speaking too soon.

```python
agent.set_params({
    "end_of_speech_timeout": 1500  # Wait 1.5s of silence (default 700ms)
})
```

### Timing Issues

#### Caller Waits Too Long

**Symptom**: Long delays before AI responds.

**Solutions**:

```python
## Use fillers
@agent.tool(
    description="Long operation",
    fillers=["One moment please..."]
)
def long_operation() -> SwaigFunctionResult:
    pass
```

#### Call Disconnects Unexpectedly

**Symptom**: Call ends without explicit hangup.

**Check inactivity timeout**:

```python
agent.set_params({
    "inactivity_timeout": 300000  # 5 minutes (default 10 minutes)
})
```

### DataMap Issues

#### Variable Not Substituting

**Symptom**: `${args.param}` appears literally in output.

**Check**: Parameter name matches

```python
data_map.add_parameter("city", "string", "City name", required=True)

## URL must use same name
data_map.add_webhook(
    url="https://api.example.com?q=${enc:args.city}",  # "city" matches
    ...
)
```

### Variable Syntax Reference

| Pattern | Usage |
|---------|-------|
| `${args.param}` | Function argument |
| `${enc:args.param}` | URL-encoded argument (use in URLs) |
| `${response.field}` | API response field |
| `${global_data.key}` | Global session data |

### Skill Issues

#### Skill Not Loading

**Symptom**: Skill added but functions not available.

**Check 1**: Skill name is correct

```python
## List available skills
print(agent.list_available_skills())

## Add by exact name
agent.add_skill("datetime")
agent.add_skill("native_vector_search")
```

**Check 2**: Dependencies installed

```bash
## Some skills require additional packages
pip install signalwire-agents[search]
```

### Serverless Issues

#### Lambda Function Errors

**Check 1**: Handler configuration

```python
## handler.py
from my_agent import agent

def handler(event, context):
    return agent.serverless_handler(event, context)
```

**Check 2**: Lambda timeout

Set Lambda timeout to at least 30 seconds for function processing.

### Common Error Messages

| Error | Solution |
|-------|----------|
| "Address already in use" | Change port or stop existing process |
| "Module not found" | `pip install signalwire-agents` |
| "401 Unauthorized" | Check basic_auth credentials |
| "Connection refused" | Ensure agent is running |
| "Function not found" | Check function name and decorator |
| "Invalid SWML" | Use `swaig-test --dump-swml` to debug |
| "Timeout" | Add fillers or optimize function |

### Getting Help

If issues persist:

1. Check SignalWire documentation
2. Review SDK examples in `/examples` directory
3. Use `swaig-test` for diagnostics
4. Check SignalWire community forums



---

## Migration Guide

> **Summary**: Guide for migrating to the SignalWire Agents SDK and common migration patterns.

### Current Version

| SDK Version | Python | SignalWire API | Status |
|-------------|--------|----------------|--------|
| 1.0.x | 3.8+ | v1 | Current stable release |

### Before Upgrading

1. **Review changelog** for breaking changes
2. **Backup your code** before upgrading
3. **Test in development** before production
4. **Check dependency compatibility**

```bash
## Check current version
pip show signalwire-agents

## View available versions
pip index versions signalwire-agents
```

### Upgrading

```bash
## Upgrade to latest
pip install --upgrade signalwire-agents

## Upgrade to specific version
pip install signalwire-agents==1.0.4

## Upgrade with all extras
pip install --upgrade "signalwire-agents[search-all]"
```

### Migration from Raw SWML

If migrating from hand-written SWML to the SDK:

#### Before (Raw SWML)

```json
{
  "version": "1.0.0",
  "sections": {
    "main": [{
      "ai": {
        "prompt": {
          "text": "You are a helpful assistant."
        },
        "languages": [{
          "name": "English",
          "code": "en-US",
          "voice": "rime.spore"
        }],
        "SWAIG": {
          "functions": [{
            "function": "lookup",
            "description": "Look up information",
            "parameters": {
              "type": "object",
              "properties": {
                "id": {
                  "type": "string",
                  "description": "Item ID"
                }
              },
              "required": ["id"]
            },
            "web_hook_url": "https://example.com/webhook"
          }]
        }
      }
    }]
  }
}
```

#### After (SDK)

```python
from signalwire_agents import AgentBase
from signalwire_agents.core.function_result import SwaigFunctionResult

agent = AgentBase(name="assistant", route="/")
agent.prompt_add_section("Role", "You are a helpful assistant.")
agent.add_language("English", "en-US", "rime.spore")

@agent.tool(description="Look up information")
def lookup(id: str) -> SwaigFunctionResult:
    # Your logic here
    return SwaigFunctionResult(f"Found item {id}")

if __name__ == "__main__":
    agent.run()
```

### Common Migration Tasks

| Old Style | New Style |
|-----------|-----------|
| JSON parameter schema | Python type hints |
| Manual webhook handler | `@agent.tool` decorator |
| Return JSON dict | Return `SwaigFunctionResult` |
| Manual response parsing | Automatic parameter injection |

### Class-Based Migration

If migrating from functional to class-based agents:

#### Before (Functional)

```python
from signalwire_agents import AgentBase
from signalwire_agents.core.function_result import SwaigFunctionResult

agent = AgentBase(name="service", route="/service")
agent.prompt_add_section("Role", "Customer service agent.")
agent.add_language("English", "en-US", "rime.spore")

@agent.tool(description="Get account balance")
def get_balance(account_id: str) -> SwaigFunctionResult:
    balance = lookup_balance(account_id)
    return SwaigFunctionResult(f"Balance: ${balance}")

if __name__ == "__main__":
    agent.run()
```

#### After (Class-Based)

```python
from signalwire_agents import AgentBase
from signalwire_agents.core.function_result import SwaigFunctionResult


class ServiceAgent(AgentBase):
    def __init__(self):
        super().__init__(name="service", route="/service")
        self.prompt_add_section("Role", "Customer service agent.")
        self.add_language("English", "en-US", "rime.spore")

    @AgentBase.tool(description="Get account balance")
    def get_balance(self, account_id: str) -> SwaigFunctionResult:
        balance = self.lookup_balance(account_id)
        return SwaigFunctionResult(f"Balance: ${balance}")

    def lookup_balance(self, account_id: str) -> float:
        # Your lookup logic
        return 100.00


if __name__ == "__main__":
    agent = ServiceAgent()
    agent.run()
```

### Multi-Agent Migration

If migrating multiple agents to use AgentServer:

#### Before (Separate Processes)

```bash
## Running separate agent processes
python sales_agent.py &
python support_agent.py &
python billing_agent.py &
```

#### After (AgentServer)

```python
from signalwire_agents import AgentServer
from sales_agent import SalesAgent
from support_agent import SupportAgent
from billing_agent import BillingAgent

server = AgentServer(host="0.0.0.0", port=8080)
server.register(SalesAgent())
server.register(SupportAgent())
server.register(BillingAgent())

if __name__ == "__main__":
    server.run()
```

### Testing After Migration

```bash
## Verify SWML generation
swaig-test agent.py --dump-swml

## Compare with expected output
swaig-test agent.py --dump-swml > new_swml.json
diff old_swml.json new_swml.json

## Test all functions
swaig-test agent.py --list-tools
swaig-test agent.py --exec function_name --param value

## Run integration tests
pytest tests/
```

### Getting Help

For migration assistance:

1. Check the changelog for breaking changes
2. Review updated examples in `/examples`
3. Use `swaig-test` to validate changes
4. Test thoroughly in development



---

## Changelog

> **Summary**: Version history and release notes for the SignalWire Agents SDK.

### Version History

| Version | Date | Type | Highlights |
|---------|------|------|------------|
| 1.0.4 | 2025 | Feature | Call flow verb insertion API for SWML customization |
| 1.0.3 | 2025 | Patch | SWML schema updates for queues and context switching |
| 1.0.2 | 2025 | Patch | Added serve_static_files() to AgentServer |
| 1.0.1 | 2025 | Patch | Minor fixes to included examples |
| 1.0.0 | 2025 | Initial | First public release |

### Version 1.0.4

**Feature Release**

Added call flow verb insertion API for customizing SWML call flow with pre-answer, post-answer, and post-AI verbs.

#### Changes

| Area | Change |
|------|--------|
| AgentBase | Added `add_pre_answer_verb()` for ringback tones, screening, routing |
| AgentBase | Added `add_post_answer_verb()` for welcome messages, disclaimers |
| AgentBase | Added `add_post_ai_verb()` for cleanup, transfers, logging |
| AgentBase | Added `add_answer_verb()` to configure answer verb (max_duration, etc.) |
| AgentBase | Added `clear_pre_answer_verbs()`, `clear_post_answer_verbs()`, `clear_post_ai_verbs()` |
| AgentBase | Fixed `auto_answer=False` to actually skip the answer verb |
| AgentBase | Added pre-answer verb validation with helpful warnings |

### Version 1.0.3

**Patch Release**

Updated SWML schema with new features for queue management and enhanced context switching.

#### Changes

| Area | Change |
|------|--------|
| SWML Schema | Added `enter_queue` method for queue management |
| SWML Schema | Added `change_context` action for SWAIG functions |
| SWML Schema | Added `change_step` action for SWAIG functions |
| SWML Schema | Added `transfer_after_bridge` parameter to `connect` method |
| SWML Schema | Improved documentation for `execute`, `transfer`, and `connect` destinations |
| SWML Schema | Fixed payment connector URL documentation link |

### Version 1.0.2

**Patch Release**

Added `serve_static_files()` method to `AgentServer` for properly serving static files alongside agents.

#### Changes

| Area | Change |
|------|--------|
| AgentServer | Added `serve_static_files(directory, route)` method |
| AgentServer | Static files now correctly fall back after agent routes |
| AgentServer | Both `/route` and `/route/` now work for agent endpoints |

### Version 1.0.1

**Patch Release**

Minor fixes to included examples for better compatibility with the `swaig-test` CLI tool.

#### Changes

| Area | Change |
|------|--------|
| Examples | Fixed deprecated API calls in `swml_service_routing_example.py` |
| Examples | Added error handling for remote search in `sigmond_remote_search.py` |
| Examples | Fixed argparse conflicts with swaig-test in several examples |
| Examples | Updated examples to return agents from `main()` for testing |

### Version 1.0.0

**Initial Release**

The first public release of the SignalWire Agents SDK, providing a comprehensive Python framework for building AI voice agents.

#### Core Features

| Feature | Description |
|---------|-------------|
| AgentBase | Base class for all voice AI agents |
| SWAIG Functions | Define callable functions with `@agent.tool` |
| SwaigFunctionResult | Chainable response builder with actions |
| DataMap | Serverless REST API integration |
| Skills System | Auto-discovered plugin architecture |
| Prefabs | Pre-built agent archetypes |
| Contexts | Multi-step conversation workflows |
| AgentServer | Host multiple agents on one server |

#### Built-in Skills

- **datetime**: Current time and date information
- **native_vector_search**: Local document search
- **web_search**: Web search integration
- **math**: Mathematical calculations
- **datasphere**: SignalWire DataSphere integration

#### Prefab Agents

- **InfoGatherer**: Structured information collection
- **FAQBot**: Knowledge base Q&A
- **Survey**: Multi-question surveys
- **Receptionist**: Call routing
- **Concierge**: Restaurant/service booking

#### CLI Tools

- **swaig-test**: Test agents and functions locally
- **sw-search**: Build and query search indexes

#### Deployment Support

- Local development server
- AWS Lambda
- Google Cloud Functions
- Azure Functions
- CGI mode
- Docker/Kubernetes

### Versioning Policy

The SDK follows [Semantic Versioning](https://semver.org/):

| Version Component | Meaning |
|-------------------|---------|
| MAJOR (1.x.x) | Breaking changes requiring code updates |
| MINOR (x.1.x) | New features, backwards compatible |
| PATCH (x.x.1) | Bug fixes, backwards compatible |

### Upgrade Notifications

To stay informed about new releases:

1. Watch the GitHub repository
2. Subscribe to release notifications
3. Check `pip show signalwire-agents` for current version
4. Use `pip install --upgrade signalwire-agents` to update

### Reporting Issues

To report bugs or request features:

1. Check existing GitHub issues
2. Create a new issue with:
   - SDK version (`pip show signalwire-agents`)
   - Python version (`python --version`)
   - Minimal reproduction code
   - Expected vs actual behavior

### Contributing

Contributions are welcome! See the repository's CONTRIBUTING.md for guidelines.


**This concludes the SignalWire Agents SDK documentation.**


