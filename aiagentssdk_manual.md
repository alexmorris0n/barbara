Don’t Panic: A Practical Manual for SignalWire AI Agents SDK

Brian West and Anthony Minessale II

**Contents**

**1 Getting Started**

**1**

1.1

What You’ll Learn . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 

1

1.2

Prerequisites . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 

1

1.3

Time to Complete . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 

1

1.4

By the End of This Chapter . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 

2

1.5

What is the SignalWire Agents SDK? . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 

2

1.6

How It Works

. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 

2

1.7

Key Concepts . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 

3

1.8

What You Can Build . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 

4

1.9

SDK Features

. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 

4

1.10 Minimal Example . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 

4

1.11 Next Steps . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 

5

1.12 Installation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 

6

1.13 Quick Start: Your First Agent . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 11

1.14 Development Environment Setup . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 16

1.15 Exposing Your Agent to the Internet . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 23

**2 Core Concepts**

**28**

2.1

What You’ll Learn . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 28

2.2

Prerequisites . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 28

2.3

The Big Picture . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 29

2.4

Key Terminology . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 29

2.5

Chapter Contents . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 30

2.6

Why These Concepts Matter . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 30

2.7

The Mixin Composition Pattern . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 30

2.8

Each Mixin’s Role . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 31

2.9

Key Internal Components . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 33

2.10 Creating Your Own Agent

. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 34

2.11 Benefits of This Architecture . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 34

2.12 Next Steps . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 34

2.13 SWML \(SignalWire Markup Language\) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 35

2.14 SWAIG \(SignalWire AI Gateway\) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 41

2.15 Request Lifecycle . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 49

2.16 Security . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 57

**3 Building Agents**

**63**

3.1

What You’ll Learn . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 63

3.2

Prerequisites . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 63

3.3

Agent Architecture Overview . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 64

3.4

A Complete Agent Example . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 64

3.5

Chapter Contents . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 66

3.6

Key Patterns . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 66

3.7

Testing Your Agent . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 67

3.8

Class Overview . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 67

3.9

Constructor Parameters . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 67

3.10 Parameter Reference . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 68

i

Contents

3.11 Creating an Agent . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 68

3.12 Key Methods . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 69

3.13 Agent Lifecycle . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 70

3.14 Configuration File . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 71

3.15 Environment Variables . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 71

3.16 Multi-Agent Server . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 71

3.17 Best Practices . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 72

3.18 Static vs Dynamic Agents . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 73

3.19 Prompts & POM . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 78

3.20 Voice & Language . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 84

3.21 AI Parameters . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 90

3.22 Hints . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 94

**4 SWAIG Functions**

**100**

4.1

What You’ll Learn . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 100

4.2

How SWAIG Functions Work . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 101

4.3

Quick Start Example . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 101

4.4

Function Types . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 102

4.5

Chapter Contents . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 102

4.6

When to Use SWAIG Functions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 103

4.7

Key Concepts . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 103

4.8

Basic Function Definition . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 103

4.9

The define\_tool\(\) Method . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 104

4.10 Handler Function Signature . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 104

4.11 Accessing Call Data . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 104

4.12 Multiple Functions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 105

4.13 Function Fillers

. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 106

4.14 The @tool Decorator . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 106

4.15 External Webhook Functions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 107

4.16 Function Security . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 107

4.17 Writing Good Descriptions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 107

4.18 Testing Functions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 108

4.19 Complete Example . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 108

4.20 Parameters . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 110

4.21 Results & Actions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 116

4.22 DataMap . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 120

4.23 Native Functions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 124

**5 Skills**

**128**

5.1

What You’ll Learn . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 128

5.2

What Are Skills? . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 128

5.3

Quick Start . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 129

5.4

Available Built-in Skills . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 129

5.5

Chapter Contents . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 129

5.6

Skills vs Functions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 130

5.7

When to Use Skills . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 130

5.8

Complete Example . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 130

5.9

Skill Architecture . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 131

5.10 How Skills Work . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 131

5.11 Skill Directory Structure . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 132

5.12 SkillBase Class . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 132

5.13 Skill Lifecycle . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 133

5.14 Skill Contributions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 133

5.15 Skill Discovery Paths . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 134

5.16 Lazy Loading . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 134

5.17 Multi-Instance Skills . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 134

5.18 Built-in Skills . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 136

ii

Contents

5.19 Adding Skills . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 141

5.20 Custom Skills . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 145

5.21 Skill Configuration . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 152

**6 Advanced Features**

**157**

6.1

What You’ll Learn . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 157

6.2

Feature Overview . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 157

6.3

When to Use These Features . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 158

6.4

Prerequisites . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 158

6.5

Chapter Contents . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 158

6.6

When to Use Contexts . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 159

6.7

Context Architecture . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 159

6.8

Basic Context Example . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 159

6.9

Step Configuration . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 160

6.10 Context Configuration . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 161

6.11 Multi-Context Example . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 162

6.12 Navigation Flow . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 163

6.13 Validation Rules . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 163

6.14 Step and Context Methods Summary . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 164

6.15 Best Practices . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 164

6.16 State Management . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 165

6.17 Call Recording . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 171

6.18 Call Transfer . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 177

6.19 Multi-Agent Servers . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 183

6.20 Search & Knowledge . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 190

**7 Deployment**

**196**

7.1

What You’ll Learn . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 196

7.2

Deployment Options Overview . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 196

7.3

Environment Detection . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 197

7.4

Chapter Contents . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 197

7.5

Quick Start . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 197

7.6

Starting the Development Server . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 197

7.7

Server Configuration . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 198

7.8

Development Endpoints . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 198

7.9

Testing Your Agent . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 198

7.10 Exposing Local Server . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 199

7.11 Environment Variables for Development . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 199

7.12 Proxy URL Configuration . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 199

7.13 Development Workflow . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 200

7.14 Debug Mode . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 200

7.15 Hot Reloading . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 200

7.16 Serving Static Files . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 201

7.17 Common Development Issues . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 202

7.18 Production Deployment . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 203

7.19 Serverless Deployment . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 208

7.20 Docker & Kubernetes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 213

7.21 CGI Mode . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 219

**8 SignalWire Integration**

**224**

8.1

What You’ll Learn . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 224

8.2

Integration Overview . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 224

8.3

Prerequisites . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 224

8.4

Chapter Contents . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 225

8.5

Quick Integration Steps . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 225

8.6

Architecture . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 226

8.7

Required URLs . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 226

iii

Contents

8.8

Security Considerations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 226

8.9

Create Account . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 227

8.10 Create a Project . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 227

8.11 Space Name

. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 227

8.12 API Credentials . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 227

8.13 Environment Variables . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 227

8.14 Dashboard Overview . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 228

8.15 Add Credit . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 228

8.16 Account Verification . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 228

8.17 Next Steps . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 228

8.18 Phone Numbers . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 229

8.19 Mapping Numbers . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 231

8.20 Testing . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 234

8.21 Troubleshooting . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 238

**9 Prefab Agents**

**241**

9.1

What Are Prefabs? . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 241

9.2

Why Use Prefabs? . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 241

9.3

Quick Examples . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 241

9.4

Chapter Contents . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 243

9.5

Importing Prefabs . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 243

9.6

Extending Prefabs . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 243

9.7

Basic Usage . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 244

9.8

Question Format . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 244

9.9

Constructor Parameters . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 244

9.10 Flow Diagram . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 245

9.11 Built-in Functions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 245

9.12 Dynamic Questions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 245

9.13 Accessing Collected Data . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 246

9.14 Complete Example . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 246

9.15 Best Practices . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 247

9.16 FAQBot . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 248

9.17 Survey . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 251

9.18 Receptionist . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 255

9.19 Concierge . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 258

**10 Reference**

**261**

10.1 Reference Overview . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 261

10.2 Quick Reference . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 261

10.3 Import Patterns . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 262

10.4 Chapter Contents . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 262

10.5 Class Definition . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 263

10.6 Constructor . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 263

10.7 Constructor Parameters . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 263

10.8 Prompt Methods . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 264

10.9 Language and Voice Methods . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 264

10.10 Tool Definition Methods . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 265

10.11 Skill Methods . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 265

10.12 AI Configuration Methods . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 265

10.13 State Methods . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 266

10.14 URL Methods . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 266

10.15 Server Methods . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 267

10.16 Serverless Methods . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 267

10.17 Callback Methods . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 267

10.18 SIP Routing Methods . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 268

10.19 Method Chaining . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 268

10.20 Class Attributes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 269

iv

Contents

10.21 SWMLService API . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 270

10.22 SWAIG Function API . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 274

10.23 SwaigFunctionResult API . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 279

10.24 DataMap API . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 287

10.25 SkillBase API . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 293

10.26 ContextBuilder API . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 299

10.27 swaig-test CLI . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 305

10.28 sw-search CLI . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 314

10.29 Environment Variables . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 329

10.30 Config Files . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 334

10.31 SWML Schema . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 339

**11 Examples**

**346**

11.1 How to Use This Chapter . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 346

11.2 Example Categories . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 346

11.3 Quick Start Examples . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 346

11.4 Running Examples . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 347

11.5 Example Structure . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 347

11.6 Chapter Contents . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 348

11.7 Basic Agent Setup . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 348

11.8 SWAIG Functions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 348

11.9 DataMap Integration . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 349

11.10 Call Transfers

. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 350

11.11 Skills Usage . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 351

11.12 Global Data . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 352

11.13 Recording . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 352

11.14 SMS Notifications . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 353

11.15 Static Files with AgentServer . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 353

11.16 Hints and Pronunciation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 354

11.17 Examples by Complexity . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 355

**12 Appendix**

**367**

12.1 About This Chapter . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 367

12.2 Quick Reference . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 367

12.3 Chapter Contents . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 368

12.4 Overview . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 368

12.5 Setting Parameters in Python . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 368

12.6 LLM API Parameters . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 369

12.7 ASR \(Speech Recognition\) Parameters . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 369

12.8 Timing Parameters . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 370

12.9 Behavior Parameters . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 370

12.10 SWAIG Control Parameters . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 371

12.11 Interrupt Parameters . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 371

12.12 Audio Parameters . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 371

12.13 Video Parameters . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 372

12.14 String Parameters . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 372

12.15 VAD Configuration

. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 372

12.16 Post-Prompt Parameter Defaults . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 372

12.17 Model-Specific Overrides . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 373

12.18 Complete Example . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 373

12.19 SWML Example . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 373

12.20 Design Patterns . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 375

12.21 Best Practices . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 380

12.22 Troubleshooting . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 384

12.23 Migration Guide . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 389

12.24 Changelog . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 393

v

**Chapter 1**

**Getting Started**

**Summary**: Everything you need to install the SignalWire Agents SDK, create your first voice AI agent, and connect it to the SignalWire platform. 

**1.1 What You’ll Learn**

This chapter walks you through the complete setup process:

1. **Introduction **- Understand what the SDK does and key concepts 2. **Installation **- Install the SDK and verify it works

3. **Quick Start **- Build your first agent in under 5 minutes

4. **Development Environment **- Set up a professional development workflow 5. **Exposing Your Agent **- Make your agent accessible to SignalWire using ngrok **1.2**

**Prerequisites**

Before starting, ensure you have:

• **Python 3.8 or higher **installed on your system

• **pip **\(Python package manager\)

• A **terminal/command line **interface

• A **text editor or IDE **\(VS Code, PyCharm, etc.\)

• \(Optional\) A **SignalWire account **for testing with real phone calls **1.3**

**Time to Complete**

**Section**

**Time**

Introduction

5 min read

Installation

5 min

Quick Start

5 min

Dev Environment

10 min

Exposing Agents

10 min

**Total**

**~35 minutes**

1

1. Getting Started

**1.4 By the End of This Chapter**

You will have:

• A working voice AI agent

• Accessible via public URL

• Ready to connect to SignalWire phone numbers

┌──────────────┐

┌──────────────┐

┌─────────────────┐

│

SignalWire

│◄──►│

ngrok

│◄──►│

Your Agent

│

│

Cloud

│

│

\(tunnel\)

│

│

localhost:3000 │

└──────────────┘

└──────────────┘

└─────────────────┘

**1.5 What is the SignalWire Agents SDK? **

The SignalWire Agents SDK lets you create **voice AI agents **- intelligent phone-based assistants that can:

• Answer incoming phone calls automatically

• Have natural conversations using AI \(GPT-4, Claude, etc.\)

• Execute custom functions \(check databases, call APIs, etc.\)

• Transfer calls, play audio, and manage complex call flows

• Scale from development to production seamlessly

**1.6 How It Works**

┌─────────────────────────────────────────────────────────────────────────────┐

│

High-Level Architecture

│

├─────────────────────────────────────────────────────────────────────────────┤

│

│

│

Phone Call

│

│

│

│

│

▼

│

│

┌─────────────────┐

┌─────────────────┐

│

│

│

│

SWML Request

│

│

│

│

│

SignalWire

│ ─────────────────► │

Your Agent

│

│

│

│

Cloud

│

│

\(Python Server\)│

│

│

│

│

SWML Response

│

│

│

│

│

• Routes calls │ ◄───────────────── │

• Defines AI

│

│

│

│

• Runs AI

│

│

behavior

│

│

│

│

• Handles TTS

│

Function Calls

│

• Provides

│

│

│

│

• Handles STT

│ ─────────────────► │

functions

│

│

│

│

│

│

• Handles

│

│

│

│

│

Function Results │

webhooks

│

│

│

│

│ ◄───────────────── │

│

│

│

└─────────────────┘

└─────────────────┘

│

│

│

└─────────────────────────────────────────────────────────────────────────────┘

**The flow:**

1. A caller dials your SignalWire phone number

2. SignalWire requests instructions from your agent \(via HTTP\)

3. Your agent returns **SWML **\(SignalWire Markup Language\) - a JSON document describing how to handle the call

4. SignalWire’s AI talks to the caller based on your configuration 5. When the AI needs to perform actions, it calls your **SWAIG functions **\(webhooks\) 6. Your functions return results, and the AI continues the conversation 2

1. Getting Started

**1.7 Key Concepts**

**1.7.1 Agent**

An **Agent **is your voice AI application. It’s a Python class that: - Defines the AI’s personality and behavior \(via prompts\) - Provides functions the AI can call \(SWAIG functions\) - Configures voice, language, and AI parameters -

Runs as a web server that responds to SignalWire requests

from signalwire\_agents import AgentBase

**class **MyAgent\(AgentBase\):

**def \_\_init\_\_**\(self\):

super\(\). **\_\_init\_\_**\(name**=**"my-agent"\)

*\# Configure your agent here*

**1.7.2**

**SWML \(SignalWire Markup Language\)**

**SWML **is a JSON format that tells SignalWire how to handle calls. Your agent generates SWML automatically -

you don’t write it by hand. 

**\{**

"version" **: **"1.0.0" **, **

"sections" **: \{**

"main" **: **\[

**\{**"answer" **: \{\}\}**, 

**\{**"ai" **: \{**

"prompt" **: \{**"text" **: **"You are a helpful assistant..." **\}, **

"SWAIG" **: \{**"functions" **: **\[**... **\]**\}**

**\}\}**

\]

**\}**

**\}**

**1.7.3**

**SWAIG Functions**

**SWAIG **\(SignalWire AI Gateway\) functions are tools your AI can use during a conversation. When a caller asks something that requires action, the AI calls your function. 

@agent.tool\(description**=**"Look up a customer by phone number"\) **def **lookup\_customer\(phone\_number: str\) **-> **str:

customer **= **database.find\(phone\_number\)

**return **f"Customer: **\{**customer**. **name**\}**, Account: **\{**customer**. **id**\}**" 

**1.7.4**

**Skills**

**Skills **are reusable plugins that add capabilities to your agent. The SDK includes built-in skills for common tasks:

• datetime - Get current time and date

• web\_search - Search the web

• weather\_api - Get weather information

• math - Perform calculations

agent.add\_skill\("datetime"\)

agent.add\_skill\("web\_search", google\_api\_key**=**"..."\) 3

1. Getting Started

**1.8 What You Can Build**

**Use Case**

**Description**

**Customer Service**

Answer FAQs, route calls, collect information

**Appointment Scheduling**

Book, reschedule, and cancel appointments

**Surveys & Feedback**

Conduct phone surveys, collect responses

**IVR Systems**

Interactive voice menus with AI intelligence

**Receptionist**

Screen calls, take messages, transfer to staff

**Notifications**

Outbound calls for alerts, reminders, confirmations

**1.9 SDK Features**

**Category**

**Features**

Core

AgentBase class, SWAIG function decorators, Prompt building \(POM\), Voice & language config, Speech hints, Built-in skills

Advanced

Multi-step workflows \(Contexts\), Multi-agent servers, Call recording, Call transfer \(SIP, PSTN\), State management, Vector search integration

Deployment

Local dev server, Production \(uvicorn\), AWS Lambda, Google Cloud

Functions, Azure Functions, CGI mode, Docker/Kubernetes

Developer Tools

swaig-test CLI, SWML debugging, Function testing, Serverless simulation Prefab Agents

InfoGathererAgent, FAQBotAgent, SurveyAgent, ReceptionistAgent, 

ConciergeAgent

DataMap

Direct API calls from SignalWire, No webhook server needed, Variable expansion, Response mapping

**1.10**

**Minimal Example**

Here’s the simplest possible agent:

from signalwire\_agents import AgentBase

**class **HelloAgent\(AgentBase\):

**def \_\_init\_\_**\(self\):

super\(\). **\_\_init\_\_**\(name**=**"hello"\)

self.prompt\_add\_section\("Role", "You are a friendly assistant."\) **if **\_\_name\_\_ **== **"\_\_main\_\_":

agent **= **HelloAgent\(\)

agent.run\(\)

This agent: - Starts a web server on port 3000 - Returns SWML that configures an AI assistant - Uses the default voice and language settings - Has no custom functions \(just conversation\) 4

1. Getting Started

**1.11 Next Steps**

Now that you understand what the SDK does, let’s install it and build something real. 

5

1. Getting Started

**1.12**

**Installation**

**Summary**: Install the SignalWire Agents SDK using pip and verify everything works correctly. 

**1.12.1 System Requirements**

**Requirement**

**Minimum**

**Recommended**

Python

3.8\+

3.10\+

pip

20.0\+

Latest

OS

Linux, macOS, Windows

Any

Memory

512MB

1GB\+

**1.12.2**

**Basic Installation**

Install the SDK from PyPI:

pip install signalwire-agents

This installs the core SDK with all essential features for building voice AI agents. 

**1.12.3**

**Verify Installation**

Confirm the installation was successful:

python -c "from signalwire\_agents import AgentBase; print\('SignalWire Agents SDK installed successfully\!'\)" 

You should see:

SignalWire Agents SDK installed successfully\! 

**1.12.4**

**Installation Extras**

The SDK provides optional extras for additional features:

**1.12.4.1**

**Search Capabilities**

*\#\# Query-only \(read .swsearch files\) - ~400MB*

pip install signalwire-agents *\[* search *-* queryonly *\]*

*\#\# Build indexes \+ vector search - ~500MB*

pip install signalwire-agents *\[* search *\]*

*\#\# Full document processing \(PDF, DOCX\) - ~600MB*

pip install signalwire-agents *\[* search *-* full *\]*

*\#\# NLP features \(spaCy\) - ~600MB*

pip install signalwire-agents *\[* search *-* nlp *\]*

*\#\# All search features - ~700MB*

pip install signalwire-agents *\[* search *-* all *\]*

6

1. Getting Started

**1.12.4.2 Database Support**

*\#\# PostgreSQL vector database support*

pip install signalwire-agents *\[* pgvector *\]*

**1.12.4.3 Development Dependencies**

*\#\# All development tools \(testing, linting\)*

pip install signalwire-agents *\[* dev *\]*

**1.12.5**

**Installation from Source**

For development or to get the latest changes:

*\#\# Clone the repository*

**git **clone https://github.com/signalwire/signalwire-agents.git cd signalwire-agents

*\#\# Create virtual environment*

python -m venv venv

source venv/bin/activate

*\# On Windows: venv\\Scripts\\activate*

*\#\# Install in development mode*

pip install -e . 

*\#\# Or with extras*

pip install -e ".\[search,dev\]" 

**1.12.6**

**Virtual Environment Setup**

Always use a virtual environment to avoid conflicts:

*\#\# Create virtual environment*

python -m venv venv

*\#\# Activate \(Linux/macOS\)*

source venv/bin/activate

*\#\# Activate \(Windows Command Prompt\)*

venv\\Scripts\\activate

*\#\# Activate \(Windows PowerShell\)*

venv\\Scripts\\Activate.ps1

*\#\# Install the SDK*

pip install signalwire-agents

*\#\# Verify activation \(should show venv path\)*

**which **python

**1.12.7**

**Quick Verification Script**

*\#\!/usr/bin/env python3*

*\#\# verify\_install.py - Verify SignalWire Agents SDK installation*

*"""Verify SignalWire Agents SDK installation.""" *

**def **main\(\):

print\("Checking SignalWire Agents SDK installation...\\n"\)

*\# Check core import*

**try**:

from signalwire\_agents import AgentBase

print\("\[OK\] Core SDK: AgentBase imported successfully"\)

7

1. Getting Started

**except ** *ImportError * as e:

print\(f"\[FAIL\] Core SDK: Failed to import AgentBase - **\{**e**\}**"\) **return **False

*\# Check SWAIG function support*

**try**:

from signalwire\_agents import SwaigFunctionResult

print\("\[OK\] SWAIG: SwaigFunctionResult imported successfully"\) **except ** *ImportError * as e:

print\(f"\[FAIL\] SWAIG: Failed to import SwaigFunctionResult - **\{**e**\}**"\) **return **False

*\# Check prefabs*

**try**:

from signalwire\_agents.prefabs import InfoGathererAgent

print\("\[OK\] Prefabs: InfoGathererAgent imported successfully"\) **except ** *ImportError * as e:

print\(f"\[FAIL\] Prefabs: Failed to import - **\{**e**\}**"\)

*\# Check search \(optional\)*

**try**:

from signalwire\_agents.search import SearchEngine

print\("\[OK\] Search: SearchEngine available"\)

**except ** *ImportError*:

print\("\[SKIP\] Search: Not installed \(optional\)"\)

print\("\\n" **\+ **"=" **\***50\)

print\("Installation verification complete\!"\)

print\("=" **\***50\)

**return **True

**if **\_\_name\_\_ **== **"\_\_main\_\_":

main\(\)

Run it:

python verify\_install.py

Expected output:

Checking SignalWire Agents SDK installation... 

\[OK\] Core SDK: AgentBase imported successfully

\[OK\] SWAIG: SwaigFunctionResult imported successfully

\[OK\] Prefabs: InfoGathererAgent imported successfully

\[SKIP\] Search: Not installed \(optional\)



==================================================
Installation verification complete\! 


==================================================
**1.12.8**


**Troubleshooting**

8

1. Getting Started

**1.12.8.1 Common Issues**

**Problem**

**Cause**

**Solution**

ModuleNotFoundError: No module named ' 

Package not installed

Run pip install signalwi

signalwire\_agents' 

re-agents

pip: command not found

pip not in PATH

Use python -m pip install

signalwire-agents

Permission errors

Installing globally without sudo

Use virtual environment or

pip install --user

Old pip version

pip can’t resolve dependencies

Run pip install --upgrad

e pip

Conflicts with other packages

Dependency version mismatch

Use a fresh virtual

environment

**1.12.8.2 Python Version Check**

Ensure you have Python 3.8\+:

python --version

*\#\# or*

python3 --version

If you have multiple Python versions:

*\#\# Use specific version*

python3.10 -m venv venv

source venv/bin/activate

pip install signalwire-agents

**1.12.8.3**

**Upgrade Existing Installation**

pip install --upgrade signalwire-agents

**1.12.8.4**

**Clean Reinstall**

pip uninstall signalwire-agents

pip cache purge

pip install signalwire-agents

**1.12.9**

**What Gets Installed**

The SDK installs these core dependencies:

**Package**

**Purpose**

fastapi

Web framework for serving SWML

uvicorn

ASGI server for running the agent

pydantic

Data validation and settings

structlog

Structured logging

httpx

HTTP client for API calls

9

1. Getting Started

**1.12.10 Next Steps**

Now that the SDK is installed, let’s create your first agent. 

10

1. Getting Started

**1.13 Quick Start: Your First Agent**

**Summary**: Build a working voice AI agent in under 5 minutes with a single Python file. 

**1.13.1 The Minimal Agent**

*\#\!/usr/bin/env python3*

*\#\# my\_first\_agent.py - A simple voice AI agent*

*""" *

*My First SignalWire Agent*

*A simple voice AI agent that greets callers and has conversations. *

*""" *

from signalwire\_agents import AgentBase

**class **MyFirstAgent\(AgentBase\):

**def \_\_init\_\_**\(self\):

super\(\). **\_\_init\_\_**\(name**=**"my-first-agent"\)

*\# Set the voice*

self.add\_language\("English", "en-US", "rime.spore"\)

*\# Define the AI's personality and behavior*

self.prompt\_add\_section\(

"Role", 

"You are a friendly and helpful assistant. Greet the caller warmly " 

"and help them with any questions they have. Keep responses concise " 

"and conversational." 

\)

self.prompt\_add\_section\(

"Guidelines", 

body**=**"Follow these rules:", 

bullets**=**\[

"Be friendly and professional", 

"Keep responses brief \(1-2 sentences when possible\)", 

"If you don't know something, say so honestly", 

"End conversations politely when the caller is done" 

\]

\)

**if **\_\_name\_\_ **== **"\_\_main\_\_":

agent **= **MyFirstAgent\(\)

print\("Starting My First Agent..."\)

print\("Server running at: http://localhost:3000"\)

print\("Press Ctrl\+C to stop"\)

agent.run\(\)

**1.13.2**

**Run the Agent**

Start your agent:

python my\_first\_agent.py

You’ll see output like:

\[12:29:56\] INFO

security\_config \(info:72\) security\_config\_loaded \(service=SWMLService, ssl\_enabled=False, domain=None, allowed\_hosts=\['\*'\], cors\_origins=\['\*'\], max\_request\_size=10485760, rate\_limit=60, use\_hsts=True, has\_basic\_auth=False\)

\[12:29:56\] INFO

swml\_service

\(info:72\) service\_initializing \(service=my-first-agent, route=, host=0.0.0.0, port=3000\)

\[12:29:56\] INFO

agent\_base

\(info:72\) agent\_initializing \(agent=my-first-agent, route=/, host=0.0.0.0, port=3000\) Starting My First Agent... 

Server running at: http://localhost:3000

Press Ctrl\+C to stop

11

1. Getting Started

\[12:29:56\] INFO

agent\_base

\(info:72\) agent\_starting \(agent=my-first-agent, url=http://localhost:3000, username=signalwire, password\_length=43, auth\_source=provided, ssl\_enabled=False\) Agent 'my-first-agent' is available at:

URL: http://localhost:3000

Basic Auth: signalwire:7vVZ8iMTOWL0Y7-BG6xaN3qhjmcm4Sf59nORNdlF9bs \(source: provided\) INFO:

Started server process \[49982\]

INFO:

Waiting for application startup. 

INFO:

Application startup complete. 

INFO:

Uvicorn running on http://0.0.0.0:3000 \(Press CTRL\+C to quit\)

**Note: **The SDK shows: - Security configuration \(SSL, CORS, rate limits\) - Service initialization details - Basic auth credentials \(username and password\) - Server startup information

**1.13.3**

**Test the Agent**

Open a new terminal and test with curl:

*\#\# Get the SWML document \(what SignalWire receives\)*

curl http://localhost:3000/

You’ll see JSON output like:

**\{**

"version" **: **"1.0.0" **, **

"sections" **: \{**

"main" **: **\[

**\{**"answer" **: \{\}\}**, 

**\{**

"ai" **: \{**

"prompt" **: \{**

"text" **: **"\# Role\\nYou are a friendly and helpful assistant..." 

**\}, **

"languages" **: **\[

**\{**"name" **: **"English" **, **"code" **: **"en-US" **, **"voice" **: **"rime.spore" **\}**

\]

**\}**

**\}**

\]

**\}**

**\}**

**1.13.4**

**What Just Happened? **

**1. You run: python my\_first\_agent.py**

Agent starts a web server on port 3000. 

**2. SignalWire \(or curl\) sends: GET http://localhost:3000/**

Agent returns SWML document \(JSON\). 

**3. SWML tells SignalWire: **- Answer the call - Use this AI prompt \(your personality config\) - Use this voice \(rime.spore\) - Use English language

**4. SignalWire’s AI: **- Converts caller’s speech to text \(STT\) - Sends text to AI model \(GPT-4, etc.\) - Gets AI response - Converts response to speech \(TTS\)

**1.13.5**

**Adding a Custom Function**

Let’s add a function the AI can call:

*\#\!/usr/bin/env python3*

*\#\# my\_first\_agent\_with\_function.py - Agent with custom function*

*""" *

*My First SignalWire Agent - With Custom Function*

12

1. Getting Started

*""" *

from signalwire\_agents import AgentBase, SwaigFunctionResult

**class **MyFirstAgent\(AgentBase\):

**def \_\_init\_\_**\(self\):

super\(\). **\_\_init\_\_**\(name**=**"my-first-agent"\)

*\# Set the voice*

self.add\_language\("English", "en-US", "rime.spore"\)

*\# Define the AI's personality*

self.prompt\_add\_section\(

"Role", 

"You are a friendly assistant who can tell jokes. " 

"When someone asks for a joke, use your tell\_joke function." 

\)

*\# Register the custom function*

self.define\_tool\(

name**=**"tell\_joke", 

description**=**"Tell a joke to the caller", 

parameters**=**\{"type": "object", "properties": \{\}\}, handler**=**self.tell\_joke

\)

**def **tell\_joke\(self, args, raw\_data\):

*"""Return a joke for the AI to tell.""" *

import random

jokes **= **\[

"Why do programmers prefer dark mode? Because light attracts bugs\!", 

"Why did the Python programmer need glasses? Because they couldn't C\!", 

"What's a programmer's favorite hangout spot? Foo Bar\!", 

\]

joke **= **random.choice\(jokes\)

**return **SwaigFunctionResult\(f"Here's a joke: **\{**joke**\}**"\) **if **\_\_name\_\_ **== **"\_\_main\_\_":

agent **= **MyFirstAgent\(\)

print\("Starting My First Agent \(with jokes\!\)..."\)

print\("Server running at: http://localhost:3000"\)

agent.run\(\)

Now when a caller asks for a joke, the AI will call your tell\_joke function\! 

**1.13.6**

**Using the Debug Endpoint**

The agent provides a debug endpoint to inspect its configuration:

curl http://localhost:3000/debug

This shows detailed information about: - Registered functions - Prompt configuration - Voice settings - Authentication credentials

**1.13.7**

**Test with swaig-test CLI**

The SDK includes a CLI tool for testing:

*\#\# Show the SWML document*

swaig-test my\_first\_agent.py --dump-swml

*\#\# List available functions*

swaig-test my\_first\_agent.py --list-tools

13

1. Getting Started

*\#\# Test a function*

swaig-test my\_first\_agent.py --exec tell\_joke

**1.13.8 Complete Example with Multiple Features**

Here’s a more complete example showing common patterns:

*\#\!/usr/bin/env python3*

*\#\# complete\_first\_agent.py - Complete agent example with multiple features*

*""" *

*Complete First Agent Example*

*Demonstrates:*

*- Voice configuration*

*- AI parameters*

*- Prompt sections*

*- Custom functions*

*- Speech hints*

*""" *

from signalwire\_agents import AgentBase, SwaigFunctionResult

**class **CompleteFirstAgent\(AgentBase\):

**def \_\_init\_\_**\(self\):

super\(\). **\_\_init\_\_**\(

name**=**"complete-agent", 

auto\_answer**=**True, 

record\_call**=**False

\)

*\# Voice and language*

self.add\_language\("English", "en-US", "rime.spore"\)

*\# AI behavior parameters*

self.set\_params\(\{

"end\_of\_speech\_timeout": 500, 

*\# Wait 500ms for speaker to finish*

"attention\_timeout": 15000

*\# 15 second attention span*

\}\)

*\# Speech recognition hints \(improves accuracy\)*

self.add\_hints\(\[

"SignalWire", 

"SWML", 

"AI agent" 

\]\)

*\# Prompt sections*

self.prompt\_add\_section\(

"Identity", 

"You are Alex, a helpful AI assistant created by SignalWire." 

\)

self.prompt\_add\_section\(

"Capabilities", 

body**=**"You can help callers with:", 

bullets**=**\[

"Answering general questions", 

"Telling jokes", 

"Providing the current time", 

"Basic conversation" 

\]

\)

self.prompt\_add\_section\(

"Style", 

"Keep responses brief and friendly. Use a conversational tone." 

\)

14

1. Getting Started

*\# Register functions*

self.define\_tool\(

name**=**"get\_current\_time", 

description**=**"Get the current time", 

parameters**=**\{"type": "object", "properties": \{\}\}, handler**=**self.get\_current\_time

\)

self.define\_tool\(

name**=**"tell\_joke", 

description**=**"Tell a random joke", 

parameters**=**\{"type": "object", "properties": \{\}\}, handler**=**self.tell\_joke

\)

**def **get\_current\_time\(self, args, raw\_data\):

*"""Return the current time.""" *

from datetime import datetime

now **= **datetime.now\(\)

**return **SwaigFunctionResult\(f"The current time is **\{**now**. **strftime\('%I:%M %p'\)**\}**"\) **def **tell\_joke\(self, args, raw\_data\):

*"""Return a random joke.""" *

import random

jokes **= **\[

"Why do programmers prefer dark mode? Because light attracts bugs\!", 

"Why did the developer go broke? Because they used up all their cache\!", 

"There are only 10 types of people: those who understand binary and those who don't.", 

\]

**return **SwaigFunctionResult\(random.choice\(jokes\)\)

**if **\_\_name\_\_ **== **"\_\_main\_\_":

agent **= **CompleteFirstAgent\(\)

print\("=" **\***60\)

print\("Complete First Agent"\)

print\("=" **\***60\)

print\(f"Server: http://localhost:3000"\)

print\(f"Debug:

http://localhost:3000/debug"\)

print\(""\)

print\("Features:"\)

print\(" 

- Custom voice \(rime.spore\)"\)

print\(" 

- Speech hints for better recognition"\)

print\(" 

- Two custom functions \(time, jokes\)"\)

print\("=" **\***60\)

agent.run\(\)

**1.13.9**

**Next Steps**

Your agent is running locally, but SignalWire can’t reach localhost. You need to expose it to the internet. 

**Or skip to: Exposing Your Agent **- Make your agent accessible via ngrok 15

1. Getting Started

**1.14 Development Environment Setup**

**Summary**: Configure a professional development environment for building SignalWire agents with proper project structure, environment variables, and debugging tools. 

**1.14.1 Recommended Project Structure**

my-agent-project/

├── venv/

\# Virtual environment

├── agents/

\# Your agent modules

│

├── \_\_init\_\_.py

│

├── customer\_service.py

│

└── support\_agent.py

├── skills/

\# Custom skills \(optional\)

│

└── my\_custom\_skill/

│

├── \_\_init\_\_.py

│

└── skill.py

├── tests/

\# Test files

│

├── \_\_init\_\_.py

│

└── test\_agents.py

├── .env

\# Environment variables \(not in git\)

├── .env.example

\# Example env file \(in git\)

├── .gitignore

├── requirements.txt

└── main.py

\# Entry point

**1.14.2**

**Create the Project**

*\#\# Create project directory*

**mkdir **my-agent-project

cd my-agent-project

*\#\# Create virtual environment*

python -m venv venv

source venv/bin/activate

*\# Windows: venv\\Scripts\\activate*

*\#\# Install dependencies*

pip install signalwire-agents

*\#\# Create directory structure*

**mkdir **-p agents skills tests

*\#\# Create initial files*

**touch **agents/\_\_init\_\_.py

**touch **tests/\_\_init\_\_.py

**touch **.env .env.example .gitignore requirements.txt main.py **1.14.3**

**Environment Variables**

Create a .env file for configuration:

*\#\# .env - DO NOT COMMIT THIS FILE*

*\#\# Authentication*

*\#\# These set your agent's basic auth credentials. *

*\#\# If not set, SDK uses username "signalwire" with an auto-generated*

*\#\# password that changes on every invocation \(printed to console\). *

SWML\_BASIC\_AUTH\_USER**=**my\_username

SWML\_BASIC\_AUTH\_PASSWORD**=**my\_secure\_password\_here

*\#\# Server Configuration*

SWML\_PROXY\_URL\_BASE**=**https://my-agent.ngrok.io

16

1. Getting Started

*\#\# SSL \(optional, for production\)*

SWML\_SSL\_ENABLED**=**false

SWML\_SSL\_CERT\_PATH**=**

SWML\_SSL\_KEY\_PATH**=**

*\#\# Skill API Keys \(as needed\)*

GOOGLE\_API\_KEY**=**your\_google\_api\_key

GOOGLE\_CX\_ID**=**your\_custom\_search\_id

WEATHER\_API\_KEY**=**your\_weather\_api\_key

*\#\# Logging*

SIGNALWIRE\_LOG\_MODE**=**default

**Important**: The SWML\_BASIC\_AUTH\_USER and SWML\_BASIC\_AUTH\_PASSWORD environment variables let you set stable credentials for your agent. Without these: - Username defaults to signalwire - Password is randomly generated on each startup - The generated password is printed to the console

For development, you can leave these unset and use the printed credentials. For production, always set explicit values. 

Create .env.example as a template \(safe to commit\):

*\#\# .env.example - Template for environment variables*

*\#\# Authentication \(optional - SDK generates credentials if not set\)* SWML\_BASIC\_AUTH\_USER**=**

SWML\_BASIC\_AUTH\_PASSWORD**=**

*\#\# Server Configuration*

SWML\_PROXY\_URL\_BASE**=**

*\#\# Skill API Keys*

GOOGLE\_API\_KEY**=**

WEATHER\_API\_KEY**=**

**1.14.4**

**Loading Environment Variables**

Install python-dotenv:

pip install python-dotenv

Load in your agent:

*\#\!/usr/bin/env python3*

*\#\# main.py - Main entry point with environment loading*

*"""Main entry point with environment loading.""" *

import os

from dotenv import load\_dotenv

*\#\# Load environment variables from .env file*

load\_dotenv\(\)

from agents.customer\_service import CustomerServiceAgent

**def **main\(\):

agent **= **CustomerServiceAgent\(\)

*\# Use environment variables*

host **= **os.getenv\("AGENT\_HOST", "0.0.0.0"\) port **= **int\(os.getenv\("AGENT\_PORT", "3000"\)\) print\(f"Starting agent on **\{**host**\}**:**\{**port**\}**"\) agent.run\(host**=**host, port**=**port\)

17

1. Getting Started

**if **\_\_name\_\_ **== **"\_\_main\_\_":

main\(\)

**1.14.5 The .gitignore File**

\#\# Virtual environment

venv/

.venv/

env/

\#\# Environment variables

.env

.env.local

.env.\*.local

\#\# Python

\_\_pycache\_\_/

\*.py\[cod\]

\*$py.class

\*.so

.Python

build/

dist/

\*.egg-info/

\#\# IDE

.idea/

.vscode/

\*.swp

\*.swo

\*~

\#\# Testing

.pytest\_cache/

.coverage

htmlcov/

\#\# Logs

\*.log

\#\# OS

.DS\_Store

Thumbs.db

**1.14.6**

**Requirements File**

Create requirements.txt:

signalwire-agents>=1.0.2

python-dotenv>=1.0.0

Or generate from current environment:

pip freeze **> **requirements.txt

**1.14.7**

**IDE Configuration**

18

1. Getting Started

**1.14.7.1 VS Code**

Create .vscode/settings.json:

**\{**

"python.defaultInterpreterPath" **: **"$\{workspaceFolder\}/venv/bin/python" **, **

"python.envFile" **: **"$\{workspaceFolder\}/.env" **, **

"python.testing.pytestEnabled" **: true, **

"python.testing.pytestArgs" **: **\["tests"\]**, **

"editor.formatOnSave" **: true, **

"python.formatting.provider" **: **"black" 

**\}**

Create .vscode/launch.json for debugging:

**\{**

"version" **: **"0.2.0" **, **

"configurations" **: **\[

**\{**

"name" **: **"Run Agent" **, **

"type" **: **"python" **, **

"request" **: **"launch" **, **

"program" **: **"$\{workspaceFolder\}/main.py" **, **

"console" **: **"integratedTerminal" **, **

"envFile" **: **"$\{workspaceFolder\}/.env" 

**\}**, 

**\{**

"name" **: **"Run Current File" **, **

"type" **: **"python" **, **

"request" **: **"launch" **, **

"program" **: **"$\{file\}" **, **

"console" **: **"integratedTerminal" **, **

"envFile" **: **"$\{workspaceFolder\}/.env" 

**\}**, 

**\{**

"name" **: **"Test Agent with swaig-test" **, **

"type" **: **"python" **, **

"request" **: **"launch" **, **

"module" **: **"signalwire\_agents.cli.test\_swaig" **, **

"args" **: **\["$\{file\}", "--dump-swml"\]**, **

"console" **: **"integratedTerminal" 

**\}**

\]

**\}**

**1.14.7.2**

**PyCharm**

1. Open Settings → Project → Python Interpreter

2. Select your virtual environment

3. Go to Run → Edit Configurations

4. Create a Python configuration:

• Script path: main.py

• Working directory: Project root

• Environment variables: Load from .env

**1.14.8**

**Using swaig-test for Development**

The swaig-test CLI is essential for development:

*\#\# View SWML output \(formatted\)*

swaig-test agents/customer\_service.py --dump-swml

*\#\# View raw SWML JSON*

swaig-test agents/customer\_service.py --dump-swml --raw

*\#\# List all registered functions*

19

1. Getting Started

swaig-test agents/customer\_service.py --list-tools

*\#\# Execute a specific function*

swaig-test agents/customer\_service.py --exec get\_customer --customer\_id 12345

*\#\# Simulate serverless environment*

swaig-test agents/customer\_service.py --simulate-serverless lambda --dump-swml **1.14.9 Development Workflow**

**1. Edit Code**

Modify your agent in agents/. 

**2. Quick Test **- swaig-test agents/my\_agent.py --dump-swml - Verify SWML looks correct **3. Function Test **- swaig-test agents/my\_agent.py --exec my\_function --arg value - Verify function returns expected result

**4. Run Server **- python main.py - curl http://localhost:3000/

**5. Integration Test **- Start ngrok \(see next section\) - Configure SignalWire webhook - Make test call **1.14.10**

**Sample Agent Module**

*\#\!/usr/bin/env python3*

*\#\# customer\_service.py - Customer service agent*

*""" *

*Customer Service Agent*

*A production-ready customer service agent template. *

*""" *

import os

from signalwire\_agents import AgentBase, SwaigFunctionResult

**class **CustomerServiceAgent\(AgentBase\):

*"""Customer service voice AI agent.""" *

**def \_\_init\_\_**\(self\):

super\(\). **\_\_init\_\_**\(

name**=**"customer-service", 

route**=**"/", 

host**=**"0.0.0.0", 

port**=**int\(os.getenv\("AGENT\_PORT", "3000"\)\)

\)

self.\_configure\_voice\(\)

self.\_configure\_prompts\(\)

self.\_configure\_functions\(\)

**def **\_configure\_voice\(self\):

*"""Set up voice and language.""" *

self.add\_language\("English", "en-US", "rime.spore"\) self.set\_params\(\{

"end\_of\_speech\_timeout": 500, 

"attention\_timeout": 15000, 

\}\)

self.add\_hints\(\[

"account", 

"billing", 

"support", 

"representative" 

\]\)

**def **\_configure\_prompts\(self\):

20

1. Getting Started

*"""Set up AI prompts.""" *

self.prompt\_add\_section\(

"Role", 

"You are a helpful customer service representative for Acme Corp. " 

"Help customers with their questions about accounts, billing, and products." 

\)

self.prompt\_add\_section\(

"Guidelines", 

body**=**"Follow these guidelines:", 

bullets**=**\[

"Be professional and courteous", 

"Ask clarifying questions when needed", 

"Offer to transfer to a human if you cannot help", 

"Keep responses concise" 

\]

\)

**def **\_configure\_functions\(self\):

*"""Register SWAIG functions.""" *

self.define\_tool\(

name**=**"lookup\_account", 

description**=**"Look up a customer account by phone number or account ID", parameters**=**\{

"type": "object", 

"properties": \{

"identifier": \{

"type": "string", 

"description": "Phone number or account ID" 

\}

\}, 

"required": \["identifier"\]

\}, 

handler**=**self.lookup\_account

\)

self.define\_tool\(

name**=**"transfer\_to\_human", 

description**=**"Transfer the call to a human representative", parameters**=**\{"type": "object", "properties": \{\}\}, handler**=**self.transfer\_to\_human

\)

**def **lookup\_account\(self, args, raw\_data\):

*"""Look up account information.""" *

identifier **= **args.get\("identifier", ""\)

*\# In production, query your database here*

**return **SwaigFunctionResult\(

f"Found account for **\{**identifier**\}**: Status is Active, Balance is $0.00" 

\)

**def **transfer\_to\_human\(self, args, raw\_data\):

*"""Transfer to human support.""" *

**return **SwaigFunctionResult\(

"Transferring you to a human representative now." 

\).connect\("\+15551234567", final**=**True, from\_addr**=**"\+15559876543"\)

*\#\# Allow running directly for testing*

**if **\_\_name\_\_ **== **"\_\_main\_\_":

agent **= **CustomerServiceAgent\(\)

agent.run\(\)

21

1. Getting Started

**1.14.11 Testing Your Agent**

*\#\!/usr/bin/env python3*

*\#\# test\_agents.py - Tests for agents*

*"""Tests for agents.""" *

import pytest

from agents.customer\_service import CustomerServiceAgent

**class **TestCustomerServiceAgent:

*"""Test customer service agent.""" *

**def **setup\_method\(self\):

*"""Set up test fixtures.""" *

self.agent **= **CustomerServiceAgent\(\)

**def **test\_agent\_name\(self\):

*"""Test agent has correct name.""" *

**assert **self.agent.name **== **"customer-service" 

**def **test\_lookup\_account\(self\):

*"""Test account lookup function.""" *

result **= **self.agent.lookup\_account\(

\{"identifier": "12345"\}, 

\{\}

\)

**assert **"Found account" **in **result

**def **test\_has\_functions\(self\):

*"""Test agent has expected functions.""" *

functions **= **self.agent.\_tool\_registry.get\_function\_names\(\)

**assert **"lookup\_account" **in **functions

**assert **"transfer\_to\_human" **in **functions

Run tests:

pytest tests/ -v

**1.14.12**

**Next Steps**

Your development environment is ready. Now let’s expose your agent to the internet so SignalWire can reach it. 

22

1. Getting Started

**1.15 Exposing Your Agent to the Internet**

**Summary**: Use ngrok to create a public URL for your local agent so SignalWire can send webhook requests to it. 

**1.15.1 Why You Need a Public URL**

SignalWire’s cloud needs to reach your agent via HTTP:

┌─────────────────────────────────────────────────────────────────────────────┐

│

The Problem

│

├─────────────────────────────────────────────────────────────────────────────┤

│

│

│

SignalWire Cloud

Your Computer

│

│

┌─────────────────┐

┌─────────────────┐

│

│

│

│

│

│

│

│

│

Needs to send

│

CANNOT

│

localhost:3000 │

│

│

│

HTTP requests

│ ───── X ─────────► │

│

│

│

│

│

REACH

│

\(Not on the

│

│

│

└─────────────────┘

│

internet\)

│

│

│

└─────────────────┘

│

│

│

└─────────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────────┐

│

The Solution: ngrok

│

├─────────────────────────────────────────────────────────────────────────────┤

│

│

│

SignalWire Cloud

ngrok Cloud

Your Computer

│

│

┌─────────────────┐

┌─────────────────┐

┌─────────────────┐

│

│

│

│

│

│

│

│

│

│

│

Sends request

│───►│

abc123.ngrok.io│──►│

localhost:3000 │

│

│

│

to public URL

│

│

\(tunnel\)

│

│

│

│

│

│

│◄───│

│◄──│

│

│

│

└─────────────────┘

└─────────────────┘

└─────────────────┘

│

│

│

│

https://abc123.ngrok.io

───►

tunnels to

───►

http://localhost:3000

│

│

│

└─────────────────────────────────────────────────────────────────────────────┘

**1.15.2**

**Installing ngrok**

**1.15.2.1**

**macOS \(Homebrew\)**

brew install ngrok

**1.15.2.2**

**Linux**

*\#\# Download*

curl -s https://ngrok-agent.s3.amazonaws.com/ngrok.asc **| **\\

**sudo **tee /etc/apt/trusted.gpg.d/ngrok.asc **> **/dev/null **&& **\\ echo "deb https://ngrok-agent.s3.amazonaws.com buster main" **| **\\ **sudo **tee /etc/apt/sources.list.d/ngrok.list

*\#\# Install*

**sudo **apt update **&& sudo **apt install ngrok

23

1. Getting Started

**1.15.2.3 Windows**

*\#\# Using Chocolatey*

choco install ngrok

*\#\# Or download from https://ngrok.com/download*

**1.15.2.4 Direct Download**

Visit ngrok.com/download and download for your platform. 

**1.15.3**

**Create an ngrok Account \(Free\)**

1. Go to ngrok.com and sign up

2. Get your auth token from the dashboard

3. Configure ngrok with your token:

ngrok config add-authtoken YOUR\_AUTH\_TOKEN\_HERE

This enables: - Longer session times - Custom subdomains \(paid\) - Multiple tunnels **1.15.4**

**Basic Usage**

Start your agent in one terminal:

*\#\# Terminal 1*

python my\_agent.py

Start ngrok in another terminal:

*\#\# Terminal 2*

ngrok http 3000

You’ll see output like:

ngrok

\(Ctrl\+C to quit\)

Session Status

online

Account

your-email@example.com \(Plan: Free\)

Version

3.x.x

Region

United States \(us\)

Latency

45ms

Web Interface

http://127.0.0.1:4040

Forwarding

https://abc123def456.ngrok-free.app -> http://localhost:3000

Connections

ttl

opn

rt1

rt5

p50

p90

0

0

0.00

0.00

0.00

0.00

Your public URL is: https://abc123def456.ngrok-free.app

**1.15.5**

**Test the Tunnel**

*\#\# Test locally*

curl http://localhost:3000/

*\#\# Test through ngrok \(use YOUR URL from ngrok output\)*

curl https://abc123def456.ngrok-free.app/

Both should return the same SWML document. 

24

1. Getting Started

**1.15.6 ngrok Web Interface**

ngrok provides a web interface at http://127.0.0.1:4040 showing:

• All requests coming through the tunnel

• Request/response headers and bodies

• Timing information

• Ability to replay requests

This is invaluable for debugging SignalWire webhook calls\! 

**1.15.7**

**Static Domains \(Recommended\)**

Free ngrok gives you random URLs that change each restart. For easier development, use a static domain: **1.15.7.1 Free Static Domain \(ngrok account required\)**

1. Go to ngrok Dashboard → Domains

2. Create a free static domain \(e.g., your-name.ngrok-free.app\)

3. Use it:

ngrok http 3000 --domain**=**your-name.ngrok-free.app

Now your URL stays the same across restarts\! 

**1.15.8**

**Configure Your Agent for ngrok**

Set the SWML\_PROXY\_URL\_BASE environment variable so your agent generates correct webhook URLs:

*\#\# In your .env file*

SWML\_PROXY\_URL\_BASE**=**https://your-name.ngrok-free.app

Or set it when running:

SWML\_PROXY\_URL\_BASE**=**https://your-name.ngrok-free.app python my\_agent.py This ensures SWAIG function webhook URLs point to your public ngrok URL, not localhost. 

**1.15.9**

**Complete Development Setup**

Here’s the full workflow:

*\#\# Terminal 1: Start ngrok with static domain*

ngrok http 3000 --domain**=**your-name.ngrok-free.app

*\#\# Terminal 2: Start agent with proxy URL*

export SWML\_PROXY\_URL\_BASE**=**https://your-name.ngrok-free.app python my\_agent.py

*\#\# Terminal 3: Test*

curl https://your-name.ngrok-free.app/

curl https://your-name.ngrok-free.app/debug

**1.15.10**

**Using a Script**

Create start-dev.sh:

*\#\!/bin/bash*

*\#\# start-dev.sh - Start development environment*

NGROK\_DOMAIN**=**"your-name.ngrok-free.app" 

25

1. Getting Started

echo "Starting development environment..." 

echo "Public URL: https://$\{NGROK\_DOMAIN\}" 

echo "" 

*\#\# Start ngrok in background*

ngrok http 3000 --domain**=**$\{NGROK\_DOMAIN\} **& **

NGROK\_PID**=**$\! 

*\#\# Wait for ngrok to start*

**sleep **2

*\#\# Start agent with proxy URL*

export SWML\_PROXY\_URL\_BASE**=**"https://$\{NGROK\_DOMAIN\}" 

python my\_agent.py

*\#\# Cleanup on exit*

trap "kill $NGROK\_PID 2>/dev/null" EXIT

Make it executable:

**chmod **\+x start-dev.sh

./start-dev.sh

**1.15.11**

**Alternative Tunneling Solutions**

**1.15.11.1 Cloudflare Tunnel \(Free\)**

*\#\# Install cloudflared*

brew install cloudflared

*\# macOS*

*\#\# Quick tunnel \(no account needed\)*

cloudflared tunnel --url http://localhost:3000

**1.15.11.2**

**localtunnel \(Free, no signup\)**

*\#\# Install*

npm install -g localtunnel

*\#\# Run*

lt --port 3000

**1.15.11.3**

**tailscale Funnel \(Requires Tailscale\)**

*\#\# If you use Tailscale*

tailscale funnel 3000

**1.15.12**

**Production Alternatives**

For production, don’t use ngrok. Instead:

**Option**

**Description**

**Cloud VM**

Deploy to AWS, GCP, Azure, DigitalOcean

**Serverless**

AWS Lambda, Google Cloud Functions, Azure Functions

**Container**

Docker on Kubernetes, ECS, Cloud Run

**VPS**

Any server with a public IP

See the Deployment chapter for production deployment guides. 

26

1. Getting Started

**1.15.13 Troubleshooting**

**1.15.13.1 ngrok shows “ERR\_NGROK\_108” **

Your auth token is invalid or expired. Get a new one from the ngrok dashboard: ngrok config add-authtoken YOUR\_NEW\_TOKEN

**1.15.13.2 Connection refused**

Your agent isn’t running or is on a different port:

*\#\# Check agent is running*

curl http://localhost:3000/

*\#\# If using different port*

ngrok http 8080

**1.15.13.3 Webhook URLs still show localhost**

Set SWML\_PROXY\_URL\_BASE:

export SWML\_PROXY\_URL\_BASE**=**https://your-domain.ngrok-free.app python my\_agent.py

**1.15.13.4**

**ngrok tunnel expires**

Free ngrok tunnels expire after a few hours. Solutions: - Restart ngrok - Use a static domain \(stays same after restart\) - Upgrade to paid ngrok plan - Use an alternative like Cloudflare Tunnel **1.15.14**

**What’s Next? **

Your agent is now accessible at a public URL. You’re ready to connect it to SignalWire\! 

**1.15.15**

**You’ve Completed Phase 1\! **

⊠ Installed the SDK

⊠ Created your first agent

⊠ Set up development environment

⊠ Exposed agent via ngrok

Your agent is ready at: https://your-domain.ngrok-free.app

**Next Chapter: Core Concepts **- Deep dive into SWML, SWAIG, and agent architecture **Or jump to: SignalWire Integration **- Connect your agent to phone numbers 27

**Chapter 2**

**Core Concepts**

**Summary**: Understand the fundamental architecture, protocols, and patterns that power the SignalWire Agents SDK. 

**2.1 What You’ll Learn**

This chapter covers the foundational concepts you need to build effective voice AI agents: 1. **Architecture **- How AgentBase and its mixins work together 2. **SWML **- The markup language that controls call flows

3. **SWAIG **- The gateway that lets AI call your functions

4. **Lifecycle **- How requests flow through the system

5. **Security **- Authentication and token-based function security **2.2**

**Prerequisites**

Before diving into these concepts, you should have:

• Completed the Getting Started chapter

• A working agent running locally

• Basic understanding of HTTP request/response patterns

28

2. Core Concepts

**2.3**

**The Big Picture**

┌─────────────────────────────────────────────────────────────────────────────┐

│

SignalWire Agents SDK Architecture

│

├─────────────────────────────────────────────────────────────────────────────┤

│

│

│

Incoming Call

│

│

│

│

│

▼

│

│

┌─────────────────────────────────────────────────────────────────────┐

│

│

│

SignalWire Cloud

│

│

│

│

• Receives call

│

│

│

│

• Requests SWML from your agent

│

│

│

│

• Executes AI conversation

│

│

│

│

• Calls SWAIG functions when AI needs tools

│

│

│

└─────────────────────────────────────────────────────────────────────┘

│

│

│

│

│

HTTP Requests

│

HTTP Responses

│

│

\(GET /, POST /swaig\) │

\(SWML JSON\)

│

│

▼

│

│

┌─────────────────────────────────────────────────────────────────────┐

│

│

│

Your Agent

│

│

│

│

┌───────────────────────────────────────────────────────────────┐

│

│

│

│

│

AgentBase

│

│

│

│

│

│

┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐

│

│

│

│

│

│

│AuthMixin │ │ WebMixin │ │ ToolMixin │ │SkillMixin│

│

│

│

│

│

│

└──────────┘ └──────────┘ └──────────┘ └──────────┘

│

│

│

│

│

│

┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐

│

│

│

│

│

│

│PromptMix │ │AIConfig

│ │Serverless│ │StateMixin│

│

│

│

│

│

│

└──────────┘ └──────────┘ └──────────┘ └──────────┘

│

│

│

│

│

│

│

│

│

│

│

│

│

┌───────────────┐

│

│

│

│

│

│

│

SWMLService

│

│

│

│

│

│

│

│

\(Generates

│

│

│

│

│

│

│

│

SWML JSON\)

│

│

│

│

│

│

│

└───────────────┘

│

│

│

│

│

└───────────────────────────────────────────────────────────────┘

│

│

│

└─────────────────────────────────────────────────────────────────────┘

│

│

│

└─────────────────────────────────────────────────────────────────────────────┘

**2.4**

**Key Terminology**

**Term**

**Definition**

**AgentBase**

The base class all agents inherit from

**SWML**

SignalWire Markup Language - JSON format for call instructions

**SWAIG**

SignalWire AI Gateway - System for AI to call your functions

**Mixin**

A class providing specific functionality to AgentBase

**POM**

Prompt Object Model - Structured prompt building

**DataMap**

Declarative REST API integration

29

2. Core Concepts

**2.5 Chapter Contents**

**Section**

**Description**

Architecture

AgentBase class and mixin composition

SWML

Understanding SWML document structure

SWAIG

How AI calls your functions

Lifecycle

Request/response flow

Security

Authentication and token security

**2.6 Why These Concepts Matter**

Understanding these core concepts helps you:

• **Debug effectively **- Know where to look when things go wrong

• **Build efficiently **- Use the right tool for each task

• **Scale confidently **- Understand how the system handles load

• **Extend properly **- Add custom functionality the right way

**2.7 The Mixin Composition Pattern**

AgentBase doesn’t inherit from a single monolithic class. Instead, it combines eight specialized mixins:

┌─────────────────────────────────────────────────────────────────────────────┐

│

AgentBase

│

│

\(Your agents inherit from this\)

│

├─────────────────────────────────────────────────────────────────────────────┤

│

│

│

Inherits from \(in MRO order\):

│

│

│

│

┌──────────────┐

┌──────────────┐

┌──────────────┐

│

│

│

AuthMixin

│───►│

WebMixin

│───►│ SWMLService

│

│

│

│

│

│

│

│

\(Base\)

│

│

│

│ • Basic auth │

│ • FastAPI

│

│ • Schema

│

│

│

│ • Credentials│

│ • Routes

│

│ • Render

│

│

│

│ • Validation │

│ • Server

│

│ • Verbs

│

│

│

└──────────────┘

└──────────────┘

└──────────────┘

│

│

│

│

│

│

│

▼

▼

▼

│

│

┌──────────────┐

┌──────────────┐

┌──────────────┐

│

│

│ PromptMixin

│───►│

ToolMixin

│───►│

SkillMixin

│

│

│

│

│

│

│

│

│

│

│

│ • POM

│

│ • SWAIG Fns

│

│ • Skill Mgmt │

│

│

│ • Sections

│

│ • Decorators │

│ • Registry

│

│

│

│ • Templates

│

│ • DataMap

│

│ • Loading

│

│

│

└──────────────┘

└──────────────┘

└──────────────┘

│

│

│

│

│

│

│

▼

▼

▼

│

│

┌──────────────┐

┌──────────────┐

┌──────────────┐

│

│

│AIConfigMixin │───►│ServerlessMix │───►│

StateMixin

│

│

│

│

│

│

│

│

│

│

│

│ • Languages

│

│ • Lambda

│

│ • Session

│

│

│

│ • Hints

│

│ • CGI

│

│ • Call State │

│

│

│ • Params

│

│ • Azure

│

│ • Persistence│

│

│

└──────────────┘

└──────────────┘

└──────────────┘

│

│

│

└─────────────────────────────────────────────────────────────────────────────┘

30

2. Core Concepts

**2.8**

**Each Mixin’s Role**

**2.8.1 AuthMixin - Authentication & Security**

Handles basic HTTP authentication for webhook endpoints. 

from signalwire\_agents import AgentBase

**class **MyAgent\(AgentBase\):

**def \_\_init\_\_**\(self\):

super\(\). **\_\_init\_\_**\(name**=**"my-agent"\)

*\# Auth credentials auto-generated or from environment:*

*\# SWML\_BASIC\_AUTH\_USER, SWML\_BASIC\_AUTH\_PASSWORD*

**Key methods: **- Validates incoming requests against stored credentials - Generates credentials if not provided via environment - Protects SWAIG function endpoints

**2.8.2**

**WebMixin - HTTP Server & Routing**

Manages the FastAPI application and HTTP endpoints. 

*\# Automatically registers these routes:*

*\# GET*

*/*

*→ Returns SWML document*

*\# POST /*

*→ Returns SWML document*

*\# POST /swaig*

*→ Handles SWAIG function calls*

*\# POST /post\_prompt → Receives call summaries*

*\# GET*

*/debug*

*→ Debug information \(dev only\)*

**Key features: **- Runs uvicorn server via agent.run\(\) - Handles proxy detection \(ngrok, load balancers\) - Manages request/response lifecycle

**2.8.3**

**SWMLService - SWML Document Generation**

The foundation for building SWML documents. 

*\# SWMLService provides:*

*\# - Schema validation against SWML spec*

*\# - Verb handler registry*

*\# - Document rendering pipeline*

**Key responsibilities: **- Validates SWML structure against JSON schema - Registers verb handlers \(answer, ai, connect, etc.\) - Renders final SWML JSON

**2.8.4**

**PromptMixin - Prompt Management**

Manages AI system prompts using POM \(Prompt Object Model\). 

agent.prompt\_add\_section\(

"Role", 

"You are a helpful customer service agent." 

\)

agent.prompt\_add\_section\(

"Guidelines", 

body**=**"Follow these rules:", 

bullets**=**\[

"Be concise", 

"Be professional", 

"Escalate when needed" 

\]

\)

**Key features: **- Structured prompt building with sections - Support for bullets, subsections - Post-prompt for call summaries

31

2. Core Concepts

**2.8.5**

**ToolMixin - SWAIG Function Management**

Handles registration and execution of SWAIG functions. 

agent.define\_tool\(

name**=**"get\_balance", 

description**=**"Get account balance", 

parameters**=**\{

"account\_id": \{

"type": "string", 

"description": "The account ID" 

\}

\}, 

handler**=**self.get\_balance

\)

**Key features: **- Multiple registration methods \(define\_tool, decorators, DataMap\) - Parameter validation - Security token generation

**2.8.6**

**SkillMixin - Skill Plugin Management**

Loads and manages reusable skill plugins. 

*\# Load built-in skill*

agent.add\_skill\("datetime"\)

*\# Load skill with configuration*

agent.add\_skill\("web\_search", 

google\_api\_key**=**"...", 

google\_cx\_id**=**"..." 

\)

**Key features: **- Auto-discovery of skill modules - Dependency checking - Configuration validation **2.8.7**

**AIConfigMixin - AI Behavior Configuration**

Configures the AI’s voice, language, and behavior parameters. 

agent.add\_language\("English", "en-US", "rime.spore"\) agent.set\_params\(\{

"end\_of\_speech\_timeout": 500, 

"attention\_timeout": 15000

\}\)

agent.add\_hints\(\["SignalWire", "SWML", "AI agent"\]\) **Key features: **- Voice and language settings - Speech recognition hints - AI behavior parameters **2.8.8**

**ServerlessMixin - Deployment Adapters**

Provides handlers for serverless deployments. 

*\# AWS Lambda*

handler **= **agent.serverless\_handler

*\# Google Cloud Functions*

**def **my\_function\(request\):

**return **agent.cloud\_function\_handler\(request\)

*\# Azure Functions*

**def **main\(req\):

**return **agent.azure\_function\_handler\(req\)

**Key features: **- Environment auto-detection - Request/response adaptation - URL generation for each platform 32

2. Core Concepts

**2.8.9**

**StateMixin - State Management**

Manages session and call state. 

*\# State is passed via global\_data in SWML*

*\# and preserved across function calls*

**Key features: **- Session tracking - State persistence patterns - Call context management **2.9 Key Internal Components**

Beyond the mixins, AgentBase uses several internal managers:

**2.9.1**

**ToolRegistry**

• Stores SWAIG functions

• Handles function lookup

• Generates webhook URLs

**2.9.2**

**PromptManager**

• Manages prompt sections

• Builds POM structure

• Handles post-prompts

**2.9.3**

**SessionManager**

• Token generation

• Token validation

• Security enforcement

**2.9.4**

**SkillManager**

• Skill discovery

• Skill loading

• Configuration validation

**2.9.5**

**SchemaUtils**

• SWML schema loading

• Document validation

• Schema-driven help

**2.9.6**

**VerbHandlerRegistry**

• Verb registration

• Handler dispatch

• Custom verb support

33

2. Core Concepts

**2.10 Creating Your Own Agent**

When you create an agent, you get all mixin functionality automatically: from signalwire\_agents import AgentBase, SwaigFunctionResult

**class **CustomerServiceAgent\(AgentBase\):

**def \_\_init\_\_**\(self\):

super\(\). **\_\_init\_\_**\(name**=**"customer-service"\)

*\# AIConfigMixin methods*

self.add\_language\("English", "en-US", "rime.spore"\) self.set\_params\(\{"end\_of\_speech\_timeout": 500\}\)

*\# PromptMixin methods*

self.prompt\_add\_section\("Role", "You are a helpful agent."\)

*\# ToolMixin methods*

self.define\_tool\(

name**=**"lookup\_order", 

description**=**"Look up an order by ID", 

parameters**=**\{

"order\_id": \{"type": "string", "description": "Order ID"\}

\}, 

handler**=**self.lookup\_order

\)

*\# SkillMixin methods*

self.add\_skill\("datetime"\)

**def **lookup\_order\(self, args, raw\_data\):

order\_id **= **args.get\("order\_id"\)

*\# Your business logic here*

**return **SwaigFunctionResult\(f"Order **\{**order\_id**\}**: Shipped, arrives tomorrow"\) **if **\_\_name\_\_ **== **"\_\_main\_\_":

agent **= **CustomerServiceAgent\(\)

agent.run\(\)

*\# WebMixin method*

**2.11**

**Benefits of This Architecture**

**Benefit**

**Description**

**Separation of Concerns**

Each mixin handles one domain

**Easy to Understand**

Look at one mixin for one feature

**Extensible**

Override specific mixin methods

**Testable**

Test mixins independently

**Type-Safe**

Full type hints throughout

**2.12**

**Next Steps**

Now that you understand how AgentBase is structured, let’s look at the SWML documents it generates. 

34

2. Core Concepts

**2.13 SWML \(SignalWire Markup Language\)**

**Summary**: SWML is the JSON format that tells SignalWire how to handle calls. Your agent generates SWML automatically - you configure the agent, and it produces the right SWML. 

**2.13.1 What is SWML? **

SWML \(SignalWire Markup Language\) is a document that instructs SignalWire how to handle a phone call. SWML

can be written in JSON or YAML format - **this guide uses JSON throughout**. When a call comes in, SignalWire requests SWML from your agent, then executes the instructions. 

┌─────────────────────────────────────────────────────────────────────────────┐

│

SWML Flow

│

├─────────────────────────────────────────────────────────────────────────────┤

│

│

│

1. Call Arrives

│

│

│

│

│

▼

│

│

2. SignalWire requests: GET https://your-agent.com/

│

│

│

│

│

▼

│

│

3. Your agent returns SWML JSON

│

│

│

│

│

▼

│

│

4. SignalWire executes the SWML instructions

│

│

│

│

│

▼

│

│

5. AI conversation begins based on SWML config

│

│

│

└─────────────────────────────────────────────────────────────────────────────┘

**2.13.2**

**SWML Document Structure**

Every SWML document has this structure:

**\{**

"version" **: **"1.0.0" **, **

"sections" **: \{**

"main" **: **\[

**\{ **"verb1" **: \{ ...config \} \}**, 

**\{ **"verb2" **: \{ ...config \} \}**, 

**\{ **"verb3" **: \{ ...config \} \}**

\]

**\}**

**\}**

**Key parts: **- version: Always "1.0.0" - sections: Contains named sections \(usually just main\) - Each section is an array of **verbs **\(instructions\)

35

2. Core Concepts

**2.13.3 Common Verbs**

**Verb**

**Purpose**

**Example**

answer

Answer the incoming call

\{"answer": \{\}\}

ai

Start AI conversation

\{"ai": \{...config\}\}

connect

Transfer to another number

\{"connect": \{"to": "\+1... 

"\}\}

play

Play audio file

\{"play": \{"url": "..."\}\}

record\_call

Record the call

\{"record\_call": \{"format" 

: "mp4"\}\}

hangup

End the call

\{"hangup": \{\}\}

**2.13.4**

**A Complete SWML Example**

Here’s what your agent generates:

**\{**

"version" **: **"1.0.0" **, **

"sections" **: \{**

"main" **: **\[

**\{**

"answer" **: \{\}**

**\}**, 

**\{**

"ai" **: \{**

"prompt" **: \{**

"text" **: **"\# Role\\nYou are a helpful customer service agent.\\n\\n\# Guidelines\\n- Be professional\\n- Be concise" 

**\}, **

"post\_prompt" **: **"Summarize what was discussed" **, **

"post\_prompt\_url" **: **"https://your-agent.com/post\_prompt" **, **

"SWAIG" **: \{**

"defaults" **: \{**

"web\_hook\_url" **: **"https://your-agent.com/swaig" 

**\}, **

"functions" **: **\[

**\{**

"function" **: **"get\_balance" **, **

"description" **: **"Get the customer's account balance" **, **

"parameters" **: \{**

"type" **: **"object" **, **

"properties" **: \{**

"account\_id" **: \{**

"type" **: **"string" **, **

"description" **: **"The account ID" 

**\}**

**\}, **

"required" **: **\["account\_id"\]

**\}**

**\}**

\]

**\}, **

"hints" **: **\["account", "balance", "payment"\]**, **

"languages" **: **\[

**\{**

"name" **: **"English" **, **

"code" **: **"en-US" **, **

"voice" **: **"rime.spore" 

**\}**

\]**, **

"params" **: \{**

"end\_of\_speech\_timeout" **: **500**, **

"attention\_timeout" **: **15000

**\}**

**\}**

36

2. Core Concepts

**\}**

\]

**\}**

**\}**

**2.13.5 The ai Verb in Detail**

The ai verb is the heart of voice AI agents. Here’s what each part does:

**\{**

"ai" **: \{**

"prompt" **: \{\}, **

**// What the AI should do \(system prompt\)**

"post\_prompt" **: **"..." **, **

**// Instructions for summarizing the call**

"post\_prompt\_url" **: **"..." **,// Where to send the summary**

"SWAIG" **: \{\}, **

**// Functions the AI can call**

"hints" **: **\[\]**, **

**// Words to help speech recognition**

"languages" **: **\[\]**, **

**// Voice and language settings**

"params" **: \{\}, **

**// AI behavior parameters**

"global\_data" **: \{\}**

**// Data available throughout the call**

**\}**

**\}**

**2.13.5.1 prompt**

The AI’s system prompt - its personality and instructions:

**\{**

"prompt" **: \{**

"text" **: **"You are a helpful assistant..." 

**\}**

**\}**

Or using POM \(Prompt Object Model\):

**\{**

"prompt" **: \{**

"pom" **: **\[

**\{**

"section" **: **"Role" **, **

"body" **: **"You are a customer service agent" 

**\}**, 

**\{**

"section" **: **"Rules" **, **

"bullets" **: **\["Be concise", "Be helpful"\]

**\}**

\]

**\}**

**\}**

**2.13.5.2**

**SWAIG**

Defines functions the AI can call:

**\{**

"SWAIG" **: \{**

"defaults" **: \{**

"web\_hook\_url" **: **"https://your-agent.com/swaig" 

**\}, **

"functions" **: **\[

**\{**

"function" **: **"check\_order" **, **

"description" **: **"Check order status" **, **

"parameters" **: \{**

"type" **: **"object" **, **

"properties" **: \{**

37

2. Core Concepts

"order\_id" **: \{**"type" **: **"string" **\}**

**\}**

**\}**

**\}**

\]

**\}**

**\}**

**2.13.5.3 hints**

Words that help speech recognition accuracy:

**\{**

"hints" **: **\["SignalWire", "SWML", "account number", "order ID"\]

**\}**

**2.13.5.4 languages**

Voice and language configuration:

**\{**

"languages" **: **\[

**\{**

"name" **: **"English" **, **

"code" **: **"en-US" **, **

"voice" **: **"rime.spore" 

**\}**

\]

**\}**

**2.13.5.5**

**params**

AI behavior settings:

**\{**

"params" **: \{**

"end\_of\_speech\_timeout" **: **500**, **

"attention\_timeout" **: **15000**, **

"barge\_match\_string" **: **"stop|cancel|quit" 

**\}**

**\}**

**2.13.6**

**How Your Agent Generates SWML**

You don’t write SWML by hand. Your agent configuration becomes SWML: from signalwire\_agents import AgentBase

**class **MyAgent\(AgentBase\):

**def \_\_init\_\_**\(self\):

super\(\). **\_\_init\_\_**\(name**=**"my-agent"\)

*\# This becomes languages in SWML*

self.add\_language\("English", "en-US", "rime.spore"\)

*\# This becomes prompt in SWML*

self.prompt\_add\_section\("Role", "You are helpful."\)

*\# This becomes hints in SWML*

self.add\_hints\(\["help", "support"\]\)

*\# This becomes params in SWML*

self.set\_params\(\{"end\_of\_speech\_timeout": 500\}\)

38

2. Core Concepts

*\# This becomes SWAIG.functions in SWML*

self.define\_tool\(

name**=**"get\_help", 

description**=**"Get help information", 

parameters**=**\{\}, 

handler**=**self.get\_help

\)

When SignalWire requests SWML, the agent’s \_render\_swml\(\) method:

1. Collects all configuration \(prompts, languages, hints, params\)

2. Builds the SWAIG functions array with webhook URLs

3. Assembles the complete SWML document

4. Returns JSON to SignalWire

**2.13.7**

**SWML Rendering Pipeline**

┌─────────────────────────────────────────────────────────────────────────────┐

│

SWML Rendering Pipeline

│

├─────────────────────────────────────────────────────────────────────────────┤

│

│

│

1. Request Arrives \(GET /\)

│

│

│

│

│

▼

│

│

2. \_render\_swml\(\) called

│

│

│

│

│

├───► Get prompt \(text or POM\)

│

│

├───► Get post-prompt

│

│

├───► Collect SWAIG functions

│

│

├───► Generate security tokens

│

│

├───► Build webhook URLs

│

│

├───► Collect hints, languages, params

│

│

│

│

│

▼

│

│

3. Assemble AI verb

│

│

│

│

│

▼

│

│

4. Build document: answer \+ ai verbs

│

│

│

│

│

▼

│

│

5. Return SWML JSON

│

│

│

└─────────────────────────────────────────────────────────────────────────────┘

**2.13.8**

**Viewing Your SWML**

You can see the SWML your agent generates:

*\#\# Using curl*

curl http://localhost:3000/

*\#\# Using swaig-test CLI*

swaig-test my\_agent.py --dump-swml

*\#\# Pretty-printed*

swaig-test my\_agent.py --dump-swml --raw **| **jq '.' 

39

2. Core Concepts

**2.13.9 SWML Schema Validation**

The SDK validates SWML against the official schema:

• Located at signalwire\_agents/core/schema.json

• Catches invalid configurations before sending to SignalWire

• Provides helpful error messages

**2.13.10 Common SWML Patterns**

**2.13.10.1 Auto-Answer with AI**

**\{**

"version" **: **"1.0.0" **, **

"sections" **: \{**

"main" **: **\[

**\{**"answer" **: \{\}\}**, 

**\{**"ai" **: \{...\}\}**

\]

**\}**

**\}**

**2.13.10.2 Record the Call**

**\{**

"version" **: **"1.0.0" **, **

"sections" **: \{**

"main" **: **\[

**\{**"answer" **: \{\}\}**, 

**\{**"record\_call" **: \{**"format" **: **"mp4" **, **"stereo" **: true\}\}**, 

**\{**"ai" **: \{...\}\}**

\]

**\}**

**\}**

**2.13.10.3**

**Transfer After AI**

When a SWAIG function returns a transfer action, the SWML for transfer is embedded in the response:

**\{**

"response" **: **"Transferring you now" **, **

"action" **: **\[

**\{**"transfer" **: true\}**, 

**\{**

"swml" **: \{**

"version" **: **"1.0.0" **, **

"sections" **: \{**

"main" **: **\[

**\{**"connect" **: \{**"to" **: **"\+15551234567" **, **"from" **: **"\+15559876543" **\}\}**

\]

**\}**

**\}**

**\}**

\]

**\}**

**2.13.11**

**Next Steps**

Now that you understand SWML structure, let’s look at SWAIG - how AI calls your functions. 

40

2. Core Concepts

**2.14 SWAIG \(SignalWire AI Gateway\)**

**Summary**: SWAIG is the system that lets the AI call your functions during a conversation. You define functions, SignalWire calls them via webhooks, and your responses guide the AI. 

**2.14.1 What is SWAIG? **

SWAIG \(SignalWire AI Gateway\) connects the AI conversation to your backend logic. When the AI decides it needs to perform an action \(like looking up an order or checking a balance\), it calls a SWAIG function that you’ve defined. 

┌─────────────────────────────────────────────────────────────────────────────┐

│

SWAIG Function Flow

│

├─────────────────────────────────────────────────────────────────────────────┤

│

│

│

User: "What's my account balance?" 

│

│

│

│

│

▼

│

│

┌─────────────────────────────────────────────────────────────────────┐

│

│

│

SignalWire AI Engine

│

│

│

│

1. Transcribes speech

│

│

│

│

2. Understands intent: "user wants account balance" 

│

│

│

│

3. Decides to call: get\_balance\(account\_id="12345"\)

│

│

│

└─────────────────────────────────────────────────────────────────────┘

│

│

│

│

│

│

POST /swaig

│

│

│

\{"function": "get\_balance", "argument": \{"account\_id": "12345"\}\}

│

│

▼

│

│

┌─────────────────────────────────────────────────────────────────────┐

│

│

│

Your Agent

│

│

│

│

def get\_balance\(self, args, raw\_data\):

│

│

│

│

account\_id = args.get\("account\_id"\)

│

│

│

│

balance = lookup\_balance\(account\_id\)

│

│

│

│

return SwaigFunctionResult\(f"Balance is $\{balance\}"\)

│

│

│

└─────────────────────────────────────────────────────────────────────┘

│

│

│

│

│

│

Response: \{"response": "Balance is $150.00"\}

│

│

▼

│

│

┌─────────────────────────────────────────────────────────────────────┐

│

│

│

SignalWire AI Engine

│

│

│

│

Speaks: "Your account balance is one hundred fifty dollars." 

│

│

│

└─────────────────────────────────────────────────────────────────────┘

│

│

│

└─────────────────────────────────────────────────────────────────────────────┘

**2.14.2**

**SWAIG in SWML**

When your agent generates SWML, it includes SWAIG function definitions in the ai verb:

**\{**

"version" **: **"1.0.0" **, **

"sections" **: \{**

"main" **: **\[

**\{**

"ai" **: \{**

"SWAIG" **: \{**

"defaults" **: \{**

"web\_hook\_url" **: **"https://your-agent.com/swaig" 

**\}, **

"functions" **: **\[

**\{**

"function" **: **"get\_balance" **, **

"description" **: **"Get the customer's current account balance" **, **

"parameters" **: \{**

41

2. Core Concepts

"type" **: **"object" **, **

"properties" **: \{**

"account\_id" **: \{**

"type" **: **"string" **, **

"description" **: **"The customer's account ID" 

**\}**

**\}, **

"required" **: **\["account\_id"\]

**\}**

**\}**

\]

**\}**

**\}**

**\}**

\]

**\}**

**\}**

**2.14.3**

**Defining SWAIG Functions**

There are three ways to define SWAIG functions in your agent:

**2.14.3.1 Method 1: define\_tool\(\)**

The most explicit way to register a function:

from signalwire\_agents import AgentBase, SwaigFunctionResult

**class **MyAgent\(AgentBase\):

**def \_\_init\_\_**\(self\):

super\(\). **\_\_init\_\_**\(name**=**"my-agent"\)

self.define\_tool\(

name**=**"get\_balance", 

description**=**"Get account balance for a customer", parameters**=**\{

"type": "object", 

"properties": \{

"account\_id": \{

"type": "string", 

"description": "The account ID to look up" 

\}

\}, 

"required": \["account\_id"\]

\}, 

handler**=**self.get\_balance

\)

**def **get\_balance\(self, args, raw\_data\):

account\_id **= **args.get\("account\_id"\)

*\# Your business logic here*

**return **SwaigFunctionResult\(f"Account **\{**account\_id**\} **has a balance of $150.00"\) **2.14.3.2**

**Method 2: @swaig\_function Decorator**

A cleaner approach using decorators:

from signalwire\_agents import AgentBase, SwaigFunctionResult, swaig\_function **class **MyAgent\(AgentBase\):

**def \_\_init\_\_**\(self\):

super\(\). **\_\_init\_\_**\(name**=**"my-agent"\)

@swaig\_function\(

description**=**"Get account balance for a customer", 42

2. Core Concepts

parameters**=**\{

"account\_id": \{

"type": "string", 

"description": "The account ID to look up" 

\}

\}

\)

**def **get\_balance\(self, args, raw\_data\):

account\_id **= **args.get\("account\_id"\)

**return **SwaigFunctionResult\(f"Account **\{**account\_id**\} **has a balance of $150.00"\) **2.14.3.3 Method 3: DataMap \(Serverless\)**

For direct API integration without code:

from signalwire\_agents import AgentBase

**class **MyAgent\(AgentBase\):

**def \_\_init\_\_**\(self\):

super\(\). **\_\_init\_\_**\(name**=**"my-agent"\)

self.data\_map.add\_tool\(

name**=**"get\_balance", 

description**=**"Get account balance", 

parameters**=**\{

"account\_id": \{

"type": "string", 

"description": "The account ID" 

\}

\}, 

data\_map**=**\{

"webhooks": \[

\{

"url": "https://api.example.com/accounts/$\{enc:args.account\_id\}/balance", 

"method": "GET", 

"headers": \{

"Authorization": "Bearer $**\{env.API\_KEY\}**" 

\}, 

"output": \{

"response": "Account balance is $$**\{balance\}**", 

"action": \[\{"set\_global\_data": \{"balance": "$**\{balance\}**"\}\}\]

\}

\}

\]

\}

\)

**2.14.4**

**Function Handler Signature**

Every SWAIG function handler receives two arguments:

**def **my\_function\(self, args, raw\_data\):

*""" *

*args: dict - The parsed arguments from the AI*

*Example: \{"account\_id": "12345", "include\_history": True\}*

*raw\_data: dict - The complete request payload from SignalWire*

*Contains metadata, call info, and conversation context*

*""" *

**pass**

43

2. Core Concepts

**2.14.4.1 The raw\_data Payload**

The raw\_data contains rich context about the call:

**def **my\_function\(self, args, raw\_data\):

*\# Call metadata*

call\_id **= **raw\_data.get\("call\_id"\)

call\_sid **= **raw\_data.get\("call\_sid"\)

*\# Caller information*

from\_number **= **raw\_data.get\("caller\_id\_num"\)

to\_number **= **raw\_data.get\("callee\_id\_num"\)

*\# Global data \(shared state\)*

global\_data **= **raw\_data.get\("global\_data", \{\}\)

customer\_name **= **global\_data.get\("customer\_name"\)

*\# Conversation context*

meta\_data **= **raw\_data.get\("meta\_data", \{\}\)

**return **SwaigFunctionResult\("Processed"\)

**2.14.5**

**SwaigFunctionResult**

Always return a SwaigFunctionResult from your handlers:

from signalwire\_agents import SwaigFunctionResult

**def **simple\_response\(self, args, raw\_data\):

*\# Simple text response - AI will speak this*

**return **SwaigFunctionResult\("Your order has been placed successfully."\) **def **response\_with\_actions\(self, args, raw\_data\):

result **= **SwaigFunctionResult\("Transferring you now."\)

*\# Add actions to control call behavior*

result.add\_action\("transfer", True\)

result.add\_action\("swml", \{

"version": "1.0.0", 

"sections": \{

"main": \[

\{"connect": \{"to": "\+15551234567", "from": "\+15559876543"\}\}

\]

\}

\}\)

**return **result

**def **response\_with\_data\(self, args, raw\_data\):

result **= **SwaigFunctionResult\("I've saved your preferences."\)

*\# Store data for later functions*

result.add\_action\("set\_global\_data", \{

"user\_preference": "email", 

"confirmed": True

\}\)

**return **result

44

2. Core Concepts

**2.14.6 Common Actions**

**Action**

**Purpose**

**Example**

set\_global\_data

Store data for later use

\{"key": "value"\}

transfer

End AI, prepare for transfer

True

swml

Execute SWML after AI ends

\{"version": "1.0.0", ...\}

stop

End the AI conversation

True

toggle\_functions

Enable/disable functions

\[\{"active": false, 

"function": "fn\_name"\}\]

say

Speak text immediately

"Please hold..." 

play\_file

Play audio file

"https://example.com/hold

\_music.mp3" 

**2.14.7**

**SWAIG Request Flow**

┌─────────────────────────────────────────────────────────────────────────────┐

│

SWAIG Request Processing

│

├─────────────────────────────────────────────────────────────────────────────┤

│

│

│

1. SignalWire sends POST to /swaig

│

│

│

│

│

▼

│

│

2. Agent validates authentication \(Basic Auth\)

│

│

│

│

│

▼

│

│

3. Agent validates function-specific token \(if configured\)

│

│

│

│

│

▼

│

│

4. Agent looks up function in ToolRegistry

│

│

│

│

│

├───► Function found ───► Execute handler

│

│

│

│

│

│

│

▼

│

│

│

Return SwaigFunctionResult

│

│

│

│

│

│

│

▼

│

│

│

Format JSON response

│

│

│

│

│

└───► Function not found ───► Return error response

│

│

│

│

5. Response sent to SignalWire

│

│

│

│

│

▼

│

│

6. AI incorporates response into conversation

│

│

│

└─────────────────────────────────────────────────────────────────────────────┘

**2.14.8**

**SWAIG Request Format**

SignalWire sends a POST request with this structure:

**\{**

"action" **: **"swaig\_action" **, **

"function" **: **"get\_balance" **, **

"argument" **: \{**

"parsed" **: **\[

**\{**

"account\_id" **: **"12345" 

45

2. Core Concepts

**\}**

\]**, **

"raw" **: **"\{\\"account\_id\\": \\"12345\\"\}" 

**\}, **

"call\_id" **: **"uuid-here" **, **

"call\_sid" **: **"call-sid-here" **, **

"caller\_id\_num" **: **"\+15551234567" **, **

"callee\_id\_num" **: **"\+15559876543" **, **

"global\_data" **: \{**

"customer\_name" **: **"John Doe" 

**\}, **

"meta\_data" **: \{\}, **

"ai\_session\_id" **: **"session-uuid" 

**\}**

**2.14.9**

**SWAIG Response Format**

Your agent responds with:

**\{**

"response" **: **"The account balance is $150.00" **, **

"action" **: **\[

**\{**

"set\_global\_data" **: \{**

"last\_balance\_check" **: **"2024-01-15T10:30:00Z" 

**\}**

**\}**

\]

**\}**

Or for a transfer:

**\{**

"response" **: **"Transferring you to a specialist now." **, **

"action" **: **\[

**\{**"transfer" **: true\}**, 

**\{**

"swml" **: \{**

"version" **: **"1.0.0" **, **

"sections" **: \{**

"main" **: **\[

**\{**"connect" **: \{**"to" **: **"\+15551234567" **, **"from" **: **"\+15559876543" **\}\}**

\]

**\}**

**\}**

**\}**

\]

**\}**

**2.14.10**

**Function Parameters \(JSON Schema\)**

SWAIG functions use JSON Schema for parameter definitions:

self.define\_tool\(

name**=**"search\_orders", 

description**=**"Search customer orders", 

parameters**=**\{

"type": "object", 

"properties": \{

"customer\_id": \{

"type": "string", 

"description": "Customer ID to search for" 

\}, 

"status": \{

"type": "string", 

"enum": \["pending", "shipped", "delivered", "cancelled"\], 46

2. Core Concepts

"description": "Filter by order status" 

\}, 

"limit": \{

"type": "integer", 

"description": "Maximum number of results", 

"default": 10

\}, 

"include\_details": \{

"type": "boolean", 

"description": "Include full order details", 

"default": False

\}

\}, 

"required": \["customer\_id"\]

\}, 

handler**=**self.search\_orders

\)

**2.14.11**

**Webhook Security**

SWAIG endpoints support multiple security layers:

1. **Basic Authentication**: HTTP Basic Auth on all requests

2. **Function Tokens**: Per-function security tokens

3. **HTTPS**: TLS encryption in transit

*\#\# Function-specific token security*

self.define\_tool\(

name**=**"sensitive\_action", 

description**=**"Perform a sensitive action", 

parameters**=**\{...\}, 

handler**=**self.sensitive\_action, 

secure**=**True

*\# Enables per-function token validation*

\)

**2.14.12**

**Testing SWAIG Functions**

Use swaig-test to test functions locally:

*\#\# List all registered functions*

swaig-test my\_agent.py --list-tools

*\#\# Execute a function with arguments*

swaig-test my\_agent.py --exec get\_balance --account\_id 12345

*\#\# View the SWAIG configuration in SWML*

swaig-test my\_agent.py --dump-swml **| grep **-A 50 '"SWAIG"' 

**2.14.13**

**Best Practices**

1. **Keep functions focused**: One function, one purpose

2. **Write clear descriptions**: Help the AI understand when to use each function 3. **Validate inputs**: Check for required arguments

4. **Handle errors gracefully**: Return helpful error messages

5. **Use global\_data**: Share state between function calls

6. **Log for debugging**: Track function calls and responses

**def **get\_balance\(self, args, raw\_data\):

account\_id **= **args.get\("account\_id"\)

**if not **account\_id:

**return **SwaigFunctionResult\(

"I need an account ID to look up the balance. " 

"Could you provide your account number?" 

47

2. Core Concepts

\)

**try**:

balance **= **self.lookup\_balance\(account\_id\)

**return **SwaigFunctionResult\(f"Your current balance is $**\{**balance**:.2f\}**"\) **except **AccountNotFoundError:

**return **SwaigFunctionResult\(

"I couldn't find an account with that ID. " 

"Could you verify the account number?" 

\)

**2.14.14**

**Next Steps**

Now that you understand how SWAIG connects AI to your code, let’s trace the complete lifecycle of a request through the system. 

48

2. Core Concepts

**2.15 Request Lifecycle**

**Summary**: Trace the complete journey of a call through the SignalWire Agents SDK, from incoming call to conversation end. 

**2.15.1 The Complete Call Flow**

Understanding the request lifecycle helps you debug issues and optimize your agents. Here’s the complete flow:

┌─────────────────────────────────────────────────────────────────────────────┐

│

Complete Call Lifecycle

│

├─────────────────────────────────────────────────────────────────────────────┤

│

│

│

PHASE 1: Call Setup

│

│

┌──────────────────────────────────────────────────────────────────────┐

│

│

│

1. Caller dials your phone number

│

│

│

│

2. SignalWire receives the call

│

│

│

│

3. SignalWire checks webhook configuration for the number

│

│

│

│

4. SignalWire requests SWML: POST https://your-agent.com/

│

│

│

└──────────────────────────────────────────────────────────────────────┘

│

│

│

│

│

▼

│

│

PHASE 2: SWML Generation

│

│

┌──────────────────────────────────────────────────────────────────────┐

│

│

│

5. Your agent receives the HTTP request

│

│

│

│

6. Agent builds SWML document \(prompts, functions, languages\)

│

│

│

│

7. Agent generates security tokens for SWAIG functions

│

│

│

│

8. Agent returns SWML JSON response

│

│

│

└──────────────────────────────────────────────────────────────────────┘

│

│

│

│

│

▼

│

│

PHASE 3: AI Conversation

│

│

┌──────────────────────────────────────────────────────────────────────┐

│

│

│

9. SignalWire executes SWML \(answers call, starts AI\)

│

│

│

│

10. AI speaks greeting from prompt

│

│

│

│

11. User speaks, AI listens and transcribes

│

│

│

│

12. AI processes and responds \(loop continues\)

│

│

│

└──────────────────────────────────────────────────────────────────────┘

│

│

│

│

│

▼

│

│

PHASE 4: Function Calls \(as needed\)

│

│

┌──────────────────────────────────────────────────────────────────────┐

│

│

│

13. AI decides to call a function

│

│

│

│

14. SignalWire sends POST to /swaig with function name and args

│

│

│

│

15. Your agent executes the handler

│

│

│

│

16. Agent returns SwaigFunctionResult

│

│

│

│

17. AI incorporates result and continues conversation

│

│

│

└──────────────────────────────────────────────────────────────────────┘

│

│

│

│

│

▼

│

│

PHASE 5: Call End

│

│

┌──────────────────────────────────────────────────────────────────────┐

│

│

│

18. Call ends \(hangup, transfer, or timeout\)

│

│

│

│

19. AI generates summary using post\_prompt

│

│

│

│

20. SignalWire sends POST to /post\_prompt with summary

│

│

│

│

21. Your agent receives and processes summary

│

│

│

└──────────────────────────────────────────────────────────────────────┘

│

│

│

└─────────────────────────────────────────────────────────────────────────────┘

49

2. Core Concepts

**2.15.2 Phase 1: Call Setup**

When a call arrives at SignalWire:

┌─────────────────────────────────────────────────────────────────────────────┐

│

Call Setup

│

├─────────────────────────────────────────────────────────────────────────────┤

│

│

│

Caller

SignalWire

Your Agent

│

│

│

│

│

│

│

│

Dial \+1-555-123-4567

│

│

│

│

│──────────────────────────►│

│

│

│

│

│

│

│

│

│

│

Look up webhook config

│

│

│

│

│

for this phone number

│

│

│

│

│

│

│

│

│

│

POST /

│

│

│

│

│───────────────────────────►│

│

│

│

│

│

│

│

│

│

Content-Type: application/json

│

│

│

│

Authorization: Basic xxx

│

│

│

│

│

│

│

│

│

└─────────────────────────────────────────────────────────────────────────────┘

**Key points: **- SignalWire knows which agent to contact based on phone number configuration - The request includes Basic Auth credentials - POST is the default; GET requests are also supported for SWML retrieval **2.15.3**

**Phase 2: SWML Generation**

Your agent builds and returns the SWML document:

*\#\# Inside AgentBase.\_render\_swml\(\)*

**def **\_render\_swml\(self, request\_body**=**None\):

*"""Generate SWML document for this agent.""" *

*\# 1. Build the prompt \(POM or text\)*

prompt **= **self.\_build\_prompt\(\)

*\# 2. Collect all SWAIG functions*

functions **= **self.\_tool\_registry.get\_functions\(\)

*\# 3. Generate webhook URLs with security tokens*

webhook\_url **= **self.\_build\_webhook\_url\("/swaig"\)

*\# 4. Assemble AI configuration*

ai\_config **= **\{

"prompt": prompt, 

"post\_prompt": self.\_post\_prompt, 

"post\_prompt\_url": self.\_build\_webhook\_url\("/post\_prompt"\), 

"SWAIG": \{

"defaults": \{"web\_hook\_url": webhook\_url\}, 

"functions": functions

\}, 

"hints": self.\_hints, 

"languages": self.\_languages, 

"params": self.\_params

\}

*\# 5. Build complete SWML document*

swml **= **\{

"version": "1.0.0", 

"sections": \{

"main": \[

\{"answer": \{\}\}, 

50

2. Core Concepts

\{"ai": ai\_config\}

\]

\}

\}

**return **swml

**2.15.4 Phase 3: AI Conversation**

Once SignalWire has the SWML, it executes the instructions:

┌─────────────────────────────────────────────────────────────────────────────┐

│

AI Conversation Loop

│

├─────────────────────────────────────────────────────────────────────────────┤

│

│

│

┌───────────────────────────────────────────────────┐

│

│

│

│

│

│

▼

│

│

│

┌─────────────┐

┌─────────────┐

┌─────────────┐

│

│

│

│

Listen

│───►│

Transcribe │───►│

Process

│

│

│

│

│

\(STT\)

│

│

Speech

│

│

Intent

│

│

│

│

└─────────────┘

└─────────────┘

└─────────────┘

│

│

│

│

│

│

│

▼

│

│

│

┌─────────────────┐

│

│

│

│

Need function? │

│

│

│

└─────────────────┘

│

│

│

│

│

│

│

│

Yes

No

│

│

│

│

│

│

│

│

▼

▼

│

│

│

┌─────────────┐ ┌─────────────┐ │

│

│

│ Call SWAIG

│ │

Generate

│ │

│

│

│

Function

│ │

Response

│ │

│

│

└─────────────┘ └─────────────┘ │

│

│

│

│

│

│

│

└─────┬─────┘

│

│

│

│

│

│

│

▼

│

│

│

┌─────────────┐

│

│

│

│

Speak

│──────────┘

│

│

│

\(TTS\)

│

│

│

└─────────────┘

│

│

│

└─────────────────────────────────────────────────────────────────────────────┘

**AI Parameters that control this loop:**

**Parameter**

**Default**

**Purpose**

end\_of\_speech\_timeout

500ms

Wait time after user stops

speaking

attention\_timeout

15000ms

Max silence before AI

prompts

inactivity\_timeout

30000ms

Max silence before ending

call

barge\_match\_string

-

Words that immediately

interrupt AI

51

2. Core Concepts

**2.15.5 Phase 4: Function Calls**

When the AI needs to call a function:

┌─────────────────────────────────────────────────────────────────────────────┐

│

SWAIG Function Call

│

├─────────────────────────────────────────────────────────────────────────────┤

│

│

│

SignalWire AI

Your Agent

│

│

│

│

│

│

│

POST /swaig

│

│

│

│

Authorization: Basic xxx

│

│

│

│

Content-Type: application/json

│

│

│

│

│

│

│

│

\{

│

│

│

│

"action": "swaig\_action", 

│

│

│

│

"function": "get\_balance", 

│

│

│

│

"argument": \{

│

│

│

│

"parsed": \[\{"account\_id": "12345"\}\]

│

│

│

│

\}, 

│

│

│

│

"call\_id": "...", 

│

│

│

│

"global\_data": \{...\}

│

│

│

│

\}

│

│

│

│──────────────────────────────────────────────────────►│

│

│

│

│

│

│

│

┌──────────┴───────────┐ │

│

│

│ 1. Validate auth

│ │

│

│

│ 2. Find handler

│ │

│

│

│ 3. Execute function

│ │

│

│

│ 4. Build response

│ │

│

│

└──────────┬───────────┘ │

│

│

│

│

│

│

200 OK

│

│

│

│

\{

│

│

│

│

"response": "Balance is $150.00", 

│

│

│

│

"action": \[...\]

│

│

│

│

\}

│

│

│

│◄──────────────────────────────────────────────────────│

│

│

│

│

│

│

│

AI speaks the response

│

│

│

│

and continues conversation

│

│

│

│

└─────────────────────────────────────────────────────────────────────────────┘

**2.15.6**

**Phase 5: Call End**

When the call ends, the post-prompt summary is sent:

52

2. Core Concepts

┌─────────────────────────────────────────────────────────────────────────────┐

│

Call Ending

│

├─────────────────────────────────────────────────────────────────────────────┤

│

│

│

Trigger Events:

│

│

├── User hangs up

│

│

├── Agent triggers transfer action

│

│

├── Agent triggers stop action

│

│

├── Inactivity timeout

│

│

└── Error condition

│

│

│

│

│

▼

│

│

┌─────────────────────────────────────────────────────────────────────┐

│

│

│

AI generates summary using post\_prompt instructions

│

│

│

│

│

│

│

│

Example post\_prompt:

│

│

│

│

"Summarize: caller's issue, resolution status, any follow-up" 

│

│

│

└─────────────────────────────────────────────────────────────────────┘

│

│

│

│

│

▼

│

│

POST /post\_prompt

│

│

\{

│

│

"post\_prompt\_data": \{

│

│

"raw": "Customer called about billing issue. Resolved by...", 

│

│

"parsed": \{...\}, 

│

│

"substituted": "..." 

│

│

\}, 

│

│

"call\_id": "...", 

│

│

"caller\_id\_num": "\+15551234567", 

│

│

"call\_duration": 180

│

│

\}

│

│

│

│

│

▼

│

│

Your agent receives summary for logging, CRM update, analytics

│

│

│

└─────────────────────────────────────────────────────────────────────────────┘

**2.15.7**

**Handling Post-Prompt**

Configure post-prompt handling in your agent:

from signalwire\_agents import AgentBase

**class **MyAgent\(AgentBase\):

**def \_\_init\_\_**\(self\):

super\(\). **\_\_init\_\_**\(name**=**"my-agent"\)

*\# Set the post-prompt instruction*

self.set\_post\_prompt\(

"Summarize this call including: " 

"1\) The caller's main question or issue " 

"2\) How it was resolved " 

"3\) Any follow-up actions needed" 

\)

*\# Or use structured post-prompt with JSON output*

self.set\_post\_prompt\_json\(\{

"issue": "string - the caller's main issue", 

"resolution": "string - how the issue was resolved", 

"follow\_up": "boolean - whether follow-up is needed", 

"sentiment": "string - caller sentiment \(positive/neutral/negative\)" 

\}\)

53

2. Core Concepts

**def **on\_post\_prompt\(self, data\):

*"""Handle the call summary.""" *

summary **= **data.get\("post\_prompt\_data", \{\}\)

call\_id **= **data.get\("call\_id"\)

*\# Log to your system*

self.log\_call\_summary\(call\_id, summary\)

*\# Update CRM*

self.update\_crm\(data\)

**2.15.8**

**Request/Response Headers**

**2.15.8.1 SWML Request \(GET or POST /\)**

GET / HTTP/1.1

Host: your-agent.com

Authorization: Basic c2lnbmFsd2lyZTpwYXNzd29yZA==

Accept: application/json

X-Forwarded-For: signalwire-ip

X-Forwarded-Proto: https

**2.15.8.2 SWML Response**

HTTP/1.1 200 OK

Content-Type: application/json

\{"version": "1.0.0", "sections": \{...\}\}

**2.15.8.3**

**SWAIG Request \(POST /swaig\)**

POST /swaig HTTP/1.1

Host: your-agent.com

Authorization: Basic c2lnbmFsd2lyZTpwYXNzd29yZA==

Content-Type: application/json

\{"action": "swaig\_action", "function": "...", ...\}

**2.15.8.4**

**SWAIG Response**

HTTP/1.1 200 OK

Content-Type: application/json

\{"response": "...", "action": \[...\]\}

**2.15.9**

**Debugging the Lifecycle**

**2.15.9.1**

**View SWML Output**

*\#\# See what your agent returns*

curl -u signalwire:password http://localhost:3000/ **| **jq '.' 

*\#\# Using swaig-test*

swaig-test my\_agent.py --dump-swml

54

2. Core Concepts

**2.15.9.2 Test Function Calls**

*\#\# Call a function directly*

swaig-test my\_agent.py --exec get\_balance --account\_id 12345

*\#\# With verbose output*

swaig-test my\_agent.py --exec get\_balance --account\_id 12345 --verbose **2.15.9.3 Monitor Live Traffic**

from signalwire\_agents import AgentBase

**class **DebugAgent\(AgentBase\):

**def \_\_init\_\_**\(self\):

super\(\). **\_\_init\_\_**\(name**=**"debug-agent"\)

**def **on\_swml\_request\(self, request\):

*"""Called when SWML is requested.""" *

print\(f"SWML requested from: **\{**request**. **client**. **host**\}**"\) print\(f"Headers: **\{**dict\(request.headers\)**\}**"\) **def **on\_swaig\_request\(self, function\_name, args, raw\_data\):

*"""Called before each SWAIG function.""" *

print\(f"Function called: **\{**function\_name**\}**"\) print\(f"Arguments: **\{**args**\}**"\)

print\(f"Call ID: **\{**raw\_data**. **get\('call\_id'\)**\}**"\) **2.15.10**

**Error Handling**

**2.15.10.1**

**SWML Errors**

If your agent can’t generate SWML:

**def **\_render\_swml\(self\):

**try**:

**return **self.\_build\_swml\(\)

**except ** *Exception * as e:

*\# Return minimal valid SWML*

**return **\{

"version": "1.0.0", 

"sections": \{

"main": \[

\{"answer": \{\}\}, 

\{"play": \{"url": "https://example.com/error.mp3"\}\}, 

\{"hangup": \{\}\}

\]

\}

\}

**2.15.10.2**

**SWAIG Errors**

If a function fails:

**def **get\_balance\(self, args, raw\_data\):

**try**:

balance **= **self.lookup\_balance\(args.get\("account\_id"\)\) **return **SwaigFunctionResult\(f"Your balance is $**\{**balance**\}**"\) **except **DatabaseError:

**return **SwaigFunctionResult\(

"I'm having trouble accessing account information right now. " 

"Please try again in a moment." 

\)

**except ** *Exception * as e:

*\# Log the error but return user-friendly message*

self.logger.error\(f"Function error: **\{**e**\}**"\)

55

2. Core Concepts

**return **SwaigFunctionResult\(

"I encountered an unexpected error. " 

"Let me transfer you to a representative." 

\)

**2.15.11 Next Steps**

Now that you understand the complete lifecycle, let’s look at how security works throughout this flow. 

56

2. Core Concepts

**2.16 Security**

**Summary**: The SDK provides layered security through HTTP Basic Authentication for all requests and optional per-function token validation for sensitive operations. 

**2.16.1 Security Layers**

The SignalWire Agents SDK implements multiple security layers:

**2.16.1.1**

**Layer 1: Transport Security \(HTTPS\)**

• TLS encryption in transit

• Certificate validation

**2.16.1.2 Layer 2: HTTP Basic Authentication**

• Username/password validation

• Applied to all webhook endpoints

**2.16.1.3 Layer 3: Function Token Security \(Optional\)**

• Per-function security tokens

• Cryptographic validation

**2.16.2**

**HTTP Basic Authentication**

Every request to your agent is protected by HTTP Basic Auth. 

**2.16.2.1**

**How It Works**

1. **SignalWire sends request **with Authorization: Basic <base64-encoded-credentials> header 2. **Agent extracts header **and Base64 decodes credentials

3. **Agent splits **the decoded string into username and password 4. **Agent compares **credentials against configured values

5. **Result**: Match returns 200 \+ response; No match returns 401 Denied **2.16.2.2**

**Configuring Credentials**

**Option 1: Environment Variables \(Recommended for production\)**

*\#\# Set explicit credentials*

export SWML\_BASIC\_AUTH\_USER**=**my\_secure\_username

export SWML\_BASIC\_AUTH\_PASSWORD**=**my\_very\_secure\_password\_here **Option 2: Let SDK Generate Credentials \(Development\)**

If you don’t set credentials, the SDK: - Uses username: signalwire - Generates a random password on each startup

- Prints the password to the console

$ python my\_agent.py

INFO: Agent 'my-agent' starting... 

INFO: Basic Auth credentials:

INFO:

Username: signalwire

INFO:

Password: a7b3x9k2m5n1p8q4

*\# Use this in SignalWire webhook config*

57

2. Core Concepts

**2.16.2.3 Credentials in Your Agent**

from signalwire\_agents import AgentBase

import os

**class **MyAgent\(AgentBase\):

**def \_\_init\_\_**\(self\):

super\(\). **\_\_init\_\_**\(

name**=**"my-agent", 

*\# Credentials from environment or defaults*

basic\_auth\_user**=**os.getenv\("SWML\_BASIC\_AUTH\_USER"\), basic\_auth\_password**=**os.getenv\("SWML\_BASIC\_AUTH\_PASSWORD"\)

\)

**2.16.3**

**Function Token Security**

For sensitive operations, enable per-function token validation. 

**2.16.3.1 How Function Tokens Work**

**SWML Generation \(GET /\)**

1. Agent generates SWML

2. For each secure function, generate unique token

3. Token embedded in function’s web\_hook\_url

"functions" **: **\[**\{**

"function" **: **"transfer\_funds" **, **

"web\_hook\_url" **: **"https://agent.com/swaig?token=abc123xyz..." 

**\}**\]

**Function Call \(POST /swaig\)**

1. SignalWire calls webhook URL with token

2. Agent extracts token from request

3. Agent validates token cryptographically

4. If valid, execute function

5. If invalid, reject with 403

**2.16.3.2**

**Enabling Token Security**

from signalwire\_agents import AgentBase, SwaigFunctionResult

**class **SecureAgent\(AgentBase\):

**def \_\_init\_\_**\(self\):

super\(\). **\_\_init\_\_**\(name**=**"secure-agent"\)

*\# Regular function - Basic Auth only*

self.define\_tool\(

name**=**"get\_balance", 

description**=**"Get account balance", 

parameters**=**\{...\}, 

handler**=**self.get\_balance

\)

*\# Secure function - Basic Auth \+ Token validation*

self.define\_tool\(

name**=**"transfer\_funds", 

description**=**"Transfer funds between accounts", 

parameters**=**\{...\}, 

handler**=**self.transfer\_funds, 

secure**=**True

*\# Enable token security*

\)

58

2. Core Concepts

**def **get\_balance\(self, args, raw\_data\):

**return **SwaigFunctionResult\("Balance is $150.00"\)

**def **transfer\_funds\(self, args, raw\_data\):

*\# This only executes if token is valid*

**return **SwaigFunctionResult\("Transfer complete"\)

**2.16.3.3 Token Generation**

Tokens are generated using cryptographic hashing:

*\#\# Simplified view of token generation*

import hashlib

import secrets

**def **generate\_function\_token\(function\_name, secret\_key, call\_context\):

*"""Generate a secure token for a function.""" *

*\# Combine function name, secret, and context*

token\_input **= **f" **\{**function\_name**\}**:**\{**secret\_key**\}**:**\{**call\_context**\}**" 

*\# Generate cryptographic hash*

token **= **hashlib.sha256\(token\_input.encode\(\)\).hexdigest\(\)

**return **token

**2.16.4**

**HTTPS Configuration**

For production, enable HTTPS:

**2.16.4.1**

**Using SSL Certificates**

*\#\# Environment variables for SSL*

export SWML\_SSL\_ENABLED**=**true

export SWML\_SSL\_CERT\_PATH**=**/path/to/cert.pem

export SWML\_SSL\_KEY\_PATH**=**/path/to/key.pem

export SWML\_DOMAIN**=**my-agent.example.com

from signalwire\_agents import AgentBase

**class **SecureAgent\(AgentBase\):

**def \_\_init\_\_**\(self\):

super\(\). **\_\_init\_\_**\(

name**=**"secure-agent", 

ssl\_enabled**=**True, 

ssl\_cert\_path**=**"/path/to/cert.pem", 

ssl\_key\_path**=**"/path/to/key.pem" 

\)

**2.16.4.2**

**Using a Reverse Proxy \(Recommended\)**

Most production deployments use a reverse proxy for SSL:

**Traffic Flow**: SignalWire → HTTPS → nginx/Caddy \(SSL termination\) → HTTP → Your Agent \(localhost:3000\) **Benefits**: - SSL handled by proxy - Easy certificate management - Load balancing - Additional security headers Set the proxy URL so your agent generates correct webhook URLs:

export SWML\_PROXY\_URL\_BASE**=**https://my-agent.example.com

59

2. Core Concepts

**2.16.5 Security Best Practices**

**2.16.5.1 1. Never Commit Credentials**

\#\# .gitignore

.env

.env.local

\*.pem

\*.key

**2.16.5.2 2. Use Strong Passwords**

*\#\# Generate a strong password*

python -c "import secrets; print\(secrets.token\_urlsafe\(32\)\)" 

**2.16.5.3 3. Validate All Inputs**

**def **transfer\_funds\(self, args, raw\_data\):

amount **= **args.get\("amount"\)

to\_account **= **args.get\("to\_account"\)

*\# Validate inputs*

**if not **amount **or not **isinstance\(amount, \(int, float\)\): **return **SwaigFunctionResult\("Invalid amount specified"\) **if **amount **<= **0:

**return **SwaigFunctionResult\("Amount must be positive"\) **if **amount **> **10000:

**return **SwaigFunctionResult\(

"Transfers over $10,000 require additional verification" 

\)

**if not **to\_account **or **len\(to\_account\) **\!= **10:

**return **SwaigFunctionResult\("Invalid account number"\)

*\# Proceed with transfer*

**return **SwaigFunctionResult\(f"Transferred $**\{**amount**\} **to account **\{**to\_account**\}**"\) **2.16.5.4**

**4. Use Secure Functions for Sensitive Operations**

*\#\# Mark sensitive functions as secure*

self.define\_tool\(

name**=**"delete\_account", 

description**=**"Delete a customer account", 

parameters**=**\{...\}, 

handler**=**self.delete\_account, 

secure**=**True

*\# Always use token security for destructive operations*

\)

self.define\_tool\(

name**=**"change\_password", 

description**=**"Change account password", 

parameters**=**\{...\}, 

handler**=**self.change\_password, 

secure**=**True

\)

self.define\_tool\(

name**=**"transfer\_funds", 

description**=**"Transfer money", 

parameters**=**\{...\}, 

handler**=**self.transfer\_funds, 

secure**=**True

\)

60

2. Core Concepts

**2.16.5.5 5. Log Security Events**

import logging

**class **SecureAgent\(AgentBase\):

**def \_\_init\_\_**\(self\):

super\(\). **\_\_init\_\_**\(name**=**"secure-agent"\)

self.logger **= **logging.getLogger\(\_\_name\_\_\)

**def **transfer\_funds\(self, args, raw\_data\):

call\_id **= **raw\_data.get\("call\_id"\)

caller **= **raw\_data.get\("caller\_id\_num"\)

amount **= **args.get\("amount"\)

to\_account **= **args.get\("to\_account"\)

*\# Log the sensitive operation*

self.logger.info\(

f"Transfer initiated: call\_id=**\{**call\_id**\}**, " 

f"caller=**\{**caller**\}**, amount=**\{**amount**\}**, to=**\{**to\_account**\}**" 

\)

*\# Process transfer*

result **= **self.process\_transfer\(amount, to\_account\)

self.logger.info\(

f"Transfer completed: call\_id=**\{**call\_id**\}**, result=**\{**result**\}**" 

\)

**return **SwaigFunctionResult\(f"Transfer of $**\{**amount**\} **complete"\) **2.16.5.6**

**6. Implement Rate Limiting**

from collections import defaultdict

from time import time

**class **RateLimitedAgent\(AgentBase\):

**def \_\_init\_\_**\(self\):

super\(\). **\_\_init\_\_**\(name**=**"rate-limited-agent"\) self.call\_counts **= **defaultdict\(list\)

self.rate\_limit **= **10

*\# calls per minute*

**def **check\_rate\_limit\(self, caller\_id\):

*"""Check if caller has exceeded rate limit.""" *

now **= **time\(\)

minute\_ago **= **now **- **60

*\# Clean old entries*

self.call\_counts\[caller\_id\] **= **\[

t **for **t **in **self.call\_counts\[caller\_id\] **if **t **> **minute\_ago

\]

*\# Check limit*

**if **len\(self.call\_counts\[caller\_id\]\) **>= **self.rate\_limit: **return **False

*\# Record this call*

self.call\_counts\[caller\_id\].append\(now\)

**return **True

**def **get\_balance\(self, args, raw\_data\):

caller **= **raw\_data.get\("caller\_id\_num"\)

**if not **self.check\_rate\_limit\(caller\):

**return **SwaigFunctionResult\(

"You've made too many requests. Please wait a moment." 

\)

61

2. Core Concepts

*\# Process normally*

**return **SwaigFunctionResult\("Your balance is $150.00"\) **2.16.6 Configuring SignalWire Webhooks**

When setting up your phone number in SignalWire:

**Setting**

**Value**

Handle Calls Using

SWML Script

SWML Script URL

https://my-agent.example.com/

Request Method

POST

Authentication

HTTP Basic Auth

Username

Your configured username

Password

Your configured password

**2.16.7**

**Summary**

**Security Feature**

**When to Use**

**How to Enable**

**Basic Auth**

Always

Automatic \(set env vars for

custom\)

**Function Tokens**

Sensitive operations

secure=True on define\_tool

**HTTPS**

Production

SSL certs or reverse proxy

**Input Validation**

All functions

Manual validation in

handlers

**Rate Limiting**

Public-facing agents

Manual implementation

**Logging**

All security events

Python logging module

**2.16.8**

**Next Steps**

You now understand the core concepts of the SignalWire Agents SDK. Let’s move on to building agents. 

62

**Chapter 3**

**Building Agents**

**Summary**: Learn how to build voice AI agents using AgentBase, from basic configuration to advanced prompt engineering and voice customization. 

**3.1 What You’ll Learn**

This chapter covers everything you need to build production-quality agents: 1. **AgentBase **- The foundation class and its capabilities

2. **Static vs Dynamic **- Choosing the right pattern for your use case 3. **Prompts & POM **- Crafting effective prompts with the Prompt Object Model 4. **Voice & Language **- Configuring voices and multi-language support 5. **AI Parameters **- Tuning conversation behavior

6. **Hints **- Improving speech recognition accuracy

**3.2**

**Prerequisites**

Before building agents, you should understand:

• Core concepts from Chapter 2 \(SWML, SWAIG, Lifecycle\)

• Basic Python class structure

• How SignalWire processes calls

63

3. Building Agents

**3.3 Agent Architecture Overview**

┌─────────────────────────────────────────────────────────────────────────────┐

│

Agent Components

│

├─────────────────────────────────────────────────────────────────────────────┤

│

│

│

┌───────────────────────────────────────────────────────────────────┐

│

│

│

Your Agent Class

│

│

│

│

\(extends AgentBase\)

│

│

│

└───────────────────────────────────────────────────────────────────┘

│

│

│

│

│

▼

│

│

┌───────────────────────────────────────────────────────────────────┐

│

│

│

Configuration

│

│

│

├───────────────────────────────────────────────────────────────────┤

│

│

│

│

│

│

│

┌─────────────┐

┌─────────────┐

┌─────────────┐

│

│

│

│

│

Prompts

│

│

Voice

│

│

AI Params

│

│

│

│

│

├─────────────┤

├─────────────┤

├─────────────┤

│

│

│

│

│ • Role

│

│ • Language

│

│ • Timeouts

│

│

│

│

│

│ • Guidelines│

│ • Voice

│

│ • Barge

│

│

│

│

│

│ • Rules

│

│ • TTS Engine│

│ • Attention │

│

│

│

│

└─────────────┘

└─────────────┘

└─────────────┘

│

│

│

│

│

│

│

│

┌─────────────┐

┌─────────────┐

┌───────────────┐

│

│

│

│

│

Hints

│

│

Functions

│

│

Skills

│

│

│

│

│

├─────────────┤

├─────────────┤

├───────────────┤

│

│

│

│

│ • Keywords

│

│ • Tools

│

│ • Plugins

│

│

│

│

│

│ • Names

│

│ • DataMap

│

│ • Add-ons

│

│

│

│

│

│ • Terms

│

│ • Handlers

│

│ • Integrations│

│

│

│

│

└─────────────┘

└─────────────┘

└───────────────┘

│

│

│

└───────────────────────────────────────────────────────────────────┘

│

│

│

│

│

▼

│

│

┌───────────────────────────────────────────────────────────────────┐

│

│

│

SWML Output

│

│

│

│

\(Generated automatically\)

│

│

│

└───────────────────────────────────────────────────────────────────┘

│

│

│

└─────────────────────────────────────────────────────────────────────────────┘

**3.4**

**A Complete Agent Example**

Here’s what a production agent looks like:

from signalwire\_agents import AgentBase, SwaigFunctionResult

**class **CustomerSupportAgent\(AgentBase\):

*"""Production customer support agent.""" *

**def \_\_init\_\_**\(self\):

super\(\). **\_\_init\_\_**\(

name**=**"customer-support", 

route**=**"/support" 

\)

*\# Voice configuration*

self.add\_language\("English", "en-US", "rime.spore"\)

*\# AI behavior*

self.set\_params\(\{

64

3. Building Agents

"end\_of\_speech\_timeout": 500, 

"attention\_timeout": 15000, 

"inactivity\_timeout": 30000

\}\)

*\# Prompts*

self.prompt\_add\_section\(

"Role", 

"You are Alex, a friendly customer support agent for Acme Inc." 

\)

self.prompt\_add\_section\(

"Guidelines", 

body**=**"Follow these guidelines:", 

bullets**=**\[

"Be helpful and professional", 

"Ask clarifying questions when needed", 

"Keep responses concise for voice", 

"Offer to transfer if you cannot help" 

\]

\)

*\# Speech recognition hints*

self.add\_hints\(\[

"Acme", "account number", "order status", 

"refund", "billing", "representative" 

\]\)

*\# Functions*

self.define\_tool\(

name**=**"check\_order", 

description**=**"Look up an order by order number", 

parameters**=**\{

"type": "object", 

"properties": \{

"order\_number": \{

"type": "string", 

"description": "The order number to look up" 

\}

\}, 

"required": \["order\_number"\]

\}, 

handler**=**self.check\_order

\)

*\# Skills*

self.add\_skill\("datetime"\)

*\# Post-call summary*

self.set\_post\_prompt\(

"Summarize: issue type, resolution, customer satisfaction" 

\)

**def **check\_order\(self, args, raw\_data\):

order\_number **= **args.get\("order\_number"\)

*\# Your business logic here*

**return **SwaigFunctionResult\(

f"Order **\{**order\_number**\}**: Shipped on Monday, arriving Thursday" 

\)

**if **\_\_name\_\_ **== **"\_\_main\_\_":

agent **= **CustomerSupportAgent\(\)

agent.run\(host**=**"0.0.0.0", port**=**3000\)

65

3. Building Agents

**3.5 Chapter Contents**

**Section**

**Description**

AgentBase

Core class and constructor options

Static vs Dynamic

Choosing the right pattern

Prompts & POM

Prompt engineering for voice AI

Voice & Language

Voice selection and multi-language

AI Parameters

Behavior tuning

Hints

Speech recognition improvement

**3.6 Key Patterns**

**3.6.1**

**Pattern 1: Class-Based Agent**

Best for complex agents with multiple functions:

**class **MyAgent\(AgentBase\):

**def \_\_init\_\_**\(self\):

super\(\). **\_\_init\_\_**\(name**=**"my-agent"\)

self.configure\(\)

**def **configure\(self\):

*\# All configuration here*

**pass**

**3.6.2**

**Pattern 2: Functional Agent**

Quick agents for simple use cases:

from signalwire\_agents import AgentBase

agent **= **AgentBase\(name**=**"simple-agent"\)

agent.add\_language\("English", "en-US", "rime.spore"\) agent.prompt\_add\_section\("Role", "You are a helpful assistant."\) agent.run\(\)

**3.6.3**

**Pattern 3: Multi-Agent Server**

Multiple agents on one server:

from signalwire\_agents import AgentServer

server **= **AgentServer\(\)

server.register\(SupportAgent\(\), "/support"\)

server.register\(SalesAgent\(\), "/sales"\)

server.register\(BillingAgent\(\), "/billing"\)

server.run\(port**=**3000\)

66

3. Building Agents

**3.7 Testing Your Agent**

Always test before deploying:

*\# View SWML output*

swaig-test my\_agent.py --dump-swml

*\# List registered functions*

swaig-test my\_agent.py --list-tools

*\# Test a function*

swaig-test my\_agent.py --exec check\_order --order\_number 12345

Let’s start with understanding AgentBase in depth. 

**3.8 Class Overview**

┌─────────────────────────────────────────────────────────────────────────────┐

│

AgentBase Inheritance

│

├─────────────────────────────────────────────────────────────────────────────┤

│

│

│

AgentBase

│

│

│

│

│

┌─────────────────┼────────────────┐

│

│

│

│

│

│

│

▼

▼

▼

│

│

┌──────────┐

┌──────────┐

┌───────────┐

│

│

│ AuthMixin│

│ WebMixin │

│SWMLService│

│

│

└──────────┘

└──────────┘

└───────────┘

│

│

│

│

┌───────────┐

┌──────────┐

┌──────────┐

│

│

│PromptMixin│

│ ToolMixin│

│SkillMixin│

│

│

└───────────┘

└──────────┘

└──────────┘

│

│

│

│

┌─────────────┐

┌───────────────┐

│

│

│AIConfigMixin│

│ServerlessMixin│

│

│

└─────────────┘

└───────────────┘

│

│

│

│

┌──────────┐

│

│

│StateMixin│

│

│

└──────────┘

│

│

│

└─────────────────────────────────────────────────────────────────────────────┘

**3.9**

**Constructor Parameters**

from signalwire\_agents import AgentBase

agent **= **AgentBase\(

*\# Required*

name**=**"my-agent", 

*\# Unique agent identifier*

*\# Server Configuration*

route**=**"/", 

*\# HTTP route path \(default: "/"\)*

host**=**"0.0.0.0", 

*\# Bind address \(default: "0.0.0.0"\)*

port**=**3000, 

*\# Server port \(default: 3000\)*

*\# Authentication*

basic\_auth**=**\("user", "pass"\), 

*\# Override env var credentials*

*\# Behavior*

auto\_answer**=**True, 

*\# Answer calls automatically*

67

3. Building Agents

use\_pom**=**True, 

*\# Use Prompt Object Model*

*\# Recording*

record\_call**=**False, 

*\# Enable call recording*

record\_format**=**"mp4", 

*\# Recording format*

record\_stereo**=**True, 

*\# Stereo recording*

*\# Tokens and Security*

token\_expiry\_secs**=**3600, 

*\# Function token expiration*

*\# Advanced*

default\_webhook\_url**=**None, 

*\# Override webhook URL*

agent\_id**=**None, 

*\# Custom agent ID \(auto-generated\)*

native\_functions**=**None, 

*\# Built-in SignalWire functions*

schema\_path**=**None, 

*\# Custom SWML schema path*

suppress\_logs**=**False, 

*\# Disable logging*

config\_file**=**None

*\# Load from config file*

\)

**3.10 Parameter Reference**

**Parameter**

**Type**

**Default**

**Description**

name

str

Required

Unique identifier for the

agent

route

str

“/” 

HTTP route where agent is

accessible

host

str

“0.0.0.0” 

IP address to bind server

port

int

3000

Port number for server

basic\_auth

tuple

None

\(username, password\) for

auth

use\_pom

bool

True

Enable Prompt Object

Model

auto\_answer

bool

True

Auto-answer incoming calls

record\_call

bool

False

Enable call recording

record\_format

str

“mp4” 

Recording file format

record\_stereo

bool

True

Record in stereo

token\_expiry\_secs

int

3600

Token validity period

native\_functions

list

None

SignalWire native functions

suppress\_logs

bool

False

Disable agent logs

**3.11**

**Creating an Agent**

**3.11.1**

**Method 1: Class-Based \(Recommended\)**

from signalwire\_agents import AgentBase, SwaigFunctionResult

**class **MyAgent\(AgentBase\):

**def \_\_init\_\_**\(self\):

super\(\). **\_\_init\_\_**\(name**=**"my-agent"\)

self.\_setup\(\)

**def **\_setup\(self\):

*\# Voice*

self.add\_language\("English", "en-US", "rime.spore"\)

*\# Prompts*

68

3. Building Agents

self.prompt\_add\_section\("Role", "You are a helpful assistant."\)

*\# Functions*

self.define\_tool\(

name**=**"greet", 

description**=**"Greet the user", 

parameters**=**\{\}, 

handler**=**self.greet

\)

**def **greet\(self, args, raw\_data\):

**return **SwaigFunctionResult\("Hello\! How can I help you today?"\) **if **\_\_name\_\_ **== **"\_\_main\_\_":

agent **= **MyAgent\(\)

agent.run\(\)

**3.11.2**

**Method 2: Instance-Based**

from signalwire\_agents import AgentBase

agent **= **AgentBase\(name**=**"quick-agent"\)

agent.add\_language\("English", "en-US", "rime.spore"\) agent.prompt\_add\_section\("Role", "You are a helpful assistant."\) agent.run\(\)

**3.11.3**

**Method 3: Declarative \(PROMPT\_SECTIONS\)**

from signalwire\_agents import AgentBase

**class **DeclarativeAgent\(AgentBase\):

PROMPT\_SECTIONS **= **\{

"Role": "You are a helpful customer service agent.", 

"Guidelines": \[

"Be professional and courteous", 

"Ask clarifying questions when needed", 

"Keep responses concise" 

\], 

"Rules": \{

"body": "Always follow these rules:", 

"bullets": \[

"Never share customer data", 

"Escalate complex issues" 

\]

\}

\}

**def \_\_init\_\_**\(self\):

super\(\). **\_\_init\_\_**\(name**=**"declarative-agent"\) self.add\_language\("English", "en-US", "rime.spore"\) **3.12**

**Key Methods**

**3.12.1**

**Configuration Methods**

*\# Voice and Language*

agent.add\_language\(name, code, voice\)

*\# Add language support*

agent.set\_languages\(languages\)

*\# Set all languages at once*

*\# Prompts*

agent.prompt\_add\_section\(title, body\)

*\# Add prompt section*

agent.prompt\_add\_subsection\(parent, title\)

*\# Add subsection*

69

3. Building Agents

agent.set\_post\_prompt\(text\)

*\# Set post-call summary prompt*

*\# AI Parameters*

agent.set\_params\(params\_dict\)

*\# Set AI behavior parameters*

agent.set\_param\_value\(key, value\)

*\# Set single parameter*

*\# Speech Recognition*

agent.add\_hints\(hints\_list\)

*\# Add speech hints*

agent.add\_hint\(hint\_string\)

*\# Add single hint*

*\# Functions*

agent.define\_tool\(name, description, ...\)

*\# Define SWAIG function*

agent.add\_skill\(skill\_name\)

*\# Add a skill*

*\# Pronunciation*

agent.add\_pronunciation\(replace, with\_text\)

*\# Add pronunciation rule*

**3.12.2**

**Runtime Methods**

*\# Start server*

agent.run\(host**=**"0.0.0.0", port**=**3000\)

*\# Get SWML document*

swml **= **agent.get\_swml\(\)

*\# Access components*

agent.pom

*\# Prompt Object Model*

agent.data\_map

*\# DataMap builder*

**3.13**

**Agent Lifecycle**

┌─────────────────────────────────────────────────────────────────────────────┐

│

Agent Lifecycle

│

├─────────────────────────────────────────────────────────────────────────────┤

│

│

│

1. Instantiation

│

│

└── \_\_init\_\_\(\) called

│

│

├── Mixins initialized

│

│

├── Config loaded

│

│

└── Routes registered

│

│

│

│

2. Configuration

│

│

└── Setup methods called

│

│

├── add\_language\(\)

│

│

├── prompt\_add\_section\(\)

│

│

├── define\_tool\(\)

│

│

└── add\_skill\(\)

│

│

│

│

3. Server Start

│

│

└── run\(\) called

│

│

├── FastAPI app created

│

│

├── Routes mounted

│

│

└── Uvicorn started

│

│

│

│

4. Request Handling

│

│

├── GET /

──► Return SWML document

│

│

├── POST / ──► Return SWML document

│

│

└── POST /swaig ──► Execute SWAIG function

│

│

│

└─────────────────────────────────────────────────────────────────────────────┘

70

3. Building Agents

**3.14 Configuration File**

Load configuration from a YAML/JSON file:

agent **= **AgentBase\(

name**=**"my-agent", 

config\_file**=**"config/agent.yaml" 

\)

*\# config/agent.yaml*

**name: **my-agent

**route: **/support

**host: **0.0.0.0

**port: **3000

**3.15 Environment Variables**

AgentBase respects these environment variables:

**Variable**

**Purpose**

SWML\_BASIC\_AUTH\_USER

Basic auth username

SWML\_BASIC\_AUTH\_PASSWORD

Basic auth password

SWML\_PROXY\_URL\_BASE

Base URL for webhooks behind proxy

SWML\_SSL\_ENABLED

Enable SSL

SWML\_SSL\_CERT\_PATH

SSL certificate path

SWML\_SSL\_KEY\_PATH

SSL key path

SWML\_DOMAIN

Domain for SSL

**3.16**

**Multi-Agent Server**

Run multiple agents on one server:

from signalwire\_agents import AgentServer

**class **SupportAgent\(AgentBase\):

**def \_\_init\_\_**\(self\):

super\(\). **\_\_init\_\_**\(name**=**"support", route**=**"/support"\)

*\# ... configuration*

**class **SalesAgent\(AgentBase\):

**def \_\_init\_\_**\(self\):

super\(\). **\_\_init\_\_**\(name**=**"sales", route**=**"/sales"\)

*\# ... configuration*

*\# Register multiple agents*

server **= **AgentServer\(\)

server.register\(SupportAgent\(\)\)

server.register\(SalesAgent\(\)\)

server.run\(host**=**"0.0.0.0", port**=**3000\)

Access agents at: - http://localhost:3000/support - http://localhost:3000/sales 71

3. Building Agents

**3.17**

**Best Practices**

1. **Use class-based agents **for anything beyond simple prototypes 2. **Organize configuration **into logical private methods

3. **Set explicit credentials **in production via environment variables 4. **Use meaningful agent names **for logging and debugging

5. **Test with swaig-test **before deploying

**class **WellOrganizedAgent\(AgentBase\):

**def \_\_init\_\_**\(self\):

super\(\). **\_\_init\_\_**\(name**=**"organized-agent"\)

self.\_configure\_voice\(\)

self.\_configure\_prompts\(\)

self.\_configure\_functions\(\)

self.\_configure\_skills\(\)

**def **\_configure\_voice\(self\):

self.add\_language\("English", "en-US", "rime.spore"\) self.set\_params\(\{

"end\_of\_speech\_timeout": 500, 

"attention\_timeout": 15000

\}\)

**def **\_configure\_prompts\(self\):

self.prompt\_add\_section\("Role", "You are a helpful assistant."\) **def **\_configure\_functions\(self\):

self.define\_tool\(

name**=**"help", 

description**=**"Get help", 

parameters**=**\{\}, 

handler**=**self.get\_help

\)

**def **\_configure\_skills\(self\):

self.add\_skill\("datetime"\)

**def **get\_help\(self, args, raw\_data\):

**return **SwaigFunctionResult\("I can help you with..."\) 72

3. Building Agents

**3.18 Static vs Dynamic Agents**

**Summary**: Choose between static agents \(fixed configuration\) and dynamic agents \(runtime customization\) based on whether you need per-call personalization. 

**3.18.1 Understanding the Difference**

**Aspect**

**Static Agent**

**Dynamic Agent**

**Configuration**

Set once at startup

Per-request based on call

data

**Behavior**

Same for all callers

Different for different callers

**Use Static When: **- Same prompt for everyone - Generic assistant - Simple IVR - FAQ bot **Use Dynamic When: **- Personalized greetings - Caller-specific data - Account-based routing - Multi-tenant applications

**3.18.2**

**Static Agents**

Static agents have fixed configuration determined at instantiation time. 

**3.18.2.1 Example: Static Customer Service Agent**

from signalwire\_agents import AgentBase, SwaigFunctionResult

**class **StaticSupportAgent\(AgentBase\):

*"""Same behavior for all callers.""" *

**def \_\_init\_\_**\(self\):

super\(\). **\_\_init\_\_**\(name**=**"static-support"\)

self.add\_language\("English", "en-US", "rime.spore"\) self.prompt\_add\_section\(

"Role", 

"You are a customer service agent for Acme Corp. " 

"Help callers with general inquiries about our products." 

\)

self.prompt\_add\_section\(

"Guidelines", 

bullets**=**\[

"Be helpful and professional", 

"Answer questions about products", 

"Transfer complex issues to support" 

\]

\)

self.define\_tool\(

name**=**"get\_store\_hours", 

description**=**"Get store hours", 

parameters**=**\{\}, 

handler**=**self.get\_store\_hours

\)

**def **get\_store\_hours\(self, args, raw\_data\):

**return **SwaigFunctionResult\(

"We're open Monday through Friday, 9 AM to 5 PM." 

\)

**if **\_\_name\_\_ **== **"\_\_main\_\_":

73

3. Building Agents

agent **= **StaticSupportAgent\(\)

agent.run\(\)

**3.18.3 Dynamic Agents**

Dynamic agents customize their behavior based on the incoming request using the on\_swml\_request method. 

**3.18.3.1 The on\_swml\_request Method**

**def **on\_swml\_request\(self, request\_data: dict\) **-> **None:

*""" *

*Called before SWML is generated for each request. *

*Args:*

*request\_data: Contains call information:*

*- call\_id: Unique call identifier*

*- caller\_id\_num: Caller's phone number*

*- caller\_id\_name: Caller's name \(if available\)*

*- called\_id\_num: Number that was called*

*- direction: "inbound" or "outbound" *

*- And more... *

*""" *

**pass**

**3.18.3.2 Example: Dynamic Personalized Agent**

from signalwire\_agents import AgentBase, SwaigFunctionResult

**class **DynamicPersonalizedAgent\(AgentBase\):

*"""Customizes greeting based on caller.""" *

*\# Simulated customer database*

CUSTOMERS **= **\{

"\+15551234567": \{"name": "John Smith", "tier": "gold", "account": "A001"\}, 

"\+15559876543": \{"name": "Jane Doe", "tier": "platinum", "account": "A002"\}, 

\}

**def \_\_init\_\_**\(self\):

super\(\). **\_\_init\_\_**\(name**=**"dynamic-agent"\)

self.add\_language\("English", "en-US", "rime.spore"\)

*\# Base configuration*

self.set\_params\(\{

"end\_of\_speech\_timeout": 500, 

"attention\_timeout": 15000

\}\)

*\# Functions available to all callers*

self.define\_tool\(

name**=**"get\_account\_status", 

description**=**"Get the caller's account status", 

parameters**=**\{\}, 

handler**=**self.get\_account\_status

\)

*\# Store caller info for function access*

self.\_current\_caller **= **None

**def **on\_swml\_request\(self, request\_data: dict\) **-> **None:

*"""Customize behavior based on caller.""" *

caller\_num **= **request\_data.get\("caller\_id\_num", ""\)

*\# Look up caller in database*

customer **= **self.CUSTOMERS.get\(caller\_num\)

74

3. Building Agents

**if **customer:

*\# Known customer - personalized experience*

self.\_current\_caller **= **customer

self.prompt\_add\_section\(

"Role", 

f"You are a premium support agent for Acme Corp. " 

f"You are speaking with **\{**customer\['name'\]**\}**, a **\{**customer\['tier'\]**\} **member." 

\)

self.prompt\_add\_section\(

"Context", 

f"Customer account: **\{**customer\['account'\]**\}**\\n" 

f"Membership tier: **\{**customer\['tier'\]**. **upper\(\)**\}**" 

\)

**if **customer\["tier"\] **== **"platinum": self.prompt\_add\_section\(

"Special Treatment", 

"This is a platinum customer. Prioritize their requests and " 

"offer expedited service on all issues." 

\)

**else**:

*\# Unknown caller - generic experience*

self.\_current\_caller **= **None

self.prompt\_add\_section\(

"Role", 

"You are a customer service agent for Acme Corp. " 

"Help the caller with their inquiry and offer to create an account." 

\)

**def **get\_account\_status\(self, args, raw\_data\):

**if **self.\_current\_caller:

**return **SwaigFunctionResult\(

f"Account **\{**self**. **\_current\_caller\['account'\]**\} **is active. " 

f"Tier: **\{**self**. **\_current\_caller\['tier'\]**. **upper\(\)**\}**" 

\)

**return **SwaigFunctionResult\(

"No account found. Would you like to create one?" 

\)

**if **\_\_name\_\_ **== **"\_\_main\_\_":

agent **= **DynamicPersonalizedAgent\(\)

agent.run\(\)

**3.18.4**

**Request Data Fields**

The request\_data dictionary contains call information:

**Field**

**Description**

**Example**

call\_id

Unique call identifier

"a1b2c3d4-..." 

caller\_id\_num

Caller’s phone number

"\+15551234567" 

caller\_id\_name

Caller’s name

"John Smith" 

called\_id\_num

Number that was called

"\+15559876543" 

direction

Call direction

"inbound" 

75

3. Building Agents

**3.18.5 Dynamic Function Registration**

You can also register functions dynamically based on the caller:

**class **DynamicFunctionsAgent\(AgentBase\):

*"""Different functions for different callers.""" *

ADMIN\_NUMBERS **= **\["\+15551111111", "\+15552222222"\]

**def \_\_init\_\_**\(self\):

super\(\). **\_\_init\_\_**\(name**=**"dynamic-functions"\) self.add\_language\("English", "en-US", "rime.spore"\)

*\# Base functions for everyone*

self.define\_tool\(

name**=**"get\_info", 

description**=**"Get general information", 

parameters**=**\{\}, 

handler**=**self.get\_info

\)

**def **on\_swml\_request\(self, request\_data: dict\) **-> **None: caller\_num **= **request\_data.get\("caller\_id\_num", ""\) self.prompt\_add\_section\("Role", "You are a helpful assistant."\)

*\# Add admin functions only for admin callers*

**if **caller\_num **in **self.ADMIN\_NUMBERS:

self.prompt\_add\_section\(

"Admin Access", 

"This caller has administrator privileges. " 

"They can access system administration functions." 

\)

self.define\_tool\(

name**=**"admin\_reset", 

description**=**"Reset system configuration \(admin only\)", parameters**=**\{\}, 

handler**=**self.admin\_reset

\)

self.define\_tool\(

name**=**"admin\_report", 

description**=**"Generate system report \(admin only\)", parameters**=**\{\}, 

handler**=**self.admin\_report

\)

**def **get\_info\(self, args, raw\_data\):

**return **SwaigFunctionResult\("General information..."\) **def **admin\_reset\(self, args, raw\_data\):

**return **SwaigFunctionResult\("System reset initiated."\) **def **admin\_report\(self, args, raw\_data\):

**return **SwaigFunctionResult\("Report generated: All systems operational."\) **3.18.6**

**Multi-Tenant Applications**

Dynamic agents are ideal for multi-tenant scenarios:

**class **MultiTenantAgent\(AgentBase\):

*"""Different branding per tenant.""" *

TENANTS **= **\{

"\+15551111111": \{

"company": "Acme Corp", 

"voice": "rime.spore", 

"greeting": "Welcome to Acme Corp support\!" 

76

3. Building Agents

\}, 

"\+15552222222": \{

"company": "Beta Industries", 

"voice": "rime.marsh", 

"greeting": "Thank you for calling Beta Industries\!" 

\}

\}

**def \_\_init\_\_**\(self\):

super\(\). **\_\_init\_\_**\(name**=**"multi-tenant"\)

**def **on\_swml\_request\(self, request\_data: dict\) **-> **None: called\_num **= **request\_data.get\("called\_id\_num", ""\) tenant **= **self.TENANTS.get\(called\_num, \{

"company": "Default Company", 

"voice": "rime.spore", 

"greeting": "Hello\!" 

\}\)

*\# Configure for this tenant*

self.add\_language\("English", "en-US", tenant\["voice"\]\) self.prompt\_add\_section\(

"Role", 

f"You are a customer service agent for **\{**tenant\['company'\]**\}**. " 

f"Start by saying: **\{**tenant\['greeting'\]**\}**" 

\)

**3.18.7**

**Comparison Summary**

**Aspect**

**Static**

**Dynamic**

**Configuration**

Once at startup

Per-request

**Performance**

Slightly faster

Minimal overhead

**Use Case**

Generic assistants

Personalized experiences

**Complexity**

Simpler

More complex

**Testing**

Easier

Requires more scenarios

**Method**

\_\_init\_\_ only

on\_swml\_request

**3.18.8**

**Best Practices**

1. **Start static, go dynamic when needed **- Don’t over-engineer 2. **Cache expensive lookups **- Database calls in on\_swml\_request add latency 3. **Clear prompts between calls **- Use self.pom.clear\(\) if reusing sections 4. **Log caller info **- Helps with debugging dynamic behavior

5. **Test multiple scenarios **- Each caller path needs testing **def **on\_swml\_request\(self, request\_data: dict\) **-> **None:

*\# Clear previous dynamic configuration*

self.pom.clear\(\)

*\# Log for debugging*

self.log.info\("request\_received", 

caller**=**request\_data.get\("caller\_id\_num"\), 

called**=**request\_data.get\("called\_id\_num"\)

\)

*\# Configure based on request*

self.\_configure\_for\_caller\(request\_data\)

77

3. Building Agents

**3.19**

**Prompts & POM**

**Summary**: The Prompt Object Model \(POM\) provides a structured way to build AI prompts using sections, subsections, and bullets rather than raw text. 

**3.19.1 Why POM? **

**Aspect**

**Raw Text Prompt**

**POM Structured**

**Prompt**

**Format**

One long string

Organized sections with

body, bullets, subsections

**Maintainability**

Hard to maintain

Easy to modify individual

sections

**Structure**

No structure

Clear hierarchy \(Role →

Guidelines → Rules\)

**Extensibility**

Difficult to extend

Reusable components

**Raw Text Problems: **- Everything mixed together in one string - Hard to find and update specific instructions -

Difficult to share sections between agents

**POM Benefits: **- Sections keep concerns separated - Bullets make lists scannable - Subsections add depth without clutter - Renders to clean, formatted markdown

**3.19.2**

**POM Structure**

┌─────────────────────────────────────────────────────────────────────────────┐

│

POM Hierarchy

│

├─────────────────────────────────────────────────────────────────────────────┤

│

│

│

Prompt

│

│

│

│

│

├── Section: "Role" 

│

│

│

└── body: "You are a customer service agent..." 

│

│

│

│

│

├── Section: "Guidelines" 

│

│

│

├── body: "Follow these guidelines:" 

│

│

│

└── bullets:

│

│

│

• "Be professional" 

│

│

│

• "Ask clarifying questions" 

│

│

│

• "Keep responses concise" 

│

│

│

│

│

└── Section: "Rules" 

│

│

├── body: "Adhere to these rules:" 

│

│

└── subsections:

│

│

├── Subsection: "Security" 

│

│

│

└── bullets: \["Never share passwords", ...\]

│

│

└── Subsection: "Privacy" 

│

│

└── bullets: \["Don't ask for SSN", ...\]

│

│

│

└─────────────────────────────────────────────────────────────────────────────┘

78

3. Building Agents

**3.19.3 Adding Sections**

**3.19.3.1 Basic Section with Body**

from signalwire\_agents import AgentBase

**class **MyAgent\(AgentBase\):

**def \_\_init\_\_**\(self\):

super\(\). **\_\_init\_\_**\(name**=**"my-agent"\)

*\# Simple section with body text*

self.prompt\_add\_section\(

"Role", 

"You are a helpful customer service representative for Acme Corp." 

\)

**3.19.3.2 Section with Bullets**

*\#\# Section with bullet points*

self.prompt\_add\_section\(

"Guidelines", 

body**=**"Follow these guidelines when speaking with customers:", bullets**=**\[

"Be professional and courteous at all times", 

"Ask clarifying questions when the request is unclear", 

"Keep responses concise - this is a voice conversation", 

"Offer to transfer to a human if you cannot help" 

\]

\)

**3.19.3.3**

**Section with Numbered Bullets**

*\#\# Use numbered list instead of bullets*

self.prompt\_add\_section\(

"Process", 

body**=**"Follow this process for each call:", 

bullets**=**\[

"Greet the customer warmly", 

"Identify the reason for their call", 

"Resolve the issue or transfer", 

"Thank them and end the call" 

\], 

numbered\_bullets**=**True

*\# 1. 2. 3. instead of bullets*

\)

**3.19.4**

**Subsections**

Add nested structure within sections:

*\#\# First, create the parent section*

self.prompt\_add\_section\(

"Policies", 

body**=**"Follow company policies in these areas:" 

\)

*\#\# Then add subsections*

self.prompt\_add\_subsection\(

"Policies", 

*\# Parent section title*

"Returns", 

*\# Subsection title*

body**=**"For return requests:", 

bullets**=**\[

"Items can be returned within 30 days", 

"Receipt is required for cash refunds", 

"Exchanges are always available" 

\]

79

3. Building Agents

\)

self.prompt\_add\_subsection\(

"Policies", 

"Billing", 

body**=**"For billing inquiries:", 

bullets**=**\[

"Verify customer identity first", 

"Review last 3 statements", 

"Offer payment plans if needed" 

\]

\)

**3.19.5**

**Declarative Prompts \(PROMPT\_SECTIONS\)**

Define prompts declaratively as a class attribute:

**class **DeclarativeAgent\(AgentBase\):

PROMPT\_SECTIONS **= **\{

"Role": "You are a friendly assistant for a pizza restaurant.", 

"Menu Knowledge": \[

"Small pizza: $10", 

"Medium pizza: $14", 

"Large pizza: $18", 

"Toppings: $1.50 each" 

\], 

"Order Process": \{

"body": "When taking orders:", 

"bullets": \[

"Confirm the size first", 

"List available toppings", 

"Repeat the order back", 

"Provide total price" 

\]

\}, 

"Policies": \{

"body": "Restaurant policies:", 

"subsections": \[

\{

"title": "Delivery", 

"body": "Delivery information:", 

"bullets": \[

"Free delivery over $25", 

"$5 fee under $25", 

"30-45 minute delivery time" 

\]

\}, 

\{

"title": "Pickup", 

"bullets": \[

"Ready in 15-20 minutes", 

"Call when you arrive" 

\]

\}

\]

\}

\}

**def \_\_init\_\_**\(self\):

super\(\). **\_\_init\_\_**\(name**=**"pizza-agent"\)

self.add\_language\("English", "en-US", "rime.spore"\) 80

3. Building Agents

**3.19.6 POM Builder Direct Access**

For advanced use, access the POM builder directly:

**class **AdvancedAgent\(AgentBase\):

**def \_\_init\_\_**\(self\):

super\(\). **\_\_init\_\_**\(name**=**"advanced-agent"\)

*\# Direct POM access*

self.pom.section\("Role"\).body\(

"You are an expert technical support agent." 

\)

self.pom.section\("Expertise"\).bullets\(\[

"Network troubleshooting", 

"Software installation", 

"Hardware diagnostics" 

\]\)

*\# Chain multiple calls*

\(self.pom

.section\("Process"\)

.body\("Follow these steps:"\)

.numbered\_bullets\(\[

"Identify the issue", 

"Run diagnostics", 

"Apply solution", 

"Verify resolution" 

\]\)\)

**3.19.7**

**Post-Call Prompts**

Configure what happens after the call ends:

*\#\# Set post-prompt for call summary*

self.set\_post\_prompt\(

"Summarize this call including: " 

"1\) The customer's issue " 

"2\) How it was resolved " 

"3\) Any follow-up needed" 

\)

*\#\# Alternative: Full post-prompt configuration*

self.set\_post\_prompt\_data\(\{

"text": "Generate a detailed call summary.", 

"temperature": 0.3, 

"top\_p": 0.9

\}\)

**3.19.8**

**Voice-Optimized Prompts**

Write prompts optimized for voice conversations:

**class **VoiceOptimizedAgent\(AgentBase\):

**def \_\_init\_\_**\(self\):

super\(\). **\_\_init\_\_**\(name**=**"voice-agent"\)

self.add\_language\("English", "en-US", "rime.spore"\) self.prompt\_add\_section\(

"Voice Guidelines", 

body**=**"Optimize all responses for voice:", 

bullets**=**\[

"Keep sentences short - under 20 words", 

"Avoid technical jargon unless necessary", 

"Use conversational language, not formal", 

"Pause naturally between topics", 

"Don't list more than 3 items at once", 

81

3. Building Agents

"Spell out acronyms on first use" 

\]

\)

self.prompt\_add\_section\(

"Response Style", 

bullets**=**\[

"Start responses with the key information", 

"Confirm understanding before long explanations", 

"Ask 'Does that make sense?' after complex topics", 

"Use filler words naturally: 'Let me check that for you'" 

\]

\)

**3.19.9**

**Prompt Best Practices**

**3.19.9.1 1. Lead with Role Definition**

*\#\# Good - clear role first*

self.prompt\_add\_section\(

"Role", 

"You are Sarah, a senior customer service representative " 

"at TechCorp with 5 years of experience helping customers " 

"with software products." 

\)

**3.19.9.2 2. Separate Concerns**

*\#\# Good - each section has one purpose*

self.prompt\_add\_section\("Role", "..."\)

self.prompt\_add\_section\("Knowledge", "..."\)

self.prompt\_add\_section\("Guidelines", "..."\)

self.prompt\_add\_section\("Restrictions", "..."\)

*\#\# Bad - everything mixed together*

self.prompt\_add\_section\("Instructions", 

"You are an agent. Be nice. Don't share secrets. " 

"You know about products. Follow the rules..." 

\)

**3.19.9.3**

**3. Use Bullets for Lists**

*\#\# Good - scannable bullets*

self.prompt\_add\_section\(

"Products", 

body**=**"You can help with these products:", 

bullets**=**\["Basic Plan - $10/mo", "Pro Plan - $25/mo", "Enterprise - Custom"\]

\)

*\#\# Bad - inline list*

self.prompt\_add\_section\(

"Products", 

"Products include Basic Plan at $10/mo, Pro Plan at $25/mo, " 

"and Enterprise with custom pricing." 

\)

**3.19.9.4**

**4. Be Specific About Restrictions**

*\#\# Good - explicit restrictions*

self.prompt\_add\_section\(

"Restrictions", 

bullets**=**\[

"Never share customer passwords or security codes", 

"Do not process refunds over $500 without transfer", 

82

3. Building Agents

"Cannot modify account ownership", 

"Must verify identity before account changes" 

\]

\)

**3.19.10 Generated Prompt Output**

POM converts your structure to formatted text:

\#\# Role

You are Sarah, a customer service representative for Acme Corp. 

\#\# Guidelines

Follow these guidelines:

\* Be professional and courteous

\* Ask clarifying questions when needed

\* Keep responses concise for voice

\#\# Policies

\#\#\# Returns

For return requests:

\* Items can be returned within 30 days

\* Receipt required for cash refunds

\#\#\# Billing

For billing inquiries:

\* Verify customer identity first

\* Review recent statements

83

3. Building Agents

**3.20**

**Voice & Language**

**Summary**: Configure Text-to-Speech voices, languages, and pronunciation to create natural-sounding agents. 

**3.20.1 Voice Configuration Overview**

**3.20.1.1 Language Configuration**

**Parameter**

**Description**

**Example**

name

Human-readable name

"English" 

code

Language code for STT

"en-US" 

voice

TTS voice identifier

"rime.spore" or "elevenlab

s.josh:eleven\_turbo\_v2\_5" 

**3.20.1.2 Fillers \(Natural Speech\)**

**Parameter**

**Description**

**Example**

speech\_fillers

Used during natural conversation

\["Um", "Well", "So"\]

pauses

function\_fillers

Used while executing a function

\["Let me check...", "One

moment..."\]

**3.20.2**

**Adding a Language**

**3.20.2.1**

**Basic Configuration**

from signalwire\_agents import AgentBase

**class **MyAgent\(AgentBase\):

**def \_\_init\_\_**\(self\):

super\(\). **\_\_init\_\_**\(name**=**"my-agent"\)

*\# Basic language setup*

self.add\_language\(

name**=**"English", 

*\# Display name*

code**=**"en-US", 

*\# Language code for STT*

voice**=**"rime.spore" 

*\# TTS voice*

\)

**3.20.2.2**

**Voice Format**

The voice parameter uses the format engine.voice:model where model is optional:

*\#\# Simple voice \(engine.voice\)*

self.add\_language\("English", "en-US", "rime.spore"\)

*\#\# With model \(engine.voice:model\)*

self.add\_language\("English", "en-US", "elevenlabs.josh:eleven\_turbo\_v2\_5"\) 84

3. Building Agents

**3.20.3 Available TTS Engines**

**Provider**

**Engine Code**

**Example Voice**

**Reference**

Amazon Polly

amazon

amazon.Joanna-Neural

Voice IDs

Cartesia

cartesia

cartesia.a167e0f3-df7e-4

Voice IDs

d52-a9c3-f949145efdab

Deepgram

deepgram

deepgram.aura-asteria-en

Voice IDs

ElevenLabs

elevenlabs

elevenlabs.thomas

Voice IDs

Google Cloud

gcloud

gcloud.en-US-Casual-K

Voice IDs

Microsoft Azure

azure

azure.en-US-AvaNeural

Voice IDs

OpenAI

openai

openai.alloy

Voice IDs

Rime

rime

rime.luna:arcana

Voice IDs

**3.20.4**

**Filler Phrases**

Add natural pauses and filler words:

self.add\_language\(

name**=**"English", 

code**=**"en-US", 

voice**=**"rime.spore", 

speech\_fillers**=**\[

"Um", 

"Well", 

"Let me think", 

"So" 

\], 

function\_fillers**=**\[

"Let me check that for you", 

"One moment please", 

"I'm looking that up now", 

"Bear with me" 

\]

\)

**Speech fillers**: Used during natural conversation pauses

**Function fillers**: Used while the AI is executing a function **3.20.5**

**Multi-Language Support**

Use code="multi" for automatic language detection and matching: **class **MultilingualAgent\(AgentBase\):

**def \_\_init\_\_**\(self\):

super\(\). **\_\_init\_\_**\(name**=**"multilingual-agent"\)

*\# Multi-language support \(auto-detects and matches caller's language\)* self.add\_language\(

name**=**"Multilingual", 

code**=**"multi", 

voice**=**"rime.spore" 

\)

self.prompt\_add\_section\(

"Language", 

"Automatically detect and match the caller's language without " 

"prompting or asking them to verify. Respond naturally in whatever " 

"language they speak." 

\)

85

3. Building Agents

The multi code supports: English, Spanish, French, German, Hindi, Russian, Portuguese, Japanese, Italian, and Dutch. 

**Note**: Speech recognition hints do not work when using code="multi". If you need hints for specific terms, use individual language codes instead. 

For more control over individual languages with custom fillers:

**class **CustomMultilingualAgent\(AgentBase\):

**def \_\_init\_\_**\(self\):

super\(\). **\_\_init\_\_**\(name**=**"custom-multilingual"\)

*\# English \(primary\)*

self.add\_language\(

name**=**"English", 

code**=**"en-US", 

voice**=**"rime.spore", 

speech\_fillers**=**\["Um", "Well", "So"\], function\_fillers**=**\["Let me check that"\]

\)

*\# Spanish*

self.add\_language\(

name**=**"Spanish", 

code**=**"es-MX", 

voice**=**"rime.luna", 

speech\_fillers**=**\["Eh", "Pues", "Bueno"\], function\_fillers**=**\["Dejame verificar", "Un momento"\]

\)

*\# French*

self.add\_language\(

name**=**"French", 

code**=**"fr-FR", 

voice**=**"rime.claire", 

speech\_fillers**=**\["Euh", "Alors", "Bon"\], function\_fillers**=**\["Laissez-moi verifier", "Un instant"\]

\)

self.prompt\_add\_section\(

"Language", 

"Automatically detect and match the caller's language without " 

"prompting or asking them to verify." 

\)

**3.20.6**

**Pronunciation Rules**

Fix pronunciation of specific words:

**class **AgentWithPronunciation\(AgentBase\):

**def \_\_init\_\_**\(self\):

super\(\). **\_\_init\_\_**\(name**=**"pronunciation-agent"\) self.add\_language\("English", "en-US", "rime.spore"\)

*\# Fix brand names*

self.add\_pronunciation\(

replace**=**"ACME", 

with\_text**=**"Ack-me" 

\)

*\# Fix technical terms*

self.add\_pronunciation\(

replace**=**"SQL", 

with\_text**=**"sequel" 

\)

*\# Case-insensitive matching*

self.add\_pronunciation\(

86

3. Building Agents

replace**=**"api", 

with\_text**=**"A P I", 

ignore\_case**=**True

\)

*\# Fix names*

self.add\_pronunciation\(

replace**=**"Nguyen", 

with\_text**=**"win" 

\)

**3.20.7**

**Set Multiple Pronunciations**

*\#\# Set all pronunciations at once*

self.set\_pronunciations\(\[

\{"replace": "ACME", "with": "Ack-me"\}, 

\{"replace": "SQL", "with": "sequel"\}, 

\{"replace": "API", "with": "A P I", "ignore\_case": True\}, 

\{"replace": "CEO", "with": "C E O"\}, 

\{"replace": "ASAP", "with": "A sap"\}

\]\)

**3.20.8**

**Voice Selection Guide**

**Use Case**

**Recommended Voice Style**

Customer Service

Warm, friendly \(rime.spore\)

Technical Support

Clear, professional \(rime.marsh\)

Sales

Energetic, persuasive \(elevenlabs voices\)

Healthcare

Calm, reassuring

Legal/Finance

Formal, authoritative

**Considerations: **- Match voice personality to brand - Test with actual callers - Consider regional accents - Evaluate TTS quality for your content

**3.20.9**

**Dynamic Voice Selection**

Change voice based on context:

**class **DynamicVoiceAgent\(AgentBase\):

DEPARTMENT\_VOICES **= **\{

"support": \{"voice": "rime.spore", "name": "Alex"\}, 

"sales": \{"voice": "rime.marsh", "name": "Jordan"\}, 

"billing": \{"voice": "rime.coral", "name": "Morgan"\}

\}

**def \_\_init\_\_**\(self\):

super\(\). **\_\_init\_\_**\(name**=**"dynamic-voice"\)

**def **on\_swml\_request\(self, request\_data: dict\) **-> **None:

*\# Determine department from called number*

called\_num **= **request\_data.get\("called\_id\_num", ""\) **if **"555-1000" **in **called\_num:

dept **= **"support" 

**elif **"555-2000" **in **called\_num:

dept **= **"sales" 

**else**:

dept **= **"billing" 

config **= **self.DEPARTMENT\_VOICES\[dept\]

self.add\_language\("English", "en-US", config\["voice"\]\) 87

3. Building Agents

self.prompt\_add\_section\(

"Role", 

f"You are **\{**config\['name'\]**\}**, a **\{**dept**\} **representative." 

\)

**3.20.10 Language Codes Reference**

Supported language codes:

**Language**

**Codes**

Multilingual

multi \(English, Spanish, French, German, Hindi, Russian, Portuguese, Japanese, Italian, Dutch\)

Bulgarian

bg

Czech

cs

Danish

da, da-DK

Dutch

nl

English

en, en-US, en-AU, en-GB, en-IN, en-NZ

Finnish

fi

French

fr, fr-CA

German

de

Hindi

hi

Hungarian

hu

Indonesian

id

Italian

it

Japanese

ja

Korean

ko, ko-KR

Norwegian

no

Polish

pl

Portuguese

pt, pt-BR, pt-PT

Russian

ru

Spanish

es, es-419

Swedish

sv, sv-SE

Turkish

tr

Ukrainian

uk

Vietnamese

vi

**3.20.11**

**Complete Voice Configuration Example**

from signalwire\_agents import AgentBase

**class **FullyConfiguredVoiceAgent\(AgentBase\):

**def \_\_init\_\_**\(self\):

super\(\). **\_\_init\_\_**\(name**=**"voice-configured"\)

*\# Primary language with all options*

self.add\_language\(

name**=**"English", 

code**=**"en-US", 

voice**=**"rime.spore", 

speech\_fillers**=**\[

"Um", 

"Well", 

88

3. Building Agents

"Let me see", 

"So" 

\], 

function\_fillers**=**\[

"Let me look that up for you", 

"One moment while I check", 

"I'm searching for that now", 

"Just a second" 

\]

\)

*\# Secondary language*

self.add\_language\(

name**=**"Spanish", 

code**=**"es-MX", 

voice**=**"rime.luna", 

speech\_fillers**=**\["Pues", "Bueno"\], 

function\_fillers**=**\["Un momento", "Dejame ver"\]

\)

*\# Pronunciation fixes*

self.set\_pronunciations\(\[

\{"replace": "ACME", "with": "Ack-me"\}, 

\{"replace": "www", "with": "dub dub dub"\}, 

\{"replace": ".com", "with": "dot com"\}, 

\{"replace": "@", "with": "at"\}

\]\)

self.prompt\_add\_section\(

"Role", 

"You are a friendly customer service agent." 

\)

89

3. Building Agents

**3.21 AI Parameters**

**Summary**: Tune conversation behavior with parameters for speech detection, timeouts, barge control, and AI model settings. For a complete parameter reference, see AI Parameters Reference. 

**3.21.1 Parameter Categories**

**Category**

**Key Parameters**

**Purpose**

**Speech Detection**

end\_of\_speech\_timeout, confidence

Control when speech ends

**Timeouts**

attention\_timeout, inactivity\_tim

Handle silence and idle

eout

callers

**Barge Control**

barge\_confidence, barge\_match\_str

Manage interruptions

ing

**AI Model**

temperature, top\_p, max\_tokens

Tune response generation

**3.21.2**

**Setting Parameters**

from signalwire\_agents import AgentBase

**class **MyAgent\(AgentBase\):

**def \_\_init\_\_**\(self\):

super\(\). **\_\_init\_\_**\(name**=**"my-agent"\)

self.add\_language\("English", "en-US", "rime.spore"\)

*\# Set multiple parameters at once*

self.set\_params\(\{

"end\_of\_speech\_timeout": 600, 

"attention\_timeout": 15000, 

"inactivity\_timeout": 45000, 

"temperature": 0.5

\}\)

**3.21.3**

**Essential Parameters**

**3.21.3.1**

**Speech Detection**

**Parameter**

**Type**

**Default**

**Description**

end\_of\_speech\_timeout

int

700

Milliseconds of silence

before speech is complete

confidence

float

0.75

Speech detection confidence

threshold \(0.0-1.0\)

energy\_level

int

52

Minimum audio level in dB

\(0-100\)

*\#\# Fast response - shorter silence detection*

self.set\_params\(\{"end\_of\_speech\_timeout": 400\}\)

*\#\# Patient agent - longer silence tolerance*

self.set\_params\(\{"end\_of\_speech\_timeout": 1000\}\)

90

3. Building Agents

**3.21.3.2 Timeouts**

**Parameter**

**Type**

**Default**

**Description**

attention\_timeout

int

5000

Milliseconds before

prompting idle caller

inactivity\_timeout

int

600000

Milliseconds before ending

call \(10 min default\)

*\#\# Quick service - prompt quickly if silent*

self.set\_params\(\{

"attention\_timeout": 5000, 

*\# "Are you there?" after 5 seconds*

"inactivity\_timeout": 30000

*\# End call after 30 seconds*

\}\)

*\#\# Patient service - give caller time to think*

self.set\_params\(\{

"attention\_timeout": 20000, 

*\# Wait 20 seconds before prompting*

"inactivity\_timeout": 60000

*\# Wait full minute before ending*

\}\)

**3.21.3.3 Barge Control**

Barge-in allows callers to interrupt the AI while it’s speaking. 

**Parameter**

**Type**

**Default**

**Description**

barge\_confidence

float

0.75

Confidence threshold for

interruption

barge\_match\_string

str

-

Phrase required to trigger

barge

transparent\_barge

bool

true

Enable transparent barge

mode

*\#\# Require specific phrase to interrupt*

self.set\_params\(\{

"barge\_match\_string": "excuse me" 

\}\)

*\#\# Higher confidence required for interruption*

self.set\_params\(\{

"barge\_confidence": 0.8

\}\)

**3.21.3.4**

**AI Model**

**Parameter**

**Type**

**Default**

**Description**

temperature

float

0.3

Randomness \(0-2, higher =

more creative\)

top\_p

float

1.0

Nucleus sampling threshold

max\_tokens

int

256

Maximum response length

frequency\_penalty

float

0.1

Reduce repetitive phrases

*\#\# Consistent responses \(FAQ bot\)*

self.set\_params\(\{"temperature": 0.2\}\)

*\#\# Creative responses \(entertainment\)*

91

3. Building Agents

self.set\_params\(\{"temperature": 0.9\}\)

*\#\# Balanced for customer service*

self.set\_params\(\{

"temperature": 0.5, 

"frequency\_penalty": 0.3

\}\)

**3.21.4 Use Case Presets**

**3.21.4.1 Customer Service**

self.set\_params\(\{

"end\_of\_speech\_timeout": 600, 

"attention\_timeout": 12000, 

"inactivity\_timeout": 45000, 

"temperature": 0.5

\}\)

**3.21.4.2 Technical Support**

self.set\_params\(\{

"end\_of\_speech\_timeout": 800, 

*\# Patient for complex explanations*

"attention\_timeout": 20000, 

"inactivity\_timeout": 60000, 

"temperature": 0.3

*\# Precise responses*

\}\)

**3.21.4.3**

**IVR Menu**

self.set\_params\(\{

"end\_of\_speech\_timeout": 400, 

*\# Quick response*

"attention\_timeout": 8000, 

"inactivity\_timeout": 20000, 

"temperature": 0.2

*\# Very consistent*

\}\)

**3.21.5**

**Tuning Guide**

**3.21.5.1**

**If callers are…**

**Problem**

**Solution**

Being cut off mid-sentence

Increase end\_of\_speech\_timeout

Waiting too long for response

Decrease end\_of\_speech\_timeout

Not hearing “Are you there?” 

Decrease attention\_timeout

Getting hung up on too fast

Increase inactivity\_timeout

Accidentally interrupting

Increase barge\_confidence

**3.21.5.2**

**If responses are…**

**Problem**

**Solution**

Too repetitive

Increase frequency\_penalty

Too random/inconsistent

Decrease temperature

Too predictable

Increase temperature

Too long

Decrease max\_tokens

92

3. Building Agents

**3.21.6 Complete Example**

*\#\!/usr/bin/env python3*

*\#\# configured\_agent.py - Agent with AI parameters configured*

from signalwire\_agents import AgentBase

**class **ConfiguredAgent\(AgentBase\):

**def \_\_init\_\_**\(self\):

super\(\). **\_\_init\_\_**\(name**=**"configured-agent"\) self.add\_language\("English", "en-US", "rime.spore"\) self.set\_params\(\{

*\# Speech detection*

"end\_of\_speech\_timeout": 600, 

"confidence": 0.6, 

*\# Timeouts*

"attention\_timeout": 15000, 

"inactivity\_timeout": 45000, 

*\# AI model*

"temperature": 0.5, 

"frequency\_penalty": 0.2

\}\)

self.prompt\_add\_section\(

"Role", 

"You are a helpful customer service agent." 

\)

**if **\_\_name\_\_ **== **"\_\_main\_\_":

agent **= **ConfiguredAgent\(\)

agent.run\(\)

**3.21.7**

**More Parameters**

For the complete list of all available parameters including: - ASR configuration \(diarization, smart formatting\) -

Audio settings \(volume, background music, hold music\) - Video parameters - Advanced behavior controls - SWAIG

control parameters

See the **AI Parameters Reference **in the Appendix. 

93

3. Building Agents

**3.22**

**Hints**

**Summary**: Speech hints improve recognition accuracy for domain-specific vocabulary, brand names, technical terms, and other words the STT engine might misinterpret. 

**3.22.1 Why Use Hints? **

┌─────────────────────────────────────────────────────────────────────────────┐

│

Speech Hints

│

├─────────────────────────────────────────────────────────────────────────────┤

│

│

│

Without Hints

With Hints

│

│

┌─────────────────────────────┐

┌─────────────────────────────┐

│

│

│

│

│

│

│

│

│

Caller: "My Acme account" 

│

│

Caller: "My Acme account" 

│

│

│

│

│

│

│

│

│

│

│

│

▼

│

│

▼

│

│

│

│

STT:

"My acne account" 

│

│

STT:

"My Acme account" 

│

│

│

│

│

│

│

│

│

│

│

│

\(misheard\)

│

│

\(correct\!\)

│

│

│

│

│

│

│

│

│

└─────────────────────────────┘

└─────────────────────────────┘

│

│

│

│

Hints tell the STT engine to listen for specific words and phrases

│

│

│

└─────────────────────────────────────────────────────────────────────────────┘

**3.22.2**

**Adding Simple Hints**

**3.22.2.1**

**Single Hint**

from signalwire\_agents import AgentBase

**class **MyAgent\(AgentBase\):

**def \_\_init\_\_**\(self\):

super\(\). **\_\_init\_\_**\(name**=**"my-agent"\)

self.add\_language\("English", "en-US", "rime.spore"\)

*\# Add single hint*

self.add\_hint\("Acme"\)

self.add\_hint\("SignalWire"\)

**3.22.2.2**

**Multiple Hints**

*\#\# Add list of hints*

self.add\_hints\(\[

"Acme", 

"SignalWire", 

"API", 

"webhook", 

"SWML" 

\]\)

94

3. Building Agents

**3.22.3 What to Hint**

**Category**

**Examples**

**Brand Names**

Acme Corp, SignalWire, company name, product names

**Technical Terms**

API, webhook, OAuth, SDK, JSON

**Industry Jargon**

KYC, AML, SLA, EOD, PTO

**Names**

Employee names, customer names, location names

**Numbers/Codes**

Account numbers, ZIP codes, reference IDs

**Actions**

Transfer, escalate, reschedule

**3.22.4**

**Hint Examples by Use Case**

**3.22.4.1 Customer Service**

self.add\_hints\(\[

*\# Brand and products*

"Acme", "Acme Pro", "Acme Enterprise", 

*\# Common actions*

"account", "billing", "refund", "exchange", "return", 

"cancel", "upgrade", "downgrade", 

*\# Support terms*

"representative", "supervisor", "escalate", "ticket", 

"case number", "reference number" 

\]\)

**3.22.4.2**

**Technical Support**

self.add\_hints\(\[

*\# Product names*

"Windows", "macOS", "Linux", "Chrome", "Firefox", 

*\# Technical terms*

"reboot", "restart", "reinstall", "cache", "cookies", 

"browser", "firewall", "antivirus", "driver", 

*\# Error terms*

"error code", "blue screen", "crash", "freeze", 

"not responding", "won't start" 

\]\)

**3.22.4.3**

**Healthcare**

self.add\_hints\(\[

*\# Appointment terms*

"appointment", "reschedule", "cancel", "follow-up", 

*\# Medical terms*

"prescription", "refill", "pharmacy", "dosage", 

"medication", "symptoms", "diagnosis", 

*\# Department names*

"cardiology", "dermatology", "pediatrics", "radiology", 

*\# Common medications \(if applicable\)*

"Tylenol", "Advil", "Lipitor", "Metformin" 

\]\)

95

3. Building Agents

**3.22.4.4 Financial Services**

self.add\_hints\(\[

*\# Account terms*

"checking", "savings", "IRA", "401k", "Roth", 

*\# Transaction terms*

"transfer", "deposit", "withdrawal", "wire", 

"ACH", "routing number", "account number", 

*\# Services*

"mortgage", "auto loan", "credit card", "overdraft", 

*\# Verification*

"social security", "date of birth", "mother's maiden name" 

\]\)

**3.22.5**

**Pattern Hints \(Advanced\)**

For words with specific patterns, use pattern hints:

*\#\# Pattern hint with replacement*

self.add\_pattern\_hint\(

hint**=**"account number", 

*\# What to listen for*

pattern**=**r"\\d**\{8,12\}**", 

*\# Regex pattern to match*

replace**=**"$**\{1\}**", 

*\# How to format it*

ignore\_case**=**True

\)

*\#\# Normalize variations*

self.add\_pattern\_hint\(

hint**=**"Acme", 

pattern**=**r" **\(**acme**|**ackme**|**ac me**\)**", 

*\# Common mishearings*

replace**=**"Acme", 

*\# Normalize to correct form*

ignore\_case**=**True

\)

**3.22.6**

**Organizing Hints**

For large hint lists, organize by category:

**class **OrganizedHintsAgent\(AgentBase\):

*\# Hint categories*

BRAND\_HINTS **= **\["Acme", "Acme Pro", "Acme Enterprise"\]

ACTION\_HINTS **= **\["account", "billing", "refund", "cancel"\]

SUPPORT\_HINTS **= **\["representative", "supervisor", "escalate"\]

**def \_\_init\_\_**\(self\):

super\(\). **\_\_init\_\_**\(name**=**"organized-hints"\)

self.add\_language\("English", "en-US", "rime.spore"\)

*\# Add all hint categories*

self.add\_hints\(self.BRAND\_HINTS\)

self.add\_hints\(self.ACTION\_HINTS\)

self.add\_hints\(self.SUPPORT\_HINTS\)

**3.22.7**

**Dynamic Hints**

Add hints based on context:

**class **DynamicHintsAgent\(AgentBase\):

DEPARTMENT\_HINTS **= **\{

"sales": \["pricing", "quote", "demo", "trial", "discount"\], 

"support": \["ticket", "bug", "error", "fix", "issue"\], 

"billing": \["invoice", "payment", "refund", "charge"\]

96

3. Building Agents

\}

**def \_\_init\_\_**\(self\):

super\(\). **\_\_init\_\_**\(name**=**"dynamic-hints"\)

self.add\_language\("English", "en-US", "rime.spore"\)

*\# Common hints for all departments*

self.add\_hints\(\["Acme", "account", "help"\]\) **def **on\_swml\_request\(self, request\_data: dict\) **-> **None: called\_num **= **request\_data.get\("called\_id\_num", ""\)

*\# Add department-specific hints*

**if **"555-1000" **in **called\_num:

self.add\_hints\(self.DEPARTMENT\_HINTS\["sales"\]\)

**elif **"555-2000" **in **called\_num:

self.add\_hints\(self.DEPARTMENT\_HINTS\["support"\]\)

**else**:

self.add\_hints\(self.DEPARTMENT\_HINTS\["billing"\]\)

**3.22.8**

**Hint Best Practices**

**DO: **- Hint brand names and product names - Hint technical terms specific to your domain - Hint common employ-ee/customer names - Hint acronyms and abbreviations - Test with actual callers to find missed words **DON’T: **- Hint common English words \(already recognized well\) - Add hundreds of hints \(quality over quantity\) -

Hint full sentences \(single words/short phrases work best\) - Forget to update hints when products/terms change **3.22.9**

**Testing Hints**

Use swaig-test to verify hints are included:

*\#\# View SWML including hints*

swaig-test my\_agent.py --dump-swml **| grep **-A 20 "hints" 

Check the generated SWML for the hints array:

**\{**

"version" **: **"1.0.0" **, **

"sections" **: \{**

"main" **: **\[**\{**

"ai" **: \{**

"hints" **: **\[

"Acme", 

"SignalWire", 

"account", 

"billing" 

\]

**\}**

**\}**\]

**\}**

**\}**

**3.22.10**

**Complete Example**

*\#\!/usr/bin/env python3*

*\#\# hinted\_agent.py - Agent with speech recognition hints*

from signalwire\_agents import AgentBase, SwaigFunctionResult

**class **HintedAgent\(AgentBase\):

**def \_\_init\_\_**\(self\):

super\(\). **\_\_init\_\_**\(name**=**"hinted-agent"\)

self.add\_language\("English", "en-US", "rime.spore"\) 97

3. Building Agents

*\# Brand hints*

self.add\_hints\(\[

"Acme", "Acme Pro", "Acme Enterprise", 

"AcmePay", "AcmeCloud" 

\]\)

*\# Product SKUs*

self.add\_hints\(\[

"SKU", "A100", "A200", "A300", 

"PRO100", "ENT500" 

\]\)

*\# Common actions*

self.add\_hints\(\[

"account", "billing", "invoice", "refund", 

"cancel", "upgrade", "downgrade", 

"representative", "supervisor" 

\]\)

*\# Technical terms*

self.add\_hints\(\[

"API", "webhook", "integration", 

"OAuth", "SSO", "MFA" 

\]\)

self.prompt\_add\_section\(

"Role", 

"You are a customer service agent for Acme Corporation." 

\)

self.define\_tool\(

name**=**"lookup\_product", 

description**=**"Look up product by SKU", 

parameters**=**\{

"type": "object", 

"properties": \{

"sku": \{

"type": "string", 

"description": "Product SKU like A100 or PRO100" 

\}

\}, 

"required": \["sku"\]

\}, 

handler**=**self.lookup\_product

\)

**def **lookup\_product\(self, args, raw\_data\):

sku **= **args.get\("sku", ""\).upper\(\)

products **= **\{

"A100": "Acme Basic - $99/month", 

"A200": "Acme Standard - $199/month", 

"A300": "Acme Premium - $299/month", 

"PRO100": "Acme Pro - $499/month", 

"ENT500": "Acme Enterprise - Custom pricing" 

\}

**if **sku **in **products:

**return **SwaigFunctionResult\(f" **\{**sku**\}**: **\{**products\[sku\]**\}**"\) **return **SwaigFunctionResult\(f"SKU **\{**sku**\} **not found."\) **if **\_\_name\_\_ **== **"\_\_main\_\_":

agent **= **HintedAgent\(\)

agent.run\(\)

98

3. Building Agents

**3.22.11 Next Steps**

You now know how to build and configure agents. Next, learn about SWAIG functions to add custom capabilities. 

99

**Chapter 4**

**SWAIG Functions**

**Summary**: SWAIG \(SignalWire AI Gateway\) functions let your AI agent call custom code to look up data, make API calls, and take actions during conversations. 

**4.1 What You’ll Learn**

This chapter covers everything about SWAIG functions:

1. **Defining Functions **- Creating functions the AI can call

2. **Parameters **- Accepting arguments from the AI

3. **Results & Actions **- Returning data and triggering actions 4. **DataMap **- Serverless API integration without webhooks

5. **Native Functions **- Built-in SignalWire functions

100

4. SWAIG Functions

**4.2 How SWAIG Functions Work**

┌─────────────────────────────────────────────────────────────────────────────┐

│

SWAIG Function Flow

│

├─────────────────────────────────────────────────────────────────────────────┤

│

│

│

1. Caller speaks

│

│

"What's my order status for order 12345?" 

│

│

│

│

│

▼

│

│

2. AI decides to call function

│

│

┌─────────────────────────────────────────────┐

│

│

│ AI: "I'll look that up using check\_order" 

│

│

│

│ Function: check\_order

│

│

│

│ Args: \{"order\_number": "12345"\}

│

│

│

└─────────────────────────────────────────────┘

│

│

│

│

│

▼

│

│

3. SignalWire calls your webhook

│

│

POST https://your-server.com/swaig

│

│

\{"function": "check\_order", "args": \{...\}\}

│

│

│

│

│

▼

│

│

4. Your handler returns result

│

│

┌─────────────────────────────────────────────┐

│

│

│ SwaigFunctionResult\(

│

│

│

│

"Order 12345 shipped Monday, 

│

│

│

│

arriving Thursday" 

│

│

│

│ \)

│

│

│

└─────────────────────────────────────────────┘

│

│

│

│

│

▼

│

│

5. AI speaks result to caller

│

│

"Your order 12345 shipped Monday and

│

│

will arrive Thursday." 

│

│

│

└─────────────────────────────────────────────────────────────────────────────┘

**4.3**

**Quick Start Example**

Here’s a complete agent with a SWAIG function:

from signalwire\_agents import AgentBase, SwaigFunctionResult

**class **OrderAgent\(AgentBase\):

**def \_\_init\_\_**\(self\):

super\(\). **\_\_init\_\_**\(name**=**"order-agent"\)

self.add\_language\("English", "en-US", "rime.spore"\) self.prompt\_add\_section\(

"Role", 

"You are an order status assistant. Help customers check their orders." 

\)

*\# Define a function the AI can call*

self.define\_tool\(

name**=**"check\_order", 

description**=**"Look up order status by order number", parameters**=**\{

"type": "object", 

"properties": \{

"order\_number": \{

"type": "string", 

101

4. SWAIG Functions

"description": "The order number to look up" 

\}

\}, 

"required": \["order\_number"\]

\}, 

handler**=**self.check\_order

\)

**def **check\_order\(self, args, raw\_data\):

order\_number **= **args.get\("order\_number"\)

*\# Your business logic here - database lookup, API call, etc. *

orders **= **\{

"12345": "Shipped Monday, arriving Thursday", 

"67890": "Processing, ships tomorrow" 

\}

status **= **orders.get\(order\_number, "Order not found"\) **return **SwaigFunctionResult\(f"Order **\{**order\_number**\}**: **\{**status**\}**"\) **if **\_\_name\_\_ **== **"\_\_main\_\_":

agent **= **OrderAgent\(\)

agent.run\(\)

**4.4 Function Types**

**Type**

**Description**

**Handler Functions**

Defined with define\_tool\(\). Python handler runs on your server with full control over logic, database access, and API calls. 

**DataMap Functions**

Serverless API integration that runs on SignalWire’s servers. No webhook endpoint needed - direct REST API calls. 

**Native Functions**

Built into SignalWire. No custom code required - handles transfer, recording, etc. 

**4.5**

**Chapter Contents**

**Section**

**Description**

Defining Functions

Creating SWAIG functions with define\_tool\(\)

Parameters

Defining and validating function parameters

Results & Actions

Returning results and triggering actions

DataMap

Serverless API integration

Native Functions

Built-in SignalWire functions

102

4. SWAIG Functions

**4.6 When to Use SWAIG Functions**

**Use Case**

**Approach**

Database lookups

Handler function

Complex business logic

Handler function

Simple REST API calls

DataMap

Pattern-based responses

DataMap expressions

Call transfers

Native function or SwaigFunctionResult.connect\(\)

SMS sending

SwaigFunctionResult.send\_sms\(\)

**4.7 Key Concepts**

**Handler Functions**: Python code that runs on your server when the AI decides to call a function. You have full access to databases, APIs, and any Python library. 

**SwaigFunctionResult**: The return type for all SWAIG functions. Contains the response text the AI will speak and optional actions to execute. 

**Parameters**: JSON Schema definitions that tell the AI what arguments your function accepts. The AI will extract these from the conversation. 

**Actions**: Side effects like call transfers, SMS sending, or context changes that execute after the function completes. 

**DataMap**: A way to define functions that call REST APIs without running any code on your server - the API calls happen directly on SignalWire’s infrastructure. 

Let’s start by learning how to define functions. 

**4.8**

**Basic Function Definition**

from signalwire\_agents import AgentBase, SwaigFunctionResult

**class **MyAgent\(AgentBase\):

**def \_\_init\_\_**\(self\):

super\(\). **\_\_init\_\_**\(name**=**"my-agent"\)

self.add\_language\("English", "en-US", "rime.spore"\)

*\# Define a function*

self.define\_tool\(

name**=**"get\_weather", 

description**=**"Get current weather for a city", 

parameters**=**\{

"type": "object", 

"properties": \{

"city": \{

"type": "string", 

"description": "City name" 

\}

\}, 

"required": \["city"\]

\}, 

handler**=**self.get\_weather

\)

**def **get\_weather\(self, args, raw\_data\):

city **= **args.get\("city"\)

*\# Your logic here*

**return **SwaigFunctionResult\(f"The weather in **\{**city**\} **is sunny, 72 degrees"\) 103

4. SWAIG Functions

**4.9 The define\_tool\(\) Method**

**Required Parameters:**

**Parameter**

**Description**

name

Unique function name \(lowercase, underscores\)

description

What the function does \(helps AI decide when to use\)

parameters

JSON Schema defining accepted arguments

handler

Python function to call

**Optional Parameters:**

**Parameter**

**Description**

secure

Require token validation \(default: True\)

fillers

Language-specific filler phrases

webhook\_url

External webhook URL \(overrides local handler\)

required

List of required parameter names

**4.10 Handler Function Signature**

All handlers receive two arguments:

**def **my\_handler\(self, args, raw\_data\):

*""" *

*Args:*

*args: Dictionary of parsed function arguments*

*\{"city": "New York", "units": "fahrenheit"\}*

*raw\_data: Full request data including:*

*- call\_id: Unique call identifier*

*- caller\_id\_num: Caller's phone number*

*- caller\_id\_name: Caller's name*

*- called\_id\_num: Number that was called*

*- And more... *

*Returns:*

*SwaigFunctionResult with response text and optional actions*

*""" *

**return **SwaigFunctionResult\("Response text"\)

**4.11**

**Accessing Call Data**

**def **check\_account\(self, args, raw\_data\):

*\# Get caller information*

caller\_number **= **raw\_data.get\("caller\_id\_num", ""\) call\_id **= **raw\_data.get\("call\_id", ""\)

*\# Get function arguments*

account\_id **= **args.get\("account\_id"\)

*\# Use both for your logic*

**return **SwaigFunctionResult\(

f"Account **\{**account\_id**\} **for caller **\{**caller\_number**\} **is active" 

\)

104

4. SWAIG Functions

**4.12**

**Multiple Functions**

Register as many functions as your agent needs:

**class **CustomerServiceAgent\(AgentBase\):

**def \_\_init\_\_**\(self\):

super\(\). **\_\_init\_\_**\(name**=**"customer-service"\) self.add\_language\("English", "en-US", "rime.spore"\)

*\# Order lookup*

self.define\_tool\(

name**=**"check\_order", 

description**=**"Look up order status by order number", parameters**=**\{

"type": "object", 

"properties": \{

"order\_number": \{

"type": "string", 

"description": "The order number" 

\}

\}, 

"required": \["order\_number"\]

\}, 

handler**=**self.check\_order

\)

*\# Account balance*

self.define\_tool\(

name**=**"get\_balance", 

description**=**"Get account balance for a customer", parameters**=**\{

"type": "object", 

"properties": \{

"account\_id": \{

"type": "string", 

"description": "Customer account ID" 

\}

\}, 

"required": \["account\_id"\]

\}, 

handler**=**self.get\_balance

\)

*\# Store hours*

self.define\_tool\(

name**=**"get\_store\_hours", 

description**=**"Get store hours for a location", 

parameters**=**\{

"type": "object", 

"properties": \{

"location": \{

"type": "string", 

"description": "Store location or city" 

\}

\}, 

"required": \["location"\]

\}, 

handler**=**self.get\_store\_hours

\)

**def **check\_order\(self, args, raw\_data\):

order\_number **= **args.get\("order\_number"\)

**return **SwaigFunctionResult\(f"Order **\{**order\_number**\} **is in transit"\) **def **get\_balance\(self, args, raw\_data\):

account\_id **= **args.get\("account\_id"\)

**return **SwaigFunctionResult\(f"Account **\{**account\_id**\} **balance: $150.00"\) **def **get\_store\_hours\(self, args, raw\_data\):

105

4. SWAIG Functions

location **= **args.get\("location"\)

**return **SwaigFunctionResult\(f" **\{**location**\} **store: Mon-Fri 9AM-9PM, Sat-Sun 10AM-6PM"\) **4.13**

**Function Fillers**

Add per-function filler phrases for when the function is executing: self.define\_tool\(

name**=**"search\_inventory", 

description**=**"Search product inventory", 

parameters**=**\{

"type": "object", 

"properties": \{

"product": \{"type": "string", "description": "Product to search"\}

\}, 

"required": \["product"\]

\}, 

handler**=**self.search\_inventory, 

fillers**=**\{

"en-US": \[

"Let me check our inventory...", 

"Searching our stock now...", 

"One moment while I look that up..." 

\], 

"es-MX": \[

"Dejame revisar nuestro inventario...", 

"Buscando en nuestro stock..." 

\]

\}

\)

**4.14**

**The @tool Decorator**

Alternative syntax using decorators:

from signalwire\_agents import AgentBase, SwaigFunctionResult

**class **MyAgent\(AgentBase\):

**def \_\_init\_\_**\(self\):

super\(\). **\_\_init\_\_**\(name**=**"my-agent"\)

self.add\_language\("English", "en-US", "rime.spore"\)

@AgentBase.tool\(

name**=**"get\_time", 

description**=**"Get the current time", 

parameters**=**\{

"type": "object", 

"properties": \{

"timezone": \{

"type": "string", 

"description": "Timezone \(e.g., 'EST', 'PST'\)" 

\}

\}

\}

\)

**def **get\_time\(self, args, raw\_data\):

timezone **= **args.get\("timezone", "UTC"\)

**return **SwaigFunctionResult\(f"The current time in **\{**timezone**\} **is 3:45 PM"\) 106

4. SWAIG Functions

**4.15**

**External Webhook Functions**

Route function calls to an external webhook:

self.define\_tool\(

name**=**"external\_lookup", 

description**=**"Look up data from external service", parameters**=**\{

"type": "object", 

"properties": \{

"query": \{"type": "string", "description": "Search query"\}

\}, 

"required": \["query"\]

\}, 

handler**=**None, 

*\# No local handler*

webhook\_url**=**"https://external-service.com/api/lookup" 

\)

**4.16 Function Security**

By default, functions require token validation. Disable for testing:

*\# Secure function \(default\)*

self.define\_tool\(

name**=**"secure\_function", 

description**=**"Requires token validation", 

parameters**=**\{"type": "object", "properties": \{\}\}, handler**=**self.secure\_handler, 

secure**=**True

*\# Default*

\)

*\# Insecure function \(testing only\)*

self.define\_tool\(

name**=**"test\_function", 

description**=**"No token validation \(testing only\)", parameters**=**\{"type": "object", "properties": \{\}\}, handler**=**self.test\_handler, 

secure**=**False

*\# Disable for testing*

\)

**4.17**

**Writing Good Descriptions**

The description helps the AI decide when to use your function:

*\# Good - specific and clear*

description**=**"Look up order status by order number. Returns shipping status and estimated delivery date." 

*\# Bad - too vague*

description**=**"Get order info" 

*\# Good - mentions what triggers it*

description**=**"Check if a product is in stock. Use when customer asks about availability." 

*\# Good - explains constraints*

description**=**"Transfer call to human support. Only use if customer explicitly requests to speak with a person." 

107

4. SWAIG Functions

**4.18**

**Testing Functions**

Use swaig-test to test your functions:

*\# List all functions*

swaig-test my\_agent.py --list-tools

*\# Test a specific function*

swaig-test my\_agent.py --exec check\_order --order\_number 12345

*\# See the generated SWML*

swaig-test my\_agent.py --dump-swml

**4.19 Complete Example**

*\#\!/usr/bin/env python3*

*\# restaurant\_agent.py - Restaurant order assistant*

from signalwire\_agents import AgentBase, SwaigFunctionResult

**class **RestaurantAgent\(AgentBase\):

MENU **= **\{

"burger": \{"price": 12.99, "description": "Angus beef burger with fries"\}, 

"pizza": \{"price": 14.99, "description": "12-inch cheese pizza"\}, 

"salad": \{"price": 9.99, "description": "Garden salad with dressing"\}

\}

**def \_\_init\_\_**\(self\):

super\(\). **\_\_init\_\_**\(name**=**"restaurant-agent"\) self.add\_language\("English", "en-US", "rime.spore"\) self.prompt\_add\_section\(

"Role", 

"You are a friendly restaurant order assistant." 

\)

self.define\_tool\(

name**=**"get\_menu\_item", 

description**=**"Get details about a menu item including price and description", parameters**=**\{

"type": "object", 

"properties": \{

"item\_name": \{

"type": "string", 

"description": "Name of the menu item" 

\}

\}, 

"required": \["item\_name"\]

\}, 

handler**=**self.get\_menu\_item, 

fillers**=**\{

"en-US": \["Let me check the menu..."\]

\}

\)

self.define\_tool\(

name**=**"place\_order", 

description**=**"Place an order for menu items", 

parameters**=**\{

"type": "object", 

"properties": \{

"items": \{

"type": "array", 

"items": \{"type": "string"\}, 

"description": "List of menu items to order" 

\}, 

"special\_requests": \{

108

4. SWAIG Functions

"type": "string", 

"description": "Any special requests or modifications" 

\}

\}, 

"required": \["items"\]

\}, 

handler**=**self.place\_order, 

fillers**=**\{

"en-US": \["Placing your order now..."\]

\}

\)

**def **get\_menu\_item\(self, args, raw\_data\):

item\_name **= **args.get\("item\_name", ""\).lower\(\) item **= **self.MENU.get\(item\_name\)

**if **item:

**return **SwaigFunctionResult\(

f" **\{**item\_name**. **title\(\)**\}**: **\{**item\['description'\]**\}**. Price: $**\{**item\['price'\]**\}**" 

\)

**return **SwaigFunctionResult\(f"Sorry, **\{**item\_name**\} **is not on our menu."\) **def **place\_order\(self, args, raw\_data\):

items **= **args.get\("items", \[\]\)

special **= **args.get\("special\_requests", ""\) total **= **sum\(

self.MENU.get\(item.lower\(\), \{\}\).get\("price", 0\)

**for **item **in **items

\)

**if **total **> **0:

msg **= **f"Order placed: **\{**', ' **. **join\(items\)**\}**. Total: $**\{**total**:.2f\}**" 

**if **special:

msg **\+= **f" Special requests: **\{**special**\}**" 

**return **SwaigFunctionResult\(msg\)

**return **SwaigFunctionResult\("Could not place order. Please check item names."\) **if **\_\_name\_\_ **== **"\_\_main\_\_":

agent **= **RestaurantAgent\(\)

agent.run\(\)

109

4. SWAIG Functions

**4.20**

**Parameters**

**Summary**: Define function parameters using JSON Schema to specify what arguments your functions accept. The AI extracts these from the conversation. 

**4.20.1 Parameter Structure**

Parameters use JSON Schema format:

parameters**=**\{

"type": "object", 

"properties": \{

"param\_name": \{

"type": "string", 

*\# Data type*

"description": "Description" *\# Help AI understand the parameter*

\}

\}, 

"required": \["param\_name"\]

*\# Required parameters*

\}

**4.20.2**

**Parameter Types**

**Type**

**Description**

**Example Values**

string

Text values

"hello", "12345", "New Yor

k" 

number

Numeric values

42, 3.14, -10

integer

Whole numbers only

1, 42, -5

boolean

True/false

true, false

array

List of values

\["a", "b", "c"\]

object

Nested structure

\{"key": "value"\}

**4.20.3**

**String Parameters**

Basic string parameters:

parameters**=**\{

"type": "object", 

"properties": \{

"name": \{

"type": "string", 

"description": "Customer name" 

\}, 

"email": \{

"type": "string", 

"description": "Email address" 

\}, 

"phone": \{

"type": "string", 

"description": "Phone number in any format" 

\}

\}, 

"required": \["name"\]

\}

110

4. SWAIG Functions

**4.20.4 Enum Parameters**

Restrict to specific values:

parameters**=**\{

"type": "object", 

"properties": \{

"department": \{

"type": "string", 

"description": "Department to transfer to", 

"enum": \["sales", "support", "billing", "returns"\]

\}, 

"priority": \{

"type": "string", 

"description": "Issue priority level", 

"enum": \["low", "medium", "high", "urgent"\]

\}

\}, 

"required": \["department"\]

\}

**4.20.5**

**Number Parameters**

parameters**=**\{

"type": "object", 

"properties": \{

"quantity": \{

"type": "integer", 

"description": "Number of items to order" 

\}, 

"amount": \{

"type": "number", 

"description": "Dollar amount" 

\}, 

"rating": \{

"type": "integer", 

"description": "Rating from 1 to 5", 

"minimum": 1, 

"maximum": 5

\}

\}, 

"required": \["quantity"\]

\}

**4.20.6**

**Boolean Parameters**

parameters**=**\{

"type": "object", 

"properties": \{

"gift\_wrap": \{

"type": "boolean", 

"description": "Whether to gift wrap the order" 

\}, 

"express\_shipping": \{

"type": "boolean", 

"description": "Use express shipping" 

\}

\}

\}

111

4. SWAIG Functions

**4.20.7 Array Parameters**

parameters**=**\{

"type": "object", 

"properties": \{

"items": \{

"type": "array", 

"description": "List of menu items to order", 

"items": \{

"type": "string" 

\}

\}, 

"tags": \{

"type": "array", 

"description": "Tags to apply", 

"items": \{

"type": "string", 

"enum": \["urgent", "vip", "callback"\]

\}

\}

\}, 

"required": \["items"\]

\}

**4.20.8**

**Object Parameters**

parameters**=**\{

"type": "object", 

"properties": \{

"address": \{

"type": "object", 

"description": "Delivery address", 

"properties": \{

"street": \{"type": "string"\}, 

"city": \{"type": "string"\}, 

"zip": \{"type": "string"\}

\}, 

"required": \["street", "city", "zip"\]

\}

\}, 

"required": \["address"\]

\}

**4.20.9**

**Optional vs Required Parameters**

parameters**=**\{

"type": "object", 

"properties": \{

*\# Required - AI must extract this*

"order\_number": \{

"type": "string", 

"description": "Order number \(required\)" 

\}, 

*\# Optional - AI will include if mentioned*

"include\_tracking": \{

"type": "boolean", 

"description": "Include tracking details" 

\}, 

*\# Optional with default handling*

"format": \{

"type": "string", 

"description": "Output format", 

"enum": \["brief", "detailed"\], 

"default": "brief" 

\}

\}, 

112

4. SWAIG Functions

"required": \["order\_number"\]

*\# Only order\_number is required*

\}

**4.20.10 Default Values**

Handle missing optional parameters in your handler:

**def **search\_products\(self, args, raw\_data\):

*\# Get required parameter*

query **= **args.get\("query"\)

*\# Get optional parameters with defaults*

category **= **args.get\("category", "all"\)

max\_results **= **args.get\("max\_results", 5\)

sort\_by **= **args.get\("sort\_by", "relevance"\)

*\# Use parameters*

results **= **self.db.search\(

query**=**query, 

category**=**category, 

limit**=**max\_results, 

sort**=**sort\_by

\)

**return **SwaigFunctionResult\(f"Found **\{**len\(results\)**\} **products"\) **4.20.11**

**Parameter Descriptions**

Good descriptions help the AI extract parameters correctly:

parameters**=**\{

"type": "object", 

"properties": \{

*\# Good - specific format guidance*

"order\_number": \{

"type": "string", 

"description": "Order number, usually starts with ORD- followed by digits" 

\}, 

*\# Good - examples help*

"date": \{

"type": "string", 

"description": "Date in MM/DD/YYYY format, e.g., 12/25/2024" 

\}, 

*\# Good - clarifies ambiguity*

"amount": \{

"type": "number", 

"description": "Dollar amount without currency symbol, e.g., 29.99" 

\}, 

*\# Bad - too vague*

"info": \{

"type": "string", 

"description": "Information" 

*\# Don't do this*

\}

\}

\}

113

4. SWAIG Functions

**4.20.12 Complex Example**

from signalwire\_agents import AgentBase, SwaigFunctionResult

**class **TravelAgent\(AgentBase\):

**def \_\_init\_\_**\(self\):

super\(\). **\_\_init\_\_**\(name**=**"travel-agent"\)

self.add\_language\("English", "en-US", "rime.spore"\) self.define\_tool\(

name**=**"search\_flights", 

description**=**"Search for available flights between cities", parameters**=**\{

"type": "object", 

"properties": \{

"from\_city": \{

"type": "string", 

"description": "Departure city or airport code" 

\}, 

"to\_city": \{

"type": "string", 

"description": "Destination city or airport code" 

\}, 

"departure\_date": \{

"type": "string", 

"description": "Departure date in YYYY-MM-DD format" 

\}, 

"return\_date": \{

"type": "string", 

"description": "Return date in YYYY-MM-DD format \(optional for one-way\)" 

\}, 

"passengers": \{

"type": "integer", 

"description": "Number of passengers", 

"minimum": 1, 

"maximum": 9

\}, 

"cabin\_class": \{

"type": "string", 

"description": "Preferred cabin class", 

"enum": \["economy", "premium\_economy", "business", "first"\]

\}, 

"preferences": \{

"type": "object", 

"description": "Travel preferences", 

"properties": \{

"nonstop\_only": \{

"type": "boolean", 

"description": "Only show nonstop flights" 

\}, 

"flexible\_dates": \{

"type": "boolean", 

"description": "Search nearby dates for better prices" 

\}

\}

\}

\}, 

"required": \["from\_city", "to\_city", "departure\_date"\]

\}, 

handler**=**self.search\_flights

\)

**def **search\_flights\(self, args, raw\_data\):

from\_city **= **args.get\("from\_city"\)

to\_city **= **args.get\("to\_city"\)

date **= **args.get\("departure\_date"\)

passengers **= **args.get\("passengers", 1\)

cabin **= **args.get\("cabin\_class", "economy"\) prefs **= **args.get\("preferences", \{\}\)

114

4. SWAIG Functions

nonstop **= **prefs.get\("nonstop\_only", False\)

*\# Your flight search logic here*

**return **SwaigFunctionResult\(

f"Found 3 flights from **\{**from\_city**\} **to **\{**to\_city**\} **on **\{**date**\}**. " 

f"Cheapest: $299 **\{**cabin**\} **class" 

\)

**4.20.13 Validating Parameters**

Add validation in your handler:

**def **process\_payment\(self, args, raw\_data\):

amount **= **args.get\("amount"\)

card\_last\_four **= **args.get\("card\_last\_four"\)

*\# Validate amount*

**if **amount **is **None **or **amount **<= **0:

**return **SwaigFunctionResult\(

"Invalid amount. Please specify a positive dollar amount." 

\)

*\# Validate card*

**if not **card\_last\_four **or **len\(card\_last\_four\) **\!= **4: **return **SwaigFunctionResult\(

"Please provide the last 4 digits of your card." 

\)

*\# Process payment*

**return **SwaigFunctionResult\(f"Processing $**\{**amount**:.2f\} **on card ending **\{**card\_last\_four**\}**"\) **4.20.14**

**Parameter Best Practices**

**DO: **- Use clear, descriptive names \(order\_number not num\) - Provide detailed descriptions with examples - Use enum for fixed choices - Mark truly required parameters as required - Handle missing optional parameters with defaults

**DON’T: **- Require parameters the caller might not know - Use ambiguous descriptions - Expect perfect formatting \(be flexible in handlers\) - Create too many required parameters

115

4. SWAIG Functions

**4.21**

**Results & Actions**

**Summary**: SwaigFunctionResult is the return type for all SWAIG functions. It contains response text for the AI to speak and optional actions like transfers, SMS, or context changes. 

**4.21.1 Basic Results**

Return a simple response:

from signalwire\_agents import SwaigFunctionResult

**def **check\_order\(self, args, raw\_data\):

order\_number **= **args.get\("order\_number"\)

**return **SwaigFunctionResult\(f"Order **\{**order\_number**\} **shipped yesterday"\) **4.21.2**

**SwaigFunctionResult Components**

**Component**

**Description**

response

Text the AI will speak to the caller

action

List of actions to execute \(transfers, SMS, context changes, etc.\) post\_process

If True, AI speaks once more before actions execute \(useful for

confirmations\)

**4.21.3**

**Method Chaining**

SwaigFunctionResult methods return self for chaining:

**def **transfer\_to\_support\(self, args, raw\_data\):

department **= **args.get\("department", "support"\) **return **\(

SwaigFunctionResult\("I'll transfer you now"\)

.connect\("\+15551234567", final**=**True\)

\)

**4.21.4**

**Call Transfer**

Transfer to another number:

**def **transfer\_call\(self, args, raw\_data\):

department **= **args.get\("department"\)

numbers **= **\{

"sales": "\+15551111111", 

"support": "\+15552222222", 

"billing": "\+15553333333" 

\}

dest **= **numbers.get\(department, "\+15550000000"\)

**return **\(

SwaigFunctionResult\(f"Transferring you to **\{**department**\}**"\)

.connect\(dest, final**=**True\)

\)

**Transfer options:**

116

4. SWAIG Functions

*\#\# Permanent transfer - call leaves agent completely*

.connect\("\+15551234567", final**=**True\)

*\#\# Temporary transfer - returns to agent if far end hangs up*

.connect\("\+15551234567", final**=**False\)

*\#\# With custom caller ID*

.connect\("\+15551234567", final**=**True, from\_addr**=**"\+15559876543"\)

*\#\# Transfer to SIP address*

.connect\("support@company.com", final**=**True\)

**4.21.5**

**Send SMS**

Send a text message during the call:

**def **send\_confirmation\(self, args, raw\_data\):

phone **= **args.get\("phone\_number"\)

order\_id **= **args.get\("order\_id"\)

**return **\(

SwaigFunctionResult\("I've sent you a confirmation text"\)

.send\_sms\(

to\_number**=**phone, 

from\_number**=**"\+15559876543", 

body**=**f"Your order **\{**order\_id**\} **has been confirmed\!" 

\)

\)

**4.21.6**

**Hang Up**

End the call:

**def **end\_call\(self, args, raw\_data\):

**return **\(

SwaigFunctionResult\("Thank you for calling. Goodbye\!"\)

.hangup\(\)

\)

**4.21.7**

**Update Global Data**

Store data accessible throughout the call:

**def **save\_customer\_info\(self, args, raw\_data\):

customer\_id **= **args.get\("customer\_id"\)

customer\_name **= **args.get\("name"\)

**return **\(

SwaigFunctionResult\(f"I've noted your information, **\{**customer\_name**\}**"\)

.update\_global\_data\(\{

"customer\_id": customer\_id, 

"customer\_name": customer\_name, 

"verified": True

\}\)

\)

117

4. SWAIG Functions

**4.21.8 Context Switching**

Change the agent’s prompt/context:

**def **switch\_to\_technical\(self, args, raw\_data\):

**return **\(

SwaigFunctionResult\("Switching to technical support mode"\)

.switch\_context\(

system\_prompt**=**"You are now a technical support specialist. " 

"Help the customer with their technical issue." 

\)

\)

**4.21.9**

**Post-Processing**

Let AI speak once more before executing actions:

**def **transfer\_with\_confirmation\(self, args, raw\_data\):

**return **\(

SwaigFunctionResult\(

"I'll transfer you to billing. Is there anything else first?", post\_process**=**True

*\# AI can respond to follow-up before transfer*

\)

.connect\("\+15551234567", final**=**True\)

\)

**4.21.10**

**Multiple Actions**

Chain multiple actions together:

**def **complete\_interaction\(self, args, raw\_data\):

customer\_phone **= **args.get\("phone"\)

**return **\(

SwaigFunctionResult\("I've completed your request"\)

.update\_global\_data\(\{"interaction\_complete": True\}\)

.send\_sms\(

to\_number**=**customer\_phone, 

from\_number**=**"\+15559876543", 

body**=**"Thank you for calling\!" 

\)

\)

**4.21.11**

**Action Reference**

**4.21.11.1**

**Call Control Actions**

**Method**

**Description**

.connect\(dest, final, from\_addr\)

Transfer call to another number or SIP URI

.hangup\(\)

End the call

.hold\(timeout\)

Put caller on hold \(max 900 seconds\)

.send\_sms\(to, from, body, media\)

Send SMS message

.record\_call\(...\)

Start call recording

.stop\_record\_call\(...\)

Stop call recording

.pay\(...\)

Process payment

.execute\_swml\(doc\)

Execute raw SWML document

118

4. SWAIG Functions

**4.21.11.2 Speech & Audio Actions**

**Method**

**Description**

.say\(text\)

Have AI speak specific text

.stop\(\)

Stop AI from speaking

.play\_background\_file\(url\)

Play background audio

.stop\_background\_file\(\)

Stop background audio

.user\_input\(text\)

Inject text as user speech

.wait\_for\_user\(\)

Wait for user to speak

**4.21.11.3 Context & Workflow Actions**

**Method**

**Description**

.switch\_context\(prompt\)

Advanced context switch with new prompts

.swml\_change\_context\(ctx\)

Switch to named context

.swml\_change\_step\(step\)

Change to specific workflow step

**4.21.11.4 Data Management Actions**

**Method**

**Description**

.update\_global\_data\(data\)

Set global session data

.unset\_global\_data\(keys\)

Remove keys from global data

.set\_meta\_data\(func, data\)

Set function-specific metadata

.unset\_meta\_data\(func, keys\)

Remove function metadata keys

**4.21.11.5**

**AI Behavior Actions**

**Method**

**Description**

.toggle\_functions\(funcs\)

Enable/disable specific functions

.settings\(config\)

Modify AI settings dynamically

.end\_of\_speech\_timeout\(ms\)

Adjust speech timeout

.speech\_event\_timeout\(ms\)

Adjust speech event timeout

.back\_to\_back\_functions\(val\)

Control sequential function execution

.extensive\_data\(enabled\)

Enable extended data in webhooks

**4.21.11.6**

**Events**

**Method**

**Description**

.user\_event\(data\)

Fire custom event to application

119

4. SWAIG Functions

**4.22**

**DataMap**

**Summary**: DataMap provides serverless API integration - define functions that call REST APIs directly from SignalWire’s infrastructure without running code on your server. 

**4.22.1 When to Use DataMap**

**Use Handler Functions When**

**Use DataMap When**

Complex business logic

Simple REST API calls

Database access needed

No custom logic required

Multi-step processing

Want serverless deployment

External service integration with custom

Pattern-based responses

handling

Variable substitution only

**4.22.2**

**DataMap Flow**

**DataMap Execution Steps:**

1. **AI decides to call function**

• Function: get\_weather

• Args: \{"city": "Seattle"\}

2. **SignalWire executes DataMap **\(no webhook to your server\!\)

• GET https://api.weather.com?city=Seattle

3. **API response processed**

• Response: \{"temp": 65, "condition": "cloudy"\}

4. **Output template filled**

• Result: “Weather in Seattle: 65 degrees, cloudy” 

**4.22.3**

**Basic DataMap**

from signalwire\_agents import AgentBase

from signalwire\_agents.core.data\_map import DataMap

from signalwire\_agents.core.function\_result import SwaigFunctionResult **class **WeatherAgent\(AgentBase\):

**def \_\_init\_\_**\(self\):

super\(\). **\_\_init\_\_**\(name**=**"weather-agent"\)

self.add\_language\("English", "en-US", "rime.spore"\)

*\# Create DataMap*

weather\_dm **= **\(

DataMap\("get\_weather"\)

.description\("Get current weather for a city"\)

.parameter\("city", "string", "City name", required**=**True\)

.webhook\("GET", "https://api.weather.com/v1/current?key=API\_KEY&q=$\{enc:args.city\}"\)

.output\(SwaigFunctionResult\(

"The weather in $**\{args.city\} **is $**\{response.current.condition.text\}**, " 

"$**\{response.current.temp\_f\} **degrees Fahrenheit" 

\)\)

\)

*\# Register it*

self.register\_swaig\_function\(weather\_dm.to\_swaig\_function\(\)\)

120

4. SWAIG Functions

**4.22.4 Variable Substitution**

DataMap supports these variable patterns:

**Pattern**

**Description**

$\{args.param\}

Function argument value

$\{enc:args.param\}

URL-encoded argument \(use in webhook URLs\)

$\{lc:args.param\}

Lowercase argument value

$\{fmt\_ph:args.phone\}

Format as phone number

$\{response.field\}

API response field

$\{response.arr\[0\]\}

Array element in response

$\{global\_data.key\}

Global session data

$\{meta\_data.key\}

Call metadata

**4.22.4.1 Chained Modifiers**

Modifiers are applied right-to-left:

**Pattern**

**Result**

$\{enc:lc:args.param\}

First lowercase, then URL encode

$\{lc:enc:args.param\}

First URL encode, then lowercase

**4.22.4.2**

**Examples**

**Pattern**

**Result**

$\{args.city\}

“Seattle” \(in body/output\)

$\{enc:args.city\}

“Seattle” URL-encoded \(in URLs\)

$\{lc:args.city\}

“seattle” \(lowercase\)

$\{enc:lc:args.city\}

“seattle” lowercased then URL-encoded

$\{fmt\_ph:args.phone\}

“\+1 \(555\) 123-4567” 

$\{response.temp\}

“65” 

$\{response.items\[0\].name\}

“First item” 

$\{global\_data.user\_id\}

“user123” 

**4.22.5**

**DataMap Builder Methods**

**4.22.5.1**

**description\(\) / purpose\(\)**

Set the function description:

DataMap\("my\_function"\)

.description\("Look up product information by SKU"\)

121

4. SWAIG Functions

**4.22.5.2 parameter\(\)**

Add a function parameter:

.parameter\("sku", "string", "Product SKU code", required**=**True\)

.parameter\("include\_price", "boolean", "Include pricing info", required**=**False\)

.parameter\("category", "string", "Filter by category", enum**=**\["electronics", "clothing", "food"\]\) **4.22.5.3 webhook\(\)**

Add an API call:

*\#\# GET request*

.webhook\("GET", "https://api.example.com/products?sku=$\{enc:args.sku\}"\)

*\#\# POST request*

.webhook\("POST", "https://api.example.com/search"\)

*\#\# With headers*

.webhook\("GET", "https://api.example.com/data", headers**=**\{"Authorization": "Bearer $**\{global\_data.api\_key\}**"\}\) **4.22.5.4 body\(\)**

Set request body for POST/PUT:

.webhook\("POST", "https://api.example.com/search"\)

.body\(\{

"query": "$**\{args.search\_term\}**", 

"limit": 5

\}\)

**4.22.5.5**

**output\(\)**

Set the response for a webhook:

.output\(SwaigFunctionResult\(

"Found product: $**\{response.name\}**. Price: $$**\{response.price\}**" 

\)\)

**4.22.5.6**

**fallback\_output\(\)**

Set fallback if all webhooks fail:

.fallback\_output\(SwaigFunctionResult\(

"Sorry, the service is currently unavailable" 

\)\)

**4.22.6**

**Complete Example**

*\#\!/usr/bin/env python3*

*\#\# weather\_datamap\_agent.py - Weather agent using DataMap*

from signalwire\_agents import AgentBase

from signalwire\_agents.core.data\_map import DataMap

from signalwire\_agents.core.function\_result import SwaigFunctionResult **class **WeatherAgent\(AgentBase\):

**def \_\_init\_\_**\(self\):

super\(\). **\_\_init\_\_**\(name**=**"weather-agent"\)

self.add\_language\("English", "en-US", "rime.spore"\) 122

4. SWAIG Functions

self.prompt\_add\_section\("Role", "You help users check the weather."\) weather\_dm **= **\(

DataMap\("get\_weather"\)

.description\("Get current weather conditions for a city"\)

.parameter\("city", "string", "City name", required**=**True\)

.webhook\(

"GET", 

"https://api.weatherapi.com/v1/current.json" 

"?key=YOUR\_API\_KEY&q=$\{enc:args.city\}" 

\)

.output\(SwaigFunctionResult\(

"Current weather in $**\{args.city\}**: " 

"$**\{response.current.condition.text\}**, " 

"$**\{response.current.temp\_f\} **degrees Fahrenheit" 

\)\)

.fallback\_output\(SwaigFunctionResult\(

"Sorry, I couldn't get weather data for $**\{args.city\}**" 

\)\)

\)

self.register\_swaig\_function\(weather\_dm.to\_swaig\_function\(\)\)

**if **\_\_name\_\_ **== **"\_\_main\_\_":

agent **= **WeatherAgent\(\)

agent.run\(\)

**4.22.7**

**DataMap Best Practices**

**DO: **- Use for simple API integrations - Set fallback\_output for resilience - Use error\_keys to detect API errors -

Test with swaig-test before deploying

**DON’T: **- Put API keys directly in URLs \(use secure storage\) - Use for complex multi-step logic - Forget to handle all error cases - Assume API responses will always have expected structure 123

4. SWAIG Functions

**4.23**

**Native Functions**

**Summary**: Native functions are built-in SignalWire capabilities that can be enabled without writing code. They provide common operations like web search and debugging. 

**4.23.1 What Are Native Functions? **

Native functions run directly on SignalWire’s platform. Enable them to give the AI access to built-in capabilities without creating handlers. 

**Handler Function**

**Native Function**

You define handler

SignalWire provides

Runs on your server

Runs on SignalWire

Custom logic

Pre-built behavior

**Available Native Functions:**

• web\_search - Search the web

• debug - Debug mode for testing

**4.23.2**

**Enabling Native Functions**

Enable native functions in the constructor:

from signalwire\_agents import AgentBase

**class **MyAgent\(AgentBase\):

**def \_\_init\_\_**\(self\):

super\(\). **\_\_init\_\_**\(

name**=**"my-agent", 

native\_functions**=**\["web\_search"\]

*\# Enable web search*

\)

self.add\_language\("English", "en-US", "rime.spore"\) **4.23.3**

**Web Search Function**

Enable web search to let the AI look up information:

**class **ResearchAgent\(AgentBase\):

**def \_\_init\_\_**\(self\):

super\(\). **\_\_init\_\_**\(

name**=**"research-agent", 

native\_functions**=**\["web\_search"\]

\)

self.add\_language\("English", "en-US", "rime.spore"\) self.prompt\_add\_section\(

"Role", 

"You are a research assistant. Search the web to answer questions." 

\)

The AI can now search the web to find answers to caller questions. 

124

4. SWAIG Functions

**4.23.4 Debug Function**

Enable debug mode for development and testing:

**class **DebugAgent\(AgentBase\):

**def \_\_init\_\_**\(self\):

super\(\). **\_\_init\_\_**\(

name**=**"debug-agent", 

native\_functions**=**\["debug"\]

\)

self.add\_language\("English", "en-US", "rime.spore"\) The debug function provides diagnostic information during testing. 

**4.23.5**

**Call Transfers**

For call transfers, use SwaigFunctionResult.connect\(\) in a custom handler function - there is no native transfer function:

from signalwire\_agents import AgentBase, SwaigFunctionResult

**class **TransferAgent\(AgentBase\):

DEPARTMENTS **= **\{

"sales": "\+15551111111", 

"support": "\+15552222222", 

"billing": "\+15553333333" 

\}

**def \_\_init\_\_**\(self\):

super\(\). **\_\_init\_\_**\(name**=**"transfer-agent"\)

self.add\_language\("English", "en-US", "rime.spore"\) self.prompt\_add\_section\(

"Role", 

"You are a receptionist. Transfer callers to the appropriate department." 

\)

self.define\_tool\(

name**=**"transfer\_call", 

description**=**"Transfer the call to a department", 

parameters**=**\{

"type": "object", 

"properties": \{

"department": \{

"type": "string", 

"description": "Department to transfer to", 

"enum": \["sales", "support", "billing"\]

\}

\}, 

"required": \["department"\]

\}, 

handler**=**self.transfer\_call

\)

**def **transfer\_call\(self, args, raw\_data\):

department **= **args.get\("department"\)

number **= **self.DEPARTMENTS.get\(department\)

**if not **number:

**return **SwaigFunctionResult\("Invalid department"\)

**return **\(

SwaigFunctionResult\(f"Transferring you to **\{**department**\}**"\)

.connect\(number, final**=**True\)

\)

125

4. SWAIG Functions

**4.23.6 Combining Native and Custom Functions**

Use native functions alongside your custom handlers:

from signalwire\_agents import AgentBase, SwaigFunctionResult

**class **HybridAgent\(AgentBase\):

**def \_\_init\_\_**\(self\):

super\(\). **\_\_init\_\_**\(

name**=**"hybrid-agent", 

native\_functions**=**\["web\_search"\]

*\# Native*

\)

self.add\_language\("English", "en-US", "rime.spore"\)

*\# Custom function alongside native ones*

self.define\_tool\(

name**=**"check\_account", 

description**=**"Look up customer account information", parameters**=**\{

"type": "object", 

"properties": \{

"account\_id": \{

"type": "string", 

"description": "Account ID" 

\}

\}, 

"required": \["account\_id"\]

\}, 

handler**=**self.check\_account

\)

self.prompt\_add\_section\(

"Role", 

"You are a customer service agent. " 

"You can check accounts and search the web for information." 

\)

**def **check\_account\(self, args, raw\_data\):

account\_id **= **args.get\("account\_id"\)

**return **SwaigFunctionResult\(f"Account **\{**account\_id**\} **is active"\) **4.23.7**

**When to Use Native vs Custom Functions**

**Scenario**

**Recommendation**

Web search capability

Use web\_search native function

Development testing

Use debug native function

Transfer to phone number

Use SwaigFunctionResult.connect\(\) in custom handler

Transfer to SIP address

Use SwaigFunctionResult.connect\(\) in custom handler

Custom business logic

Use define\_tool\(\) with handler

Database lookups

Use define\_tool\(\) with handler

**4.23.8**

**Native Functions Reference**

**Function**

**Description**

**Use Case**

web\_search

Search the web

Answer general questions

debug

Debug information

Development/testing

126

4. SWAIG Functions

**4.23.9 Next Steps**

You’ve now learned all about SWAIG functions. Next, explore Skills to add pre-built capabilities to your agents. 

127

**Chapter 5**

**Skills**

**Summary**: Skills are modular, reusable capabilities that add functions, prompts, and integrations to your agents without custom code. 

**5.1 What You’ll Learn**

This chapter covers the skills system:

1. **Understanding Skills **- What skills are and how they work 2. **Built-in Skills **- Pre-built skills available in the SDK

3. **Adding Skills **- How to add skills to your agents

4. **Custom Skills **- Creating your own skills

5. **Skill Configuration **- Parameters and advanced options

**5.2**

**What Are Skills? **

Skills are pre-packaged capabilities that add:

• **Functions **- SWAIG tools the AI can call

• **Prompts **- Instructions for how to use the skill

• **Hints **- Speech recognition keywords

• **Global Data **- Variables available throughout the call

**Without Skills**

**With Skills**

Write weather function

self.add\_skill\("weather"\)

Add API integration

Write prompts

Done\! 

Add speech hints

Handle errors

128

5. Skills

**5.3 Quick Start**

Add a skill in one line:

from signalwire\_agents import AgentBase

**class **MyAgent\(AgentBase\):

**def \_\_init\_\_**\(self\):

super\(\). **\_\_init\_\_**\(name**=**"my-agent"\)

self.add\_language\("English", "en-US", "rime.spore"\)

*\# Add datetime capability*

self.add\_skill\("datetime"\)

*\# Add math capability*

self.add\_skill\("math"\)

self.prompt\_add\_section\(

"Role", 

"You are a helpful assistant that can tell time and do math." 

\)

**5.4 Available Built-in Skills**

**Skill**

**Description**

datetime

Get current date and time

math

Perform calculations

web\_search

Search the web \(requires API key\)

wikipedia\_search

Search Wikipedia

weather\_api

Get weather information

joke

Tell jokes

play\_background\_file

Play audio files

swml\_transfer

Transfer calls to SWML endpoints

datasphere

Search DataSphere documents

native\_vector\_search

Local vector search

**5.5**

**Chapter Contents**

**Section**

**Description**

Understanding Skills

How skills work internally

Built-in Skills

Reference for included skills

Adding Skills

How to use skills in your agents

Custom Skills

Creating your own skills

Skill Configuration

Parameters and advanced options

129

5. Skills

**5.6 Skills vs Functions**

**Aspect**

**SWAIG Function**

**Skill**

**Scope**

Single function

Multiple functions \+

prompts \+ hints

**Reusability**

Per-agent

Across all agents

**Setup**

define\_tool\(\)

add\_skill\(\)

**Customization**

Full control

Parameters only

**Maintenance**

You maintain

SDK maintains

**5.7 When to Use Skills**

**5.7.1**

**Use Built-in Skills When:**

• Standard capability needed \(datetime, search, etc.\)

• Want quick setup without custom code

• Need tested, maintained functionality

**5.7.2**

**Create Custom Skills When:**

• Reusing capability across multiple agents

• Want to share functionality with team/community

• Packaging complex integrations

**5.7.3**

**Use SWAIG Functions When:**

• One-off custom logic

• Agent-specific business rules

• Need full control over implementation

**5.8**

**Complete Example**

*\#\!/usr/bin/env python3*

*\# assistant\_agent.py - Agent with multiple skills*

from signalwire\_agents import AgentBase

**class **AssistantAgent\(AgentBase\):

**def \_\_init\_\_**\(self\):

super\(\). **\_\_init\_\_**\(name**=**"assistant"\)

self.add\_language\("English", "en-US", "rime.spore"\)

*\# Add multiple skills*

self.add\_skill\("datetime"\)

self.add\_skill\("math"\)

self.prompt\_add\_section\(

"Role", 

"You are a helpful assistant named Alex." 

\)

self.prompt\_add\_section\(

"Capabilities", 

body**=**"You can help with:", 

bullets**=**\[

"Telling the current date and time", 

"Performing math calculations" 

\]

\)

130

5. Skills

**if **\_\_name\_\_ **== **"\_\_main\_\_":

agent **= **AssistantAgent\(\)

agent.run\(\)

Let’s start by understanding how skills work internally. 

**5.9**

**Skill Architecture**

**5.9.1 SkillBase \(Abstract Base Class\)**

**Required Methods: **- setup\(\) - Initialize the skill - register\_tools\(\) - Register SWAIG functions **Optional Methods: **- get\_hints\(\) - Speech recognition hints - get\_global\_data\(\) - Session data - get\_prompt\_sections\(\) - Prompt additions - cleanup\(\) - Resource cleanup

**5.9.2**

**SkillRegistry \(Discovery & Loading\)**

• Discovers skills from directories

• Loads skills on-demand \(lazy loading\)

• Validates requirements \(packages, env vars\)

• Supports external skill paths

**5.10 How Skills Work**

When you call add\_skill\(\):

┌─────────────────────────────────────────────────────────────────────────────┐

│

Skill Loading Process

│

├─────────────────────────────────────────────────────────────────────────────┤

│

│

│

1. Agent calls add\_skill\("datetime"\)

│

│

│

│

│

▼

│

│

2. SkillRegistry looks up skill class

│

│

• Checks already loaded skills

│

│

• Searches built-in skills directory

│

│

• Searches external paths

│

│

│

│

│

▼

│

│

3. SkillManager instantiates skill

│

│

• Creates skill instance with agent reference

│

│

• Passes configuration parameters

│

│

│

│

│

▼

│

│

4. Skill setup\(\) is called

│

│

• Validates required packages

│

│

• Validates environment variables

│

│

• Initializes APIs/connections

│

│

│

│

│

▼

│

│

5. Skill register\_tools\(\) is called

│

│

• Registers SWAIG functions with agent

│

│

│

│

│

▼

│

│

6. Skill contributions applied

│

│

• Prompts added to agent

│

│

• Hints added for speech recognition

│

│

• Global data merged

│

│

│

└─────────────────────────────────────────────────────────────────────────────┘

131

5. Skills

**5.11 Skill Directory Structure**

Built-in skills live in the SDK:

signalwire\_agents/

└── skills/

├── datetime/

│

├── \_\_init\_\_.py

│

└── skill.py

├── math/

│

├── \_\_init\_\_.py

│

└── skill.py

├── web\_search/

│

├── \_\_init\_\_.py

│

├── skill.py

│

└── requirements.txt

└── ... 

Each skill directory contains:

**File**

**Purpose**

skill.py

Skill class implementation

\_\_init\_\_.py

Python package marker

requirements.txt

Optional extra dependencies

**5.12**

**SkillBase Class**

All skills inherit from SkillBase:

from signalwire\_agents.core.skill\_base import SkillBase

from signalwire\_agents.core.function\_result import SwaigFunctionResult **class **MySkill\(SkillBase\):

*\# Required class attributes*

SKILL\_NAME **= **"my\_skill" 

SKILL\_DESCRIPTION **= **"Does something useful" 

SKILL\_VERSION **= **"1.0.0" 

*\# Optional requirements*

REQUIRED\_PACKAGES **= **\[\]

*\# Python packages needed*

REQUIRED\_ENV\_VARS **= **\[\]

*\# Environment variables needed*

*\# Multi-instance support*

SUPPORTS\_MULTIPLE\_INSTANCES **= **False

**def **setup\(self\) **-> **bool:

*"""Initialize the skill. Return True if successful.""" *

**return **True

**def **register\_tools\(self\) **-> **None:

*"""Register SWAIG tools with the agent.""" *

self.define\_tool\(

name**=**"my\_function", 

description**=**"Does something", 

parameters**=**\{\}, 

handler**=**self.my\_handler

\)

**def **my\_handler\(self, args, raw\_data\):

*"""Handle function calls.""" *

**return **SwaigFunctionResult\("Result"\)

132

5. Skills

**5.13 Skill Lifecycle**

Discover → Load → Setup → Register → Active → Cleanup

**Stage**

**Description**

**Discover**

Registry finds skill class in directory

**Load**

Skill class is imported and validated

**Setup**

setup\(\) validates requirements, initializes resources

**Register**

register\_tools\(\) adds functions to agent

**Active**

Skill is ready, functions can be called

**Cleanup**

cleanup\(\) releases resources on shutdown

**5.14 Skill Contributions**

Skills can contribute to the agent in multiple ways:

**5.14.1**

**1. Tools \(Functions\)**

**def **register\_tools\(self\) **-> **None:

self.define\_tool\(

name**=**"get\_time", 

description**=**"Get current time", 

parameters**=**\{

"timezone": \{

"type": "string", 

"description": "Timezone name" 

\}

\}, 

handler**=**self.get\_time\_handler

\)

**5.14.2**

**2. Prompt Sections**

**def **get\_prompt\_sections\(self\):

**return **\[

\{

"title": "Time Information", 

"body": "You can tell users the current time.", 

"bullets": \[

"Use get\_time for time queries", 

"Support multiple timezones" 

\]

\}

\]

**5.14.3**

**3. Speech Hints**

**def **get\_hints\(self\):

**return **\["time", "date", "clock", "timezone"\]

133

5. Skills

**5.14.4 4. Global Data**

**def **get\_global\_data\(self\):

**return **\{

"datetime\_enabled": True, 

"default\_timezone": "UTC" 

\}

**5.15**

**Skill Discovery Paths**

Skills are discovered from multiple locations in priority order:

**Priority**

**Source**

**Example**

1

Already registered skills \(in memory\)

-

2

Entry points \(pip installed packages\)

entry\_points=\{' 

signalwire\_-

agents.skills':

\['my\_skill = pkg:Skill'\]\}

3

Built-in skills directory

signalwire\_agents/skills/

4

External paths

skill\_registry.add\_skill

\_directory\(' 

/opt/custom\_skills'\)

5

Environment variable paths

SIGNALWIRE\_SKILL\_PATHS=/p

ath1:/path2

**5.16**

**Lazy Loading**

Skills are loaded on-demand to minimize startup time:

*\# Skill NOT loaded yet*

agent **= **MyAgent\(\)

*\# Skill loaded when first referenced*

agent.add\_skill\("datetime"\)

*\# datetime skill loaded here*

*\# Already loaded, reused*

agent.add\_skill\("datetime"\)

*\# Uses cached class*

**5.17**

**Multi-Instance Skills**

Some skills support multiple instances with different configurations: **class **MySkill\(SkillBase\):

SUPPORTS\_MULTIPLE\_INSTANCES **= **True

**def **get\_instance\_key\(self\) **-> **str:

*\# Unique key for this instance*

tool\_name **= **self.params.get\('tool\_name', self.SKILL\_NAME\)

**return **f" **\{**self**. **SKILL\_NAME**\}**\_**\{**tool\_name**\}**" 

Usage:

*\# Add two instances with different configs*

agent.add\_skill\("web\_search", \{

"tool\_name": "search\_news", 

"search\_engine\_id": "NEWS\_ENGINE\_ID", 

"api\_key": "KEY" 

134

5. Skills

\}\)

agent.add\_skill\("web\_search", \{

"tool\_name": "search\_docs", 

"search\_engine\_id": "DOCS\_ENGINE\_ID", 

"api\_key": "KEY" 

\}\)

135

5. Skills

**5.18 Built-in Skills**

**Summary**: The SDK includes ready-to-use skills for common tasks like datetime, math, web search, and more. Each skill adds specific capabilities to your agents. 

**5.18.1 Available Skills**

**Skill**

**Description**

**Requirements**

datetime

Date/time information

pytz

math

Mathematical calculations

\(none\)

web\_search

Web search via Google API

API key

wikipedia\_search

Wikipedia lookups

\(none\)

weather\_api

Weather information

API key

joke

Tell jokes

\(none\)

play\_background\_file

Play audio files

\(none\)

swml\_transfer

Transfer to SWML endpoint

\(none\)

datasphere

DataSphere document search

API credentials

native\_vector\_search

Local vector search

search extras

**5.18.2**

**datetime**

Get current date \(today\) and time information with timezone support. 

**Functions: **- get\_current\_time - Get current time in a timezone - get\_current\_date - Get today’s date **Requirements: **pytz package

from signalwire\_agents import AgentBase

**class **TimeAgent\(AgentBase\):

**def \_\_init\_\_**\(self\):

super\(\). **\_\_init\_\_**\(name**=**"time-agent"\)

self.add\_language\("English", "en-US", "rime.spore"\) self.add\_skill\("datetime"\)

self.prompt\_add\_section\(

"Role", 

"You help users with date and time information." 

\)

**5.18.3**

**math**

Perform mathematical calculations. 

**Functions: **- calculate - Evaluate mathematical expressions

**Requirements: **None

from signalwire\_agents import AgentBase

**class **CalculatorAgent\(AgentBase\):

**def \_\_init\_\_**\(self\):

super\(\). **\_\_init\_\_**\(name**=**"calculator"\)

self.add\_language\("English", "en-US", "rime.spore"\) self.add\_skill\("math"\)

136

5. Skills

self.prompt\_add\_section\(

"Role", 

"You are a calculator that helps with math." 

\)

**5.18.4 web\_search**

Search the web using Google Custom Search API with quality filtering. 

**Functions: **- web\_search - Search the web

**Requirements: **- Google Custom Search API key - Search Engine ID

from signalwire\_agents import AgentBase

**class **SearchAgent\(AgentBase\):

**def \_\_init\_\_**\(self\):

super\(\). **\_\_init\_\_**\(name**=**"search-agent"\)

self.add\_language\("English", "en-US", "rime.spore"\) self.add\_skill\("web\_search", \{

"api\_key": "YOUR\_GOOGLE\_API\_KEY", 

"search\_engine\_id": "YOUR\_SEARCH\_ENGINE\_ID", 

"num\_results": 3

\}\)

self.prompt\_add\_section\(

"Role", 

"You search the web to answer questions." 

\)

**Parameters:**

**Parameter**

**Type**

**Description**

**Default**

api\_key

string

Google API key

Required

search\_engine\_id

string

Search engine ID

Required

num\_results

integer

Results to return

3

min\_quality\_score

number

Quality threshold

0.3

**5.18.5**

**wikipedia\_search**

Search Wikipedia for information. 

**Functions: **- search\_wikipedia - Search Wikipedia articles

**Requirements: **None

from signalwire\_agents import AgentBase

**class **WikiAgent\(AgentBase\):

**def \_\_init\_\_**\(self\):

super\(\). **\_\_init\_\_**\(name**=**"wiki-agent"\)

self.add\_language\("English", "en-US", "rime.spore"\) self.add\_skill\("wikipedia\_search"\)

self.prompt\_add\_section\(

"Role", 

"You look up information on Wikipedia." 

\)

137

5. Skills

**5.18.6 weather\_api**

Get weather information for locations. 

**Functions: **- get\_weather - Get current weather

**Requirements: **Weather API key

from signalwire\_agents import AgentBase

**class **WeatherAgent\(AgentBase\):

**def \_\_init\_\_**\(self\):

super\(\). **\_\_init\_\_**\(name**=**"weather-agent"\)

self.add\_language\("English", "en-US", "rime.spore"\) self.add\_skill\("weather\_api", \{

"api\_key": "YOUR\_WEATHER\_API\_KEY" 

\}\)

self.prompt\_add\_section\(

"Role", 

"You provide weather information." 

\)

**5.18.7**

**joke**

Tell jokes to users. 

**Functions: **- tell\_joke - Get a random joke

**Requirements: **None

from signalwire\_agents import AgentBase

**class **FunAgent\(AgentBase\):

**def \_\_init\_\_**\(self\):

super\(\). **\_\_init\_\_**\(name**=**"fun-agent"\)

self.add\_language\("English", "en-US", "rime.spore"\) self.add\_skill\("joke"\)

self.prompt\_add\_section\(

"Role", 

"You are a fun assistant that tells jokes." 

\)

**5.18.8**

**play\_background\_file**

Play audio files during the call. 

**Functions: **- play\_background\_file - Start playing audio - stop\_background\_file - Stop playing audio **Requirements: **None

from signalwire\_agents import AgentBase

**class **MusicAgent\(AgentBase\):

**def \_\_init\_\_**\(self\):

super\(\). **\_\_init\_\_**\(name**=**"music-agent"\)

self.add\_language\("English", "en-US", "rime.spore"\) self.add\_skill\("play\_background\_file", \{

"audio\_url": "https://example.com/music.mp3" 

\}\)

138

5. Skills

**5.18.9 swml\_transfer**

Transfer calls to another SWML endpoint. 

**Functions: **- transfer\_to\_swml - Transfer to SWML URL

**Requirements: **None

from signalwire\_agents import AgentBase

**class **TransferAgent\(AgentBase\):

**def \_\_init\_\_**\(self\):

super\(\). **\_\_init\_\_**\(name**=**"transfer-agent"\)

self.add\_language\("English", "en-US", "rime.spore"\) self.add\_skill\("swml\_transfer", \{

"swml\_url": "https://your-server.com/other-agent", 

"description": "Transfer to specialist" 

\}\)

**5.18.10**

**datasphere**

Search SignalWire DataSphere documents. 

**Functions: **- search\_datasphere - Search uploaded documents

**Requirements: **DataSphere API credentials

from signalwire\_agents import AgentBase

**class **KnowledgeAgent\(AgentBase\):

**def \_\_init\_\_**\(self\):

super\(\). **\_\_init\_\_**\(name**=**"knowledge-agent"\)

self.add\_language\("English", "en-US", "rime.spore"\) self.add\_skill\("datasphere", \{

"space\_name": "your-space", 

"project\_id": "YOUR\_PROJECT\_ID", 

"api\_token": "YOUR\_API\_TOKEN" 

\}\)

**5.18.11**

**native\_vector\_search**

Local vector search using .swsearch index files. 

**Functions: **- search\_knowledge - Search local vector index

**Requirements: **Search extras installed \(pip install signalwire-agents\[search\]\) from signalwire\_agents import AgentBase

**class **LocalSearchAgent\(AgentBase\):

**def \_\_init\_\_**\(self\):

super\(\). **\_\_init\_\_**\(name**=**"local-search"\)

self.add\_language\("English", "en-US", "rime.spore"\) self.add\_skill\("native\_vector\_search", \{

"index\_path": "/path/to/knowledge.swsearch", 

"tool\_name": "search\_docs" 

\}\)

139

5. Skills

**5.18.12 Skills Summary Table**

**Skill**

**Functions**

**API Required**

**Multi-Instance**

datetime

2

No

No

math

1

No

No

web\_search

1

Yes

Yes

wikipedia\_search

1

No

No

weather\_api

1

Yes

No

joke

1

No

No

play\_background\_file

2

No

No

swml\_transfer

1

No

Yes

datasphere

1

Yes

Yes

native\_vector\_search

1

No

Yes

140

5. Skills

**5.19 Adding Skills**

**Summary**: Add skills to your agents with add\_skill\(\). Pass configuration parameters to customize behavior. 

**5.19.1 Basic Usage**

Add a skill with no configuration:

from signalwire\_agents import AgentBase

**class **MyAgent\(AgentBase\):

**def \_\_init\_\_**\(self\):

super\(\). **\_\_init\_\_**\(name**=**"my-agent"\)

self.add\_language\("English", "en-US", "rime.spore"\)

*\# Add skill with default settings*

self.add\_skill\("datetime"\)

**5.19.2**

**With Configuration**

Pass parameters as a dictionary:

from signalwire\_agents import AgentBase

**class **MyAgent\(AgentBase\):

**def \_\_init\_\_**\(self\):

super\(\). **\_\_init\_\_**\(name**=**"my-agent"\)

self.add\_language\("English", "en-US", "rime.spore"\)

*\# Add skill with configuration*

self.add\_skill\("web\_search", \{

"api\_key": "YOUR\_API\_KEY", 

"search\_engine\_id": "YOUR\_ENGINE\_ID", 

"num\_results": 5

\}\)

**5.19.3**

**Method Chaining**

add\_skill\(\) returns self for chaining:

from signalwire\_agents import AgentBase

**class **MyAgent\(AgentBase\):

**def \_\_init\_\_**\(self\):

super\(\). **\_\_init\_\_**\(name**=**"my-agent"\)

self.add\_language\("English", "en-US", "rime.spore"\)

*\# Chain multiple skills*

\(self

.add\_skill\("datetime"\)

.add\_skill\("math"\)

.add\_skill\("joke"\)\)

141

5. Skills

**5.19.4 Multiple Skills**

Add as many skills as needed:

from signalwire\_agents import AgentBase

**class **AssistantAgent\(AgentBase\):

**def \_\_init\_\_**\(self\):

super\(\). **\_\_init\_\_**\(name**=**"assistant"\)

self.add\_language\("English", "en-US", "rime.spore"\)

*\# Add multiple capabilities*

self.add\_skill\("datetime"\)

self.add\_skill\("math"\)

self.add\_skill\("wikipedia\_search"\)

self.prompt\_add\_section\(

"Role", 

"You are a helpful assistant." 

\)

self.prompt\_add\_section\(

"Capabilities", 

body**=**"You can help with:", 

bullets**=**\[

"Date and time information", 

"Math calculations", 

"Wikipedia lookups" 

\]

\)

**5.19.5**

**Checking Loaded Skills**

*\#\# Check if skill is loaded*

**if **agent.has\_skill\("datetime"\):

print\("Datetime skill is active"\)

*\#\# List all loaded skills*

skills **= **agent.list\_skills\(\)

print\(f"Loaded skills: **\{**skills**\}**"\)

**5.19.6**

**Removing Skills**

*\#\# Remove a skill*

agent.remove\_skill\("datetime"\)

**5.19.7**

**Multi-Instance Skills**

Some skills support multiple instances:

from signalwire\_agents import AgentBase

**class **MultiSearchAgent\(AgentBase\):

**def \_\_init\_\_**\(self\):

super\(\). **\_\_init\_\_**\(name**=**"multi-search"\)

self.add\_language\("English", "en-US", "rime.spore"\)

*\# First search instance for news*

self.add\_skill\("web\_search", \{

"tool\_name": "search\_news", 

"api\_key": "YOUR\_API\_KEY", 

"search\_engine\_id": "NEWS\_ENGINE\_ID" 

\}\)

142

5. Skills

*\# Second search instance for documentation*

self.add\_skill\("web\_search", \{

"tool\_name": "search\_docs", 

"api\_key": "YOUR\_API\_KEY", 

"search\_engine\_id": "DOCS\_ENGINE\_ID" 

\}\)

self.prompt\_add\_section\(

"Role", 

"You can search news and documentation separately." 

\)

**5.19.8**

**SWAIG Fields**

Add extra SWAIG metadata to skill functions:

self.add\_skill\("datetime", \{

"swaig\_fields": \{

"fillers": \{

"en-US": \["Let me check the time..."\]

\}

\}

\}\)

**5.19.9**

**Error Handling**

Skills may fail to load:

**try**:

agent.add\_skill\("web\_search", \{

"api\_key": "invalid" 

\}\)

**except ** *ValueError * as e:

print\(f"Skill failed to load: **\{**e**\}**"\)

Common errors:

**Error**

**Cause**

**Solution**

Skill not found

Invalid skill name

Check spelling

Missing parameters

Required config not provided

Add required params

Package not installed

Missing Python dependency

Install with pip

Env var missing

Required environment variable

Set the variable

**5.19.10**

**Skills with Environment Variables**

Some skills read from environment variables:

import os

*\#\# Set API key via environment*

os.environ\["GOOGLE\_SEARCH\_API\_KEY"\] **= **"your-key" 

*\#\# Skill can read from env*

self.add\_skill\("web\_search", \{

"api\_key": os.environ\["GOOGLE\_SEARCH\_API\_KEY"\], 

"search\_engine\_id": "your-engine-id" 

\}\)

143

5. Skills

**5.19.11 Complete Example**

*\#\!/usr/bin/env python3*

*\#\# full\_featured\_agent.py - Agent with multiple configured skills* from signalwire\_agents import AgentBase

**class **FullFeaturedAgent\(AgentBase\):

**def \_\_init\_\_**\(self\):

super\(\). **\_\_init\_\_**\(name**=**"full-featured"\)

self.add\_language\("English", "en-US", "rime.spore"\)

*\# Simple skills \(no config needed\)*

self.add\_skill\("datetime"\)

self.add\_skill\("math"\)

self.prompt\_add\_section\(

"Role", 

"You are a versatile assistant named Alex." 

\)

self.prompt\_add\_section\(

"Capabilities", 

body**=**"You can help with:", 

bullets**=**\[

"Current date and time", 

"Math calculations" 

\]

\)

**if **\_\_name\_\_ **== **"\_\_main\_\_":

agent **= **FullFeaturedAgent\(\)

agent.run\(\)

**Note**: Skills like web\_search and joke require additional configuration or API keys. See the Built-in Skills section for details on each skill’s requirements. 

**5.19.12**

**Best Practices**

**DO: **- Add skills in **init **before prompt configuration - Use environment variables for API keys - Check skill availability with has\_skill\(\) if conditional - Update prompts to mention skill capabilities **DON’T: **- Hardcode API keys in source code - Add duplicate skills \(unless multi-instance\) - Assume skills are available without checking - Forget to handle skill loading errors 144

5. Skills

**5.20 Custom Skills**

**Summary**: Create your own skills by inheriting from SkillBase. Custom skills can be reused across agents and shared with others. 

**5.20.1 Skill Structure**

Create a directory with these files:

my\_custom\_skill/

\_\_init\_\_.py

\# Empty or exports

skill.py

\# Skill implementation

requirements.txt

\# Optional dependencies

**5.20.2**

**Basic Custom Skill**

*\#\# my\_custom\_skill/skill.py*

from typing import List, Dict, Any

from signalwire\_agents.core.skill\_base import SkillBase

from signalwire\_agents.core.function\_result import SwaigFunctionResult **class **GreetingSkill\(SkillBase\):

*"""A skill that provides personalized greetings""" *

*\# Required class attributes*

SKILL\_NAME **= **"greeting" 

SKILL\_DESCRIPTION **= **"Provides personalized greetings" 

SKILL\_VERSION **= **"1.0.0" 

*\# Optional requirements*

REQUIRED\_PACKAGES **= **\[\]

REQUIRED\_ENV\_VARS **= **\[\]

**def **setup\(self\) **-> **bool:

*"""Initialize the skill. Return True if successful.""" *

*\# Get configuration parameter with default*

self.greeting\_style **= **self.params.get\("style", "friendly"\) **return **True

**def **register\_tools\(self\) **-> **None:

*"""Register SWAIG tools with the agent.""" *

self.define\_tool\(

name**=**"greet\_user", 

description**=**"Generate a personalized greeting", 

parameters**=**\{

"name": \{

"type": "string", 

"description": "Name of the person to greet" 

\}

\}, 

handler**=**self.greet\_handler

\)

**def **greet\_handler\(self, args, raw\_data\):

*"""Handle greeting requests.""" *

name **= **args.get\("name", "friend"\)

**if **self.greeting\_style **== **"formal":

greeting **= **f"Good day, **\{**name**\}**. How may I assist you?" 

**else**:

greeting **= **f"Hey **\{**name**\}**\! Great to hear from you\!" 

**return **SwaigFunctionResult\(greeting\)

145

5. Skills

**5.20.3 Required Class Attributes**

**Attribute**

**Type**

**Description**

SKILL\_NAME

str

Unique identifier for the skill

SKILL\_DESCRIPTION

str

Human-readable description

SKILL\_VERSION

str

Semantic version \(default:

“1.0.0”\)

**Optional Attributes:**

**Attribute**

**Type**

**Description**

REQUIRED\_PACKAGES

List\[str\]

Python packages needed

REQUIRED\_ENV\_VARS

List\[str\]

Environment variables

needed

SUPPORTS\_MULTIPLE

bool

Allow multiple instances

**5.20.4**

**Required Methods**

**5.20.4.1 setup\(\)**

Initialize the skill and validate requirements:

**def **setup\(self\) **-> **bool:

*""" *

*Initialize the skill. *

*Returns:*

*True if setup successful, False otherwise*

*""" *

*\# Validate packages are installed*

**if not **self.validate\_packages\(\):

**return **False

*\# Validate environment variables*

**if not **self.validate\_env\_vars\(\):

**return **False

*\# Initialize from parameters*

self.api\_url **= **self.params.get\("api\_url", "https://api.example.com"\) self.timeout **= **self.params.get\("timeout", 30\)

*\# Any other initialization*

**return **True

**5.20.4.2**

**register\_tools\(\)**

Register SWAIG functions:

**def **register\_tools\(self\) **-> **None:

*"""Register all tools this skill provides.""" *

self.define\_tool\(

name**=**"my\_function", 

description**=**"Does something useful", 

parameters**=**\{

"param1": \{

"type": "string", 

"description": "First parameter" 

\}, 

"param2": \{

146

5. Skills

"type": "integer", 

"description": "Second parameter" 

\}

\}, 

handler**=**self.my\_handler

\)

*\# Register multiple tools if needed*

self.define\_tool\(

name**=**"another\_function", 

description**=**"Does something else", 

parameters**=**\{\}, 

handler**=**self.another\_handler

\)

**5.20.5**

**Optional Methods**

**5.20.5.1 get\_hints\(\)**

Provide speech recognition hints:

**def **get\_hints\(self\) **-> **List\[str\]:

*"""Return words to improve speech recognition.""" *

**return **\["greeting", "hello", "hi", "welcome"\]

**5.20.5.2 get\_prompt\_sections\(\)**

Add sections to the agent’s prompt:

**def **get\_prompt\_sections\(self\) **-> **List\[Dict\[str, Any\]\]:

*"""Return prompt sections for the agent.""" *

**return **\[

\{

"title": "Greeting Capability", 

"body": "You can greet users by name.", 

"bullets": \[

"Use greet\_user when someone introduces themselves", 

"Match the greeting style to the conversation tone" 

\]

\}

\]

**5.20.5.3**

**get\_global\_data\(\)**

Provide data for the agent’s global context:

**def **get\_global\_data\(self\) **-> **Dict\[str, Any\]:

*"""Return data to add to global context.""" *

**return **\{

"greeting\_skill\_enabled": True, 

"greeting\_style": self.greeting\_style

\}

**5.20.5.4**

**cleanup\(\)**

Release resources when skill is unloaded:

**def **cleanup\(self\) **-> **None:

*"""Clean up when skill is removed.""" *

*\# Close connections, release resources*

**if **hasattr\(self, "connection"\):

self.connection.close\(\)

147

5. Skills

**5.20.6 Parameter Schema**

Define parameters your skill accepts:

@classmethod

**def **get\_parameter\_schema\(cls\) **-> **Dict\[str, Dict\[str, Any\]\]:

*"""Define the parameters this skill accepts.""" *

*\# Start with base schema*

schema **= **super\(\).get\_parameter\_schema\(\)

*\# Add skill-specific parameters*

schema.update\(\{

"style": \{

"type": "string", 

"description": "Greeting style", 

"default": "friendly", 

"enum": \["friendly", "formal", "casual"\], 

"required": False

\}, 

"api\_key": \{

"type": "string", 

"description": "API key for external service", 

"required": True, 

"hidden": True, 

"env\_var": "MY\_SKILL\_API\_KEY" 

\}

\}\)

**return **schema

**5.20.7**

**Multi-Instance Skills**

Support multiple instances with different configurations:

**class **MultiInstanceSkill\(SkillBase\):

SKILL\_NAME **= **"multi\_search" 

SKILL\_DESCRIPTION **= **"Searchable with multiple instances" 

SKILL\_VERSION **= **"1.0.0" 

*\# Enable multiple instances*

SUPPORTS\_MULTIPLE\_INSTANCES **= **True

**def **get\_instance\_key\(self\) **-> **str:

*"""Return unique key for this instance.""" *

tool\_name **= **self.params.get\("tool\_name", self.SKILL\_NAME\) **return **f" **\{**self**. **SKILL\_NAME**\}**\_**\{**tool\_name**\}**" 

**def **setup\(self\) **-> **bool:

self.tool\_name **= **self.params.get\("tool\_name", "search"\) **return **True

**def **register\_tools\(self\) **-> **None:

*\# Use custom tool name*

self.define\_tool\(

name**=**self.tool\_name, 

description**=**"Search function", 

parameters**=**\{

"query": \{"type": "string", "description": "Search query"\}

\}, 

handler**=**self.search\_handler

\)

148

5. Skills

**5.20.8 Complete Example**

*\#\!/usr/bin/env python3*

*\#\# product\_search\_skill.py - Custom skill for product search*

from typing import List, Dict, Any

import requests

from signalwire\_agents.core.skill\_base import SkillBase

from signalwire\_agents.core.function\_result import SwaigFunctionResult **class **ProductSearchSkill\(SkillBase\):

*"""Search product catalog""" *

SKILL\_NAME **= **"product\_search" 

SKILL\_DESCRIPTION **= **"Search and lookup products in catalog" 

SKILL\_VERSION **= **"1.0.0" 

REQUIRED\_PACKAGES **= **\["requests"\]

REQUIRED\_ENV\_VARS **= **\[\]

SUPPORTS\_MULTIPLE\_INSTANCES **= **False

**def **setup\(self\) **-> **bool:

**if not **self.validate\_packages\(\):

**return **False

self.api\_url **= **self.params.get\("api\_url"\)

self.api\_key **= **self.params.get\("api\_key"\)

**if not **self.api\_url **or not **self.api\_key:

self.logger.error\("api\_url and api\_key are required"\)

**return **False

**return **True

**def **register\_tools\(self\) **-> **None:

self.define\_tool\(

name**=**"search\_products", 

description**=**"Search for products by name or category", parameters**=**\{

"query": \{

"type": "string", 

"description": "Search term" 

\}, 

"category": \{

"type": "string", 

"description": "Product category filter", 

"enum": \["electronics", "clothing", "home", "all"\]

\}

\}, 

handler**=**self.search\_handler

\)

self.define\_tool\(

name**=**"get\_product\_details", 

description**=**"Get details for a specific product", parameters**=**\{

"product\_id": \{

"type": "string", 

"description": "Product ID" 

\}

\}, 

handler**=**self.details\_handler

\)

**def **search\_handler\(self, args, raw\_data\):

query **= **args.get\("query", ""\)

category **= **args.get\("category", "all"\)

**try**:

response **= **requests.get\(

f" **\{**self**. **api\_url**\}**/search", 

149

5. Skills

params**=**\{"q": query, "cat": category\}, 

headers**=**\{"Authorization": f"Bearer **\{**self**. **api\_key**\}**"\}, timeout**=**10

\)

response.raise\_for\_status\(\)

data **= **response.json\(\)

products **= **data.get\("products", \[\]\)

**if not **products:

**return **SwaigFunctionResult\(f"No products found for ' **\{**query**\}**'"\) result **= **f"Found **\{**len\(products\)**\} **products:\\n" 

**for **p **in **products\[:5\]:

result **\+= **f"- **\{**p\['name'\]**\} **\($**\{**p\['price'\]**\}**\)\\n" 

**return **SwaigFunctionResult\(result\)

**except ** *Exception * as e:

self.logger.error\(f"Search failed: **\{**e**\}**"\)

**return **SwaigFunctionResult\("Product search is temporarily unavailable"\) **def **details\_handler\(self, args, raw\_data\):

product\_id **= **args.get\("product\_id"\)

**try**:

response **= **requests.get\(

f" **\{**self**. **api\_url**\}**/products/**\{**product\_id**\}**", headers**=**\{"Authorization": f"Bearer **\{**self**. **api\_key**\}**"\}, timeout**=**10

\)

response.raise\_for\_status\(\)

product **= **response.json\(\)

**return **SwaigFunctionResult\(

f" **\{**product\['name'\]**\}**: **\{**product\['description'\]**\}**. " 

f"Price: $**\{**product\['price'\]**\}**. In stock: **\{**product\['stock'\]**\}**" 

\)

**except ** *Exception * as e:

self.logger.error\(f"Details lookup failed: **\{**e**\}**"\) **return **SwaigFunctionResult\("Could not retrieve product details"\) **def **get\_hints\(self\) **-> **List\[str\]:

**return **\["product", "search", "find", "lookup", "catalog"\]

**def **get\_prompt\_sections\(self\) **-> **List\[Dict\[str, Any\]\]: **return **\[

\{

"title": "Product Search", 

"body": "You can search the product catalog.", 

"bullets": \[

"Use search\_products to find products", 

"Use get\_product\_details for specific items" 

\]

\}

\]

@classmethod

**def **get\_parameter\_schema\(cls\) **-> **Dict\[str, Dict\[str, Any\]\]: schema **= **super\(\).get\_parameter\_schema\(\)

schema.update\(\{

"api\_url": \{

"type": "string", 

"description": "Product catalog API URL", 

"required": True

\}, 

"api\_key": \{

"type": "string", 

"description": "API authentication key", 

"required": True, 

"hidden": True

150

5. Skills

\}

\}\)

**return **schema

**5.20.9 Using Custom Skills**

Register the skill directory:

from signalwire\_agents.skills.registry import skill\_registry

*\#\# Add your skills directory*

skill\_registry.add\_skill\_directory\("/path/to/my\_skills"\)

*\#\# Now use in agent*

**class **MyAgent\(AgentBase\):

**def \_\_init\_\_**\(self\):

super\(\). **\_\_init\_\_**\(name**=**"my-agent"\)

self.add\_language\("English", "en-US", "rime.spore"\) self.add\_skill\("product\_search", \{

"api\_url": "https://api.mystore.com", 

"api\_key": "secret" 

\}\)

151

5. Skills

**5.21 Skill Configuration**

**Summary**: Configure skills with parameters, environment variables, and SWAIG field overrides. Understand the parameter schema and discovery options. 

**5.21.1 Configuration Methods**

**Method**

**Description**

Parameters dict

Pass config when calling add\_skill\(\)

Environment variables

Set via OS environment

SWAIG fields

Customize tool metadata

External directories

Register custom skill paths

**5.21.2**

**Parameter Dictionary**

Pass configuration when adding a skill:

self.add\_skill\("web\_search", \{

"api\_key": "your-api-key", 

"search\_engine\_id": "your-engine-id", 

"num\_results": 5, 

"min\_quality\_score": 0.4

\}\)

**5.21.3**

**Parameter Schema**

Skills define their parameters via get\_parameter\_schema\(\):

\{

"api\_key": \{

"type": "string", 

"description": "Google API key", 

"required": True, 

"hidden": True, 

"env\_var": "GOOGLE\_API\_KEY" 

\}, 

"num\_results": \{

"type": "integer", 

"description": "Number of results", 

"default": 3, 

"min": 1, 

"max": 10

\}, 

"style": \{

"type": "string", 

"description": "Output style", 

"enum": \["brief", "detailed"\], 

"default": "brief" 

\}

\}

152

5. Skills

**5.21.4 Parameter Properties**

**Property**

**Type**

**Description**

type

string

Data type: string, integer, 

number, boolean, object, 

array

description

string

Human-readable description

default

any

Default value if not provided

required

bool

Whether parameter is

required

hidden

bool

Hide in UIs \(for secrets\)

env\_var

string

Environment variable source

enum

array

Allowed values

min/max

number

Value range for numbers

**5.21.5**

**Environment Variables**

Skills can read from environment variables:

import os

*\#\# Set environment variable*

os.environ\["GOOGLE\_API\_KEY"\] **= **"your-key" 

*\#\# Skill reads from params or falls back to env*

self.add\_skill\("web\_search", \{

"api\_key": os.getenv\("GOOGLE\_API\_KEY"\), 

"search\_engine\_id": os.getenv\("SEARCH\_ENGINE\_ID"\)

\}\)

**5.21.6**

**SWAIG Fields**

Override SWAIG function metadata for skill tools:

self.add\_skill\("datetime", \{

"swaig\_fields": \{

*\# Add filler phrases while function executes*

"fillers": \{

"en-US": \[

"Let me check the time...", 

"One moment..." 

\]

\}, 

*\# Disable security for testing*

"secure": False

\}

\}\)

Available SWAIG fields:

**Field**

**Description**

fillers

Language-specific filler phrases

secure

Enable/disable token validation

webhook\_url

Override webhook URL

153

5. Skills

**5.21.7 External Skill Directories**

Register custom skill directories:

from signalwire\_agents.skills.registry import skill\_registry

*\#\# Add directory at runtime*

skill\_registry.add\_skill\_directory\("/opt/custom\_skills"\)

*\#\# Environment variable \(colon-separated paths\)*

*\#\# SIGNALWIRE\_SKILL\_PATHS=/path1:/path2:/path3*

**5.21.8**

**Entry Points**

Install skills via pip packages:

*\#\# In setup.py*

setup\(

name**=**"my-skills-package", 

entry\_points**=**\{

"signalwire\_agents.skills": \[

"weather = my\_package.skills:WeatherSkill", 

"stock = my\_package.skills:StockSkill" 

\]

\}

\)

**5.21.9**

**Listing Available Skills**

from signalwire\_agents.skills.registry import skill\_registry

*\#\# List all available skills*

skills **= **skill\_registry.list\_skills\(\)

**for **skill **in **skills:

print\(f" **\{**skill\['name'\]**\}**: **\{**skill\['description'\]**\}**"\)

*\#\# Get complete schema for all skills*

schema **= **skill\_registry.get\_all\_skills\_schema\(\)

print\(schema\)

**5.21.10**

**Multi-Instance Configuration**

Skills supporting multiple instances need unique tool names:

*\#\# Instance 1: News search*

self.add\_skill\("web\_search", \{

"tool\_name": "search\_news", 

*\# Unique function name*

"api\_key": "KEY", 

"search\_engine\_id": "NEWS\_ENGINE" 

\}\)

*\#\# Instance 2: Documentation search*

self.add\_skill\("web\_search", \{

"tool\_name": "search\_docs", 

*\# Different function name*

"api\_key": "KEY", 

"search\_engine\_id": "DOCS\_ENGINE" 

\}\)

154

5. Skills

**5.21.11 Configuration Validation**

Skills validate configuration in setup\(\):

┌─────────────────────────────────────────────────────────────────────────────┐

│

Validation Flow

│

├─────────────────────────────────────────────────────────────────────────────┤

│

│

│

1. add\_skill\(\) called with params

│

│

│

│

│

▼

│

│

2. Skill instantiated

│

│

• params stored in self.params

│

│

• swaig\_fields extracted

│

│

│

│

│

▼

│

│

3. setup\(\) called

│

│

• validate\_packages\(\) - check Python packages

│

│

• validate\_env\_vars\(\) - check environment

│

│

• Custom validation

│

│

│

│

│

▼

│

│

4. Success: register\_tools\(\) called

│

│

Failure: ValueError raised

│

│

│

└─────────────────────────────────────────────────────────────────────────────┘

**5.21.12**

**Complete Configuration Example**

from signalwire\_agents import AgentBase

from signalwire\_agents.skills.registry import skill\_registry

import os

*\#\# Register external skills*

skill\_registry.add\_skill\_directory\("/opt/my\_company/skills"\) **class **ConfiguredAgent\(AgentBase\):

**def \_\_init\_\_**\(self\):

super\(\). **\_\_init\_\_**\(name**=**"configured-agent"\) self.add\_language\("English", "en-US", "rime.spore"\)

*\# Simple skill - no config*

self.add\_skill\("datetime"\)

*\# Skill with parameters*

self.add\_skill\("web\_search", \{

"api\_key": os.getenv\("GOOGLE\_API\_KEY"\), 

"search\_engine\_id": os.getenv\("SEARCH\_ENGINE\_ID"\), 

"num\_results": 5, 

"min\_quality\_score": 0.4

\}\)

*\# Skill with SWAIG field overrides*

self.add\_skill\("math", \{

"swaig\_fields": \{

"fillers": \{

"en-US": \["Calculating..."\]

\}

\}

\}\)

*\# Multi-instance skill*

self.add\_skill\("native\_vector\_search", \{

"tool\_name": "search\_products", 

155

5. Skills

"index\_path": "/data/products.swsearch" 

\}\)

self.add\_skill\("native\_vector\_search", \{

"tool\_name": "search\_faqs", 

"index\_path": "/data/faqs.swsearch" 

\}\)

self.prompt\_add\_section\(

"Role", 

"You are a customer service agent." 

\)

**if **\_\_name\_\_ **== **"\_\_main\_\_":

agent **= **ConfiguredAgent\(\)

agent.run\(\)

**5.21.13**

**Configuration Best Practices**

**5.21.13.1 Security**

• Store API keys in environment variables

• Never commit secrets to version control

• Use hidden: true for sensitive parameters

**5.21.13.2 Organization**

• Group related configuration

• Use descriptive tool\_name for multi-instance

• Document required configuration

**5.21.13.3**

**Validation**

• Check has\_skill\(\) before using conditionally

• Handle ValueError from add\_skill\(\)

• Validate parameters early in setup\(\)

**5.21.14**

**Next Steps**

You’ve learned the complete skills system. Next, explore advanced topics like contexts, workflows, and state management. 

156

**Chapter 6**

**Advanced Features**

**Summary**: This chapter covers advanced SDK features including multi-step workflows with contexts, state management, call recording, call transfers, multi-agent servers, and knowledge search integration. 

**6.1 What You’ll Learn**

This chapter covers advanced capabilities:

1. **Contexts & Workflows **- Multi-step conversation flows with branching logic 2. **State Management **- Session data, global state, and metadata handling 3. **Call Recording **- Record calls with various formats and options 4. **Call Transfer **- Transfer calls to other destinations

5. **Multi-Agent Servers **- Run multiple agents on a single server 6. **Search & Knowledge **- Vector search for RAG-style knowledge integration **6.2**

**Feature Overview**

**6.2.1**

**Contexts & Workflows**

• Multi-step conversations

• Branching logic

• Context switching

• Step validation

**6.2.2**

**State Management**

• global\_data dictionary

• metadata per call

• Tool-specific tokens

• Post-prompt data injection

**6.2.3**

**Call Recording**

• Stereo/mono recording

• Multiple formats \(mp3, wav, mp4 for video\)

• Pause/resume control

• Transcription support

157

6. Advanced Features

**6.2.4**

**Call Transfer**

• Blind transfers

• Announced transfers

• SIP destinations

• PSTN destinations

**6.2.5 Multi-Agent Servers**

• Multiple agents per server

• Path-based routing

• SIP username routing

• Shared configuration

**6.2.6**

**Search & Knowledge**

• Vector similarity search

• SQLite/pgvector backends

• Document processing

• RAG integration

**6.3 When to Use These Features**

**Feature**

**Use Case**

Contexts

Multi-step forms, wizards, guided flows

State Management

Persisting data across function calls

Call Recording

Compliance, training, quality assurance

Call Transfer

Escalation, routing to humans

Multi-Agent

Different agents for different purposes

Search

Knowledge bases, FAQ lookup, documentation

**6.4**

**Prerequisites**

Before diving into advanced features:

• Understand basic agent creation \(Chapter 3\)

• Know how SWAIG functions work \(Chapter 4\)

• Be comfortable with skills \(Chapter 5\)

**6.5**

**Chapter Contents**

**Section**

**Description**

Contexts & Workflows

Build multi-step conversation flows

State Management

Manage session and call state

Call Recording

Record calls with various options

Call Transfer

Transfer calls to destinations

Multi-Agent

Run multiple agents on one server

Search & Knowledge

Vector search integration

158

6. Advanced Features

**6.6 When to Use Contexts**

**Regular Prompts**

**Contexts**

Free-form conversations

Structured workflows

Simple Q&A agents

Multi-step data collection

Single-purpose tasks

Wizard-style flows

No defined sequence

Branching conversations

Multiple personas

**Use contexts when you need: **- Guaranteed step completion - Controlled navigation - Step-specific function access - Context-dependent personas - Department transfers - Isolated conversation segments **6.7 Context Architecture**

┌─────────────────────────────────────────────────────────────────────────────┐

│

Context Structure

│

├─────────────────────────────────────────────────────────────────────────────┤

│

│

│

┌─────────────────────────────────────────────────────────────────────┐

│

│

│

ContextBuilder

│

│

│

│

┌─────────────────────────────────────────────────────────────┐

│

│

│

│

│

Context "sales" 

│

│

│

│

│

│

┌────────────┐ ┌────────────┐ ┌────────────┐

│

│

│

│

│

│

│

Step 1

│→│

Step 2

│→│

Step 3

│

│

│

│

│

│

│

│ get\_info

│ │ confirm

│ │ process

│

│

│

│

│

│

│

└────────────┘ └────────────┘ └────────────┘

│

│

│

│

│

└─────────────────────────────────────────────────────────────┘

│

│

│

│

↕

│

│

│

│

┌─────────────────────────────────────────────────────────────┐

│

│

│

│

│

Context "support" 

│

│

│

│

│

│

┌────────────┐

│

│

│

│

│

│

│

Step 1

│

│

│

│

│

│

│

│ help

│

│

│

│

│

│

│

└────────────┘

│

│

│

│

│

└─────────────────────────────────────────────────────────────┘

│

│

│

└─────────────────────────────────────────────────────────────────────┘

│

│

│

└─────────────────────────────────────────────────────────────────────────────┘

**6.8**

**Basic Context Example**

from signalwire\_agents import AgentBase

**class **OrderAgent\(AgentBase\):

**def \_\_init\_\_**\(self\):

super\(\). **\_\_init\_\_**\(name**=**"order-agent"\)

self.add\_language\("English", "en-US", "rime.spore"\)

*\# Base prompt \(required even with contexts\)*

self.prompt\_add\_section\(

"Role", 

"You help customers place orders." 

\)

*\# Define contexts after setting base prompt*

contexts **= **self.define\_contexts\(\)

159

6. Advanced Features

*\# Add a context with steps*

order **= **contexts.add\_context\("default"\)

order.add\_step\("get\_item"\) **\\**

.set\_text\("Ask what item they want to order."\) **\\**

.set\_step\_criteria\("Customer has specified an item"\) **\\**

.set\_valid\_steps\(\["get\_quantity"\]\)

order.add\_step\("get\_quantity"\) **\\**

.set\_text\("Ask how many they want."\) **\\**

.set\_step\_criteria\("Customer has specified a quantity"\) **\\**

.set\_valid\_steps\(\["confirm"\]\)

order.add\_step\("confirm"\) **\\**

.set\_text\("Confirm the order details and thank them."\) **\\**

.set\_step\_criteria\("Order has been confirmed"\)

**if **\_\_name\_\_ **== **"\_\_main\_\_":

agent **= **OrderAgent\(\)

agent.run\(\)

**6.9 Step Configuration**

**6.9.1**

**set\_text\(\)**

Simple text prompt for the step:

step.set\_text\("What item would you like to order?"\)

**6.9.2**

**add\_section\(\) / add\_bullets\(\)**

POM-style structured prompts:

step.add\_section\("Task", "Collect customer information"\) **\\**

.add\_bullets\("Required Information", \[

"Full name", 

"Phone number", 

"Email address" 

\]\)

**6.9.3**

**set\_step\_criteria\(\)**

Define when the step is complete:

step.set\_step\_criteria\("Customer has provided their full name and phone number"\) **6.9.4**

**set\_valid\_steps\(\)**

Control step navigation:

*\# Can go to specific steps*

step.set\_valid\_steps\(\["confirm", "cancel"\]\)

*\# Use "next" for sequential flow*

step.set\_valid\_steps\(\["next"\]\)

160

6. Advanced Features

**6.9.5**

**set\_functions\(\)**

Restrict available functions per step:

*\# Disable all functions*

step.set\_functions\("none"\)

*\# Allow specific functions only*

step.set\_functions\(\["check\_inventory", "get\_price"\]\) **6.9.6 set\_valid\_contexts\(\)**

Allow navigation to other contexts:

step.set\_valid\_contexts\(\["support", "manager"\]\) **6.10 Context Configuration**

**6.10.1**

**set\_isolated\(\)**

Truncate conversation history when entering:

context.set\_isolated\(True\)

**6.10.2**

**set\_system\_prompt\(\)**

New system prompt when entering context:

context.set\_system\_prompt\("You are now a technical support specialist."\) **6.10.3**

**set\_user\_prompt\(\)**

Inject a user message when entering:

context.set\_user\_prompt\("I need help with a technical issue."\) **6.10.4**

**set\_consolidate\(\)**

Summarize previous conversation when switching:

context.set\_consolidate\(True\)

**6.10.5**

**set\_full\_reset\(\)**

Completely reset conversation state:

context.set\_full\_reset\(True\)

161

6. Advanced Features

**6.10.6 add\_enter\_filler\(\) / add\_exit\_filler\(\)**

Add transition phrases:

context.add\_enter\_filler\("en-US", \[

"Let me connect you with our support team...", 

"Transferring you to a specialist..." 

\]\)

context.add\_exit\_filler\("en-US", \[

"Returning you to the main menu...", 

"Back to the sales department..." 

\]\)

**6.11 Multi-Context Example**

from signalwire\_agents import AgentBase

**class **MultiDepartmentAgent\(AgentBase\):

**def \_\_init\_\_**\(self\):

super\(\). **\_\_init\_\_**\(name**=**"multi-dept-agent"\) self.add\_language\("English-Sales", "en-US", "rime.spore"\) self.add\_language\("English-Support", "en-US", "rime.cove"\) self.add\_language\("English-Manager", "en-US", "rime.marsh"\) self.prompt\_add\_section\(

"Instructions", 

"Guide customers through sales or transfer to appropriate departments." 

\)

contexts **= **self.define\_contexts\(\)

*\# Sales context*

sales **= **contexts.add\_context\("sales"\) **\\**

.set\_isolated\(True\) **\\**

.add\_section\("Role", "You are Alex, a sales representative."\) sales.add\_step\("qualify"\) **\\**

.add\_section\("Task", "Determine customer needs"\) **\\**

.set\_step\_criteria\("Customer needs are understood"\) **\\**

.set\_valid\_steps\(\["recommend"\]\) **\\**

.set\_valid\_contexts\(\["support", "manager"\]\)

sales.add\_step\("recommend"\) **\\**

.add\_section\("Task", "Make product recommendations"\) **\\**

.set\_step\_criteria\("Recommendation provided"\) **\\**

.set\_valid\_contexts\(\["support", "manager"\]\)

*\# Support context*

support **= **contexts.add\_context\("support"\) **\\**

.set\_isolated\(True\) **\\**

.add\_section\("Role", "You are Sam, technical support."\) **\\**

.add\_enter\_filler\("en-US", \[

"Connecting you with technical support...", 

"Let me transfer you to our tech team..." 

\]\)

support.add\_step\("assist"\) **\\**

.add\_section\("Task", "Help with technical questions"\) **\\**

.set\_step\_criteria\("Technical issue resolved"\) **\\**

.set\_valid\_contexts\(\["sales", "manager"\]\)

*\# Manager context*

manager **= **contexts.add\_context\("manager"\) **\\**

.set\_isolated\(True\) **\\**

.add\_section\("Role", "You are Morgan, the store manager."\) **\\**

.add\_enter\_filler\("en-US", \[

162

6. Advanced Features

"Let me get the manager for you...", 

"One moment, connecting you with management..." 

\]\)

manager.add\_step\("escalate"\) **\\**

.add\_section\("Task", "Handle escalated issues"\) **\\**

.set\_step\_criteria\("Issue resolved by manager"\) **\\**

.set\_valid\_contexts\(\["sales", "support"\]\)

**if **\_\_name\_\_ **== **"\_\_main\_\_":

agent **= **MultiDepartmentAgent\(\)

agent.run\(\)

**6.12 Navigation Flow**

**6.12.1**

**Within Context \(Steps\)**

• set\_valid\_steps\(\["next"\]\) - Go to next sequential step

• set\_valid\_steps\(\["step\_name"\]\) - Go to specific step

• set\_valid\_steps\(\["a", "b"\]\) - Multiple options **6.12.2**

**Between Contexts**

• set\_valid\_contexts\(\["other\_context"\]\) - Allow context switch

• AI calls change\_context\("context\_name"\) automatically

• Enter/exit fillers provide smooth transitions

**6.12.3**

**Context Entry Behavior**

• isolated=True - Clear conversation history

• consolidate=True - Summarize previous conversation

• full\_reset=True - Complete prompt replacement

**6.13**

**Validation Rules**

The ContextBuilder validates your configuration:

• Single context must be named “default” 

• Every context must have at least one step

• valid\_steps must reference existing steps \(or “next”\)

• valid\_contexts must reference existing contexts

• Cannot mix set\_text\(\) with add\_section\(\) on same step

• Cannot mix set\_prompt\(\) with add\_section\(\) on same context

163

6. Advanced Features

**6.14 Step and Context Methods Summary**

**Method**

**Level**

**Purpose**

set\_text\(\)

Step

Simple text prompt

add\_section\(\)

Both

POM-style section

add\_bullets\(\)

Both

Bulleted list section

set\_step\_criteria\(\)

Step

Completion criteria

set\_functions\(\)

Step

Restrict available functions

set\_valid\_steps\(\)

Step

Allowed step navigation

set\_valid\_contexts\(\)

Both

Allowed context navigation

set\_isolated\(\)

Context

Clear history on entry

set\_consolidate\(\)

Context

Summarize on entry

set\_full\_reset\(\)

Context

Complete reset on entry

set\_system\_prompt\(\)

Context

New system prompt

set\_user\_prompt\(\)

Context

Inject user message

add\_enter\_filler\(\)

Context

Entry transition phrases

add\_exit\_filler\(\)

Context

Exit transition phrases

**6.15**

**Best Practices**

**DO: **- Set clear step\_criteria for each step - Use isolated=True for persona changes - Add enter\_fillers for smooth transitions - Define valid\_contexts to enable department transfers - Test navigation paths thoroughly **DON’T: **- Create circular navigation without exit paths - Skip setting a base prompt before define\_contexts\(\) - Mix set\_text\(\) with add\_section\(\) on the same step - Forget to validate step/context references 164

6. Advanced Features

**6.16 State Management**

**Summary**: Manage data throughout call sessions using global\_data for persistent state, metadata for function-scoped data, and post\_prompt for call summaries. 

**6.16.1 State Types Overview**

**State Type**

**Scope**

**Key Features**

**global\_data**

Entire session

Persists entire session, 

available to all functions, 

accessible in prompts, set at

init or runtime

**metadata**

Function-scoped

Scoped to function’s token, 

private to specific function, 

isolated per meta\_data\_toke

n, set via function results

**post\_prompt**

After call

Executes after call ends, 

generates summaries, 

extracts structured data, 

webhook delivery

**call\_info**

Read-only

Read-only call metadata, 

caller ID, call ID, available

in raw\_data, 

SignalWire-provided

**6.16.2**

**Global Data**

Global data persists throughout the entire call session and is available to all functions and prompts. 

**6.16.2.1**

**Setting Initial Global Data**

from signalwire\_agents import AgentBase

**class **CustomerAgent\(AgentBase\):

**def \_\_init\_\_**\(self\):

super\(\). **\_\_init\_\_**\(name**=**"customer-agent"\)

self.add\_language\("English", "en-US", "rime.spore"\)

*\# Set initial global data at agent creation*

self.set\_global\_data\(\{

"business\_name": "Acme Corp", 

"support\_hours": "9 AM - 5 PM EST", 

"current\_promo": "20**% o**ff first order" 

\}\)

self.prompt\_add\_section\(

"Role", 

"You are a customer service agent for $**\{global\_data.business\_name\}**." 

\)

**if **\_\_name\_\_ **== **"\_\_main\_\_":

agent **= **CustomerAgent\(\)

agent.run\(\)

165

6. Advanced Features

**6.16.2.2 Updating Global Data at Runtime**

self.update\_global\_data\(\{

"customer\_tier": "premium", 

"account\_balance": 150.00

\}\)

**6.16.2.3 Updating Global Data from Functions**

from signalwire\_agents import AgentBase

from signalwire\_agents.core.function\_result import SwaigFunctionResult **class **StateAgent\(AgentBase\):

**def \_\_init\_\_**\(self\):

super\(\). **\_\_init\_\_**\(name**=**"state-agent"\)

self.add\_language\("English", "en-US", "rime.spore"\) self.define\_tool\(

name**=**"set\_customer\_name", 

description**=**"Store the customer's name", 

parameters**=**\{

"type": "object", 

"properties": \{

"name": \{"type": "string", "description": "Customer name"\}

\}, 

"required": \["name"\]

\}, 

handler**=**self.set\_customer\_name

\)

**def **set\_customer\_name\(self, args, raw\_data\):

name **= **args.get\("name", ""\)

**return **\(

SwaigFunctionResult\(f"Stored name: **\{**name**\}**"\)

.update\_global\_data\(\{"customer\_name": name\}\)

\)

**if **\_\_name\_\_ **== **"\_\_main\_\_":

agent **= **StateAgent\(\)

agent.run\(\)

**6.16.2.4**

**Accessing Global Data in Prompts**

Use $\{global\_data.key\} syntax in prompts:

self.prompt\_add\_section\(

"Customer Info", 

""" 

Customer Name: $**\{global\_data.customer\_name\}**

Account Tier: $**\{global\_data.customer\_tier\}**

Current Balance: $**\{global\_data.account\_balance\}**

""" 

\)

**6.16.3**

**Metadata**

Metadata is scoped to a specific function’s meta\_data\_token, providing isolated storage per function. 

166

6. Advanced Features

**6.16.3.1 Setting Metadata**

**def **process\_order\(self, args, raw\_data\):

order\_id **= **create\_order\(\)

**return **\(

SwaigFunctionResult\(f"Created order **\{**order\_id**\}**"\)

.set\_metadata\(\{"order\_id": order\_id, "status": "pending"\}\)

\)

**6.16.3.2 Removing Metadata**

**def **cancel\_order\(self, args, raw\_data\):

**return **\(

SwaigFunctionResult\("Order cancelled"\)

.remove\_metadata\(\["order\_id", "status"\]\)

\)

**6.16.4**

**Post-Prompt Data**

The post-prompt runs after the call ends and generates structured data from the conversation. 

**6.16.4.1 Setting Post-Prompt**

from signalwire\_agents import AgentBase

**class **SurveyAgent\(AgentBase\):

**def \_\_init\_\_**\(self\):

super\(\). **\_\_init\_\_**\(name**=**"survey-agent"\)

self.add\_language\("English", "en-US", "rime.spore"\) self.prompt\_add\_section\(

"Role", 

"Conduct a customer satisfaction survey." 

\)

*\# Post-prompt extracts structured data after call*

self.set\_post\_prompt\(""" 

Summarize the survey results as JSON:

\{

"satisfaction\_score": <1-10>, 

"main\_feedback": "<summary>", 

"would\_recommend": <true/false>, 

"issues\_mentioned": \["<issue1>", "<issue2>"\]

\}

"""\)

*\# Optionally set where to send the data*

self.set\_post\_prompt\_url\("https://example.com/survey-results"\) **if **\_\_name\_\_ **== **"\_\_main\_\_":

agent **= **SurveyAgent\(\)

agent.run\(\)

**6.16.4.2**

**Post-Prompt LLM Parameters**

Configure a different model for post-prompt processing:

self.set\_post\_prompt\_llm\_params\(

model**=**"gpt-4o-mini", 

temperature**=**0.3

*\# Lower for consistent extraction*

\)

167

6. Advanced Features

**6.16.5 Accessing Call Information**

The raw\_data parameter contains call metadata:

**def **my\_handler\(self, args, raw\_data\):

*\# Available call information*

call\_id **= **raw\_data.get\("call\_id"\)

caller\_id\_number **= **raw\_data.get\("caller\_id\_number"\) caller\_id\_name **= **raw\_data.get\("caller\_id\_name"\)

call\_direction **= **raw\_data.get\("call\_direction"\)

*\# "inbound" or "outbound" *

*\# Current AI interaction state*

ai\_session\_id **= **raw\_data.get\("ai\_session\_id"\)

self.log.info\(f"Call from **\{**caller\_id\_number**\}**"\) **return **SwaigFunctionResult\("Processing..."\)

**6.16.6**

**State Flow Diagram**

┌─────────────────────────────────────────────────────────────────────────────┐

│

State Flow

│

├─────────────────────────────────────────────────────────────────────────────┤

│

│

│

Call Start

│

│

│

│

│

▼

│

│

┌─────────────────────┐

│

│

│

set\_global\_data\(\)

│

Initial state from agent config

│

│

└─────────────────────┘

│

│

│

│

│

▼

│

│

┌─────────────────────┐

│

│

│

Conversation

│

AI uses $\{global\_data.key\} in prompts

│

│

└─────────────────────┘

│

│

│

│

│

▼

│

│

┌─────────────────────┐

│

│

│

Function Call

│

Handler receives raw\_data with call info

│

│

└─────────────────────┘

│

│

│

│

│

▼

│

│

┌─────────────────────────────────────────────────────────┐

│

│

│

SwaigFunctionResult

│

│

│

│

.update\_global\_data\(\)

→ Updates session state

│

│

│

│

.set\_metadata\(\)

→ Updates function-scoped

│

│

│

└─────────────────────────────────────────────────────────┘

│

│

│

│

│

▼

│

│

┌─────────────────────┐

│

│

│

Call Ends

│

│

│

└─────────────────────┘

│

│

│

│

│

▼

│

│

┌─────────────────────┐

│

│

│

Post-Prompt

│

Extracts structured data from conversation

│

│

└─────────────────────┘

│

│

│

└─────────────────────────────────────────────────────────────────────────────┘

168

6. Advanced Features

**6.16.7 Complete Example**

*\#\!/usr/bin/env python3*

*\#\# order\_agent.py - Order management with state*

from signalwire\_agents import AgentBase

from signalwire\_agents.core.function\_result import SwaigFunctionResult **class **OrderAgent\(AgentBase\):

**def \_\_init\_\_**\(self\):

super\(\). **\_\_init\_\_**\(name**=**"order-agent"\)

self.add\_language\("English", "en-US", "rime.spore"\)

*\# Initial global state*

self.set\_global\_data\(\{

"store\_name": "Pizza Palace", 

"order\_items": \[\], 

"order\_total": 0.0

\}\)

self.prompt\_add\_section\(

"Role", 

"You are an order assistant for $**\{global\_data.store\_name\}**. " 

"Help customers place their order." 

\)

self.prompt\_add\_section\(

"Current Order", 

"Items: $**\{global\_data.order\_items\}**\\n" 

"Total: $$**\{global\_data.order\_total\}**" 

\)

*\# Post-prompt for order summary*

self.set\_post\_prompt\(""" 

Extract the final order as JSON:

\{

"items": \[\{"name": "", "quantity": 0, "price": 0.00\}\], 

"total": 0.00, 

"customer\_name": "", 

"special\_instructions": "" 

\}

"""\)

self.\_register\_functions\(\)

**def **\_register\_functions\(self\):

self.define\_tool\(

name**=**"add\_item", 

description**=**"Add an item to the order", 

parameters**=**\{

"type": "object", 

"properties": \{

"item": \{"type": "string", "description": "Item name"\}, 

"price": \{"type": "number", "description": "Item price"\}

\}, 

"required": \["item", "price"\]

\}, 

handler**=**self.add\_item

\)

**def **add\_item\(self, args, raw\_data\):

item **= **args.get\("item"\)

price **= **args.get\("price", 0.0\)

*\# Note: In real implementation, maintain state server-side*

*\# This example shows the pattern*

**return **\(

SwaigFunctionResult\(f"Added **\{**item**\} **\($**\{**price**\}**\) to your order"\)

.update\_global\_data\(\{

"last\_item\_added": item, 

"last\_item\_price": price

169

6. Advanced Features

\}\)

\)

**if **\_\_name\_\_ **== **"\_\_main\_\_":

agent **= **OrderAgent\(\)

agent.run\(\)

**6.16.8 DataMap Variable Access**

In DataMap functions, use variable substitution:

from signalwire\_agents.core.data\_map import DataMap

from signalwire\_agents.core.function\_result import SwaigFunctionResult lookup\_dm **= **\(

DataMap\("lookup\_customer"\)

.description\("Look up customer by ID"\)

.parameter\("customer\_id", "string", "Customer ID", required**=**True\)

.webhook\(

"GET", 

"https://api.example.com/customers/$\{enc:args.customer\_id\}" 

"?store=$\{enc:global\_data.store\_id\}" 

\)

.output\(SwaigFunctionResult\(

"Customer: $**\{response.name\}**, Tier: $**\{response.tier\}**" 

\)\)

\)

**6.16.9**

**State Methods Summary**

**Method**

**Scope**

**Purpose**

set\_global\_data\(\)

Agent

Set initial global state

update\_global\_data\(\)

Agent

Update global state at

runtime

SwaigFunctionResult.update\_global\_data\(\)

Function

Update state from function

SwaigFunctionResult.set\_metadata\(\)

Function

Set function-scoped data

SwaigFunctionResult.remove\_metadata\(\)

Function

Remove function-scoped

data

set\_post\_prompt\(\)

Agent

Set post-call data extraction

set\_post\_prompt\_url\(\)

Agent

Set webhook for

post-prompt data

set\_post\_prompt\_llm\_params\(\)

Agent

Configure post-prompt

model

**6.16.10**

**Best Practices**

**DO: **- Use global\_data for data needed across functions - Use metadata for function-specific isolated data - Set initial state in **init **for predictable behavior - Use post\_prompt to extract structured call summaries - Log state changes for debugging

**DON’T: **- Store sensitive data \(passwords, API keys\) in global\_data - Rely on global\_data for complex state machines \(use server-side\) - Assume metadata persists across function boundaries - Forget that state resets between calls

170

6. Advanced Features

**6.17 Call Recording**

**Summary**: Record calls using record\_call\(\) and stop\_record\_call\(\) methods on SwaigFunctionResult. Supports stereo/mono, multiple formats, and webhook notifications. 

**6.17.1 Recording Overview**

**record\_call\(\) **- Starts background recording - Continues while conversation proceeds - Supports stereo \(separate channels\) or mono - Output formats: WAV, MP3, or MP4 - Direction: speak only, listen only, or both **stop\_record\_call\(\) **- Stops an active recording - Uses control\_id to target specific recording - Recording is automatically stopped on call end

**6.17.2**

**Basic Recording**

from signalwire\_agents import AgentBase

from signalwire\_agents.core.function\_result import SwaigFunctionResult **class **RecordingAgent\(AgentBase\):

**def \_\_init\_\_**\(self\):

super\(\). **\_\_init\_\_**\(name**=**"recording-agent"\)

self.add\_language\("English", "en-US", "rime.spore"\) self.prompt\_add\_section\(

"Role", 

"You are a customer service agent. " 

"Start recording when the customer agrees." 

\)

self.define\_tool\(

name**=**"start\_recording", 

description**=**"Start recording the call with customer consent", parameters**=**\{"type": "object", "properties": \{\}\}, handler**=**self.start\_recording

\)

**def **start\_recording\(self, args, raw\_data\):

**return **\(

SwaigFunctionResult\("Recording has started."\)

.record\_call\(

control\_id**=**"main\_recording", 

stereo**=**True, 

format**=**"wav" 

\)

\)

**if **\_\_name\_\_ **== **"\_\_main\_\_":

agent **= **RecordingAgent\(\)

agent.run\(\)

171

6. Advanced Features

**6.17.3 Recording Parameters**

**Parameter**

**Type**

**Default**

**Description**

control\_id

str

None

Identifier to stop specific

recording

stereo

bool

False

True for separate L/R

channels

format

str

"wav" 

Output format: “wav”, 

“mp3”, or “mp4” 

direction

str

"both" 

“speak”, “listen”, or “both” 

terminators

str

None

DTMF digits that stop

recording

beep

bool

False

Play beep before recording

input\_sensitivity

float

44.0

Audio sensitivity threshold

initial\_timeout

float

0.0

Seconds to wait for speech

end\_silence\_timeout

float

0.0

Silence duration to

auto-stop

max\_length

float

None

Maximum recording seconds

status\_url

str

None

Webhook for recording

events

**6.17.4**

**Stereo Recording**

Record caller and agent on separate channels:

**def **start\_stereo\_recording\(self, args, raw\_data\):

**return **\(

SwaigFunctionResult\("Recording in stereo mode"\)

.record\_call\(

control\_id**=**"stereo\_rec", 

stereo**=**True, 

*\# Caller on left, agent on right*

format**=**"wav" 

\)

\)

**6.17.5**

**Direction Options**

*\#\# Record only what the AI/agent speaks*

**def **record\_agent\_only\(self, args, raw\_data\):

**return **\(

SwaigFunctionResult\("Recording agent audio"\)

.record\_call\(direction**=**"speak"\)

\)

*\#\# Record only what the caller says*

**def **record\_caller\_only\(self, args, raw\_data\):

**return **\(

SwaigFunctionResult\("Recording caller audio"\)

.record\_call\(direction**=**"listen"\)

\)

*\#\# Record both sides \(default\)*

**def **record\_both\(self, args, raw\_data\):

**return **\(

SwaigFunctionResult\("Recording full conversation"\)

.record\_call\(direction**=**"both"\)

\)

172

6. Advanced Features

**6.17.6 Recording with Webhook**

Receive notifications when recording completes:

**def **start\_recording\_with\_callback\(self, args, raw\_data\):

**return **\(

SwaigFunctionResult\("Recording started"\)

.record\_call\(

control\_id**=**"webhook\_rec", 

status\_url**=**"https://example.com/recording-complete" 

\)

\)

The webhook receives recording metadata including the URL to download the file. 

**6.17.7**

**Auto-Stop Recording**

Configure automatic stop conditions:

**def **start\_auto\_stop\_recording\(self, args, raw\_data\):

**return **\(

SwaigFunctionResult\("Recording with auto-stop"\)

.record\_call\(

max\_length**=**300.0, 

*\# Stop after 5 minutes*

end\_silence\_timeout**=**5.0, *\# Stop after 5 seconds of silence* terminators**=**"\#" 

*\# Stop if user presses \#*

\)

\)

**6.17.8**

**Stop Recording**

Stop a recording by control\_id:

from signalwire\_agents import AgentBase

from signalwire\_agents.core.function\_result import SwaigFunctionResult **class **ControlledRecordingAgent\(AgentBase\):

**def \_\_init\_\_**\(self\):

super\(\). **\_\_init\_\_**\(name**=**"controlled-recording-agent"\) self.add\_language\("English", "en-US", "rime.spore"\) self.prompt\_add\_section\(

"Role", 

"You handle call recordings. You can start and stop recording." 

\)

self.\_register\_functions\(\)

**def **\_register\_functions\(self\):

self.define\_tool\(

name**=**"start\_recording", 

description**=**"Start recording the call", 

parameters**=**\{"type": "object", "properties": \{\}\}, handler**=**self.start\_recording

\)

self.define\_tool\(

name**=**"stop\_recording", 

description**=**"Stop recording the call", 

parameters**=**\{"type": "object", "properties": \{\}\}, handler**=**self.stop\_recording

\)

**def **start\_recording\(self, args, raw\_data\):

**return **\(

SwaigFunctionResult\("Recording has started"\)

173

6. Advanced Features

.record\_call\(control\_id**=**"main"\)

\)

**def **stop\_recording\(self, args, raw\_data\):

**return **\(

SwaigFunctionResult\("Recording has stopped"\)

.stop\_record\_call\(control\_id**=**"main"\)

\)

**if **\_\_name\_\_ **== **"\_\_main\_\_":

agent **= **ControlledRecordingAgent\(\)

agent.run\(\)

**6.17.9**

**Recording with Beep**

Alert the caller that recording is starting:

**def **start\_recording\_with\_beep\(self, args, raw\_data\):

**return **\(

SwaigFunctionResult\("This call will be recorded"\)

.record\_call\(

beep**=**True, 

*\# Plays a beep before recording starts*

format**=**"mp3" 

\)

\)

**6.17.10**

**Complete Example**

*\#\!/usr/bin/env python3*

*\#\# compliance\_agent.py - Agent with recording compliance features* from signalwire\_agents import AgentBase

from signalwire\_agents.core.function\_result import SwaigFunctionResult **class **ComplianceAgent\(AgentBase\):

*"""Agent with full recording compliance features""" *

**def \_\_init\_\_**\(self\):

super\(\). **\_\_init\_\_**\(name**=**"compliance-agent"\) self.add\_language\("English", "en-US", "rime.spore"\) self.prompt\_add\_section\(

"Role", 

"You are a customer service agent. Before recording, you must " 

"inform the customer and get their verbal consent." 

\)

self.prompt\_add\_section\(

"Recording Policy", 

""" 

1. Always inform customer: "This call may be recorded for quality purposes." 

2. Ask for consent: "Do you agree to the recording?" 

3. Only start recording after explicit "yes" or agreement. 

4. If customer declines, proceed without recording. 

""" 

\)

self.\_register\_functions\(\)

**def **\_register\_functions\(self\):

self.define\_tool\(

name**=**"start\_compliant\_recording", 

description**=**"Start recording after customer consent is obtained", parameters**=**\{"type": "object", "properties": \{\}\}, handler**=**self.start\_compliant\_recording

\)

174

6. Advanced Features

self.define\_tool\(

name**=**"pause\_recording", 

description**=**"Pause recording for sensitive information", parameters**=**\{"type": "object", "properties": \{\}\}, handler**=**self.pause\_recording

\)

self.define\_tool\(

name**=**"resume\_recording", 

description**=**"Resume recording after sensitive section", parameters**=**\{"type": "object", "properties": \{\}\}, handler**=**self.resume\_recording

\)

**def **start\_compliant\_recording\(self, args, raw\_data\):

call\_id **= **raw\_data.get\("call\_id", "unknown"\) **return **\(

SwaigFunctionResult\("Recording has begun. Thank you for your consent."\)

.record\_call\(

control\_id**=**f"compliance\_**\{**call\_id**\}**", stereo**=**True, 

format**=**"wav", 

beep**=**True, 

status\_url**=**"https://example.com/recordings/status" 

\)

.update\_global\_data\(\{"recording\_active": True\}\)

\)

**def **pause\_recording\(self, args, raw\_data\):

call\_id **= **raw\_data.get\("call\_id", "unknown"\) **return **\(

SwaigFunctionResult\(

"Recording paused. You may now provide sensitive information." 

\)

.stop\_record\_call\(control\_id**=**f"compliance\_**\{**call\_id**\}**"\)

.update\_global\_data\(\{"recording\_active": False\}\)

\)

**def **resume\_recording\(self, args, raw\_data\):

call\_id **= **raw\_data.get\("call\_id", "unknown"\) **return **\(

SwaigFunctionResult\("Recording resumed."\)

.record\_call\(

control\_id**=**f"compliance\_**\{**call\_id**\}**", stereo**=**True, 

format**=**"wav" 

\)

.update\_global\_data\(\{"recording\_active": True\}\)

\)

**if **\_\_name\_\_ **== **"\_\_main\_\_":

agent **= **ComplianceAgent\(\)

agent.run\(\)

**6.17.11**

**Recording Best Practices**

**6.17.11.1**

**Compliance**

• Always inform callers before recording

• Obtain consent where legally required

• Provide option to decline recording

• Document consent in call logs

175

6. Advanced Features

**6.17.11.2 Technical**

• Use control\_id for multiple recordings

• Use stereo=True for transcription accuracy

• Use status\_url to track recording completion

• Set max\_length to prevent oversized files

**6.17.11.3 Storage**

• Use WAV for quality, MP3 for size, MP4 for video

• Implement retention policies

• Secure storage with encryption

176

6. Advanced Features

**6.18 Call Transfer**

**Summary**: Transfer calls to other destinations using connect\(\) for phone numbers/SIP and swml\_transfer\(\) for SWML endpoints. Support for both permanent and temporary transfers. 

**6.18.1 Transfer Types**

**6.18.1.1 Permanent Transfer \(final=True\)**

• Call exits the agent completely

• Caller connected directly to destination

• Agent conversation ends

• **Use for: **Handoff to human, transfer to another system

**6.18.1.2 Temporary Transfer \(final=False\)**

• Call returns to agent when far end hangs up

• Agent can continue conversation after transfer

• **Use for: **Conferencing, brief consultations

**6.18.2**

**Basic Phone Transfer**

from signalwire\_agents import AgentBase

from signalwire\_agents.core.function\_result import SwaigFunctionResult **class **TransferAgent\(AgentBase\):

**def \_\_init\_\_**\(self\):

super\(\). **\_\_init\_\_**\(name**=**"transfer-agent"\)

self.add\_language\("English", "en-US", "rime.spore"\) self.prompt\_add\_section\(

"Role", 

"You are a receptionist who can transfer calls to different departments." 

\)

self.define\_tool\(

name**=**"transfer\_to\_sales", 

description**=**"Transfer the caller to the sales department", parameters**=**\{"type": "object", "properties": \{\}\}, handler**=**self.transfer\_to\_sales

\)

**def **transfer\_to\_sales\(self, args, raw\_data\):

**return **\(

SwaigFunctionResult\("Transferring you to sales now."\)

.connect\("\+15551234567", final**=**True\)

\)

**if **\_\_name\_\_ **== **"\_\_main\_\_":

agent **= **TransferAgent\(\)

agent.run\(\)

177

6. Advanced Features

**6.18.3 Connect Method Parameters**

**Parameter**

**Type**

**Default**

**Description**

destination

str

required

Phone number, SIP address, 

or URI

final

bool

True

Permanent \(True\) or

temporary \(False\)

from\_addr

str

None

Override caller ID for

outbound leg

**6.18.4**

**Permanent vs Temporary Transfer**

from signalwire\_agents import AgentBase

from signalwire\_agents.core.function\_result import SwaigFunctionResult **class **SmartTransferAgent\(AgentBase\):

**def \_\_init\_\_**\(self\):

super\(\). **\_\_init\_\_**\(name**=**"smart-transfer-agent"\) self.add\_language\("English", "en-US", "rime.spore"\) self.prompt\_add\_section\(

"Role", 

"You can transfer calls permanently or temporarily." 

\)

self.\_register\_functions\(\)

**def **\_register\_functions\(self\):

self.define\_tool\(

name**=**"transfer\_permanent", 

description**=**"Permanently transfer to support \(call ends with agent\)", parameters**=**\{

"type": "object", 

"properties": \{

"number": \{"type": "string", "description": "Phone number"\}

\}, 

"required": \["number"\]

\}, 

handler**=**self.transfer\_permanent

\)

self.define\_tool\(

name**=**"transfer\_temporary", 

description**=**"Temporarily connect to expert, then return to agent", parameters**=**\{

"type": "object", 

"properties": \{

"number": \{"type": "string", "description": "Phone number"\}

\}, 

"required": \["number"\]

\}, 

handler**=**self.transfer\_temporary

\)

**def **transfer\_permanent\(self, args, raw\_data\):

number **= **args.get\("number"\)

**return **\(

SwaigFunctionResult\(f"Transferring you now. Goodbye\!"\)

.connect\(number, final**=**True\)

\)

**def **transfer\_temporary\(self, args, raw\_data\):

number **= **args.get\("number"\)

**return **\(

SwaigFunctionResult\("Connecting you briefly. I'll be here when you're done."\) 178

6. Advanced Features

.connect\(number, final**=**False\)

\)

**if **\_\_name\_\_ **== **"\_\_main\_\_":

agent **= **SmartTransferAgent\(\)

agent.run\(\)

**6.18.5 SIP Transfer**

Transfer to SIP endpoints:

**def **transfer\_to\_sip\(self, args, raw\_data\):

**return **\(

SwaigFunctionResult\("Connecting to internal support"\)

.connect\("sip:support@company.com", final**=**True\)

\)

**6.18.6**

**Transfer with Caller ID Override**

**def **transfer\_with\_custom\_callerid\(self, args, raw\_data\):

**return **\(

SwaigFunctionResult\("Connecting you now"\)

.connect\(

"\+15551234567", 

final**=**True, 

from\_addr**=**"\+15559876543" 

*\# Custom caller ID*

\)

\)

**6.18.7**

**SWML Transfer**

Transfer to another SWML endpoint \(another agent\):

from signalwire\_agents import AgentBase

from signalwire\_agents.core.function\_result import SwaigFunctionResult **class **MultiAgentTransfer\(AgentBase\):

**def \_\_init\_\_**\(self\):

super\(\). **\_\_init\_\_**\(name**=**"multi-agent-transfer"\) self.add\_language\("English", "en-US", "rime.spore"\) self.prompt\_add\_section\("Role", "You route calls to specialized agents."\) self.define\_tool\(

name**=**"transfer\_to\_billing", 

description**=**"Transfer to the billing specialist agent", parameters**=**\{"type": "object", "properties": \{\}\}, handler**=**self.transfer\_to\_billing

\)

**def **transfer\_to\_billing\(self, args, raw\_data\):

**return **\(

SwaigFunctionResult\(

"I'm transferring you to our billing specialist.", 

post\_process**=**True

*\# Speak message before transfer*

\)

.swml\_transfer\(

dest**=**"https://agents.example.com/billing", 

ai\_response**=**"How else can I help?", 

*\# Used if final=False*

final**=**True

\)

\)

179

6. Advanced Features

**if **\_\_name\_\_ **== **"\_\_main\_\_":

agent **= **MultiAgentTransfer\(\)

agent.run\(\)

**6.18.8 Transfer Flow**

┌─────────────────────────────────────────────────────────────────────────────┐

│

Transfer Flow Diagram

│

├─────────────────────────────────────────────────────────────────────────────┤

│

│

│

Permanent Transfer \(final=True\):

│

│

│

│

Caller ──→ Agent ──→ "Transferring..." ──→ Destination

│

│

│

│

│

│

└── Agent exits ─────┘

│

│

│

│

Temporary Transfer \(final=False\):

│

│

│

│

Caller ──→ Agent ──→ "Connecting..." ──→ Destination

│

│

│

│

│

│

│

▼

│

│

│

Destination hangs up

│

│

│

│

│

│

└───────────── Returns ─────────┘

│

│

│

│

│

▼

│

│

Agent continues conversation

│

│

│

└─────────────────────────────────────────────────────────────────────────────┘

**6.18.9**

**Department Transfer Example**

from signalwire\_agents import AgentBase

from signalwire\_agents.core.function\_result import SwaigFunctionResult **class **ReceptionistAgent\(AgentBase\):

*"""Receptionist that routes calls to departments""" *

DEPARTMENTS **= **\{

"sales": "\+15551111111", 

"support": "\+15552222222", 

"billing": "\+15553333333", 

"hr": "\+15554444444" 

\}

**def \_\_init\_\_**\(self\):

super\(\). **\_\_init\_\_**\(name**=**"receptionist-agent"\) self.add\_language\("English", "en-US", "rime.spore"\) self.prompt\_add\_section\(

"Role", 

"You are the company receptionist. Help callers reach the right department." 

\)

self.prompt\_add\_section\(

"Available Departments", 

"Sales, Support, Billing, Human Resources \(HR\)" 

\)

self.define\_tool\(

name**=**"transfer\_to\_department", 

description**=**"Transfer caller to a specific department", parameters**=**\{

"type": "object", 

180

6. Advanced Features

"properties": \{

"department": \{

"type": "string", 

"description": "Department name", 

"enum": \["sales", "support", "billing", "hr"\]

\}

\}, 

"required": \["department"\]

\}, 

handler**=**self.transfer\_to\_department

\)

**def **transfer\_to\_department\(self, args, raw\_data\):

dept **= **args.get\("department", ""\).lower\(\) **if **dept **not in **self.DEPARTMENTS:

**return **SwaigFunctionResult\(

f"I don't recognize the department ' **\{**dept**\}**'. " 

"Available departments are: Sales, Support, Billing, and HR." 

\)

number **= **self.DEPARTMENTS\[dept\]

dept\_name **= **dept.upper\(\) **if **dept **== **"hr" **else **dept.capitalize\(\) **return **\(

SwaigFunctionResult\(f"Transferring you to **\{**dept\_name**\} **now. Have a great day\!"\)

.connect\(number, final**=**True\)

\)

**if **\_\_name\_\_ **== **"\_\_main\_\_":

agent **= **ReceptionistAgent\(\)

agent.run\(\)

**6.18.10**

**Sending SMS During Transfer**

Notify the user via SMS before transfer:

**def **transfer\_with\_sms\(self, args, raw\_data\):

caller\_number **= **raw\_data.get\("caller\_id\_number"\)

**return **\(

SwaigFunctionResult\("I'm transferring you and sending a confirmation text."\)

.send\_sms\(

to\_number**=**caller\_number, 

from\_number**=**"\+15559876543", 

body**=**"You're being transferred to our support team. Reference \#12345" 

\)

.connect\("\+15551234567", final**=**True\)

\)

**6.18.11**

**Post-Process Transfer**

Use post\_process=True to have the AI speak before executing the transfer: **def **announced\_transfer\(self, args, raw\_data\):

**return **\(

SwaigFunctionResult\(

"Please hold while I transfer you to our specialist. " 

"This should only take a moment.", 

post\_process**=**True

*\# AI speaks this before transfer executes*

\)

.connect\("\+15551234567", final**=**True\)

\)

181

6. Advanced Features

**6.18.12 Transfer Methods Summary**

**Method**

**Use Case**

**Destination Types**

connect\(\)

Direct call transfer

Phone numbers, SIP URIs

swml\_transfer\(\)

Transfer to another agent

SWML endpoint URLs

**6.18.13 Best Practices**

**DO: **- Use post\_process=True to announce transfers - Validate destination numbers before transfer - Log transfers for tracking and compliance - Use final=False for consultation/return flows - Provide clear confirmation to the caller **DON’T: **- Transfer without informing the caller - Use hard-coded numbers without validation - Forget to handle transfer failures gracefully - Use final=True when you need the call to return 182

6. Advanced Features

**6.19 Multi-Agent Servers**

**Summary**: Run multiple agents on a single server using AgentServer. Each agent gets its own route, and you can configure SIP-based routing for username-to-agent mapping. 

**6.19.1 When to Use AgentServer**

**Single Agent \(agent.run\(\)\)**

**AgentServer**

One agent per process

Multiple agents per process

Simple deployment

Shared resources

Separate ports per agent

Single port, multiple routes

SIP username routing

Unified health checks

**6.19.2**

**Basic AgentServer**

from signalwire\_agents import AgentBase, AgentServer

**class **SalesAgent\(AgentBase\):

**def \_\_init\_\_**\(self\):

super\(\). **\_\_init\_\_**\(name**=**"sales-agent"\)

self.add\_language\("English", "en-US", "rime.spore"\) self.prompt\_add\_section\("Role", "You are a sales representative."\) **class **SupportAgent\(AgentBase\):

**def \_\_init\_\_**\(self\):

super\(\). **\_\_init\_\_**\(name**=**"support-agent"\)

self.add\_language\("English", "en-US", "rime.spore"\) self.prompt\_add\_section\("Role", "You are a support specialist."\) **if **\_\_name\_\_ **== **"\_\_main\_\_":

server **= **AgentServer\(host**=**"0.0.0.0", port**=**3000\) server.register\(SalesAgent\(\), "/sales"\)

server.register\(SupportAgent\(\), "/support"\)

server.run\(\)

Agents are available at: - http://localhost:3000/sales - http://localhost:3000/support - http://localhost:3000/health \(built-in health check\)

**6.19.3**

**AgentServer Configuration**

server **= **AgentServer\(

host**=**"0.0.0.0", 

*\# Bind address*

port**=**3000, 

*\# Listen port*

log\_level**=**"info" 

*\# debug, info, warning, error, critical*

\)

183

6. Advanced Features

**6.19.4 Registering Agents**

**6.19.4.1 With Explicit Route**

server.register\(SalesAgent\(\), "/sales"\)

**6.19.4.2 Using Agent’s Default Route**

**class **BillingAgent\(AgentBase\):

**def \_\_init\_\_**\(self\):

super\(\). **\_\_init\_\_**\(

name**=**"billing-agent", 

route**=**"/billing" 

*\# Default route*

\)

server.register\(BillingAgent\(\)\)

*\# Uses "/billing" *

**6.19.5**

**Server Architecture**

┌─────────────────────────────────────────────────────────────────────────────┐

│

AgentServer Architecture

│

├─────────────────────────────────────────────────────────────────────────────┤

│

│

│

AgentServer

│

│

\(FastAPI Application\)

│

│

│

│

│

┌────────────────────┼────────────────────┐

│

│

│

│

│

│

│

▼

▼

▼

│

│

┌─────────┐

┌─────────┐

┌─────────┐

│

│

│ /sales

│

│/support │

│/billing │

│

│

│

│

│

│

│

│

│

│

│ Sales

│

│ Support │

│ Billing │

│

│

│ Agent

│

│ Agent

│

│ Agent

│

│

│

└─────────┘

└─────────┘

└─────────┘

│

│

│

│

Each agent has:

│

│

• GET/POST /route

→ SWML document

│

│

• POST /route/swaig

→ Function calls

│

│

• POST /route/post\_prompt → Post-prompt handling

│

│

│

└─────────────────────────────────────────────────────────────────────────────┘

**6.19.6**

**Managing Agents**

**6.19.6.1**

**Get All Agents**

agents **= **server.get\_agents\(\)

**for **route, agent **in **agents:

print\(f" **\{**route**\}**: **\{**agent**. **get\_name\(\)**\}**"\) **6.19.6.2**

**Get Specific Agent**

sales\_agent **= **server.get\_agent\("/sales"\)

184

6. Advanced Features

**6.19.6.3 Unregister Agent**

server.unregister\("/sales"\)

**6.19.7 SIP Routing**

Route SIP calls to specific agents based on username:

from signalwire\_agents import AgentBase, AgentServer

**class **SalesAgent\(AgentBase\):

**def \_\_init\_\_**\(self\):

super\(\). **\_\_init\_\_**\(name**=**"sales-agent"\)

self.add\_language\("English", "en-US", "rime.spore"\) self.prompt\_add\_section\("Role", "You are a sales representative."\) **class **SupportAgent\(AgentBase\):

**def \_\_init\_\_**\(self\):

super\(\). **\_\_init\_\_**\(name**=**"support-agent"\)

self.add\_language\("English", "en-US", "rime.spore"\) self.prompt\_add\_section\("Role", "You are a support specialist."\) **if **\_\_name\_\_ **== **"\_\_main\_\_":

server **= **AgentServer\(\)

server.register\(SalesAgent\(\), "/sales"\)

server.register\(SupportAgent\(\), "/support"\)

*\# Enable SIP routing*

server.setup\_sip\_routing\("/sip", auto\_map**=**True\)

*\# Manual SIP username mapping*

server.register\_sip\_username\("sales-team", "/sales"\) server.register\_sip\_username\("help-desk", "/support"\) server.run\(\)

When auto\_map=True, the server automatically creates mappings: - Agent name → route \(e.g., “salesagent” →

“/sales”\) - Route path → route \(e.g., “sales” → “/sales”\)

185

6. Advanced Features

**6.19.8 SIP Routing Flow**

┌─────────────────────────────────────────────────────────────────────────────┐

│

SIP Routing Flow

│

├─────────────────────────────────────────────────────────────────────────────┤

│

│

│

SIP Call to: sip:sales-team@example.com

│

│

│

│

│

▼

│

│

┌──────────────────────┐

│

│

│

POST /sip

│

│

│

│

\(routing endpoint\)

│

│

│

└──────────────────────┘

│

│

│

│

│

▼

│

│

┌──────────────────────┐

│

│

│ Extract username:

│

│

│

│ "sales-team" 

│

│

│

└──────────────────────┘

│

│

│

│

│

▼

│

│

┌──────────────────────┐

│

│

│ Lookup route:

│

│

│

│ "/sales" 

│

│

│

└──────────────────────┘

│

│

│

│

│

▼

│

│

┌──────────────────────┐

│

│

│ Return SWML from

│

│

│

│ Sales Agent

│

│

│

└──────────────────────┘

│

│

│

└─────────────────────────────────────────────────────────────────────────────┘

**6.19.9**

**Health Check Endpoint**

AgentServer provides a built-in health check:

curl http://localhost:3000/health

Response:

**\{**

"status" **: **"ok" **, **

"agents" **: **2**, **

"routes" **: **\["/sales", "/support"\]

**\}**

**6.19.10**

**Serverless Deployment**

AgentServer supports serverless environments automatically:

from signalwire\_agents import AgentBase, AgentServer

**class **MyAgent\(AgentBase\):

**def \_\_init\_\_**\(self\):

super\(\). **\_\_init\_\_**\(name**=**"my-agent"\)

self.add\_language\("English", "en-US", "rime.spore"\) 186

6. Advanced Features

server **= **AgentServer\(\)

server.register\(MyAgent\(\), "/agent"\)

*\#\# AWS Lambda handler*

**def **lambda\_handler\(event, context\):

**return **server.run\(event, context\)

*\#\# CGI mode \(auto-detected\)*

**if **\_\_name\_\_ **== **"\_\_main\_\_":

server.run\(\)

**6.19.11**

**Complete Example**

*\#\!/usr/bin/env python3*

*\#\# multi\_agent\_server.py - Server with multiple specialized agents* from signalwire\_agents import AgentBase, AgentServer

from signalwire\_agents.core.function\_result import SwaigFunctionResult **class **SalesAgent\(AgentBase\):

**def \_\_init\_\_**\(self\):

super\(\). **\_\_init\_\_**\(name**=**"sales-agent"\)

self.add\_language\("English", "en-US", "rime.spore"\) self.prompt\_add\_section\(

"Role", 

"You are a sales representative for Acme Corp." 

\)

self.define\_tool\(

name**=**"get\_pricing", 

description**=**"Get product pricing", 

parameters**=**\{

"type": "object", 

"properties": \{

"product": \{"type": "string", "description": "Product name"\}

\}, 

"required": \["product"\]

\}, 

handler**=**self.get\_pricing

\)

**def **get\_pricing\(self, args, raw\_data\):

product **= **args.get\("product", ""\)

*\# Pricing lookup logic*

**return **SwaigFunctionResult\(f"The price for **\{**product**\} **is $99.99"\) **class **SupportAgent\(AgentBase\):

**def \_\_init\_\_**\(self\):

super\(\). **\_\_init\_\_**\(name**=**"support-agent"\)

self.add\_language\("English", "en-US", "rime.spore"\) self.prompt\_add\_section\(

"Role", 

"You are a technical support specialist." 

\)

self.define\_tool\(

name**=**"create\_ticket", 

description**=**"Create a support ticket", 

parameters**=**\{

"type": "object", 

"properties": \{

"issue": \{"type": "string", "description": "Issue description"\}

\}, 

"required": \["issue"\]

187

6. Advanced Features

\}, 

handler**=**self.create\_ticket

\)

**def **create\_ticket\(self, args, raw\_data\):

issue **= **args.get\("issue", ""\)

*\# Ticket creation logic*

**return **SwaigFunctionResult\(f"Created ticket \#12345 for: **\{**issue**\}**"\) **class **BillingAgent\(AgentBase\):

**def \_\_init\_\_**\(self\):

super\(\). **\_\_init\_\_**\(name**=**"billing-agent"\)

self.add\_language\("English", "en-US", "rime.spore"\) self.prompt\_add\_section\(

"Role", 

"You help customers with billing questions." 

\)

**if **\_\_name\_\_ **== **"\_\_main\_\_":

*\# Create server*

server **= **AgentServer\(host**=**"0.0.0.0", port**=**3000\)

*\# Register agents*

server.register\(SalesAgent\(\), "/sales"\)

server.register\(SupportAgent\(\), "/support"\)

server.register\(BillingAgent\(\), "/billing"\)

*\# Enable SIP routing*

server.setup\_sip\_routing\("/sip", auto\_map**=**True\)

*\# Custom SIP mappings*

server.register\_sip\_username\("sales", "/sales"\) server.register\_sip\_username\("help", "/support"\) server.register\_sip\_username\("accounts", "/billing"\) print\("Agents available:"\)

**for **route, agent **in **server.get\_agents\(\):

print\(f" 

**\{**route**\}**: **\{**agent**. **get\_name\(\)**\}**"\) server.run\(\)

**6.19.12**

**AgentServer Methods Summary**

**Method**

**Purpose**

register\(agent, route\)

Register an agent at a route

unregister\(route\)

Remove an agent

get\_agents\(\)

Get all registered agents

get\_agent\(route\)

Get agent by route

setup\_sip\_routing\(route, auto\_map\)

Enable SIP-based routing

register\_sip\_username\(username, route\)

Map SIP username to route

run\(\)

Start the server

188

6. Advanced Features

**6.19.13 Best Practices**

**DO: **- Use meaningful route names \(/sales, /support, /billing\) - Enable SIP routing for SIP-based deployments -

Monitor /health endpoint for availability - Use consistent naming between routes and SIP usernames **DON’T: **- Register duplicate routes - Forget to handle routing conflicts - Mix agent.run\(\) and AgentServer for the same agent

189

6. Advanced Features

**6.20**

**Search & Knowledge**

**Summary**: Add RAG-style knowledge search to your agents using local vector indexes \(.swsearch files\) or PostgreSQL with pgvector. Build indexes with sw-search CLI and integrate using the native\_vector\_search skill. 

**6.20.1 Search System Overview**

**Build Time:**

Documents → sw-search CLI → .swsearch file \(SQLite \+ vectors\)

**Runtime:**

Agent → native\_vector\_search skill → SearchEngine → Results

**Backends: **| Backend | Description | |———|————-| | SQLite | .swsearch files - Local, portable, no infrastructure

| | pgvector | PostgreSQL extension for production deployments | | Remote | Network mode for centralized search servers |

**6.20.2**

**Building Search Indexes**

Use the sw-search CLI to create search indexes:

*\#\# Basic usage - index a directory*

sw-search ./docs --output knowledge.swsearch

*\#\# Multiple directories*

sw-search ./docs ./examples --file-types md,txt,py

*\#\# Specific files*

sw-search README.md ./docs/guide.md

*\#\# Mixed sources*

sw-search ./docs README.md ./examples --file-types md,txt

**6.20.3**

**Chunking Strategies**

**Strategy**

**Best For**

**Parameters**

sentence

General text

--max-sentences-per-chunk

5

paragraph

Structured docs

\(default\)

sliding

Dense text

--chunk-size 100 --overla

p-size 20

page

PDFs

\(uses page boundaries\)

markdown

Documentation

\(header-aware, code

detection\)

semantic

Topic clustering

--semantic-threshold 0.6

topic

Long documents

--topic-threshold 0.2

qa

Q&A applications

\(optimized for questions\)

190

6. Advanced Features

**6.20.3.1 Markdown Chunking \(Recommended for Docs\)**

sw-search ./docs \\

--chunking-strategy markdown \\

--file-types md \\

--output docs.swsearch

This strategy: - Chunks at header boundaries - Detects code blocks and extracts language - Adds “code” tags to chunks containing code - Preserves section hierarchy in metadata

**6.20.3.2 Sentence Chunking**

sw-search ./docs \\

--chunking-strategy sentence \\

--max-sentences-per-chunk 10 \\

--output knowledge.swsearch

**6.20.4**

**Installing Search Dependencies**

*\#\# Query-only \(smallest footprint\)*

pip install signalwire-agents *\[* search *-* queryonly *\]*

*\#\# Build indexes \+ vector search*

pip install signalwire-agents *\[* search *\]*

*\#\# Full features \(PDF, DOCX processing\)*

pip install signalwire-agents *\[* search *-* full *\]*

*\#\# All features including NLP*

pip install signalwire-agents *\[* search *-* all *\]*

*\#\# PostgreSQL pgvector support*

pip install signalwire-agents *\[* pgvector *\]*

**6.20.5**

**Using Search in Agents**

Add the native\_vector\_search skill to enable search:

from signalwire\_agents import AgentBase

**class **KnowledgeAgent\(AgentBase\):

**def \_\_init\_\_**\(self\):

super\(\). **\_\_init\_\_**\(name**=**"knowledge-agent"\)

self.add\_language\("English", "en-US", "rime.spore"\) self.prompt\_add\_section\(

"Role", 

"You are a helpful assistant with access to company documentation. " 

"Use the search\_documents function to find relevant information." 

\)

*\# Add search skill with local index*

self.add\_skill\(

"native\_vector\_search", 

index\_file**=**"./knowledge.swsearch", 

count**=**5, 

*\# Number of results*

tool\_name**=**"search\_documents", 

tool\_description**=**"Search the company documentation" 

\)

**if **\_\_name\_\_ **== **"\_\_main\_\_":

agent **= **KnowledgeAgent\(\)

agent.run\(\)

191

6. Advanced Features

**6.20.6 Skill Configuration Options**

self.add\_skill\(

"native\_vector\_search", 

*\# Index source \(choose one\)*

index\_file**=**"./knowledge.swsearch", 

*\# Local SQLite index*

*\# OR*

*\# remote\_url="http://search-server:8001", \# Remote search server*

*\# index\_name="default", *

*\# Search parameters*

count**=**5, 

*\# Results to return \(1-20\)*

similarity\_threshold**=**0.0, 

*\# Min score \(0.0-1.0\)*

tags**=**\["docs", "api"\], 

*\# Filter by tags*

*\# Tool configuration*

tool\_name**=**"search\_knowledge", 

tool\_description**=**"Search the knowledge base for information" 

\)

**6.20.7**

**pgvector Backend**

For production deployments, use PostgreSQL with pgvector:

self.add\_skill\(

"native\_vector\_search", 

backend**=**"pgvector", 

connection\_string**=**"postgresql://user:pass@localhost/db", collection\_name**=**"knowledge\_base", 

count**=**5, 

tool\_name**=**"search\_docs" 

\)

192

6. Advanced Features

**6.20.8 Search Flow**

┌─────────────────────────────────────────────────────────────────────────────┐

│

Search Flow

│

├─────────────────────────────────────────────────────────────────────────────┤

│

│

│

User: "What is the return policy?" 

│

│

│

│

│

▼

│

│

┌────────────────────────────────────────┐

│

│

│ AI decides to call search\_documents\(\)

│

│

│

│ with query: "return policy" 

│

│

│

└────────────────────────────────────────┘

│

│

│

│

│

▼

│

│

┌────────────────────────────────────────┐

│

│

│ SearchEngine performs:

│

│

│

│

• Vector similarity search

│

│

│

│

• Keyword matching

│

│

│

│

• Metadata filtering

│

│

│

│

• Result ranking

│

│

│

└────────────────────────────────────────┘

│

│

│

│

│

▼

│

│

┌────────────────────────────────────────┐

│

│

│ Returns top results:

│

│

│

│

1. returns.md - "30-day return..." 

│

│

│

│

2. faq.md - "Return shipping..." 

│

│

│

│

3. policies.md - "Refund process..." 

│

│

│

└────────────────────────────────────────┘

│

│

│

│

│

▼

│

│

┌────────────────────────────────────────┐

│

│

│ AI synthesizes response using results

│

│

│

└────────────────────────────────────────┘

│

│

│

└─────────────────────────────────────────────────────────────────────────────┘

**6.20.9**

**CLI Commands**

**6.20.9.1**

**Build Index**

*\#\# Basic build*

sw-search ./docs --output knowledge.swsearch

*\#\# With specific file types*

sw-search ./docs --file-types md,txt,rst --output knowledge.swsearch

*\#\# With chunking strategy*

sw-search ./docs --chunking-strategy markdown --output knowledge.swsearch

*\#\# With tags*

sw-search ./docs --tags documentation,api --output knowledge.swsearch **6.20.9.2**

**Validate Index**

sw-search validate knowledge.swsearch

193

6. Advanced Features

**6.20.9.3 Search Index**

sw-search search knowledge.swsearch "how do I configure auth" 

**6.20.10 Complete Example**

*\#\!/usr/bin/env python3*

*\#\# documentation\_agent.py - Agent that searches documentation*

from signalwire\_agents import AgentBase

from signalwire\_agents.core.function\_result import SwaigFunctionResult **class **DocumentationAgent\(AgentBase\):

*"""Agent that searches documentation to answer questions""" *

**def \_\_init\_\_**\(self\):

super\(\). **\_\_init\_\_**\(name**=**"docs-agent"\)

self.add\_language\("English", "en-US", "rime.spore"\) self.prompt\_add\_section\(

"Role", 

"You are a documentation assistant. When users ask questions, " 

"search the documentation to find accurate answers. Always cite " 

"the source document when providing information." 

\)

self.prompt\_add\_section\(

"Instructions", 

""" 

1. When asked a question, use search\_docs to find relevant information 2. Review the search results carefully

3. Synthesize an answer from the results

4. Mention which document the information came from

5. If nothing relevant is found, say so honestly

""" 

\)

*\# Add a simple search function for demonstration*

*\# In production, use native\_vector\_search skill with a .swsearch index:*

*\# self.add\_skill\("native\_vector\_search", index\_file="./docs.swsearch"\)* self.define\_tool\(

name**=**"search\_docs", 

description**=**"Search the documentation for information", parameters**=**\{

"type": "object", 

"properties": \{

"query": \{"type": "string", "description": "Search query"\}

\}, 

"required": \["query"\]

\}, 

handler**=**self.search\_docs

\)

**def **search\_docs\(self, args, raw\_data\):

*"""Stub search function for demonstration""" *

query **= **args.get\("query", ""\)

**return **SwaigFunctionResult\(

f"Search results for ' **\{**query**\}**': This is a demonstration. " 

"In production, use native\_vector\_search skill with a .swsearch index file." 

\)

**if **\_\_name\_\_ **== **"\_\_main\_\_":

agent **= **DocumentationAgent\(\)

agent.run\(\)

**Note**: This example uses a stub function for demonstration. In production, use the native\_vector\_search skill with a .swsearch index file built using sw-search. 

194

6. Advanced Features

**6.20.11 Multiple Knowledge Bases**

Add multiple search instances for different topics:

*\#\# Product documentation*

self.add\_skill\(

"native\_vector\_search", 

index\_file**=**"./products.swsearch", 

tool\_name**=**"search\_products", 

tool\_description**=**"Search product catalog and specifications" 

\)

*\#\# Support articles*

self.add\_skill\(

"native\_vector\_search", 

index\_file**=**"./support.swsearch", 

tool\_name**=**"search\_support", 

tool\_description**=**"Search support articles and troubleshooting guides" 

\)

*\#\# API documentation*

self.add\_skill\(

"native\_vector\_search", 

index\_file**=**"./api-docs.swsearch", 

tool\_name**=**"search\_api", 

tool\_description**=**"Search API reference documentation" 

\)

**6.20.12**

**Search Best Practices**

**6.20.12.1**

**Index Building**

• Use markdown chunking for documentation

• Keep chunks reasonably sized \(5-10 sentences\)

• Add meaningful tags for filtering

• Rebuild indexes when source docs change

**6.20.12.2**

**Agent Configuration**

• Set count=3-5 for most use cases

• Use similarity\_threshold to filter noise

• Give descriptive tool\_name and tool\_description

• Tell AI when/how to use search in the prompt

**6.20.12.3**

**Production**

• Use pgvector for high-volume deployments

• Consider remote search server for shared indexes

• Monitor search latency and result quality

195

**Chapter 7**

**Deployment**

**Summary**: Deploy your agents as local servers, production services, or serverless functions. This chapter covers all deployment options from development to production. 

**7.1 What You’ll Learn**

This chapter covers deployment options:

1. **Local Development **- Running agents during development

2. **Production **- Deploying to production servers

3. **Serverless **- AWS Lambda, Google Cloud Functions, Azure Functions 4. **Docker & Kubernetes **- Container-based deployment

5. **CGI Mode **- Traditional web server deployment

**7.2**

**Deployment Options Overview**

**Environment**

**Options**

**Development**

agent.run\(\) on localhost, ngrok for public testing, auto-reload on changes **Production**

Uvicorn with workers, HTTPS with certificates, load balancing, health monitoring

**Serverless**

AWS Lambda, Google Cloud Functions, Azure Functions, auto-scaling, pay per invocation

**Container**

Docker, Kubernetes, auto-scaling, rolling updates, service mesh

**Traditional**

CGI mode, Apache/nginx integration, shared hosting compatible

196

7. Deployment

**7.3**

**Environment Detection**

The SDK automatically detects your deployment environment:

**Environment Variable**

**Detected Mode**

GATEWAY\_INTERFACE

CGI mode

AWS\_LAMBDA\_FUNCTION\_NAME

AWS Lambda

LAMBDA\_TASK\_ROOT

AWS Lambda

FUNCTION\_TARGET

Google Cloud Functions

K\_SERVICE

Google Cloud Functions

GOOGLE\_CLOUD\_PROJECT

Google Cloud Functions

AZURE\_FUNCTIONS\_ENVIRONMENT

Azure Functions

FUNCTIONS\_WORKER\_RUNTIME

Azure Functions

\(none of above\)

Server mode \(default\)

**7.4 Chapter Contents**

**Section**

**Description**

Local Development

Development server and testing

Production

Production server deployment

Serverless

Lambda, Cloud Functions, Azure

Docker & Kubernetes

Container deployment

CGI Mode

Traditional CGI deployment

**7.5**

**Quick Start**

from signalwire\_agents import AgentBase

**class **MyAgent\(AgentBase\):

**def \_\_init\_\_**\(self\):

super\(\). **\_\_init\_\_**\(name**=**"my-agent"\)

self.add\_language\("English", "en-US", "rime.spore"\) self.prompt\_add\_section\("Role", "You are a helpful assistant."\) **if **\_\_name\_\_ **== **"\_\_main\_\_":

agent **= **MyAgent\(\)

agent.run\(\)

*\# Automatically detects environment*

The run\(\) method automatically: - Detects serverless environments \(Lambda, Cloud Functions, Azure\) - Starts a development server on localhost for local development - Handles CGI mode when deployed to traditional web servers **7.6**

**Starting the Development Server**

The simplest way to run your agent locally:

from signalwire\_agents import AgentBase

**class **MyAgent\(AgentBase\):

**def \_\_init\_\_**\(self\):

super\(\). **\_\_init\_\_**\(name**=**"my-agent"\)

self.add\_language\("English", "en-US", "rime.spore"\) 197

7. Deployment

self.prompt\_add\_section\("Role", "You are a helpful assistant."\) **if **\_\_name\_\_ **== **"\_\_main\_\_":

agent **= **MyAgent\(\)

agent.run\(\)

*\# Starts on http://localhost:3000*

**7.7**

**Server Configuration**

**7.7.1 Custom Host and Port**

agent.run\(host**=**"0.0.0.0", port**=**8080\)

**7.7.2**

**Using serve\(\) Directly**

For more control, use serve\(\) instead of run\(\):

*\# Development server*

agent.serve\(host**=**"127.0.0.1", port**=**3000\)

*\# Listen on all interfaces*

agent.serve\(host**=**"0.0.0.0", port**=**3000\)

**7.8**

**Development Endpoints**

**Endpoint**

**Method**

**Purpose**

/

GET/POST

SWML document

/swaig

POST

SWAIG function calls

/post\_prompt

POST

Post-prompt handling

/debug

GET/POST

Debug information

/health

GET

Health check \(AgentServer

only\)

**7.9**

**Testing Your Agent**

**7.9.1**

**View SWML Output**

*\# Get the SWML document*

curl http://localhost:3000/

*\# Pretty print with jq*

curl http://localhost:3000/ **| **jq . 

**7.9.2**

**Using swaig-test CLI**

*\# List available functions*

swaig-test my\_agent.py --list-tools

*\# Test a specific function*

swaig-test my\_agent.py --exec get\_weather --city "Seattle" 

*\# Dump SWML output*

swaig-test my\_agent.py --dump-swml

198

7. Deployment

**7.10 Exposing Local Server**

SignalWire needs to reach your agent via a public URL. Use ngrok or similar: **Connection Flow: **SignalWire Cloud → ngrok tunnel → localhost:3000

**Steps: **1. Start your agent: python my\_agent.py 2. Start ngrok: ngrok http 3000 3. Use ngrok URL in SignalWire: https://abc123.ngrok.io

**7.10.1 Using ngrok**

*\# Start your agent*

python my\_agent.py

*\# In another terminal, start ngrok*

ngrok http 3000

ngrok provides a public URL like https://abc123.ngrok.io that forwards to your local server. 

**7.10.2**

**Using localtunnel**

*\# Install*

npm install -g localtunnel

*\# Start tunnel*

lt --port 3000

**7.11**

**Environment Variables for Development**

*\# Disable authentication for local testing*

export SWML\_BASIC\_AUTH\_USER**=**"" 

export SWML\_BASIC\_AUTH\_PASSWORD**=**"" 

*\# Or set custom credentials*

export SWML\_BASIC\_AUTH\_USER**=**"dev" 

export SWML\_BASIC\_AUTH\_PASSWORD**=**"test123" 

*\# Override proxy URL if behind ngrok*

export SWML\_PROXY\_URL\_BASE**=**"https://abc123.ngrok.io" 

**7.12**

**Proxy URL Configuration**

When behind ngrok or another proxy, the SDK needs to know the public URL: import os

*\# Option 1: Environment variable*

os.environ\['SWML\_PROXY\_URL\_BASE'\] **= **'https://abc123.ngrok.io' 

*\# Option 2: Auto-detection from X-Forwarded headers*

*\# The SDK automatically detects proxy from request headers*

199

7. Deployment

**7.13 Development Workflow**

**1. Code**

Write/modify your agent code. 

**2. Test Locally **- swaig-test my\_agent.py --dump-swml - swaig-test my\_agent.py --exec function\_name

--param value

**3. Run Server**

python my\_agent.py

**4. Expose Publicly**

ngrok http 3000

**5. Test with SignalWire**

Point phone number to ngrok URL and make test call. 

**7.14 Debug Mode**

Enable debug logging:

import logging

logging.basicConfig\(level**=**logging.DEBUG\)

agent **= **MyAgent\(\)

agent.run\(\)

Or via environment variable:

export SIGNALWIRE\_LOG\_MODE**=**default

python my\_agent.py

**7.15**

**Hot Reloading**

For automatic reloading during development, use uvicorn directly:

*\# Install uvicorn with reload support*

pip install uvicorn *\[* standard *\]*

*\# Run with auto-reload*

uvicorn my\_agent:agent.\_app --reload --host 0.0.0.0 --port 3000

Or create a development script:

*\# dev.py*

from my\_agent import MyAgent

agent **= **MyAgent\(\)

app **= **agent.\_app

*\# Expose the ASGI app for uvicorn*

Then run:

uvicorn dev:app --reload --port 3000

200

7. Deployment

**7.16 Serving Static Files**

Use AgentServer.serve\_static\_files\(\) to serve static files alongside your agents. This is useful for web dashboards, documentation, or any static content:

from signalwire\_agents import AgentServer

from pathlib import Path

*\# Create your agents*

from my\_agents import SupportAgent, SalesAgent

HOST **= **"0.0.0.0" 

PORT **= **3000

server **= **AgentServer\(host**=**HOST, port**=**PORT\)

server.register\(SupportAgent\(\), "/support"\)

server.register\(SalesAgent\(\), "/sales"\)

*\# Serve static files from web directory*

web\_dir **= **Path\(\_\_file\_\_\).parent **/ **"web" 

**if **web\_dir.exists\(\):

server.serve\_static\_files\(str\(web\_dir\)\)

server.run\(\)

**Directory Structure:**

my\_project/

├── server.py

├── my\_agents.py

└── web/

├── index.html

├── styles.css

└── app.js

**Key Points:**

• Use server.serve\_static\_files\(directory\) to serve static files

• Agent routes always take priority over static files

• Requests to / serve index.html from the static directory

• Both /support and /support/ work correctly with agents

**Route Priority:**

**Route**

**Handler**

/support

SupportAgent

/sales

SalesAgent

/health

AgentServer health check

/\*

Static files \(fallback\)

201

7. Deployment

**7.17 Common Development Issues**

**Issue**

**Solution**

Port already in use

Use different port: agent.run\(port=8080\)

401 Unauthorized

Check SWML\_BASIC\_AUTH\_\* env vars

Functions not found

Verify function registration

SWML URL wrong

Set SWML\_PROXY\_URL\_BASE for ngrok

Connection refused

Ensure agent is running on correct port

Static files not found

Check web\_dir.exists\(\) and path is correct

202

7. Deployment

**7.18**

**Production Deployment**

**Summary**: Deploy agents to production with proper SSL, authentication, monitoring, and scaling. Use uvicorn workers, nginx reverse proxy, and systemd for process management. 

**7.18.1 Production Checklist**

**7.18.1.1 Security**

□ HTTPS enabled with valid certificates

□ Basic authentication configured

□ Firewall rules in place

□ No secrets in code or logs

**7.18.1.2 Reliability**

□ Process manager \(systemd/supervisor\)

□ Health checks configured

□ Logging to persistent storage

□ Error monitoring/alerting

**7.18.1.3 Performance**

□ Multiple workers for concurrency

□ Reverse proxy \(nginx\) for SSL termination

□ Load balancing if needed

**7.18.2**

**Environment Variables**

*\#\# Authentication \(required for production\)*

export SWML\_BASIC\_AUTH\_USER**=**"your-username" 

export SWML\_BASIC\_AUTH\_PASSWORD**=**"your-secure-password" 

*\#\# SSL Configuration*

export SWML\_SSL\_ENABLED**=**"true" 

export SWML\_SSL\_CERT\_PATH**=**"/etc/ssl/certs/agent.crt" 

export SWML\_SSL\_KEY\_PATH**=**"/etc/ssl/private/agent.key" 

*\#\# Domain configuration*

export SWML\_DOMAIN**=**"agent.example.com" 

*\#\# Proxy URL \(if behind load balancer/reverse proxy\)*

export SWML\_PROXY\_URL\_BASE**=**"https://agent.example.com" 

**7.18.3**

**Running with Uvicorn Workers**

For production, run with multiple workers:

*\#\# Run with 4 workers*

uvicorn my\_agent:app --host 0.0.0.0 --port 3000 --workers 4

Create an entry point module:

*\#\# app.py*

from my\_agent import MyAgent

agent **= **MyAgent\(\)

app **= **agent.\_app

203

7. Deployment

**7.18.4 Systemd Service**

Create /etc/systemd/system/signalwire-agent.service:

**\[Unit\]**

Description=SignalWire AI Agent

After=network.target

**\[Service\]**

Type=simple

User=www-data

Group=www-data

WorkingDirectory=/opt/agent

Environment="PATH=/opt/agent/venv/bin" 

Environment="SWML\_BASIC\_AUTH\_USER=your-username" 

Environment="SWML\_BASIC\_AUTH\_PASSWORD=your-password" 

ExecStart=/opt/agent/venv/bin/uvicorn app:app --host 127.0.0.1 --port 3000 --workers 4

Restart=always

RestartSec=5

**\[Install\]**

WantedBy=multi-user.target

Enable and start:

**sudo **systemctl enable signalwire-agent

**sudo **systemctl start signalwire-agent

**sudo **systemctl status signalwire-agent

**7.18.5**

**Nginx Reverse Proxy**

\#\# /etc/nginx/sites-available/agent

server \{

listen 443 ssl http2; 

server\_name agent.example.com; 

ssl\_certificate /etc/ssl/certs/agent.crt; 

ssl\_certificate\_key /etc/ssl/private/agent.key; 

location / \{

proxy\_pass http://127.0.0.1:3000; 

proxy\_http\_version 1.1; 

proxy\_set\_header Host $host; 

proxy\_set\_header X-Real-IP $remote\_addr; 

proxy\_set\_header X-Forwarded-For $proxy\_add\_x\_forwarded\_for; 

proxy\_set\_header X-Forwarded-Proto $scheme; 

proxy\_set\_header X-Forwarded-Host $host; 

proxy\_read\_timeout 300s; 

proxy\_connect\_timeout 75s; 

\}

\}

server \{

listen 80; 

server\_name agent.example.com; 

return 301 https://$server\_name$request\_uri; 

\}

Enable the site:

**sudo **ln -s /etc/nginx/sites-available/agent /etc/nginx/sites-enabled/

**sudo **nginx -t

**sudo **systemctl reload nginx

204

7. Deployment

**7.18.6 Production Architecture**

┌─────────────────────────────────────────────────────────────────────────────┐

│

Production Architecture

│

├─────────────────────────────────────────────────────────────────────────────┤

│

│

│

Internet

│

│

│

│

│

▼

│

│

┌──────────────────┐

│

│

│

Load Balancer

│

\(optional, for high availability\)

│

│

└──────────────────┘

│

│

│

│

│

▼

│

│

┌──────────────────┐

│

│

│

Nginx

│

SSL termination, rate limiting

│

│

│

\(reverse proxy\)│

│

│

└──────────────────┘

│

│

│

│

│

▼

│

│

┌──────────────────┐

│

│

│

Uvicorn

│

Multiple workers \(--workers 4\)

│

│

│

\+ Agent

│

│

│

└──────────────────┘

│

│

│

│

│

▼

│

│

┌──────────────────┐

│

│

│

External APIs

│

Databases, services, etc. 

│

│

└──────────────────┘

│

│

│

└─────────────────────────────────────────────────────────────────────────────┘

**7.18.7**

**SSL Configuration**

**7.18.7.1**

**Using Environment Variables**

export SWML\_SSL\_ENABLED**=**"true" 

export SWML\_SSL\_CERT\_PATH**=**"/path/to/cert.pem" 

export SWML\_SSL\_KEY\_PATH**=**"/path/to/key.pem" 

**7.18.7.2**

**Let’s Encrypt with Certbot**

*\#\# Install certbot*

**sudo **apt install certbot python3-certbot-nginx

*\#\# Get certificate*

**sudo **certbot --nginx -d agent.example.com

*\#\# Auto-renewal is configured automatically*

**7.18.8**

**Health Checks**

For AgentServer deployments:

*\#\# Health check endpoint*

curl https://agent.example.com/health

Response:

205

7. Deployment

**\{**

"status" **: **"ok" **, **

"agents" **: **1**, **

"routes" **: **\["/"\]

**\}**

For load balancers, use this endpoint to verify agent availability. 

**7.18.9 Logging Configuration**

import logging

*\#\# Configure logging for production*

logging.basicConfig\(

level**=**logging.INFO, 

format**=**' **%\(asctime\)s **- **%\(name\)s **- **%\(levelname\)s **- **%\(message\)s**', handlers**=**\[

logging.FileHandler\('/var/log/agent/agent.log'\), 

logging.StreamHandler\(\)

\]

\)

Or use environment variable:

export SIGNALWIRE\_LOG\_MODE**=**default

**7.18.10**

**Monitoring**

**7.18.10.1**

**Prometheus Metrics**

Add custom metrics to your agent:

from prometheus\_client import Counter, Histogram, start\_http\_server

*\#\# Start metrics server on port 9090*

start\_http\_server\(9090\)

*\#\# Define metrics*

call\_counter **= **Counter\('agent\_calls\_total', 'Total calls handled'\) call\_duration **= **Histogram\('agent\_call\_duration\_seconds', 'Call duration'\) **7.18.10.2**

**External Monitoring**

• **Uptime monitoring**: Monitor the health endpoint

• **Log aggregation**: Ship logs to ELK, Datadog, or similar

• **APM**: Use Application Performance Monitoring tools

**7.18.11**

**Scaling Considerations**

**7.18.11.1**

**Vertical Scaling**

• Increase uvicorn workers \(--workers N\)

• Use larger server instances

• Optimize agent code and external calls

206

7. Deployment

**7.18.11.2 Horizontal Scaling**

• Multiple server instances behind load balancer

• Stateless agent design

• Shared session storage \(Redis\) if needed

**7.18.11.3 Serverless**

• Auto-scaling with Lambda/Cloud Functions

• Pay per invocation

• No server management

**7.18.12**

**Security Best Practices**

**DO: **- Use HTTPS everywhere - Set strong basic auth credentials - Use environment variables for secrets - Enable firewall and limit access - Regularly update dependencies - Monitor for suspicious activity **DON’T: **- Expose debug endpoints in production - Log sensitive data - Use default credentials - Disable SSL

verification - Run as root user

207

7. Deployment

**7.19 Serverless Deployment**

**Summary**: Deploy agents to AWS Lambda, Google Cloud Functions, or Azure Functions. The SDK

automatically detects serverless environments and adapts accordingly. 

**7.19.1 Serverless Overview**

**Platform**

**Detection**

**Handler**

AWS Lambda

AWS\_LAMBDA\_FUNCTION\_NAME

agent.run\(event, ctx\)

Google Cloud Functions

FUNCTION\_TARGET

agent.run\(request\)

Azure Functions

AZURE\_FUNCTIONS\_ENV

agent.run\(req\)

**Benefits: **- Auto-scaling - Pay per invocation - No server management - High availability **7.19.2**

**AWS Lambda**

**7.19.2.1 Basic Lambda Handler**

from signalwire\_agents import AgentBase

**class **MyAgent\(AgentBase\):

**def \_\_init\_\_**\(self\):

super\(\). **\_\_init\_\_**\(name**=**"my-agent"\)

self.add\_language\("English", "en-US", "rime.spore"\) self.prompt\_add\_section\("Role", "You are a helpful assistant."\)

*\#\# Create agent instance*

agent **= **MyAgent\(\)

**def **lambda\_handler\(event, context\):

*"""AWS Lambda entry point""" *

**return **agent.run\(event, context\)

**7.19.2.2**

**Lambda with API Gateway**

Configure API Gateway to pass requests to your Lambda:

*\#\# serverless.yml \(Serverless Framework\)*

**service: **signalwire-agent

**provider:**

**name: **aws

**runtime: **python3.11

**region: **us-east-1

**functions:**

**agent:**

**handler: **handler.lambda\_handler

**events:**

**- http:**

**path: **/

**method: **any

**- http:**

**path: **/\{proxy\+\}

**method: **any

208

7. Deployment

**7.19.2.3 Lambda Environment Variables**

*\#\# In serverless.yml*

**provider:**

**environment:**

**SWML\_BASIC\_AUTH\_USER: **$\{env:SWML\_BASIC\_AUTH\_USER\}

**SWML\_BASIC\_AUTH\_PASSWORD: **$\{env:SWML\_BASIC\_AUTH\_PASSWORD\}

**7.19.2.4 Lambda Request Flow**

┌─────────────────────────────────────────────────────────────────────────────┐

│

Lambda Request Flow

│

├─────────────────────────────────────────────────────────────────────────────┤

│

│

│

SignalWire

│

│

│

│

│

▼

│

│

┌──────────────────┐

│

│

│

API Gateway

│

HTTPS endpoint

│

│

└──────────────────┘

│

│

│

│

│

▼

│

│

┌──────────────────┐

│

│

│

Lambda

│

agent.run\(event, context\)

│

│

│

Function

│

│

│

└──────────────────┘

│

│

│

│

│

│

Path: /

→ Return SWML document

│

│

│

Path: /swaig

→ Execute SWAIG function

│

│

│

│

│

▼

│

│

┌──────────────────┐

│

│

│

Response

│

JSON response to SignalWire

│

│

└──────────────────┘

│

│

│

└─────────────────────────────────────────────────────────────────────────────┘

**7.19.3**

**Google Cloud Functions**

**7.19.3.1**

**Cloud Functions Handler**

from signalwire\_agents import AgentBase

**class **MyAgent\(AgentBase\):

**def \_\_init\_\_**\(self\):

super\(\). **\_\_init\_\_**\(name**=**"my-agent"\)

self.add\_language\("English", "en-US", "rime.spore"\) self.prompt\_add\_section\("Role", "You are a helpful assistant."\)

*\#\# Create agent instance*

agent **= **MyAgent\(\)

**def **main\(request\):

*"""Google Cloud Functions entry point""" *

**return **agent.run\(request\)

209

7. Deployment

**7.19.3.2 Deploying to Cloud Functions**

gcloud functions deploy signalwire-agent \\

--runtime python311 \\

--trigger-http \\

--allow-unauthenticated \\

--entry-point main \\

--set-env-vars SWML\_BASIC\_AUTH\_USER=user,SWML\_BASIC\_AUTH\_PASSWORD=pass **7.19.3.3 requirements.txt**

signalwire-agents>=1.0.2

**7.19.4**

**Azure Functions**

**7.19.4.1 Azure Functions Handler**

import azure.functions as func

from signalwire\_agents import AgentBase

**class **MyAgent\(AgentBase\):

**def \_\_init\_\_**\(self\):

super\(\). **\_\_init\_\_**\(name**=**"my-agent"\)

self.add\_language\("English", "en-US", "rime.spore"\) self.prompt\_add\_section\("Role", "You are a helpful assistant."\)

*\#\# Create agent instance*

agent **= **MyAgent\(\)

**def **main\(req: func.HttpRequest\) **-> **func.HttpResponse:

*"""Azure Functions entry point""" *

**return **agent.run\(req\)

**7.19.4.2**

**function.json**

**\{**

"scriptFile" **: **"\_\_init\_\_.py" **, **

"bindings" **: **\[

**\{**

"authLevel" **: **"anonymous" **, **

"type" **: **"httpTrigger" **, **

"direction" **: **"in" **, **

"name" **: **"req" **, **

"methods" **: **\["get", "post"\]**, **

"route" **: **"\{\*path\}" 

**\}**, 

**\{**

"type" **: **"http" **, **

"direction" **: **"out" **, **

"name" **: **"$return" 

**\}**

\]

**\}**

210

7. Deployment

**7.19.5 Testing Serverless Locally**

Use swaig-test to simulate serverless environments:

*\#\# Simulate AWS Lambda*

swaig-test my\_agent.py --simulate-serverless lambda --dump-swml

*\#\# Simulate Google Cloud Functions*

swaig-test my\_agent.py --simulate-serverless cloud\_function --dump-swml

*\#\# Simulate Azure Functions*

swaig-test my\_agent.py --simulate-serverless azure\_function --dump-swml **7.19.6**

**Force Mode Override**

For testing, you can force a specific execution mode:

*\#\# Force Lambda mode*

agent.run\(event**=**\{\}, context**=**None, force\_mode**=**'lambda'\)

*\#\# Force Cloud Functions mode*

agent.run\(request, force\_mode**=**'google\_cloud\_function'\)

*\#\# Force Azure mode*

agent.run\(req, force\_mode**=**'azure\_function'\)

**7.19.7**

**Serverless Best Practices**

**7.19.7.1**

**Cold Starts**

• Keep dependencies minimal

• Initialize agent outside handler function

• Use provisioned concurrency for low latency

**7.19.7.2**

**Timeouts**

• Set appropriate timeout \(Lambda: up to 15 min\)

• Account for external API calls

• Monitor and optimize slow functions

**7.19.7.3**

**Memory**

• Allocate sufficient memory

• More memory = more CPU in Lambda

• Monitor memory usage

**7.19.7.4**

**State**

• Design for statelessness

• Use external storage for persistent data

• Don’t rely on local filesystem

**7.19.8**

**Multi-Agent Serverless**

Deploy multiple agents with AgentServer:

from signalwire\_agents import AgentBase, AgentServer

**class **SalesAgent\(AgentBase\):

**def \_\_init\_\_**\(self\):

super\(\). **\_\_init\_\_**\(name**=**"sales-agent"\)

211

7. Deployment

self.add\_language\("English", "en-US", "rime.spore"\) **class **SupportAgent\(AgentBase\):

**def \_\_init\_\_**\(self\):

super\(\). **\_\_init\_\_**\(name**=**"support-agent"\)

self.add\_language\("English", "en-US", "rime.spore"\) server **= **AgentServer\(\)

server.register\(SalesAgent\(\), "/sales"\)

server.register\(SupportAgent\(\), "/support"\)

**def **lambda\_handler\(event, context\):

*"""Lambda handler for multi-agent server""" *

**return **server.run\(event, context\)

**7.19.9**

**Environment Detection**

The SDK detects serverless environments automatically:

**Environment Variable**

**Platform**

AWS\_LAMBDA\_FUNCTION\_NAME

AWS Lambda

LAMBDA\_TASK\_ROOT

AWS Lambda

FUNCTION\_TARGET

Google Cloud Functions

K\_SERVICE

Google Cloud Functions

GOOGLE\_CLOUD\_PROJECT

Google Cloud Functions

AZURE\_FUNCTIONS\_ENVIRONMENT

Azure Functions

FUNCTIONS\_WORKER\_RUNTIME

Azure Functions

212

7. Deployment

**7.20**

**Docker & Kubernetes**

**Summary**: Containerize your agents with Docker and deploy to Kubernetes for scalable, manageable production deployments. 

**7.20.1 Dockerfile**

**FROM **python:3.11-slim

**WORKDIR **/app

*\#\# Install dependencies*

**COPY **requirements.txt . 

**RUN **pip install --no-cache-dir -r requirements.txt

*\#\# Copy application*

**COPY **. . 

*\#\# Create non-root user*

**RUN **useradd -m appuser **&& chown **-R appuser:appuser /app **USER **appuser

*\#\# Expose port*

**EXPOSE **3000

*\#\# Run with uvicorn*

**CMD **\["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "3000", "--workers", "4"\]

**7.20.2**

**requirements.txt**

signalwire-agents>=1.0.2

uvicorn\[standard\]>=0.20.0

**7.20.3**

**Application Entry Point**

*\#\# app.py*

from signalwire\_agents import AgentBase

**class **MyAgent\(AgentBase\):

**def \_\_init\_\_**\(self\):

super\(\). **\_\_init\_\_**\(name**=**"my-agent"\)

self.add\_language\("English", "en-US", "rime.spore"\) self.prompt\_add\_section\("Role", "You are a helpful assistant."\) agent **= **MyAgent\(\)

app **= **agent.\_app

**7.20.4**

**Building and Running**

*\#\# Build image*

docker build -t signalwire-agent . 

*\#\# Run container*

docker run -d \\

-p 3000:3000 \\

-e SWML\_BASIC\_AUTH\_USER=myuser \\

-e SWML\_BASIC\_AUTH\_PASSWORD=mypassword \\

--name agent \\

signalwire-agent

*\#\# View logs*

213

7. Deployment

docker logs -f agent

*\#\# Stop container*

docker stop agent

**7.20.5 Docker Compose**

*\#\# docker-compose.yml*

**version: **'3.8' 

**services:**

**agent:**

**build: **. 

**ports:**

**- **"3000:3000" 

**environment:**

**- **SWML\_BASIC\_AUTH\_USER=$\{SWML\_BASIC\_AUTH\_USER\}

**- **SWML\_BASIC\_AUTH\_PASSWORD=$\{SWML\_BASIC\_AUTH\_PASSWORD\}

**- **SWML\_PROXY\_URL\_BASE=$\{SWML\_PROXY\_URL\_BASE\}

**restart: **unless-stopped

**healthcheck:**

**test: \[**"CMD" **, **"curl" **, **"-f" **, **"http://localhost:3000/health" **\]**

**interval: **30s

**timeout: **10s

**retries: **3

**nginx:**

**image: **nginx:alpine

**ports:**

**- **"443:443" 

**- **"80:80" 

**volumes:**

**- **./nginx.conf:/etc/nginx/nginx.conf:ro

**- **./certs:/etc/ssl/certs:ro

**depends\_on:**

**- **agent

**restart: **unless-stopped

Run with:

docker-compose up -d

**7.20.6**

**Kubernetes Deployment**

**7.20.6.1**

**Deployment Manifest**

*\#\# deployment.yaml*

**apiVersion: **apps/v1

**kind: **Deployment

**metadata:**

**name: **signalwire-agent

**labels:**

**app: **signalwire-agent

**spec:**

**replicas: **3

**selector:**

**matchLabels:**

**app: **signalwire-agent

**template:**

**metadata:**

**labels:**

**app: **signalwire-agent

**spec:**

**containers:**

**- name: **agent

**image: **your-registry/signalwire-agent:latest

214

7. Deployment

**ports:**

**- containerPort: **3000

**env:**

**- name: **SWML\_BASIC\_AUTH\_USER

**valueFrom:**

**secretKeyRef:**

**name: **agent-secrets

**key: **auth-user

**- name: **SWML\_BASIC\_AUTH\_PASSWORD

**valueFrom:**

**secretKeyRef:**

**name: **agent-secrets

**key: **auth-password

**resources:**

**requests:**

**memory: **"256Mi" 

**cpu: **"250m" 

**limits:**

**memory: **"512Mi" 

**cpu: **"500m" 

**livenessProbe:**

**httpGet:**

**path: **/health

**port: **3000

**initialDelaySeconds: **10

**periodSeconds: **30

**readinessProbe:**

**httpGet:**

**path: **/health

**port: **3000

**initialDelaySeconds: **5

**periodSeconds: **10

**7.20.6.2**

**Service Manifest**

*\#\# service.yaml*

**apiVersion: **v1

**kind: **Service

**metadata:**

**name: **signalwire-agent

**spec:**

**selector:**

**app: **signalwire-agent

**ports:**

**- protocol: **TCP

**port: **80

**targetPort: **3000

**type: **ClusterIP

**7.20.6.3**

**Ingress Manifest**

*\#\# ingress.yaml*

**apiVersion: **networking.k8s.io/v1

**kind: **Ingress

**metadata:**

**name: **signalwire-agent

**annotations:**

**nginx.ingress.kubernetes.io/ssl-redirect: **"true" 

**cert-manager.io/cluster-issuer: **"letsencrypt-prod" 

**spec:**

**ingressClassName: **nginx

**tls:**

**- hosts:**

**- **agent.example.com

**secretName: **agent-tls

**rules:**

**- host: **agent.example.com

**http:**

215

7. Deployment

**paths:**

**- path: **/

**pathType: **Prefix

**backend:**

**service:**

**name: **signalwire-agent

**port:**

**number: **80

**7.20.6.4 Secrets**

*\#\# secrets.yaml*

**apiVersion: **v1

**kind: **Secret

**metadata:**

**name: **agent-secrets

**type: **Opaque

**stringData:**

**auth-user: **your-username

**auth-password: **your-secure-password

**7.20.7**

**Kubernetes Architecture**

┌─────────────────────────────────────────────────────────────────────────────┐

│

Kubernetes Architecture

│

├─────────────────────────────────────────────────────────────────────────────┤

│

│

│

Internet

│

│

│

│

│

▼

│

│

┌──────────────────┐

│

│

│

Ingress

│

SSL termination, routing

│

│

│

\(nginx/traefik\)│

│

│

└──────────────────┘

│

│

│

│

│

▼

│

│

┌──────────────────┐

│

│

│

Service

│

Load balancing across pods

│

│

│

\(ClusterIP\)

│

│

│

└──────────────────┘

│

│

│

│

│

├──────────────┬──────────────┐

│

│

▼

▼

▼

│

│

┌────────┐

┌────────┐

┌────────┐

│

│

│

Pod

│

│

Pod

│

│

Pod

│

replicas: 3

│

│

│ Agent

│

│ Agent

│

│ Agent

│

│

│

└────────┘

└────────┘

└────────┘

│

│

│

└─────────────────────────────────────────────────────────────────────────────┘

**7.20.8**

**Deploying to Kubernetes**

*\#\# Create secrets*

kubectl apply -f secrets.yaml

*\#\# Deploy application*

kubectl apply -f deployment.yaml

kubectl apply -f service.yaml

kubectl apply -f ingress.yaml

*\#\# Check status*

kubectl get pods -l app=signalwire-agent

kubectl get svc signalwire-agent

216

7. Deployment

kubectl get ingress signalwire-agent

*\#\# View logs*

kubectl logs -f -l app=signalwire-agent

*\#\# Scale deployment*

kubectl scale deployment signalwire-agent --replicas**=**5

**7.20.9 Horizontal Pod Autoscaler**

*\#\# hpa.yaml*

**apiVersion: **autoscaling/v2

**kind: **HorizontalPodAutoscaler

**metadata:**

**name: **signalwire-agent

**spec:**

**scaleTargetRef:**

**apiVersion: **apps/v1

**kind: **Deployment

**name: **signalwire-agent

**minReplicas: **2

**maxReplicas: **10

**metrics:**

**- type: **Resource

**resource:**

**name: **cpu

**target:**

**type: **Utilization

**averageUtilization: **70

**7.20.10**

**Multi-Architecture Builds**

*\#\# Build for multiple architectures*

**FROM --platform=$TARGETPLATFORM **python:3.11-slim

*\#\# ... rest of Dockerfile*

Build with:

docker buildx build --platform linux/amd64,linux/arm64 -t your-registry/agent:latest --push . 

**7.20.11**

**Container Best Practices**

**7.20.11.1**

**Security**

• Run as non-root user

• Use minimal base images \(slim, alpine\)

• Scan images for vulnerabilities

• Don’t store secrets in images

**7.20.11.2**

**Performance**

• Use multi-stage builds to reduce image size

• Layer dependencies efficiently

• Set appropriate resource limits

217

7. Deployment

**7.20.11.3 Reliability**

• Add health checks

• Use restart policies

• Configure proper logging

• Set graceful shutdown handling

218

7. Deployment

**7.21 CGI Mode**

**Summary**: Deploy agents as CGI scripts on traditional web servers like Apache or nginx. The SDK

automatically detects CGI environments and handles requests appropriately. 

**7.21.1 CGI Overview**

CGI \(Common Gateway Interface\) allows web servers to execute scripts and return their output as HTTP responses. 

**Benefits: **- Works with shared hosting - Simple deployment - just upload files - No separate process management -

Compatible with Apache, nginx

**Drawbacks: **- New process per request \(slower\) - No persistent connections - Limited scalability **7.21.2**

**CGI Detection**

The SDK detects CGI mode via the GATEWAY\_INTERFACE environment variable:

*\#\# Automatic detection*

**if **os.getenv\('GATEWAY\_INTERFACE'\):

*\# CGI mode detected*

mode **= **'cgi' 

**7.21.3**

**Basic CGI Script**

*\#\!/usr/bin/env python3*

*\#\# agent.py - Basic CGI agent script*

from signalwire\_agents import AgentBase

**class **MyAgent\(AgentBase\):

**def \_\_init\_\_**\(self\):

super\(\). **\_\_init\_\_**\(name**=**"my-agent"\)

self.add\_language\("English", "en-US", "rime.spore"\) self.prompt\_add\_section\("Role", "You are a helpful assistant."\) **if **\_\_name\_\_ **== **"\_\_main\_\_":

agent **= **MyAgent\(\)

agent.run\(\)

*\# Automatically detects CGI mode*

Make it executable:

**chmod **\+x agent.py

219

7. Deployment

**7.21.4 CGI Request Flow**

┌─────────────────────────────────────────────────────────────────────────────┐

│

CGI Request Flow

│

├─────────────────────────────────────────────────────────────────────────────┤

│

│

│

SignalWire

│

│

│

│

│

▼

│

│

┌──────────────────┐

│

│

│

Web Server

│

Apache/nginx

│

│

│

\(httpd\)

│

│

│

└──────────────────┘

│

│

│

│

│

│

Sets environment variables:

│

│

│

• GATEWAY\_INTERFACE=CGI/1.1

│

│

│

• PATH\_INFO=/swaig

│

│

│

• CONTENT\_LENGTH=... 

│

│

│

│

│

▼

│

│

┌──────────────────┐

│

│

│

Python CGI

│

agent.py

│

│

│

Script

│

│

│

└──────────────────┘

│

│

│

│

│

│

PATH\_INFO="" 

→ Return SWML document

│

│

│

PATH\_INFO=/swaig → Execute SWAIG function

│

│

│

│

│

▼

│

│

┌──────────────────┐

│

│

│

stdout

│

JSON response to web server

│

│

└──────────────────┘

│

│

│

└─────────────────────────────────────────────────────────────────────────────┘

**7.21.5**

**Apache Configuration**

**7.21.5.1**

**Enable CGI**

*\#\# Enable CGI module*

LoadModule cgi\_module modules/mod\_cgi.so

*\#\# Configure CGI directory*

**<Directory **"/var/www/cgi-bin" **> **

Options **\+ExecCGI**

AddHandler cgi-script .py

Require all granted

**</Directory> **

**7.21.5.2**

**Virtual Host Configuration**

**<VirtualHost **\*:443**> **

ServerName agent.example.com

SSLEngine **on**

SSLCertificateFile /etc/ssl/certs/agent.crt

SSLCertificateKeyFile /etc/ssl/private/agent.key

ScriptAlias / /var/www/cgi-bin/agent.py

**<Directory **"/var/www/cgi-bin" **> **

Options **\+ExecCGI**

220

7. Deployment

SetHandler cgi-script

Require all granted

**</Directory> **

*\# Set environment variables*

SetEnv SWML\_BASIC\_AUTH\_USER "myuser" 

SetEnv SWML\_BASIC\_AUTH\_PASSWORD "mypassword" 

**</VirtualHost> **

**7.21.6 nginx Configuration**

nginx doesn’t natively support CGI, but you can use FastCGI with fcgiwrap: server \{

listen 443 ssl; 

server\_name agent.example.com; 

ssl\_certificate /etc/ssl/certs/agent.crt; 

ssl\_certificate\_key /etc/ssl/private/agent.key; 

location / \{

fastcgi\_pass unix:/var/run/fcgiwrap.socket; 

fastcgi\_param SCRIPT\_FILENAME /var/www/cgi-bin/agent.py; 

fastcgi\_param GATEWAY\_INTERFACE CGI/1.1; 

fastcgi\_param PATH\_INFO $uri; 

fastcgi\_param SWML\_BASIC\_AUTH\_USER "myuser"; 

fastcgi\_param SWML\_BASIC\_AUTH\_PASSWORD "mypassword"; 

include fastcgi\_params; 

\}

\}

**7.21.7**

**CGI Host Configuration**

In CGI mode, the SDK needs to know the external hostname for generating URLs:

*\#\# Using swaig-test to simulate CGI mode*

swaig-test my\_agent.py --simulate-serverless cgi --cgi-host agent.example.com Or set environment variable:

SetEnv SWML\_PROXY\_URL\_BASE "https://agent.example.com" 

**7.21.8**

**Testing CGI Locally**

Use swaig-test to simulate CGI environment:

*\#\# Test SWML generation in CGI mode*

swaig-test my\_agent.py --simulate-serverless cgi --dump-swml

*\#\# With custom host*

swaig-test my\_agent.py --simulate-serverless cgi --cgi-host mysite.com --dump-swml

*\#\# Test a function*

swaig-test my\_agent.py --simulate-serverless cgi --exec function\_name --param value 221

7. Deployment

**7.21.9 Authentication in CGI Mode**

The SDK checks basic auth in CGI mode:

*\#\# Authentication is automatic when these are set*

*\#\# SWML\_BASIC\_AUTH\_USER*

*\#\# SWML\_BASIC\_AUTH\_PASSWORD*

*\#\# The SDK reads Authorization header and validates*

If authentication fails, returns 401 with WWW-Authenticate header. 

**7.21.10**

**Directory Structure**

/var/www/cgi-bin/

├── agent.py

\# Main CGI script

├── requirements.txt

\# Dependencies

└── venv/

\# Virtual environment \(optional\)

**7.21.11**

**Shared Hosting Deployment**

For shared hosting where you can’t install system packages:

*\#\!/usr/bin/env python3*

*\#\# agent\_shared.py - CGI agent for shared hosting*

import sys

import os

*\#\# Add local packages directory*

sys.path.insert\(0, os.path.join\(os.path.dirname\(\_\_file\_\_\), 'packages'\)\) from signalwire\_agents import AgentBase

**class **MyAgent\(AgentBase\):

**def \_\_init\_\_**\(self\):

super\(\). **\_\_init\_\_**\(name**=**"my-agent"\)

self.add\_language\("English", "en-US", "rime.spore"\) **if **\_\_name\_\_ **== **"\_\_main\_\_":

agent **= **MyAgent\(\)

agent.run\(\)

Install packages locally:

pip install --target**=**./packages signalwire-agents

**7.21.12**

**CGI Best Practices**

**7.21.12.1**

**Performance**

• Keep imports minimal - each request starts fresh

• Consider FastCGI for better performance

• Cache what you can \(but remember process dies\)

222

7. Deployment

**7.21.12.2 Security**

• Set proper file permissions \(750 or 755\)

• Don’t expose .py files directly if possible

• Use HTTPS always

• Set auth credentials as environment variables

**7.21.12.3 Debugging**

• Check web server error logs

• Verify shebang line \(\#\!/usr/bin/env python3\)

• Test script from command line first

• Ensure proper line endings \(LF, not CRLF\)

**7.21.13**

**Common CGI Issues**

**Issue**

**Solution**

500 Internal Server Error

Check error logs, verify permissions

Permission denied

chmod \+x agent.py

Module not found

Check sys.path, install dependencies

Wrong Python version

Update shebang to correct Python

Malformed headers

Ensure proper Content-Type output

Timeout

Optimize code, increase server timeout

**7.21.14**

**Migration from CGI**

When you outgrow CGI:

**7.21.14.1**

**CGI → FastCGI**

Keep same code, use fcgiwrap or gunicorn. Better performance, persistent processes. 

**7.21.14.2**

**CGI → Server Mode**

Same code works - just run differently \(python agent.py instead of CGI\). Add systemd service, nginx reverse proxy. 

**7.21.14.3**

**CGI → Serverless**

Same code works with minor changes. Add Lambda handler wrapper. Deploy to AWS/GCP/Azure. 

223

**Chapter 8**

**SignalWire Integration**

**Summary**: Connect your agents to phone numbers through SignalWire. This chapter covers account setup, phone number configuration, and testing your voice agents. 

**8.1 What You’ll Learn**

This chapter covers SignalWire integration:

1. **Account Setup **- Create and configure your SignalWire account 2. **Phone Numbers **- Purchase and manage phone numbers

3. **Mapping Numbers **- Connect phone numbers to your agents

4. **Testing **- Test your agents before going live

5. **Troubleshooting **- Common issues and solutions

**8.2**

**Integration Overview**

┌─────────────────────────────────────────────────────────────────────────────┐

│

SignalWire Integration

│

├─────────────────────────────────────────────────────────────────────────────┤

│

│

│

┌─────────┐

┌─────────────┐

┌─────────────┐

┌─────────────┐

│

│

│ Caller

│ →

│ SignalWire

│ →

│ Your Server │ →

│

Agent

│

│

│

│

Phone

│

│

Network

│

│

\(SWML\)

│

│

Logic

│

│

│

└─────────┘

└─────────────┘

└─────────────┘

└─────────────┘

│

│

│

│

1. Caller dials your phone number

│

│

2. SignalWire receives the call

│

│

3. SignalWire requests SWML from your server

│

│

4. Your agent handles the conversation

│

│

│

└─────────────────────────────────────────────────────────────────────────────┘

**8.3**

**Prerequisites**

Before connecting to SignalWire:

• Working agent \(tested locally\)

• Publicly accessible server

• SignalWire account

224

8. SignalWire Integration

**8.4 Chapter Contents**

**Section**

**Description**

Account Setup

Create SignalWire account and project

Phone Numbers

Purchase and manage numbers

Mapping Numbers

Connect numbers to agents

Testing

Test calls and debugging

Troubleshooting

Common issues and fixes

**8.5 Quick Integration Steps**

**8.5.1**

**Step 1: Account Setup**

• Create SignalWire account

• Create a project

• Note your Space Name

**8.5.2**

**Step 2: Phone Number**

• Purchase a phone number

• Or use a SIP endpoint

**8.5.3**

**Step 3: Deploy Agent**

• Deploy agent to public URL

• Verify HTTPS is working

• Test SWML endpoint responds

**8.5.4**

**Step 4: Connect**

• Point phone number to agent URL

• Make test call

• Verify agent responds

225

8. SignalWire Integration

**8.6 Architecture**

┌─────────────────────────────────────────────────────────────────────────────┐

│

Call Flow Architecture

│

├─────────────────────────────────────────────────────────────────────────────┤

│

│

│

┌───────────────────────────────────────────────────────────────────────┐

│

│

│

SignalWire Cloud

│

│

│

│

┌─────────────────────────────────────────────────────────────────┐

│

│

│

│

│ Inbound Call

SWML Processor

│

│

│

│

│

│

→

│

│

│

│

│

│

• Fetches SWML from your server

│

│

│

│

│

│

• Executes AI verbs

│

│

│

│

│

│

• Handles speech

│

│

│

│

│

│

• Calls SWAIG funcs

│

│

│

│

│

│

│

│

│

│

│

│

└──────────────────────────────┼──────────────────────────────────┘

│

│

│

└─────────────────────────────────┼─────────────────────────────────────┘

│

│

│

│

│

▼ HTTPS

│

│

│

│

┌───────────────────────────────────────────────────────────────────────┐

│

│

│

Your Server

│

│

│

│

┌─────────────────────────────────────────────────────────────────┐

│

│

│

│

│

Agent \(SWML\)

│

│

│

│

│

│

│

│

│

│

│

│

• Returns SWML doc

│

│

│

│

│

│

• Handles functions

│

│

│

│

│

│

• Business logic

│

│

│

│

│

│

│

│

│

│

│

└─────────────────────────────────────────────────────────────────┘

│

│

│

└───────────────────────────────────────────────────────────────────────┘

│

│

│

└─────────────────────────────────────────────────────────────────────────────┘

**8.7**

**Required URLs**

Your agent needs to be accessible at these endpoints:

**Endpoint**

**Method**

**Purpose**

/

POST

Main SWML document

/swaig

POST

SWAIG function calls

**8.8**

**Security Considerations**

• Always use HTTPS for production

• Enable basic auth for SWML endpoints

• Use secure tokens for SWAIG functions

• Don’t expose sensitive data in prompts

• Monitor for unusual call patterns

Let’s start with setting up your SignalWire account. 

226

8. SignalWire Integration

**8.9 Create Account**

1. Go to signalwire.com

2. Click Sign Up or Login

3. Complete registration with email and password

4. Verify your email address

**Note: **If you have problems verifying your account, email support@signalwire.com **8.10 Create a Project**

After logging in:

1. Navigate to Projects in the dashboard

2. Click “Create New Project” 

3. Enter a project name \(e.g., “Voice Agents”\)

4. Select your use case

**8.11 Space Name**

Your Space Name is your unique SignalWire identifier. 

**URL Format: **https://YOUR-SPACE-NAME.signalwire.com

**Example: **https://mycompany.signalwire.com

**You’ll need this for: **- API authentication - Dashboard access - SWML webhook configuration **8.12**

**API Credentials**

Get your API credentials from the project:

1. Go to API Credentials

2. Note your Project ID

3. Create an API Token if needed

**Credential**

**Format**

Project ID

xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx

API Token

PTxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

Space Name

your-space

**Keep these secure - don’t commit to version control\! **

**8.13**

**Environment Variables**

Set these for your agent:

export SIGNALWIRE\_PROJECT\_ID**=**"your-project-id" 

export SIGNALWIRE\_API\_TOKEN**=**"your-api-token" 

export SIGNALWIRE\_SPACE\_NAME**=**"your-space" 

227

8. SignalWire Integration

**8.14 Dashboard Overview**

**Section**

**Purpose**

**Phone Numbers**

Purchase and manage phone numbers

**SWML**

Configure SWML scripts and webhooks

**Logs**

View call history and debugging info

**API Credentials**

Credentials and API explorer

**Billing**

Account balance and usage

**8.15 Add Credit**

Before making calls:

1. Go to Billing

2. Add payment method

3. Add credit to your account

Trial accounts may have limited credit for testing. 

**8.16 Account Verification**

Some features require account verification:

• Phone number purchases

• Outbound calling

• Certain number types

Complete verification in Account Settings if prompted. 

**8.17**

**Next Steps**

With your account ready:

1. Purchase a phone number

2. Deploy your agent

3. Connect the number to your agent

228

8. SignalWire Integration

**8.18**

**Phone Numbers**

**Summary**: Purchase and configure phone numbers to receive calls for your agents. 

**8.18.1 Purchasing Numbers**

1. Go to Phone Numbers in dashboard 2. Click “Buy a New Phone Number” 

3. Search by area code or location

4. Select a number and purchase

**8.18.2**

**Number Types**

**Type**

**Description**

**Use Case**

Local

Standard local numbers

General business use

Toll-Free

800/888/877/866 numbers

Customer service

Short Code

5-6 digit numbers

SMS campaigns

**8.18.3**

**Number Features**

Each number can support:

**Feature**

**Description**

Voice

Inbound/outbound calls

SMS

Text messaging

MMS

Picture messaging

Fax

Fax transmission

**8.18.4**

**Managing Numbers**

View your numbers in Phone Numbers section. Each number shows: **Field**

**Example**

Number

\+1 \(555\) 123-4567

Type

Local

Capabilities

Voice, SMS

Status

Active

Voice Handler

https://your-server.com/agent

**Available Actions: **- Edit Settings - View Logs - Release Number **8.18.5**

**Number Settings**

Configure each number:

**Voice Settings: **- Accept Incoming: Enable/disable - Voice URL: Your agent’s SWML endpoint - Fallback URL: Backup if primary fails

**SMS Settings: **- Accept Incoming: Enable/disable - Message URL: Webhook for SMS

229

8. SignalWire Integration

**8.18.6 SIP Endpoints**

Alternative to phone numbers - use SIP for testing. 

**SIP Address Format: **sip:username@your-space.signalwire.com

**Use with: **- Software phones \(Zoiper, Linphone\) - SIP-enabled devices - Testing without PSTN charges **8.18.7 Number Porting**

Bring existing numbers to SignalWire:

1. Go to Phone Numbers > Porting Request

2. Submit porting request

3. Provide current carrier info

4. Wait for port completion \(~1 week in most cases\)

**8.18.8**

**Costs**

**Phone Number Costs: **- Monthly rental fee per number - Varies by number type and country **Voice Usage: **- Per-minute charges for calls - Inbound vs outbound rates differ - See Voice Pricing

**AI Agent Usage: **- Per-minute AI processing costs - Includes STT, TTS, and LLM usage - See AI Agent Pricing

**Questions? **Contact sales@signalwire.com for custom pricing and volume discounts. 

**8.18.9**

**Multiple Numbers**

You can have multiple numbers pointing to:

• Same agent \(multiple entry points\)

• Different agents \(department routing\)

• Different configurations per number

*\#\# Agent can check which number was called*

**def **my\_handler\(self, args, raw\_data\):

called\_number **= **raw\_data.get\("called\_id\_num"\)

**if **called\_number **== **"\+15551234567":

**return **SwaigFunctionResult\("Sales line"\)

**else**:

**return **SwaigFunctionResult\("Support line"\)

230

8. SignalWire Integration

**8.19**

**Mapping Numbers**

**Summary**: Connect phone numbers to your agent’s SWML endpoint so calls are handled by your agent. 

**8.19.1 Overview**

┌─────────────────────────────────────────────────────────────────────────────┐

│

Number to Agent Mapping

│

├─────────────────────────────────────────────────────────────────────────────┤

│

│

│

Phone Number

→

Voice URL

→

Agent

│

│

\+1 \(555\) 123-4567

https://server/

SupportAgent

│

│

\+1 \(555\) 987-6543

https://server/sales

SalesAgent

│

│

│

│

When a call comes in:

│

│

1. SignalWire receives call on your number

│

│

2. SignalWire makes POST request to Voice URL

│

│

3. Your server returns SWML document

│

│

4. SignalWire executes the SWML \(runs your agent\)

│

│

│

└─────────────────────────────────────────────────────────────────────────────┘

**8.19.2**

**Configure Voice URL**

1. Go to Phone Numbers in dashboard

2. Click on your number

3. Set Voice URL to your agent endpoint

4. Save changes

**8.19.3**

**URL Format**

Your agent URL structure:

**Single Agent:**

https://your-server.com/

**Multiple Agents:**

https://your-server.com/support

https://your-server.com/sales

https://your-server.com/billing

**With Authentication:**

https://user:pass@your-server.com/

**8.19.4**

**HTTPS Requirements**

**Production: **- HTTPS required - Valid SSL certificate - Properly configured domain **Development: **- Use ngrok or similar tunnel - ngrok provides HTTPS automatically - Update URL when tunnel restarts

231

8. SignalWire Integration

**8.19.5 Using ngrok for Development**

*\#\# Start your agent locally*

python my\_agent.py

*\#\# In another terminal, start ngrok*

ngrok http 3000

*\#\# Use the ngrok HTTPS URL in SignalWire*

*\#\# https://abc123.ngrok.io*

**8.19.6**

**Basic Authentication**

Set authentication credentials:

from signalwire\_agents import AgentBase

**class **SecureAgent\(AgentBase\):

**def \_\_init\_\_**\(self\):

super\(\). **\_\_init\_\_**\(

name**=**"secure-agent", 

*\# Basic auth credentials*

*\# Also configurable via environment variables:*

*\# SWML\_BASIC\_AUTH\_USER, SWML\_BASIC\_AUTH\_PASSWORD*

\)

In SignalWire, use URL with credentials:

https://username:password@your-server.com/

**8.19.7**

**Multi-Agent Server**

Run multiple agents on one server:

from signalwire\_agents import AgentServer

server **= **AgentServer\(\)

*\#\# Register agents at different paths*

server.register\(SupportAgent\(\), "/support"\)

server.register\(SalesAgent\(\), "/sales"\)

server.register\(BillingAgent\(\), "/billing"\)

server.run\(host**=**"0.0.0.0", port**=**3000\)

Map each number to its agent:

**Number**

**Voice URL**

\+1 \(555\) 111-1111

https://server.com/support

\+1 \(555\) 222-2222

https://server.com/sales

\+1 \(555\) 333-3333

https://server.com/billing

232

8. SignalWire Integration

**8.19.8 SWML Scripts**

Alternative: Use SWML scripts directly in SignalWire:

**\{**

"version" **: **"1.0.0" **, **

"sections" **: \{**

"main" **: **\[

**\{**

"ai" **: \{**

"prompt" **: \{**

"text" **: **"You are a helpful assistant." 

**\}, **

"SWAIG" **: \{**

"defaults" **: \{**

"web\_hook\_url" **: **"https://your-server.com/swaig" 

**\}**

**\}**

**\}**

**\}**

\]

**\}**

**\}**

**8.19.9**

**Fallback URL**

Configure a fallback for errors:

**Setting**

**Value**

Primary URL

https://your-server.com/agent

Fallback URL

https://backup-server.com/agent

**Fallback triggers on: **- Connection timeout - HTTP 5xx errors - Invalid SWML response **8.19.10**

**Status Callbacks**

Receive notifications about call events:

Status Callback URL: https://your-server.com/status

Events:

• Call started

• Call answered

• Call completed

• Call failed

**8.19.11**

**Verification Checklist**

Before going live:

□ Agent is deployed and running

□ HTTPS URL is accessible

□ URL returns valid SWML on POST request

□ Basic auth is configured \(if used\)

□ Phone number Voice URL is set

□ Fallback URL is configured \(recommended\)

□ Test call completes successfully

233

8. SignalWire Integration

**8.20**

**Testing**

**Summary**: Test your agent thoroughly before production. Use local testing, swaig-test CLI, and test calls. 

**8.20.1 Testing Stages**

**8.20.1.1 1. Local Testing**

• Run agent locally

• Test with swaig-test CLI

• Verify SWML output

**8.20.1.2 2. Tunnel Testing**

• Expose via ngrok

• Make real calls

• Test end-to-end

**8.20.1.3 3. Production Testing**

• Deploy to production server

• Test with real phone

• Monitor call logs

**8.20.2**

**swaig-test CLI**

Test agents without making calls:

*\#\# List available functions*

swaig-test my\_agent.py --list-tools

*\#\# View SWML output*

swaig-test my\_agent.py --dump-swml

*\#\# Execute a function*

swaig-test my\_agent.py --exec get\_weather --city Seattle

*\#\# Raw JSON output*

swaig-test my\_agent.py --dump-swml --raw

**8.20.3**

**Local Server Testing**

Run your agent locally:

*\#\# Start the agent*

python my\_agent.py

*\#\# In another terminal, test the endpoint*

curl -X POST http://localhost:3000/ \\

-H "Content-Type: application/json" \\

-d '\{"call\_id": "test-123"\}' 

**8.20.4**

**Using ngrok**

Expose local server for real calls:

*\#\# Terminal 1: Run agent*

python my\_agent.py

*\#\# Terminal 2: Start ngrok*

ngrok http 3000

234

8. SignalWire Integration

Copy the ngrok HTTPS URL and configure in SignalWire. 

**8.20.5 Test Call Checklist**

**8.20.5.1 Basic Functionality**

□ Call connects successfully

□ Agent greeting plays

□ Speech recognition works

□ Agent responds appropriately

**8.20.5.2 Function Calls**

□ Functions execute correctly

□ Results returned to AI

□ AI summarizes results properly

**8.20.5.3 Edge Cases**

□ Silence handling

□ Interruption handling

□ Long responses

□ Multiple function calls

**8.20.5.4 Error Handling**

□ Invalid input handled

□ Function errors handled gracefully

□ Timeout behavior correct

**8.20.6**

**Viewing Logs**

In SignalWire dashboard:

1. Go to Logs

2. Find your test call

3. View details:

• Call duration

• SWML executed

• Function calls

• Errors

**8.20.7**

**Debugging with Logs**

Add logging to your agent:

import logging

logging.basicConfig\(level**=**logging.DEBUG\)

**class **MyAgent\(AgentBase\):

**def \_\_init\_\_**\(self\):

super\(\). **\_\_init\_\_**\(name**=**"my-agent"\)

self.log.info\("Agent initialized"\)

**def **my\_handler\(self, args, raw\_data\):

self.log.debug\(f"Function called with args: **\{**args**\}**"\) self.log.debug\(f"Raw data: **\{**raw\_data**\}**"\)

result **= **"Some result" 

self.log.info\(f"Returning: **\{**result**\}**"\)

235

8. SignalWire Integration

**return **SwaigFunctionResult\(result\)

**8.20.8 Testing Transfers**

Test call transfers carefully:

**def **test\_transfer\(self, args, raw\_data\):

*\# Use a test number you control*

test\_number **= **"\+15551234567" 

**return **\(

SwaigFunctionResult\("Transferring now"\)

.connect\(test\_number, final**=**True\)

\)

**8.20.9**

**Testing SMS**

Test SMS sending:

**def **test\_sms\(self, args, raw\_data\):

*\# Send to your own phone for testing*

**return **\(

SwaigFunctionResult\("Sent test SMS"\)

.send\_sms\(

to\_number**=**"\+15551234567", 

*\# Your test phone*

from\_number**=**"\+15559876543", *\# Your SignalWire number* body**=**"Test message from agent" 

\)

\)

**8.20.10**

**Load Testing**

For production readiness:

• Test concurrent call handling

• Monitor server resources

• Check response times under load

• Verify function execution at scale

• Test database/API connection pooling

**8.20.11**

**Common Test Scenarios**

**Scenario**

**What to Test**

Happy path

Normal conversation flow

No speech

Silence and timeout handling

Background noise

Speech recognition accuracy

Rapid speech

Interruption handling

Invalid requests

Error handling

Function errors

Graceful degradation

Long calls

Memory and stability

236

8. SignalWire Integration

**8.20.12 Automated Testing**

Create test scripts:

import requests

**def **test\_swml\_endpoint\(\):

*"""Test that SWML endpoint returns valid response""" *

response **= **requests.post\(

"http://localhost:3000/", 

json**=**\{"call\_id": "test-123"\}, 

headers**=**\{"Content-Type": "application/json"\}

\)

**assert **response.status\_code **== **200

data **= **response.json\(\)

**assert **"version" **in **data

**assert **data\["version"\] **== **"1.0.0" 

**def **test\_function\_execution\(\):

*"""Test that functions execute correctly""" *

response **= **requests.post\(

"http://localhost:3000/swaig", 

json**=**\{

"function": "get\_weather", 

"argument": \{"parsed": \[\{"city": "Seattle"\}\]\}, 

"call\_id": "test-123" 

\}

\)

**assert **response.status\_code **== **200

237

8. SignalWire Integration

**8.21**

**Troubleshooting**

**Summary**: Common issues and solutions when integrating agents with SignalWire. 

**8.21.1 Connection Issues**

**Problem: **Call doesn’t connect to agent

**Check: **- Is the server running? - Is the URL correct in SignalWire? - Is HTTPS configured properly? - Is the firewall allowing connections? - Can you access the URL from browser? 

**Test:**

curl -X POST https://your-server.com/ -H "Content-Type: application/json" 

**8.21.2**

**Authentication Errors**

**Problem: **401 Unauthorized

**Check: **- Is basic auth enabled on the server? - Are credentials in the URL correct? - Are credentials URL-encoded if special chars? 

**URL Format:**

https://username:password@your-server.com/

**Special characters in password need encoding:**

**Character**

**Encoded**

@

%40

:

%3A

/

%2F

**8.21.3**

**SWML Errors**

**Problem: **Invalid SWML response

**Verify with swaig-test:**

swaig-test my\_agent.py --dump-swml --raw

**Common issues: **- Missing "version": "1.0.0" - Invalid JSON format - Missing required sections - Syntax errors in SWML verbs

**8.21.4**

**No Speech Response**

**Problem: **Agent doesn’t speak

**Check: **- Is a language configured? self.add\_language\("English", "en-US", "rime.spore"\) - Is there a prompt? 

self.prompt\_add\_section\("Role", "You are..."\) - Is the AI model specified? Check SWML output for ai.params 238

8. SignalWire Integration

**8.21.5 Function Not Called**

**Problem: **AI doesn’t call your function

**Check: **- Is the function registered? Run swaig-test my\_agent.py --list-tools - Is the description clear? AI needs to understand when to use it - Is the prompt mentioning the capability? Example: “You can check the weather using get\_weather” 

**8.21.6 Function Errors**

**Problem: **Function returns error

**Test locally:**

swaig-test my\_agent.py --exec function\_name --param value

**Check: **- Are all required parameters provided? - Is the handler returning SwaigFunctionResult? - Are there exceptions in the handler? 

**Add error handling:**

**try**:

result **= **do\_something\(\)

**return **SwaigFunctionResult\(result\)

**except ** *Exception * as e:

self.log.error\(f"Error: **\{**e**\}**"\)

**return **SwaigFunctionResult\("Sorry, an error occurred"\) **8.21.7**

**SSL Certificate Issues**

**Problem: **SSL handshake failed

**Check: **- Is certificate valid and not expired? - Is the full certificate chain provided? - Is the domain correct on the certificate? 

**Test:**

openssl s\_client -connect your-server.com:443

For development, use ngrok \(handles SSL automatically\). 

**8.21.8**

**Timeout Issues**

**Problem: **Requests timing out

**SWML Request Timeout: **- SignalWire waits ~5 seconds for SWML - Make sure server responds quickly **Function Timeout: **- SWAIG functions should complete in <30 seconds - Use async operations for slow tasks -

Consider background processing for long tasks

**8.21.9**

**Quick Diagnostic Steps**

**Issue**

**First Check**

**Command**

Server down

Process running

ps aux \\| grep python

Bad URL

Test endpoint

curl -X POST https://url/

Bad SWML

View output

swaig-test agent.py --dum

p-swml

Function error

Execute directly

swaig-test agent.py --exe

c func

Auth error

Check credentials

Verify URL format

239

8. SignalWire Integration

**8.21.10 Getting Help**

If issues persist:

1. Check SignalWire documentation

2. Review call logs in dashboard

3. Enable debug logging in your agent

4. Contact SignalWire support

**8.21.11 Common Error Messages**

**Error**

**Meaning**

**Solution**

“No route to host” 

Server unreachable

Check network/firewall

“Connection refused” 

Server not listening

Start the server

“Invalid SWML” 

Bad response format

Check swaig-test output

“Function not found” 

Missing function

Register the function

“Unauthorized” 

Auth failed

Check credentials

**8.21.12**

**Logging for Debugging**

Enable detailed logging:

import logging

import structlog

*\#\# Enable debug logging*

logging.basicConfig\(level**=**logging.DEBUG\)

*\#\# The agent uses structlog*

structlog.configure\(

wrapper\_class**=**structlog.make\_filtering\_bound\_logger\(logging.DEBUG\)

\)

240

**Chapter 9**

**Prefab Agents**

**Summary**: Prefabs are pre-built agent archetypes for common use cases. Use them directly or extend them to quickly build information gatherers, FAQ bots, surveys, receptionists, and concierges. 

**9.1 What Are Prefabs? **

Prefabs are ready-to-use agent classes that implement common conversational patterns: **Prefab**

**Description**

**InfoGatherer**

Collect answers to a series of questions

**FAQBot**

Answer questions from a knowledge base

**Survey**

Conduct automated surveys with validation

**Receptionist**

Greet callers and transfer to departments

**Concierge**

Provide information and booking assistance

**9.2**

**Why Use Prefabs? **

• **Faster Development: **Pre-built conversation flows

• **Best Practices: **Proven patterns for common scenarios

• **Extensible: **Inherit and customize as needed

• **Production-Ready: **Includes validation, error handling, summaries **9.3**

**Quick Examples**

**9.3.1**

**InfoGatherer**

from signalwire\_agents.prefabs import InfoGathererAgent

agent **= **InfoGathererAgent\(

questions**=**\[

\{"key\_name": "name", "question\_text": "What is your name?"\}, 

\{"key\_name": "email", "question\_text": "What is your email?", "confirm": True\}, 

\{"key\_name": "reason", "question\_text": "How can I help you?"\}

\]

\)

agent.run\(\)

241

9. Prefab Agents

**9.3.2**

**FAQBot**

from signalwire\_agents.prefabs import FAQBotAgent

agent **= **FAQBotAgent\(

faqs**=**\[

\{"question": "What are your hours?", "answer": "We're open 9 AM to 5 PM."\}, 

\{"question": "Where are you located?", "answer": "123 Main Street, Downtown."\}

\]

\)

agent.run\(\)

**9.3.3**

**Survey**

from signalwire\_agents.prefabs import SurveyAgent

agent **= **SurveyAgent\(

survey\_name**=**"Customer Satisfaction", 

questions**=**\[

\{"id": "rating", "text": "Rate your experience?", "type": "rating", "scale": 5\}, 

\{"id": "feedback", "text": "Any comments?", "type": "open\_ended", "required": False\}

\]

\)

agent.run\(\)

**9.3.4**

**Receptionist**

from signalwire\_agents.prefabs import ReceptionistAgent

agent **= **ReceptionistAgent\(

departments**=**\[

\{"name": "sales", "description": "Product inquiries", "number": "\+15551234567"\}, 

\{"name": "support", "description": "Technical help", "number": "\+15551234568"\}

\]

\)

agent.run\(\)

**9.3.5**

**Concierge**

from signalwire\_agents.prefabs import ConciergeAgent

agent **= **ConciergeAgent\(

venue\_name**=**"Grand Hotel", 

services**=**\["room service", "spa", "restaurant"\], amenities**=**\{

"pool": \{"hours": "7 AM - 10 PM", "location": "2nd Floor"\}, 

"gym": \{"hours": "24 hours", "location": "3rd Floor"\}

\}

\)

agent.run\(\)

242

9. Prefab Agents

**9.4 Chapter Contents**

**Section**

**Description**

InfoGatherer

Collect information through questions

FAQBot

Answer frequently asked questions

Survey

Conduct automated surveys

Receptionist

Greet and transfer callers

Concierge

Provide venue information and services

**9.5 Importing Prefabs**

*\# Import individual prefabs*

from signalwire\_agents.prefabs import InfoGathererAgent

from signalwire\_agents.prefabs import FAQBotAgent

from signalwire\_agents.prefabs import SurveyAgent

from signalwire\_agents.prefabs import ReceptionistAgent

from signalwire\_agents.prefabs import ConciergeAgent

*\# Or import all*

from signalwire\_agents.prefabs import \(

InfoGathererAgent, 

FAQBotAgent, 

SurveyAgent, 

ReceptionistAgent, 

ConciergeAgent

\)

**9.6**

**Extending Prefabs**

All prefabs inherit from AgentBase, so you can extend them:

from signalwire\_agents.prefabs import FAQBotAgent

from signalwire\_agents.core.function\_result import SwaigFunctionResult **class **MyFAQBot\(FAQBotAgent\):

**def \_\_init\_\_**\(self\):

super\(\). **\_\_init\_\_**\(

faqs**=**\[

\{"question": "What is your return policy?", "answer": "30-day returns."\}

\]

\)

*\# Add custom prompt sections*

self.prompt\_add\_section\("Brand", "You represent Acme Corp."\)

*\# Add custom functions*

self.define\_tool\(

name**=**"escalate", 

description**=**"Escalate to human agent", 

parameters**=**\{"type": "object", "properties": \{\}\}, handler**=**self.escalate

\)

**def **escalate\(self, args, raw\_data\):

**return **SwaigFunctionResult\("Transferring to agent..."\).connect\("\+15551234567"\) 243

9. Prefab Agents

**9.7**

**Basic Usage**

from signalwire\_agents.prefabs import InfoGathererAgent

agent **= **InfoGathererAgent\(

questions**=**\[

\{"key\_name": "full\_name", "question\_text": "What is your full name?"\}, 

\{"key\_name": "email", "question\_text": "What is your email address?", "confirm": True\}, 

\{"key\_name": "reason", "question\_text": "How can I help you today?"\}

\]

\)

**if **\_\_name\_\_ **== **"\_\_main\_\_":

agent.run\(\)

**9.8 Question Format**

**Field**

**Type**

**Required**

**Description**

key\_name

string

Yes

Identifier for storing the

answer

question\_text

string

Yes

The question to ask the user

confirm

boolean

No

If true, confirm answer

before next

**9.9**

**Constructor Parameters**

InfoGathererAgent\(

questions**=**None, 

*\# List of question dictionaries*

name**=**"info\_gatherer", 

*\# Agent name*

route**=**"/info\_gatherer", 

*\# HTTP route*

**\*\***kwargs

*\# Additional AgentBase arguments*

\)

244

9. Prefab Agents

**9.10**

**Flow Diagram**

┌─────────────────────────────────────────────────────────────────────────────┐

│

InfoGatherer Flow

│

├─────────────────────────────────────────────────────────────────────────────┤

│

│

│

1. Agent asks if user is ready

│

│

│

│

│

▼

│

│

2. User confirms → AI calls start\_questions\(\)

│

│

│

│

│

▼

│

│

3. Agent asks first question

│

│

│

│

│

▼

│

│

4. User answers → AI calls submit\_answer\(\)

│

│

│

│

│

├── If confirm=true → Verify with user

│

│

│

│

│

▼

│

│

5. Repeat for each question

│

│

│

│

│

▼

│

│

6. All questions answered → Summary

│

│

│

└─────────────────────────────────────────────────────────────────────────────┘

**9.11**

**Built-in Functions**

InfoGatherer provides these SWAIG functions automatically:

**Function**

**Description**

start\_questions

Begin the question sequence

submit\_answer

Submit answer and get next question

**9.12**

**Dynamic Questions**

Instead of static questions, use a callback to determine questions at runtime: from signalwire\_agents.prefabs import InfoGathererAgent

**def **get\_questions\(query\_params, body\_params, headers\):

*"""Dynamically determine questions based on request""" *

question\_set **= **query\_params.get\('type', 'default'\)

**if **question\_set **== **'support':

**return **\[

\{"key\_name": "name", "question\_text": "What is your name?"\}, 

\{"key\_name": "issue", "question\_text": "Describe your issue."\}, 

\{"key\_name": "urgency", "question\_text": "How urgent is this?"\}

\]

**else**:

**return **\[

\{"key\_name": "name", "question\_text": "What is your name?"\}, 

\{"key\_name": "message", "question\_text": "How can I help?"\}

\]

245

9. Prefab Agents

*\# Create agent without static questions*

agent **= **InfoGathererAgent\(\)

*\# Set the callback for dynamic questions*

agent.set\_question\_callback\(get\_questions\)

**if **\_\_name\_\_ **== **"\_\_main\_\_":

agent.run\(\)

**9.13 Accessing Collected Data**

The collected answers are stored in global\_data:

*\# In a SWAIG function or callback:*

global\_data **= **raw\_data.get\("global\_data", \{\}\)

answers **= **global\_data.get\("answers", \[\]\)

*\# answers is a list like:*

*\# \[*

*\#*

*\{"key\_name": "full\_name", "answer": "John Doe"\}, *

*\#*

*\{"key\_name": "email", "answer": "john@example.com"\}, *

*\#*

*\{"key\_name": "reason", "answer": "Product inquiry"\}*

*\# \]*

**9.14 Complete Example**

*\#\!/usr/bin/env python3*

*\# appointment\_scheduler.py - Info gatherer for scheduling appointments* from signalwire\_agents.prefabs import InfoGathererAgent

agent **= **InfoGathererAgent\(

questions**=**\[

\{"key\_name": "name", "question\_text": "What is your name?"\}, 

\{"key\_name": "phone", "question\_text": "What is your phone number?", "confirm": True\}, 

\{"key\_name": "date", "question\_text": "What date would you like to schedule?"\}, 

\{"key\_name": "time", "question\_text": "What time works best for you?"\}, 

\{"key\_name": "notes", "question\_text": "Any special notes or requests?"\}

\], 

name**=**"appointment-scheduler" 

\)

*\# Add custom language*

agent.add\_language\("English", "en-US", "rime.spore"\)

*\# Customize prompt*

agent.prompt\_add\_section\(

"Brand", 

"You are scheduling appointments for Dr. Smith's office." 

\)

**if **\_\_name\_\_ **== **"\_\_main\_\_":

agent.run\(\)

246

9. Prefab Agents

**9.15**

**Best Practices**

**9.15.1 Questions**

• Keep questions clear and specific

• Use confirm=true for critical data \(email, phone\)

• Limit to 5-7 questions max per session

• Order from simple to complex

**9.15.2**

**key\_name Values**

• Use descriptive, unique identifiers

• snake\_case convention recommended

• Match your backend/database field names

**9.15.3**

**Dynamic Questions**

• Use callbacks for multi-purpose agents

• Validate questions in callback

• Handle errors gracefully

247

9. Prefab Agents

**9.16 FAQBot**

**Summary**: FAQBotAgent answers frequently asked questions from a provided knowledge base. It matches user questions to FAQs and optionally suggests related questions. 

**9.16.1 Basic Usage**

from signalwire\_agents.prefabs import FAQBotAgent

agent **= **FAQBotAgent\(

faqs**=**\[

\{

"question": "What are your business hours?", 

"answer": "We're open Monday through Friday, 9 AM to 5 PM." 

\}, 

\{

"question": "Where are you located?", 

"answer": "Our main office is at 123 Main Street, Downtown." 

\}, 

\{

"question": "How do I contact support?", 

"answer": "Email support@example.com or call 555-1234." 

\}

\]

\)

**if **\_\_name\_\_ **== **"\_\_main\_\_":

agent.run\(\)

**9.16.2**

**FAQ Format**

**Field**

**Type**

**Required**

**Description**

question

string

Yes

The FAQ question

answer

string

Yes

The answer to provide

categories

list\[string\]

No

Category tags for filtering

**9.16.3**

**Constructor Parameters**

FAQBotAgent\(

faqs**=**\[...\], 

*\# List of FAQ dictionaries \(required\)*

suggest\_related**=**True, 

*\# Suggest related questions*

persona**=**None, 

*\# Custom personality description*

name**=**"faq\_bot", 

*\# Agent name*

route**=**"/faq", 

*\# HTTP route*

**\*\***kwargs

*\# Additional AgentBase arguments*

\)

**9.16.4**

**With Categories**

Use categories to organize FAQs:

from signalwire\_agents.prefabs import FAQBotAgent

agent **= **FAQBotAgent\(

faqs**=**\[

\{

"question": "How do I reset my password?", 

"answer": "Click 'Forgot Password' on the login page.", 

"categories": \["account", "security"\]

\}, 

\{

248

9. Prefab Agents

"question": "How do I update my email?", 

"answer": "Go to Settings > Account > Email.", 

"categories": \["account", "settings"\]

\}, 

\{

"question": "What payment methods do you accept?", 

"answer": "We accept Visa, Mastercard, and PayPal.", 

"categories": \["billing", "payments"\]

\}

\]

\)

**9.16.5**

**Built-in Functions**

FAQBot provides this SWAIG function automatically:

**Function**

**Description**

search\_faqs

Search FAQs by query or category

**9.16.6**

**Custom Persona**

Customize the bot’s personality:

agent **= **FAQBotAgent\(

faqs**=**\[...\], 

persona**=**"You are a friendly and knowledgeable support agent for Acme Corp. " 

"You speak in a warm, professional tone and always try to be helpful." 

\)

**9.16.7**

**Complete Example**

249

9. Prefab Agents

*\#\!/usr/bin/env python3*

*\#\# product\_faq\_bot.py - FAQ bot for product questions*

from signalwire\_agents.prefabs import FAQBotAgent

agent **= **FAQBotAgent\(

faqs**=**\[

\{

"question": "What is the warranty period?", 

"answer": "All products come with a 2-year warranty.", 

"categories": \["warranty", "products"\]

\}, 

\{

"question": "How do I return a product?", 

"answer": "Start a return within 30 days at returns.example.com.", 

"categories": \["returns", "products"\]

\}, 

\{

"question": "Do you ship internationally?", 

"answer": "Yes, we ship to over 50 countries.", 

"categories": \["shipping"\]

\}

\], 

suggest\_related**=**True, 

persona**=**"You are a helpful product specialist for TechGadgets Inc.", name**=**"product-faq" 

\)

*\#\# Add language*

agent.add\_language\("English", "en-US", "rime.spore"\) **if **\_\_name\_\_ **== **"\_\_main\_\_":

agent.run\(\)

**9.16.8**

**Best Practices**

**9.16.8.1**

**FAQ Content**

• Write questions as users would ask them

• Keep answers concise but complete

• Include variations of common questions

• Update FAQs based on actual user queries

**9.16.8.2**

**Categories**

• Use consistent category naming

• Limit to 2-3 categories per FAQ

• Use categories for related question suggestions

**9.16.8.3**

**Scaling**

• For large FAQ sets, consider native\_vector\_search skill

• FAQBot works best with 50 or fewer FAQs

• Use categories to help matching

250

9. Prefab Agents

**9.17 Survey**

**Summary**: SurveyAgent conducts automated surveys with different question types \(rating, multiple choice, yes/no, open-ended\), validation, and response logging. 

**9.17.1 Basic Usage**

from signalwire\_agents.prefabs import SurveyAgent

agent **= **SurveyAgent\(

survey\_name**=**"Customer Satisfaction Survey", 

questions**=**\[

\{

"id": "satisfaction", 

"text": "How satisfied were you with our service?", 

"type": "rating", 

"scale": 5

\}, 

\{

"id": "recommend", 

"text": "Would you recommend us to others?", 

"type": "yes\_no" 

\}, 

\{

"id": "comments", 

"text": "Any additional comments?", 

"type": "open\_ended", 

"required": False

\}

\]

\)

**if **\_\_name\_\_ **== **"\_\_main\_\_":

agent.run\(\)

**9.17.2**

**Question Types**

**Type**

**Fields**

**Example**

rating

scale \(1-10\)

“Rate 1-5, where 5 is best” 

multiple\_choice

options \(list\)

“Choose: Poor, Fair, Good, 

Excellent” 

yes\_no

\(none\)

“Would you recommend

us?” 

open\_ended

\(none\)

“Any comments?” 

251

9. Prefab Agents

**9.17.3 Question Format**

**Field**

**Type**

**Required**

**Description**

id

string

Yes

Unique identifier for the

question

text

string

Yes

The question to ask

type

string

Yes

rating, multiple\_choice, 

yes\_no, open\_ended

options

list\[string\]

\*

Required for

multiple\_choice

scale

integer

No

For rating \(default: 5\)

required

boolean

No

Is answer required \(default:

true\)

**9.17.4**

**Constructor Parameters**

SurveyAgent\(

survey\_name**=**"...", 

*\# Name of the survey \(required\)*

questions**=**\[...\], 

*\# List of question dictionaries \(required\)*

introduction**=**None, 

*\# Custom intro message*

conclusion**=**None, 

*\# Custom conclusion message*

brand\_name**=**None, 

*\# Company/brand name*

max\_retries**=**2, 

*\# Retries for invalid answers*

name**=**"survey", 

*\# Agent name*

route**=**"/survey", 

*\# HTTP route*

**\*\***kwargs

*\# Additional AgentBase arguments*

\)

**9.17.5**

**Built-in Functions**

SurveyAgent provides these SWAIG functions automatically:

**Function**

**Description**

validate\_response

Check if response is valid for question type

log\_response

Record a validated response

252

9. Prefab Agents

**9.17.6 Survey Flow**

┌─────────────────────────────────────────────────────────────────────────────┐

│

Survey Flow

│

├─────────────────────────────────────────────────────────────────────────────┤

│

│

│

1. Introduction

│

│

│

│

│

▼

│

│

2. Ask question

│

│

│

│

│

▼

│

│

3. Get response

│

│

│

│

│

├── Valid → Log and continue

│

│

│

│

│

└── Invalid → Retry \(up to max\_retries\)

│

│

│

│

│

└── Still invalid → Skip or ask again

│

│

│

│

│

▼

│

│

4. Next question \(repeat 2-3\)

│

│

│

│

│

▼

│

│

5. Conclusion

│

│

│

│

│

▼

│

│

6. Generate summary

│

│

│

└─────────────────────────────────────────────────────────────────────────────┘

**9.17.7**

**Complete Example**

*\#\!/usr/bin/env python3*

*\#\# product\_survey.py - Product feedback survey agent*

from signalwire\_agents.prefabs import SurveyAgent

agent **= **SurveyAgent\(

survey\_name**=**"Product Feedback Survey", 

brand\_name**=**"TechGadgets Inc.", 

introduction**=**"Thank you for purchasing our product. We'd love your feedback\!", conclusion**=**"Thank you for completing our survey. Your input helps us improve.", questions**=**\[

\{

"id": "overall\_rating", 

"text": "How would you rate the product overall?", 

"type": "rating", 

"scale": 5, 

"required": True

\}, 

\{

"id": "quality", 

"text": "How would you rate the build quality?", 

"type": "multiple\_choice", 

"options": \["Poor", "Fair", "Good", "Excellent"\], 

"required": True

\}, 

\{

"id": "purchase\_again", 

"text": "Would you purchase from us again?", 

"type": "yes\_no", 

"required": True

\}, 

\{

253

9. Prefab Agents

"id": "improvements", 

"text": "What could we improve?", 

"type": "open\_ended", 

"required": False

\}

\], 

max\_retries**=**2

\)

**if **\_\_name\_\_ **== **"\_\_main\_\_":

agent.add\_language\("English", "en-US", "rime.spore"\) agent.run\(\)

**9.17.8**

**Best Practices**

**9.17.8.1 Question Design**

• Keep surveys short \(5-7 questions max\)

• Start with easy questions

• Put open-ended questions at the end

• Make non-essential questions optional

**9.17.8.2 Question Types**

• Use rating for satisfaction metrics \(NPS, CSAT\)

• Use multiple\_choice for specific options

• Use yes\_no for simple binary questions

• Use open\_ended sparingly - harder to analyze

**9.17.8.3**

**Validation**

• Set appropriate max\_retries \(2-3\)

• Use clear scale descriptions

• List all options for multiple choice

254

9. Prefab Agents

**9.18**

**Receptionist**

**Summary**: ReceptionistAgent greets callers, collects their information, and transfers them to the appropriate department based on their needs. 

**9.18.1 Basic Usage**

from signalwire\_agents.prefabs import ReceptionistAgent

agent **= **ReceptionistAgent\(

departments**=**\[

\{

"name": "sales", 

"description": "Product inquiries, pricing, and purchasing", 

"number": "\+15551234567" 

\}, 

\{

"name": "support", 

"description": "Technical help and troubleshooting", 

"number": "\+15551234568" 

\}, 

\{

"name": "billing", 

"description": "Payment questions and account issues", 

"number": "\+15551234569" 

\}

\]

\)

**if **\_\_name\_\_ **== **"\_\_main\_\_":

agent.run\(\)

**9.18.2**

**Department Format**

**Field**

**Type**

**Required**

**Description**

name

string

Yes

Department identifier \(e.g., 

“sales”\)

description

string

Yes

What the department

handles

number

string

Yes

Phone number for transfer

**9.18.3**

**Constructor Parameters**

ReceptionistAgent\(

departments**=**\[...\], 

*\# List of department dicts \(required\)*

name**=**"receptionist", 

*\# Agent name*

route**=**"/receptionist", 

*\# HTTP route*

greeting**=**"Thank you for calling. How can I help you today?", voice**=**"rime.spore", 

*\# Voice ID*

**\*\***kwargs

*\# Additional AgentBase arguments*

\)

255

9. Prefab Agents

**9.18.4 Built-in Functions**

ReceptionistAgent provides these SWAIG functions automatically:

**Function**

**Description**

collect\_caller\_info

Collect caller’s name and reason for calling

transfer\_call

Transfer to a specific department

**9.18.5 Call Flow**

┌─────────────────────────────────────────────────────────────────────────────┐

│

Receptionist Flow

│

├─────────────────────────────────────────────────────────────────────────────┤

│

│

│

1. Greeting

│

│

│

"Thank you for calling. How can I help you today?" 

│

│

│

│

│

▼

│

│

2. Collect Information

│

│

│

• Caller's name

│

│

│

• Reason for calling

│

│

│

│

│

▼

│

│

3. AI calls collect\_caller\_info\(\)

│

│

│

Stores info in global\_data

│

│

│

│

│

▼

│

│

4. Determine Department

│

│

│

AI matches reason to department

│

│

│

│

│

▼

│

│

5. Confirm Transfer

│

│

│

"I'll transfer you to sales. Is that correct?" 

│

│

│

│

│

▼

│

│

6. AI calls transfer\_call\(\)

│

│

│

Connects to department number

│

│

│

│

│

▼

│

│

7. Call Transferred

│

│

│

└─────────────────────────────────────────────────────────────────────────────┘

**9.18.6**

**Complete Example**

*\#\!/usr/bin/env python3*

*\#\# company\_receptionist.py - Custom receptionist agent*

from signalwire\_agents.prefabs import ReceptionistAgent

agent **= **ReceptionistAgent\(

departments**=**\[

\{

"name": "sales", 

"description": "New orders, pricing, quotes, and product information", 

"number": "\+15551001001" 

\}, 

\{

"name": "support", 

"description": "Technical issues, troubleshooting, and product help", 

"number": "\+15551001002" 

256

9. Prefab Agents

\}, 

\{

"name": "billing", 

"description": "Invoices, payments, refunds, and account questions", 

"number": "\+15551001003" 

\}, 

\{

"name": "hr", 

"description": "Employment, careers, and benefits", 

"number": "\+15551001004" 

\}

\], 

greeting**=**"Thank you for calling Acme Corporation. How may I direct your call?", voice**=**"rime.spore", 

name**=**"acme-receptionist" 

\)

*\#\# Add custom prompt section*

agent.prompt\_add\_section\(

"Company", 

"You are the receptionist for Acme Corporation, a leading technology company." 

\)

**if **\_\_name\_\_ **== **"\_\_main\_\_":

agent.run\(\)

**9.18.7**

**Best Practices**

**9.18.7.1**

**Departments**

• Use clear, distinct department names

• Write descriptions that help AI route correctly

• Include common reasons in descriptions

• Verify transfer numbers are correct

**9.18.7.2**

**Greeting**

• Keep greeting professional and welcoming

• Include company name if appropriate

• Ask how to help \(prompts caller to state need\)

**9.18.7.3**

**Transfers**

• Always confirm before transferring

• Use final=True for permanent transfers

• Test all transfer numbers

257

9. Prefab Agents

**9.19 Concierge**

**Summary**: ConciergeAgent provides venue information, answers questions about amenities and services, helps with bookings, and gives directions. 

**9.19.1 Basic Usage**

from signalwire\_agents.prefabs import ConciergeAgent

agent **= **ConciergeAgent\(

venue\_name**=**"Grand Hotel", 

services**=**\["room service", "spa bookings", "restaurant reservations", "tours"\], amenities**=**\{

"pool": \{"hours": "7 AM - 10 PM", "location": "2nd Floor"\}, 

"gym": \{"hours": "24 hours", "location": "3rd Floor"\}, 

"spa": \{"hours": "9 AM - 8 PM", "location": "4th Floor"\}

\}

\)

**if **\_\_name\_\_ **== **"\_\_main\_\_":

agent.run\(\)

**9.19.2**

**Amenity Format**

amenities **= **\{

"amenity\_name": \{

"hours": "Operating hours", 

"location": "Where to find it", 

"description": "Optional description", 

*\# ... any other key-value pairs*

\}

\}

**9.19.3**

**Constructor Parameters**

ConciergeAgent\(

venue\_name**=**"...", 

*\# Name of venue \(required\)*

services**=**\[...\], 

*\# List of services offered \(required\)*

amenities**=**\{...\}, 

*\# Dict of amenities with details \(required\)*

hours\_of\_operation**=**None, 

*\# Dict of operating hours*

special\_instructions**=**None, 

*\# List of special instructions*

welcome\_message**=**None, 

*\# Custom welcome message*

name**=**"concierge", 

*\# Agent name*

route**=**"/concierge", 

*\# HTTP route*

**\*\***kwargs

*\# Additional AgentBase arguments*

\)

**9.19.4**

**Built-in Functions**

ConciergeAgent provides these SWAIG functions automatically:

**Function**

**Description**

check\_availability

Check service availability for date/time

get\_directions

Get directions to an amenity or location

258

9. Prefab Agents

**9.19.5 Concierge Flow**

┌─────────────────────────────────────────────────────────────────────────────┐

│

Concierge Flow

│

├─────────────────────────────────────────────────────────────────────────────┤

│

│

│

Guest: "What time does the pool close?" 

│

│

│

│

│

▼

│

│

AI looks up pool in amenities

│

│

│

│

│

▼

│

│

Response: "The pool is open until 10 PM and located on the 2nd Floor." 

│

│

│

│

─────────────────────────────────────────────────────────────────────────

│

│

│

│

Guest: "Can I book a spa appointment for tomorrow at 2 PM?" 

│

│

│

│

│

▼

│

│

AI calls check\_availability\("spa", "2025-01-16", "14:00"\)

│

│

│

│

│

▼

│

│

Response: "Yes, the spa is available tomorrow at 2 PM. Shall I book it?" 

│

│

│

│

─────────────────────────────────────────────────────────────────────────

│

│

│

│

Guest: "How do I get to the gym?" 

│

│

│

│

│

▼

│

│

AI calls get\_directions\("gym"\)

│

│

│

│

│

▼

│

│

Response: "The gym is on Level 2, West Wing. From the lobby..." 

│

│

│

└─────────────────────────────────────────────────────────────────────────────┘

**9.19.6**

**Complete Example**

*\#\!/usr/bin/env python3*

*\#\# resort\_concierge.py - Hotel concierge agent*

from signalwire\_agents.prefabs import ConciergeAgent

agent **= **ConciergeAgent\(

venue\_name**=**"The Riverside Resort", 

services**=**\[

"room service", 

"spa treatments", 

"restaurant reservations", 

"golf tee times", 

"airport shuttle", 

"event planning" 

\], 

amenities**=**\{

"swimming pool": \{

"hours": "6 AM - 10 PM", 

"location": "Ground Floor, East Wing", 

"description": "Heated indoor/outdoor pool with poolside bar" 

\}, 

"fitness center": \{

"hours": "24 hours", 

"location": "Level 2, West Wing", 

"description": "Full gym with personal trainers available" 

\}, 

259

9. Prefab Agents

"spa": \{

"hours": "9 AM - 9 PM", 

"location": "Level 3, East Wing", 

"description": "Full service spa with massage and facials" 

\}, 

"restaurant": \{

"hours": "Breakfast 7-10 AM, Lunch 12-3 PM, Dinner 6-10 PM", 

"location": "Lobby Level", 

"description": "Fine dining with panoramic river views" 

\}

\}, 

hours\_of\_operation**=**\{

"front desk": "24 hours", 

"concierge": "7 AM - 11 PM", 

"valet": "6 AM - 12 AM" 

\}, 

special\_instructions**=**\[

"Always offer to make reservations when guests ask about restaurants or spa.", 

"Mention the daily happy hour at the pool bar \(4-6 PM\)." 

\], 

welcome\_message**=**"Welcome to The Riverside Resort\! How may I assist you today?" 

\)

**if **\_\_name\_\_ **== **"\_\_main\_\_":

agent.add\_language\("English", "en-US", "rime.spore"\) agent.run\(\)

**9.19.7**

**Best Practices**

**9.19.7.1**

**Amenities**

• Include hours for all amenities

• Provide clear location descriptions

• Add any special requirements or dress codes

• Keep information up to date

**9.19.7.2**

**Services**

• List all bookable services

• Connect to real booking system for availability

• Include service descriptions and pricing if possible

**9.19.7.3**

**Special Instructions**

• Use for promotions and special offers

• Include upselling opportunities

• Add seasonal information

260

**Chapter 10**

**Reference**

**Summary**: Complete API reference for all SignalWire Agents SDK classes, methods, CLI tools, and configuration options. 

This chapter provides detailed reference documentation for the SignalWire Agents SDK. 

**10.1 Reference Overview**

**10.1.1**

**API Reference**

• **AgentBase **- Main agent class with all methods

• **SWMLService **- Base service for SWML generation

• **SwaigFunctionResult **- Function return values and actions

• **DataMap **- Serverless REST API integration

• **SkillBase **- Custom skill development

• **ContextBuilder **- Multi-step workflows

**10.1.2**

**CLI Tools**

• **swaig-test **- Test agents and functions locally

• **sw-search **- Build and query search indexes

**10.1.3**

**Configuration**

• **Environment Variables **- Runtime configuration

• **Config Files **- YAML/JSON configuration

• **SWML Schema **- Document structure reference

**10.2**

**Quick Reference**

**10.2.1**

**Creating an Agent**

agent **= **AgentBase\(name**=**"my-agent", route**=**"/agent"\) agent.add\_language\("English", "en-US", "rime.spore"\) agent.prompt\_add\_section\("Role", "You are a helpful assistant."\) agent.run\(\)

261

10. Reference

**10.2.2 Defining a Function**

@agent.tool\(description**=**"Search for information"\) **def **search\(query: str\) **-> **SwaigFunctionResult:

**return **SwaigFunctionResult\(f"Found results for: **\{**query**\}**"\) **10.2.3 Returning Actions**

**return **SwaigFunctionResult\("Transferring..."\).connect\("\+15551234567"\) **return **SwaigFunctionResult\("Goodbye"\).hangup\(\)

**return **SwaigFunctionResult\(\).update\_global\_data\(\{"key": "value"\}\) **10.3 Import Patterns**

*\# Main imports*

from signalwire\_agents import AgentBase

from signalwire\_agents.core.function\_result import SwaigFunctionResult from signalwire\_agents.core.data\_map import DataMap

*\# Prefab agents*

from signalwire\_agents.prefabs import \(

InfoGathererAgent, 

FAQBotAgent, 

SurveyAgent, 

ReceptionistAgent, 

ConciergeAgent

\)

*\# Context/workflow system*

from signalwire\_agents.core.contexts import ContextBuilder

*\# Skill development*

from signalwire\_agents.core.skill\_base import SkillBase

**10.4**

**Chapter Contents**

**Section**

**Description**

AgentBase API

Main agent class reference

SWMLService API

Base service class reference

SWAIG Function API

Function definition reference

SwaigFunctionResult API

Return value and actions reference

DataMap API

Serverless API integration reference

SkillBase API

Custom skill development reference

ContextBuilder API

Workflow system reference

swaig-test CLI

Testing tool reference

sw-search CLI

Search tool reference

Environment Variables

Environment configuration

Config Files

File-based configuration

SWML Schema

Document structure reference

262

10. Reference

**10.5 Class Definition**

from signalwire\_agents import AgentBase

**class **AgentBase\(

AuthMixin, 

WebMixin, 

SWMLService, 

PromptMixin, 

ToolMixin, 

SkillMixin, 

AIConfigMixin, 

ServerlessMixin, 

StateMixin

\)

**10.6 Constructor**

AgentBase\(

name: str, 

*\# Agent name/identifier \(required\)*

route: str **= **"/", 

*\# HTTP route path*

host: str **= **"0.0.0.0", 

*\# Host to bind*

port: int **= **3000, 

*\# Port to bind*

basic\_auth: Optional\[Tuple\[str, str\]\] **= **None, 

*\# \(username, password\)*

use\_pom: bool **= **True, 

*\# Use POM for prompts*

token\_expiry\_secs: int **= **3600, 

*\# Token expiration time*

auto\_answer: bool **= **True, 

*\# Auto-answer calls*

record\_call: bool **= **False, 

*\# Enable recording*

record\_format: str **= **"mp4", 

*\# Recording format*

record\_stereo: bool **= **True, 

*\# Stereo recording*

default\_webhook\_url: Optional\[str\] **= **None, 

*\# Default webhook URL*

agent\_id: Optional\[str\] **= **None, 

*\# Unique agent ID*

native\_functions: Optional\[List\[str\]\] **= **None, 

*\# Native function list*

schema\_path: Optional\[str\] **= **None, 

*\# SWML schema path*

suppress\_logs: bool **= **False, 

*\# Suppress structured logs*

enable\_post\_prompt\_override: bool **= **False, 

*\# Enable post-prompt override*

check\_for\_input\_override: bool **= **False, *\# Enable input override* config\_file: Optional\[str\] **= **None

*\# Path to config file*

\)

**10.7**

**Constructor Parameters**

**Parameter**

**Type**

**Default**

**Description**

name

str

required

Agent identifier

route

str

"/" 

HTTP endpoint path

host

str

"0.0.0.0" 

Bind address

port

int

3000

Bind port

basic\_auth

Tuple\[str, str\]

None

Auth credentials

use\_pom

bool

True

Use POM prompts

token\_expiry\_secs

int

3600

Token TTL

auto\_answer

bool

True

Auto-answer calls

record\_call

bool

False

Record calls

record\_format

str

"mp4" 

Recording format

record\_stereo

bool

True

Stereo recording

native\_functions

List\[str\]

None

Native functions

263

10. Reference

**10.8**

**Prompt Methods**

**10.8.1 prompt\_add\_section**

**def **prompt\_add\_section\(

self, 

section: str, 

*\# Section title*

body: str, 

*\# Section content*

bullets: List\[str\] **= **None

*\# Optional bullet points*

\) **-> **'AgentBase' 

Add a section to the agent’s prompt. 

**10.8.2**

**prompt\_add\_text**

**def **prompt\_add\_text\(

self, 

text: str

*\# Text to add*

\) **-> **'AgentBase' 

Add raw text to the prompt. 

**10.8.3**

**get\_prompt**

**def **get\_prompt\(self\) **-> **Union\[str, List\[Dict\]\]

Get the complete prompt. Returns POM structure if use\_pom=True, otherwise plain text. 

**10.9**

**Language and Voice Methods**

**10.9.1**

**add\_language**

**def **add\_language\(

self, 

name: str, 

*\# Language name \(e.g., "English"\)*

code: str, 

*\# Language code \(e.g., "en-US"\)*

voice: str, 

*\# Voice ID \(e.g., "rime.spore"\)*

speech\_fillers: Optional\[List\[str\]\] **= **None, 

*\# Filler words*

function\_fillers: Optional\[List\[str\]\] **= **None, *\# Processing phrases* language\_order: int **= **0

*\# Priority order*

\) **-> **'AgentBase' 

Add a supported language with voice configuration. 

**10.9.2**

**set\_voice**

**def **set\_voice\(

self, 

voice: str

*\# Voice ID*

\) **-> **'AgentBase' 

Set the default voice for the agent. 

264

10. Reference

**10.10**

**Tool Definition Methods**

**10.10.1 tool \(decorator\)**

@agent.tool\(

name: str **= **None, 

*\# Function name \(default: function name\)*

description: str **= **"", 

*\# Function description*

secure: bool **= **False, 

*\# Require token authentication*

fillers: List\[str\] **= **None, 

*\# Processing phrases*

wait\_file: str **= **None

*\# Audio file URL for hold*

\)

**def **my\_function\(args...\) **-> **SwaigFunctionResult:

... 

Decorator to register a SWAIG function. 

**10.10.2**

**define\_tool**

**def **define\_tool\(

self, 

name: str, 

*\# Function name*

description: str, 

*\# Function description*

handler: Callable, 

*\# Function handler*

parameters: Dict\[str, Any\] **= **None, 

*\# Parameter schema*

secure: bool **= **False, 

*\# Require authentication*

fillers: List\[str\] **= **None, 

*\# Processing phrases*

wait\_file: str **= **None

*\# Hold audio URL*

\) **-> **'AgentBase' 

Programmatically define a SWAIG function. 

**10.11**

**Skill Methods**

**10.11.1**

**add\_skill**

**def **add\_skill\(

self, 

skill\_name: str, 

*\# Skill identifier*

params: Dict\[str, Any\] **= **None

*\# Skill configuration*

\) **-> **'AgentBase' 

Add a skill to the agent. 

**10.11.2**

**list\_available\_skills**

**def **list\_available\_skills\(self\) **-> **List\[str\]

List all available skills. 

**10.12**

**AI Configuration Methods**

**10.12.1**

**set\_params**

**def **set\_params\(

self, 

params: Dict\[str, Any\]

*\# AI parameters*

\) **-> **'AgentBase' 

Set AI model parameters \(temperature, top\_p, etc.\). 

265

10. Reference

**10.12.2 add\_hints**

**def **add\_hints\(

self, 

hints: List\[str\]

*\# Speech recognition hints*

\) **-> **'AgentBase' 

Add speech recognition hints. 

**10.12.3 add\_pronounce**

**def **add\_pronounce\(

self, 

patterns: List\[Dict\[str, str\]\]

*\# Pronunciation rules*

\) **-> **'AgentBase' 

Add pronunciation rules. 

**10.13 State Methods**

**10.13.1**

**set\_global\_data**

**def **set\_global\_data\(

self, 

data: Dict\[str, Any\]

*\# Data to store*

\) **-> **'AgentBase' 

Set initial global data for the agent session. 

**10.14**

**URL Methods**

**10.14.1**

**get\_full\_url**

**def **get\_full\_url\(

self, 

include\_auth: bool **= **False

*\# Include credentials in URL*

\) **-> **str

Get the full URL for the agent endpoint. 

**10.14.2**

**set\_web\_hook\_url**

**def **set\_web\_hook\_url\(

self, 

url: str

*\# Webhook URL*

\) **-> **'AgentBase' 

Override the default webhook URL. 

**10.14.3**

**set\_post\_prompt\_url**

**def **set\_post\_prompt\_url\(

self, 

url: str

*\# Post-prompt URL*

\) **-> **'AgentBase' 

Override the post-prompt summary URL. 

266

10. Reference

**10.15**

**Server Methods**

**10.15.1 run**

**def **run\(

self, 

host: str **= **None, 

*\# Override host*

port: int **= **None

*\# Override port*

\) **-> **None

Start the development server. 

**10.15.2**

**get\_app**

**def **get\_app\(self\) **-> **FastAPI

Get the FastAPI application instance. 

**10.16 Serverless Methods**

**10.16.1**

**serverless\_handler**

**def **serverless\_handler\(

self, 

event: Dict\[str, Any\], 

*\# Lambda event*

context: Any

*\# Lambda context*

\) **-> **Dict\[str, Any\]

Handle AWS Lambda invocations. 

**10.16.2**

**cloud\_function\_handler**

**def **cloud\_function\_handler\(

self, 

request

*\# Flask request*

\) **-> **Response

Handle Google Cloud Function invocations. 

**10.16.3**

**azure\_function\_handler**

**def **azure\_function\_handler\(

self, 

req

*\# Azure HttpRequest*

\) **-> **HttpResponse

Handle Azure Function invocations. 

**10.17**

**Callback Methods**

**10.17.1**

**on\_summary**

**def **on\_summary\(

self, 

summary: Optional\[Dict\[str, Any\]\], 

*\# Summary data*

raw\_data: Optional\[Dict\[str, Any\]\] **= **None

*\# Raw POST data*

\) **-> **None

Override to handle post-prompt summaries. 

267

10. Reference

**10.17.2 set\_dynamic\_config\_callback**

**def **set\_dynamic\_config\_callback\(

self, 

callback: Callable

*\# Config callback*

\) **-> **'AgentBase' 

Set a callback for dynamic configuration. 

**10.18**

**SIP Routing Methods**

**10.18.1**

**enable\_sip\_routing**

**def **enable\_sip\_routing\(

self, 

auto\_map: bool **= **True, 

*\# Auto-map usernames*

path: str **= **"/sip" 

*\# Routing endpoint path*

\) **-> **'AgentBase' 

Enable SIP-based routing. 

**10.18.2**

**register\_sip\_username**

**def **register\_sip\_username\(

self, 

sip\_username: str

*\# SIP username*

\) **-> **'AgentBase' 

Register a SIP username for routing. 

**10.19**

**Method Chaining**

All setter methods return self for method chaining:

from signalwire\_agents import AgentBase

from signalwire\_agents.core.function\_result import SwaigFunctionResult agent **= **\(

AgentBase\(name**=**"assistant", route**=**"/assistant"\)

.add\_language\("English", "en-US", "rime.spore"\)

.add\_hints\(\["SignalWire", "SWML", "SWAIG"\]\)

.set\_params\(\{"temperature": 0.7\}\)

.set\_global\_data\(\{"user\_tier": "standard"\}\)

\)

@agent.tool\(description**=**"Get help"\)

**def **get\_help\(topic: str\) **-> **SwaigFunctionResult:

**return **SwaigFunctionResult\(f"Help for **\{**topic**\}**"\) **if **\_\_name\_\_ **== **"\_\_main\_\_":

agent.run\(\)

268

10. Reference

**10.20**

**Class Attributes**

**Attribute**

**Type**

**Description**

PROMPT\_SECTIONS

List\[Dict\]

Declarative prompt sections

name

str

Agent name

route

str

HTTP route path

host

str

Bind host

port

int

Bind port

agent\_id

str

Unique agent identifier

pom

PromptObject

POM instance \(if

use\_pom=True\)

skill\_manager

SkillManager

Skill manager instance

269

10. Reference

**10.21**

**SWMLService API**

**Summary**: API reference for SWMLService, the base class for creating and serving SWML documents. 

**10.21.1 Class Definition**

from signalwire\_agents.core.swml\_service import SWMLService

**class **SWMLService:

*"""Base class for creating and serving SWML documents.""" *

**10.21.2**

**Constructor**

SWMLService\(

name: str, 

*\# Service name \(required\)*

route: str **= **"/", 

*\# HTTP route path*

host: str **= **"0.0.0.0", 

*\# Host to bind*

port: int **= **3000, 

*\# Port to bind*

basic\_auth: Optional\[Tuple\[str, str\]\] **= **None, 

*\# \(username, password\)*

schema\_path: Optional\[str\] **= **None, 

*\# SWML schema path*

config\_file: Optional\[str\] **= **None

*\# Config file path*

\)

**10.21.3**

**Core Responsibilities**

**SWML Generation: **- Create and validate SWML documents - Add verbs to document sections - Render complete SWML JSON output

**Web Server: **- Serve SWML documents via FastAPI - Handle SWAIG webhook callbacks - Manage authentication **Schema Validation: **- Load and validate SWML schema - Auto-generate verb methods from schema - Validate document structure

**10.21.4**

**Document Methods**

**10.21.4.1**

**reset\_document**

**def **reset\_document\(self\) **-> **None

Reset the SWML document to a clean state. 

**10.21.4.2**

**add\_verb**

**def **add\_verb\(

self, 

verb\_name: str, 

*\# Verb name \(e.g., "ai", "play"\)*

params: Dict\[str, Any\]

*\# Verb parameters*

\) **-> **'SWMLService' 

Add a verb to the current document section. 

**10.21.4.3**

**get\_document**

**def **get\_document\(self\) **-> **Dict\[str, Any\]

Get the current SWML document as a dictionary. 

270

10. Reference

**10.21.4.4 render**

**def **render\(self\) **-> **str

Render the SWML document as a JSON string. 

**10.21.5 Auto-Generated Verb Methods**

SWMLService automatically generates methods for all SWML verbs defined in the schema:

*\#\# These methods are auto-generated from schema*

service.ai\(...\)

*\# AI verb*

service.play\(...\)

*\# Play audio*

service.record\(...\)

*\# Record audio*

service.connect\(...\)

*\# Connect call*

service.transfer\(...\)

*\# Transfer call*

service.hangup\(...\)

*\# End call*

service.sleep\(...\)

*\# Pause execution*

*\#\# ... many more*

**10.21.6**

**Server Methods**

**10.21.6.1 run**

**def **run\(

self, 

host: str **= **None, 

*\# Override host*

port: int **= **None

*\# Override port*

\) **-> **None

Start the development server. 

**10.21.6.2**

**get\_app**

**def **get\_app\(self\) **-> **FastAPI

Get the FastAPI application instance. 

**10.21.7**

**Authentication Methods**

**10.21.7.1**

**get\_basic\_auth\_credentials**

**def **get\_basic\_auth\_credentials\(self\) **-> **Tuple\[str, str\]

Get the current basic auth credentials. 

**10.21.8**

**URL Building Methods**

**10.21.8.1**

**\_build\_full\_url**

**def **\_build\_full\_url\(

self, 

endpoint: str **= **"", 

*\# Endpoint path*

include\_auth: bool **= **False

*\# Include credentials*

\) **-> **str

Build a full URL for an endpoint. 

271

10. Reference

**10.21.8.2 \_build\_webhook\_url**

**def **\_build\_webhook\_url\(

self, 

endpoint: str, 

*\# Endpoint path*

query\_params: Dict\[str, str\] **= **None

*\# Query parameters*

\) **-> **str

Build a webhook URL with authentication. 

**10.21.9 Routing Methods**

**10.21.9.1 register\_routing\_callback**

**def **register\_routing\_callback\(

self, 

callback: Callable, 

*\# Routing callback*

path: str **= **"/" 

*\# Path to register*

\) **-> **None

Register a routing callback for dynamic request handling. 

**10.21.10**

**Security Configuration**

**Attribute**

**Type**

**Description**

ssl\_enabled

bool

Whether SSL is enabled

domain

str

Domain for SSL certificates

ssl\_cert\_path

str

Path to SSL certificate

ssl\_key\_path

str

Path to SSL private key

security

SecurityConfig

Unified security

configuration

**10.21.11**

**Schema Utils**

The schema\_utils attribute provides access to SWML schema validation:

*\#\# Access schema utilities*

service.schema\_utils.validate\(document\)

service.schema\_utils.get\_all\_verb\_names\(\)

service.schema\_utils.get\_verb\_schema\("ai"\)

**10.21.12**

**Verb Registry**

The verb\_registry manages SWML verb handlers:

*\#\# Access verb registry*

service.verb\_registry.register\_handler\("custom\_verb", handler\) service.verb\_registry.get\_handler\("ai"\)

272

10. Reference

**10.21.13**

**Instance Attributes**

**Attribute**

**Type**

**Description**

name

str

Service name

route

str

HTTP route path

host

str

Bind host

port

int

Bind port

schema\_utils

SchemaUtils

Schema validation utilities

verb\_registry

VerbRegistry

Verb handler registry

log

Logger

Structured logger

**10.21.14**

**Usage Example**

from signalwire\_agents.core.swml\_service import SWMLService

*\#\# Create a basic SWML service*

service **= **SWMLService\(

name**=**"my-service", 

route**=**"/swml", 

port**=**8080

\)

*\#\# Add verbs to build a document*

service.reset\_document\(\)

service.play\(url**=**"https://example.com/welcome.mp3"\) service.ai\(

prompt**=**\{"text": "You are a helpful assistant"\}, SWAIG**=**\{"functions": \[\]\}

\)

*\#\# Get the rendered SWML*

swml\_json **= **service.render\(\)

print\(swml\_json\)

**10.21.15**

**Relationship to AgentBase**

AgentBase extends SWMLService with higher-level abstractions:

**SWMLService provides: **- SWML document generation - Schema validation - Basic web server - Authentication **AgentBase adds: **- Prompt management \(POM\) - Tool/function definitions - Skills system - AI configuration -

Serverless support - State management

273

10. Reference

**10.22**

**SWAIG Function API**

**Summary**: API reference for defining SWAIG functions using decorators and programmatic methods. 

**10.22.1 Overview**

SWAIG \(SignalWire AI Gateway\) functions are the primary way for AI agents to perform actions and retrieve information during conversations. 

**SWAIG Function Flow:**

User speaks → AI decides to call function → Webhook invoked → Result 1. AI determines a function should be called based on conversation 2. SignalWire invokes the webhook with function arguments

3. Function executes and returns SwaigFunctionResult

4. AI uses the result to continue the conversation

**10.22.2**

**Decorator Syntax**

**10.22.2.1 Basic Usage**

from signalwire\_agents import AgentBase

from signalwire\_agents.core.function\_result import SwaigFunctionResult agent **= **AgentBase\(name**=**"my-agent"\)

@agent.tool\(description**=**"Search for information"\) **def **search\(query: str\) **-> **SwaigFunctionResult:

results **= **perform\_search\(query\)

**return **SwaigFunctionResult\(f"Found: **\{**results**\}**"\) **10.22.2.2**

**Decorator Parameters**

@agent.tool\(

name: str **= **None, 

*\# Function name \(default: function name\)*

description: str **= **"", 

*\# Function description \(required\)*

secure: bool **= **False, 

*\# Require token authentication*

fillers: List\[str\] **= **None, 

*\# Phrases to say while processing*

wait\_file: str **= **None, 

*\# Audio URL to play while processing*

meta\_data: Dict **= **None, 

*\# Custom metadata*

meta\_data\_token: str **= **None *\# Token for metadata access*

\)

274

10. Reference

**10.22.3 Decorator Parameter Details**

**Parameter**

**Type**

**Description**

name

str

Override function name

description

str

What the function does

\(shown to AI\)

secure

bool

Require per-call token

authentication

fillers

List\[str\]

Phrases like “Let me check

on that…” 

wait\_file

str

Hold music URL during

processing

meta\_data

Dict

Static metadata for the

function

meta\_data\_token

str

Token scope for metadata

access

**10.22.4**

**Parameter Types**

Function parameters are automatically converted to JSON Schema:

@agent.tool\(description**=**"Book a reservation"\)

**def **book\_reservation\(

name: str, 

*\# Required string*

party\_size: int, 

*\# Required integer*

date: str, 

*\# Required string*

time: str **= **"7:00 PM", 

*\# Optional with default*

special\_requests: str **= **None

*\# Optional, nullable*

\) **-> **SwaigFunctionResult:

... 

Generated parameter schema:

**\{**

"type" **: **"object" **, **

"properties" **: \{**

"name" **: \{**"type" **: **"string" **, **"description" **: **"name parameter" **\}, **

"party\_size" **: \{**"type" **: **"integer" **, **"description" **: **"party\_size parameter" **\}, **

"date" **: \{**"type" **: **"string" **, **"description" **: **"date parameter" **\}, **

"time" **: \{**"type" **: **"string" **, **"description" **: **"time parameter" **\}, **

"special\_requests" **: \{**"type" **: **"string" **, **"description" **: **"special\_requests parameter" **\}**

**\}, **

"required" **: **\["name", "party\_size", "date"\]

**\}**

**10.22.5**

**Type Mapping**

**Python Type**

**JSON Schema Type**

**Notes**

str

string

Basic string

int

integer

Whole numbers

float

number

Decimal numbers

bool

boolean

True/False

list

array

List of items

dict

object

Key-value pairs

Optional\[T\]

T \(nullable\)

Optional parameter

275

10. Reference

**10.22.6 Programmatic Definition**

**10.22.6.1 define\_tool Method**

agent.define\_tool\(

name**=**"search", 

description**=**"Search for information", 

parameters**=**\{

"type": "object", 

"properties": \{

"query": \{

"type": "string", 

"description": "Search query" 

\}, 

"limit": \{

"type": "integer", 

"description": "Maximum results", 

"default": 10

\}

\}, 

"required": \["query"\]

\}, 

handler**=**search\_handler, 

secure**=**False, 

fillers**=**\["Searching now..."\]

\)

**10.22.7**

**Handler Function Signature**

Handler functions receive parsed arguments and raw data:

**def **my\_handler\(

args: Dict\[str, Any\], 

*\# Parsed function arguments*

raw\_data: Dict\[str, Any\]

*\# Complete POST data*

\) **-> **SwaigFunctionResult:

*\# args contains: \{"query": "...", "limit": 10\}*

*\# raw\_data contains full request including metadata*

**return **SwaigFunctionResult\("Result"\)

**10.22.8**

**Raw Data Contents**

The raw\_data parameter contains:

**\{**

"function" **: **"function\_name" **, **

"argument" **: \{**

"parsed" **: **\[**\{**"name" **: **"..." **, **"value" **: **"..." **\}**\]

**\}, **

"call\_id" **: **"uuid-call-id" **, **

"global\_data" **: \{**"key" **: **"value" **\}, **

"meta\_data" **: \{**"key" **: **"value" **\}, **

"caller\_id\_name" **: **"Caller Name" **, **

"caller\_id\_number" **: **"\+15551234567" **, **

"ai\_session\_id" **: **"uuid-session-id" 

**\}**

**10.22.9**

**Accessing Raw Data**

@agent.tool\(description**=**"Process order"\)

**def **process\_order\(order\_id: str, args**=**None, raw\_data**=**None\) **-> **SwaigFunctionResult:

*\# Get global data*

global\_data **= **raw\_data.get\("global\_data", \{\}\)

user\_id **= **global\_data.get\("user\_id"\)

*\# Get caller info*

276

10. Reference

caller\_number **= **raw\_data.get\("caller\_id\_number"\)

*\# Get session info*

call\_id **= **raw\_data.get\("call\_id"\)

**return **SwaigFunctionResult\(f"Order **\{**order\_id**\} **processed"\) **10.22.10**

**Secure Functions**

Secure functions require token authentication per call:

@agent.tool\(

description**=**"Access sensitive data", 

secure**=**True

\)

**def **get\_account\_info\(account\_id: str\) **-> **SwaigFunctionResult:

*\# This function requires a valid token*

**return **SwaigFunctionResult\(f"Account info for **\{**account\_id**\}**"\) **10.22.11**

**Fillers and Wait Files**

Keep users engaged during processing:

*\#\# Text fillers - AI speaks these while processing*

@agent.tool\(

description**=**"Search database", 

fillers**=**\[

"Let me search for that...", 

"One moment please...", 

"Checking our records..." 

\]

\)

**def **search\_database\(query: str\) **-> **SwaigFunctionResult:

... 

*\#\# Wait file - Play audio while processing*

@agent.tool\(

description**=**"Long operation", 

wait\_file**=**"https://example.com/hold\_music.mp3" 

\)

**def **long\_operation\(data: str\) **-> **SwaigFunctionResult:

... 

**10.22.12**

**Return Value Requirements**

**IMPORTANT**: All SWAIG functions MUST return SwaigFunctionResult:

*\#\# Correct*

@agent.tool\(description**=**"Get info"\)

**def **get\_info\(id: str\) **-> **SwaigFunctionResult:

**return **SwaigFunctionResult\("Information retrieved"\)

*\#\# WRONG - Never return plain strings*

@agent.tool\(description**=**"Get info"\)

**def **get\_info\(id: str\) **-> **str:

**return **"Information retrieved" 

*\# This will fail\! *

277

10. Reference

**10.22.13**

**Complete Example**

*\#\!/usr/bin/env python3*

*\#\# order\_functions\_agent.py - Agent with various SWAIG function patterns* from signalwire\_agents import AgentBase

from signalwire\_agents.core.function\_result import SwaigFunctionResult agent **= **AgentBase\(name**=**"order-agent", route**=**"/orders"\)

*\#\# Simple function*

@agent.tool\(description**=**"Get order status"\)

**def **get\_order\_status\(order\_id: str\) **-> **SwaigFunctionResult: status **= **lookup\_order\(order\_id\)

**return **SwaigFunctionResult\(f"Order **\{**order\_id**\} **is **\{**status**\}**"\)

*\#\# Function with multiple parameters*

@agent.tool\(description**=**"Place a new order"\)

**def **place\_order\(

product: str, 

quantity: int **= **1, 

shipping: str **= **"standard" 

\) **-> **SwaigFunctionResult:

order\_id **= **create\_order\(product, quantity, shipping\)

**return **SwaigFunctionResult\(f"Order **\{**order\_id**\} **placed successfully"\)

*\#\# Secure function with fillers*

@agent.tool\(

description**=**"Cancel an order", 

secure**=**True, 

fillers**=**\["Let me process that cancellation..."\]

\)

**def **cancel\_order\(order\_id: str, reason: str **= **None\) **-> **SwaigFunctionResult: cancel\_result **= **do\_cancel\(order\_id, reason\)

**return **SwaigFunctionResult\(f"Order **\{**order\_id**\} **has been cancelled"\)

*\#\# Function that returns actions*

@agent.tool\(description**=**"Transfer to support"\)

**def **transfer\_to\_support\(issue\_type: str\) **-> **SwaigFunctionResult: **return **\(

SwaigFunctionResult\("I'll transfer you to our support team"\)

.connect\("\+15551234567", final**=**True\)

\)

**if **\_\_name\_\_ **== **"\_\_main\_\_":

agent.run\(\)

278

10. Reference

**10.23**

**SwaigFunctionResult API**

**Summary**: Complete API reference for SwaigFunctionResult, the class for returning responses and actions from SWAIG functions. 

**10.23.1 Class Definition**

from signalwire\_agents.core.function\_result import SwaigFunctionResult **class **SwaigFunctionResult:

*"""Wrapper around SWAIG function responses.""" *

**10.23.2**

**Constructor**

SwaigFunctionResult\(

response: Optional\[str\] **= **None, 

*\# Text for AI to speak*

post\_process: bool **= **False

*\# Let AI respond before actions*

\)

**10.23.3**

**Core Concept**

**Component**

**Purpose**

response

Text the AI should say back to the user

action

List of structured actions to execute

post\_process

Let AI respond once more before executing actions

**Post-Processing Behavior:**

• post\_process=False \(default\): Execute actions immediately

• post\_process=True: AI responds first, then actions execute

**10.23.4**

**Basic Methods**

**10.23.4.1**

**set\_response**

**def **set\_response\(self, response: str\) **-> **'SwaigFunctionResult' 

Set the response text. 

**10.23.4.2**

**set\_post\_process**

**def **set\_post\_process\(self, post\_process: bool\) **-> **'SwaigFunctionResult' 

Set post-processing behavior. 

**10.23.4.3**

**add\_action**

**def **add\_action\(self, name: str, data: Any\) **-> **'SwaigFunctionResult' 

Add a single action. 

279

10. Reference

**10.23.4.4 add\_actions**

**def **add\_actions\(self, actions: List\[Dict\[str, Any\]\]\) **-> **'SwaigFunctionResult' 

Add multiple actions. 

**10.23.5 Call Control Actions**

**10.23.5.1 connect**

**def **connect\(

self, 

destination: str, 

*\# Phone number or SIP address*

final: bool **= **True, 

*\# Permanent \(True\) or temporary \(False\)*

from\_addr: Optional\[str\] **= **None

*\# Caller ID override*

\) **-> **'SwaigFunctionResult' 

Transfer the call to another destination. 

*\#\# Permanent transfer*

**return **SwaigFunctionResult\("Transferring you now"\).connect\("\+15551234567"\)

*\#\# Temporary transfer \(returns to agent when far end hangs up\)* **return **SwaigFunctionResult\("Connecting you"\).connect\("\+15551234567", final**=**False\)

*\#\# With custom caller ID*

**return **SwaigFunctionResult\("Transferring"\).connect\(

"support@company.com", 

final**=**True, 

from\_addr**=**"\+15559876543" 

\)

**10.23.5.2**

**hangup**

**def **hangup\(self\) **-> **'SwaigFunctionResult' 

End the call. 

**return **SwaigFunctionResult\("Goodbye\!"\).hangup\(\)

**10.23.5.3**

**hold**

**def **hold\(self, timeout: int **= **300\) **-> **'SwaigFunctionResult' 

Put the call on hold \(max 900 seconds\). 

**return **SwaigFunctionResult\("Please hold"\).hold\(timeout**=**120\) **10.23.5.4**

**stop**

**def **stop\(self\) **-> **'SwaigFunctionResult' 

Stop agent execution. 

**return **SwaigFunctionResult\("Stopping now"\).stop\(\) 280

10. Reference

**10.23.6 Speech Actions**

**10.23.6.1 say**

**def **say\(self, text: str\) **-> **'SwaigFunctionResult' 

Make the agent speak specific text. 

**return **SwaigFunctionResult\(\).say\("Important announcement\!"\) **10.23.6.2 wait\_for\_user**

**def **wait\_for\_user\(

self, 

enabled: Optional\[bool\] **= **None, 

*\# Enable/disable*

timeout: Optional\[int\] **= **None, 

*\# Seconds to wait*

answer\_first: bool **= **False

*\# Special mode*

\) **-> **'SwaigFunctionResult' 

Control how agent waits for user input. 

**return **SwaigFunctionResult\("Take your time"\).wait\_for\_user\(timeout**=**30\) **10.23.7**

**Data Actions**

**10.23.7.1**

**update\_global\_data**

**def **update\_global\_data\(self, data: Dict\[str, Any\]\) **-> **'SwaigFunctionResult' 

Update global session data. 

**return **SwaigFunctionResult\("Account verified"\).update\_global\_data\(\{

"verified": True, 

"user\_id": "12345" 

\}\)

**10.23.7.2**

**remove\_global\_data**

**def **remove\_global\_data\(self, keys: Union\[str, List\[str\]\]\) **-> **'SwaigFunctionResult' 

Remove keys from global data. 

**return **SwaigFunctionResult\("Cleared"\).remove\_global\_data\(\["temp\_data", "cache"\]\) **10.23.7.3**

**set\_metadata**

**def **set\_metadata\(self, data: Dict\[str, Any\]\) **-> **'SwaigFunctionResult' 

Set metadata scoped to the function’s token. 

**return **SwaigFunctionResult\("Saved"\).set\_metadata\(\{"last\_action": "search"\}\) 281

10. Reference

**10.23.7.4 remove\_metadata**

**def **remove\_metadata\(self, keys: Union\[str, List\[str\]\]\) **-> **'SwaigFunctionResult' 

Remove metadata keys. 

**10.23.8 Media Actions**

**10.23.8.1 play\_background\_file**

**def **play\_background\_file\(

self, 

filename: str, 

*\# Audio/video URL*

wait: bool **= **False

*\# Suppress attention-getting*

\) **-> **'SwaigFunctionResult' 

Play background audio. 

**return **SwaigFunctionResult\(\).play\_background\_file\(

"https://example.com/music.mp3", 

wait**=**True

\)

**10.23.8.2 stop\_background\_file**

**def **stop\_background\_file\(self\) **-> **'SwaigFunctionResult' 

Stop background playback. 

**10.23.9**

**Recording Actions**

**10.23.9.1**

**record\_call**

**def **record\_call\(

self, 

control\_id: Optional\[str\] **= **None, 

*\# Recording identifier*

stereo: bool **= **False, 

*\# Stereo recording*

format: str **= **"wav", 

*\# "wav", "mp3", or "mp4" *

direction: str **= **"both", 

*\# "speak", "listen", or "both" *

terminators: Optional\[str\] **= **None, *\# Digits to stop recording* beep: bool **= **False, 

*\# Play beep before recording*

input\_sensitivity: float **= **44.0, 

*\# Input sensitivity*

initial\_timeout: float **= **0.0, 

*\# Wait for speech start*

end\_silence\_timeout: float **= **0.0, 

*\# Silence before ending*

max\_length: Optional\[float\] **= **None, 

*\# Max duration*

status\_url: Optional\[str\] **= **None

*\# Status webhook URL*

\) **-> **'SwaigFunctionResult' 

Start call recording. 

**return **SwaigFunctionResult\("Recording started"\).record\_call\(

control\_id**=**"main\_recording", 

stereo**=**True, 

format**=**"mp3" 

\)

282

10. Reference

**10.23.9.2 stop\_record\_call**

**def **stop\_record\_call\(

self, 

control\_id: Optional\[str\] **= **None

*\# Recording to stop*

\) **-> **'SwaigFunctionResult' 

Stop recording. 

**10.23.10**

**Messaging Actions**

**10.23.10.1 send\_sms**

**def **send\_sms\(

self, 

to\_number: str, 

*\# Destination \(E.164\)*

from\_number: str, 

*\# Sender \(E.164\)*

body: Optional\[str\] **= **None, 

*\# Message text*

media: Optional\[List\[str\]\] **= **None, *\# Media URLs*

tags: Optional\[List\[str\]\] **= **None, 

*\# Tags for searching*

region: Optional\[str\] **= **None

*\# Origin region*

\) **-> **'SwaigFunctionResult' 

Send SMS message. 

**return **SwaigFunctionResult\("Confirmation sent"\).send\_sms\(

to\_number**=**"\+15551234567", 

from\_number**=**"\+15559876543", 

body**=**"Your order has been confirmed\!" 

\)

**10.23.11**

**Payment Actions**

**10.23.11.1 pay**

**def **pay\(

self, 

payment\_connector\_url: str, 

*\# Payment endpoint \(required\)*

input\_method: str **= **"dtmf", 

*\# "dtmf" or "voice" *

payment\_method: str **= **"credit-card", 

timeout: int **= **5, 

*\# Digit timeout*

max\_attempts: int **= **1, 

*\# Retry attempts*

security\_code: bool **= **True, 

*\# Prompt for CVV*

postal\_code: Union\[bool, str\] **= **True, 

*\# Prompt for zip*

charge\_amount: Optional\[str\] **= **None, 

*\# Amount to charge*

currency: str **= **"usd", 

language: str **= **"en-US", 

voice: str **= **"woman", 

valid\_card\_types: str **= **"visa mastercard amex", 

ai\_response: Optional\[str\] **= **None

*\# Post-payment response*

\) **-> **'SwaigFunctionResult' 

Process payment. 

**return **SwaigFunctionResult\("Processing payment"\).pay\(

payment\_connector\_url**=**"https://pay.example.com/process", charge\_amount**=**"49.99", 

currency**=**"usd" 

\)

283

10. Reference

**10.23.12**

**Context Actions**

**10.23.12.1 swml\_change\_step**

**def **swml\_change\_step\(self, step\_name: str\) **-> **'SwaigFunctionResult' 

Change conversation step. 

**return **SwaigFunctionResult\("Moving to confirmation"\).swml\_change\_step\("confirm"\) **10.23.12.2 swml\_change\_context**

**def **swml\_change\_context\(self, context\_name: str\) **-> **'SwaigFunctionResult' 

Change conversation context. 

**return **SwaigFunctionResult\("Switching to support"\).swml\_change\_context\("support"\) **10.23.12.3 switch\_context**

**def **switch\_context\(

self, 

system\_prompt: Optional\[str\] **= **None, 

*\# New system prompt*

user\_prompt: Optional\[str\] **= **None, 

*\# User message to add*

consolidate: bool **= **False, 

*\# Summarize conversation*

full\_reset: bool **= **False

*\# Complete reset*

\) **-> **'SwaigFunctionResult' 

Advanced context switching. 

**10.23.13**

**Conference Actions**

**10.23.13.1 join\_room**

**def **join\_room\(self, name: str\) **-> **'SwaigFunctionResult' 

Join a RELAY room. 

**10.23.13.2 join\_conference**

**def **join\_conference\(

self, 

name: str, 

*\# Conference name \(required\)*

muted: bool **= **False, 

*\# Join muted*

beep: str **= **"true", 

*\# Beep config*

start\_on\_enter: bool **= **True, 

*\# Start when joining*

end\_on\_exit: bool **= **False, 

*\# End when leaving*

max\_participants: int **= **250, 

*\# Max attendees*

record: str **= **"do-not-record" *\# Recording mode*

\) **-> **'SwaigFunctionResult' 

Join audio conference. 

284

10. Reference

**10.23.14**

**Tap/Stream Actions**

**10.23.14.1 tap**

**def **tap\(

self, 

uri: str, 

*\# Destination URI \(required\)*

control\_id: Optional\[str\] **= **None, 

direction: str **= **"both", 

*\# "speak", "hear", "both" *

codec: str **= **"PCMU", 

*\# "PCMU" or "PCMA" *

rtp\_ptime: int **= **20

\) **-> **'SwaigFunctionResult' 

Start media tap/stream. 

**10.23.14.2 stop\_tap**

**def **stop\_tap\(self, control\_id: Optional\[str\] **= **None\) **-> **'SwaigFunctionResult' 

Stop media tap. 

**10.23.15**

**SIP Actions**

**10.23.15.1 sip\_refer**

**def **sip\_refer\(self, to\_uri: str\) **-> **'SwaigFunctionResult' 

Send SIP REFER for call transfer. 

**10.23.16**

**Advanced Actions**

**10.23.16.1 execute\_swml**

**def **execute\_swml\(

self, 

swml\_content, 

*\# String, Dict, or SWML object*

transfer: bool **= **False

*\# Exit agent after execution*

\) **-> **'SwaigFunctionResult' 

Execute raw SWML. 

swml\_doc **= **\{

"version": "1.0.0", 

"sections": \{

"main": \[\{"play": \{"url": "https://example.com/audio.mp3"\}\}\]

\}

\}

**return **SwaigFunctionResult\(\).execute\_swml\(swml\_doc\)

**10.23.16.2 toggle\_functions**

**def **toggle\_functions\(

self, 

function\_toggles: List\[Dict\[str, Any\]\]

\) **-> **'SwaigFunctionResult' 

Enable/disable specific functions. 

**return **SwaigFunctionResult\("Functions updated"\).toggle\_functions\(\[

\{"function": "transfer\_call", "active": True\}, 285

10. Reference

\{"function": "cancel\_order", "active": False\}

\]\)

**10.23.17**

**Settings Actions**

**10.23.17.1 update\_settings**

**def **update\_settings\(self, settings: Dict\[str, Any\]\) **-> **'SwaigFunctionResult' 

Update AI runtime settings. 

**return **SwaigFunctionResult\(\).update\_settings\(\{

"temperature": 0.5, 

"confidence": 0.8

\}\)

**10.23.17.2 set\_end\_of\_speech\_timeout**

**def **set\_end\_of\_speech\_timeout\(self, milliseconds: int\) **-> **'SwaigFunctionResult' 

Adjust speech detection timeout. 

**10.23.18**

**Method Chaining**

All methods return self for chaining:

**return **\(

SwaigFunctionResult\("Processing your order"\)

.update\_global\_data\(\{"order\_id": "12345"\}\)

.send\_sms\(

to\_number**=**"\+15551234567", 

from\_number**=**"\+15559876543", 

body**=**"Order confirmed\!" 

\)

.swml\_change\_step\("confirmation"\)

\)

**10.23.19**

**to\_dict Method**

**def **to\_dict\(self\) **-> **Dict\[str, Any\]

Convert to SWAIG response format. Called automatically when returning from functions. 

286

10. Reference

**10.24**

**DataMap API**

**Summary**: API reference for DataMap, enabling serverless REST API integration without webhooks. 

**10.24.1 Class Definition**

from signalwire\_agents.core.data\_map import DataMap

**class **DataMap:

*"""Builder class for creating SWAIG data\_map configurations.""" *

**10.24.2**

**Overview**

DataMap enables SWAIG functions that execute on SignalWire servers without requiring your own webhook endpoints. 

**Use Cases: **- Call external APIs directly from SWML - Pattern-based responses without API calls - Reduce infrastructure requirements - Serverless function execution

**10.24.3**

**Constructor**

DataMap\(function\_name: str\)

Create a new DataMap builder. 

**10.24.4**

**Core Methods**

**10.24.4.1**

**purpose / description**

**def **purpose\(self, description: str\) **-> **'DataMap' 

**def **description\(self, description: str\) **-> **'DataMap' 

*\# Alias*

Set the function description shown to the AI. 

data\_map **= **DataMap\("get\_weather"\).purpose\("Get current weather for a city"\) **10.24.4.2**

**parameter**

**def **parameter\(

self, 

name: str, 

*\# Parameter name*

param\_type: str, 

*\# JSON schema type*

description: str, 

*\# Parameter description*

required: bool **= **False, 

*\# Is required*

enum: Optional\[List\[str\]\] **= **None

*\# Allowed values*

\) **-> **'DataMap' 

Add a function parameter. 

data\_map **= **\(

DataMap\("search"\)

.purpose\("Search for items"\)

.parameter\("query", "string", "Search query", required**=**True\)

.parameter\("limit", "integer", "Max results", required**=**False\)

.parameter\("category", "string", "Category filter", enum**=**\["electronics", "clothing", "food"\]\)

\)

287

10. Reference

**10.24.5 Parameter Types**

**Type**

**JSON Schema**

**Description**

string

string

Text values

integer

integer

Whole numbers

number

number

Decimal numbers

boolean

boolean

True/False

array

array

List of items

object

object

Key-value pairs

**10.24.6**

**Webhook Methods**

**10.24.6.1 webhook**

**def **webhook\(

self, 

method: str, 

*\# HTTP method*

url: str, 

*\# API endpoint*

headers: Optional\[Dict\[str, str\]\] **= **None, 

*\# HTTP headers*

form\_param: Optional\[str\] **= **None, 

*\# Form parameter name*

input\_args\_as\_params: bool **= **False, 

*\# Merge args to params*

require\_args: Optional\[List\[str\]\] **= **None

*\# Required args*

\) **-> **'DataMap' 

Add an API call. 

data\_map **= **\(

DataMap\("get\_weather"\)

.purpose\("Get weather information"\)

.parameter\("city", "string", "City name", required**=**True\)

.webhook\("GET", "https://api.weather.com/v1/current?q=$\{enc:args.city\}&key=API\_KEY"\)

\)

**10.24.6.2**

**body**

**def **body\(self, data: Dict\[str, Any\]\) **-> **'DataMap' 

Set request body for POST/PUT. 

data\_map **= **\(

DataMap\("create\_ticket"\)

.purpose\("Create support ticket"\)

.parameter\("subject", "string", "Ticket subject", required**=**True\)

.parameter\("message", "string", "Ticket message", required**=**True\)

.webhook\("POST", "https://api.support.com/tickets", headers**=**\{"Authorization": "Bearer TOKEN"\}\)

.body\(\{

"subject": "$**\{args.subject\}**", 

"body": "$**\{args.message\}**", 

"priority": "normal" 

\}\)

\)

288

10. Reference

**10.24.6.3 params**

**def **params\(self, data: Dict\[str, Any\]\) **-> **'DataMap' 

Set request parameters \(alias for body\). 

**10.24.7 Output Methods**

**10.24.7.1 output**

**def **output\(self, result: SwaigFunctionResult\) **-> **'DataMap' 

Set the output for the most recent webhook. 

from signalwire\_agents.core.function\_result import SwaigFunctionResult data\_map **= **\(

DataMap\("get\_weather"\)

.purpose\("Get weather"\)

.parameter\("city", "string", "City", required**=**True\)

.webhook\("GET", "https://api.weather.com/current?q=$\{enc:args.city\}"\)

.output\(SwaigFunctionResult\(

"The weather in $**\{args.city\} **is $**\{response.condition\} **with a temperature of $**\{response.temp\}**°F" 

\)\)

\)

**10.24.7.2**

**fallback\_output**

**def **fallback\_output\(self, result: SwaigFunctionResult\) **-> **'DataMap' 

Set output when all webhooks fail. 

data\_map **= **\(

DataMap\("search"\)

.purpose\("Search multiple sources"\)

.webhook\("GET", "https://api.primary.com/search?q=$\{enc:args.query\}"\)

.output\(SwaigFunctionResult\("Found: $**\{response.title\}**"\)\)

.webhook\("GET", "https://api.backup.com/search?q=$\{enc:args.query\}"\)

.output\(SwaigFunctionResult\("Backup result: $**\{response.title\}**"\)\)

.fallback\_output\(SwaigFunctionResult\("Sorry, search is unavailable"\)\)

\)

**10.24.8**

**Variable Patterns**

**Pattern**

**Description**

$\{args.param\}

Function argument value

$\{enc:args.param\}

URL-encoded argument \(use in webhook URLs\)

$\{lc:args.param\}

Lowercase argument value

$\{fmt\_ph:args.phone\}

Format as phone number

$\{response.field\}

API response field

$\{response.arr\[0\]\}

Array element in response

$\{global\_data.key\}

Global session data

$\{meta\_data.key\}

Call metadata

$\{this.field\}

Current item in foreach

289

10. Reference

**10.24.8.1 Chained Modifiers**

Modifiers are applied right-to-left:

**Pattern**

**Result**

$\{enc:lc:args.param\}

First lowercase, then URL encode

$\{lc:enc:args.param\}

First URL encode, then lowercase

**10.24.8.2 Examples**

**Pattern**

**Result**

$\{args.city\}

“Seattle” \(in body/output\)

$\{enc:args.city\}

“Seattle” URL-encoded \(in URLs\)

$\{lc:args.city\}

“seattle” \(lowercase\)

$\{enc:lc:args.city\}

“seattle” lowercased then URL-encoded

$\{fmt\_ph:args.phone\}

“\+1 \(555\) 123-4567” 

$\{response.temp\}

“65” 

$\{response.items\[0\].name\}

“First item” 

$\{global\_data.user\_id\}

“user123” 

**10.24.9**

**Expression Methods**

**10.24.9.1**

**expression**

**def **expression\(

self, 

test\_value: str, 

*\# Template to test*

pattern: Union\[str, Pattern\], 

*\# Regex pattern*

output: SwaigFunctionResult, 

*\# Match output*

nomatch\_output: Optional\[SwaigFunctionResult\] **= **None

*\# No-match output*

\) **-> **'DataMap' 

Add pattern-based response \(no API call needed\). 

data\_map **= **\(

DataMap\("control\_playback"\)

.purpose\("Control media playback"\)

.parameter\("command", "string", "Playback command", required**=**True\)

.expression\(

"$**\{args.command\}**", 

r"play**|**start", 

SwaigFunctionResult\("Starting playback"\).add\_action\("playback\_bg", "music.mp3"\)

\)

.expression\(

"$**\{args.command\}**", 

r"stop**|**pause", 

SwaigFunctionResult\("Stopping playback"\).add\_action\("stop\_playback\_bg", True\)

\)

\)

290

10. Reference

**10.24.10**

**Array Processing**

**10.24.10.1 foreach**

**def **foreach\(self, foreach\_config: Dict\[str, Any\]\) **-> **'DataMap' 

Process array from API response. 

data\_map **= **\(

DataMap\("search\_products"\)

.purpose\("Search product catalog"\)

.parameter\("query", "string", "Search query", required**=**True\)

.webhook\("GET", "https://api.store.com/products?q=$\{enc:args.query\}"\)

.foreach\(\{

"input\_key": "products", 

"output\_key": "product\_list", 

"max": 3, 

"append": "- $**\{this.name\}**: $$**\{this.price\}**\\n" 

\}\)

.output\(SwaigFunctionResult\("Found products:\\n$**\{product\_list\}**"\)\)

\)

**10.24.11**

**Foreach Configuration**

**Key**

**Type**

**Description**

input\_key

string

Key in response containing

array

output\_key

string

Variable name for built

string

max

integer

Maximum items to process

\(optional\)

append

string

Template for each item

**10.24.12**

**Webhook Expressions**

**10.24.12.1 webhook\_expressions**

**def **webhook\_expressions\(

self, 

expressions: List\[Dict\[str, Any\]\]

\) **-> **'DataMap' 

Add expressions to run after webhook completes. 

**10.24.13**

**Registering with Agent**

from signalwire\_agents import AgentBase

from signalwire\_agents.core.data\_map import DataMap

from signalwire\_agents.core.function\_result import SwaigFunctionResult agent **= **AgentBase\(name**=**"weather-agent"\)

*\#\# Create DataMap*

weather\_map **= **\(

DataMap\("get\_weather"\)

.purpose\("Get current weather for a location"\)

.parameter\("city", "string", "City name", required**=**True\)

.webhook\("GET", "https://api.weather.com/v1/current?q=$\{enc:args.city\}&key=YOUR\_KEY"\)

.output\(SwaigFunctionResult\(

"The weather in $**\{args.city\} **is $**\{response.current.condition.text\} **" 

291

10. Reference

"with $**\{response.current.temp\_f\}**°F" 

\)\)

\)

*\#\# Register with agent - convert DataMap to SWAIG function dictionary* agent.register\_swaig\_function\(weather\_map.to\_swaig\_function\(\)\)

**10.24.14**

**Complete Example**

*\#\!/usr/bin/env python3*

*\#\# datamap\_api\_agent.py - Agent using DataMap for API calls*

from signalwire\_agents import AgentBase

from signalwire\_agents.core.data\_map import DataMap

from signalwire\_agents.core.function\_result import SwaigFunctionResult agent **= **AgentBase\(name**=**"api-agent", route**=**"/api"\) agent.add\_language\("English", "en-US", "rime.spore"\)

*\#\# Weather lookup*

weather **= **\(

DataMap\("check\_weather"\)

.purpose\("Check weather conditions"\)

.parameter\("location", "string", "City or zip code", required**=**True\)

.webhook\("GET", "https://api.weather.com/v1/current?q=$\{enc:args.location\}"\)

.output\(SwaigFunctionResult\(

"Current conditions in $**\{args.location\}**: $**\{response.condition\}**, $**\{response.temp\}**°F" 

\)\)

.fallback\_output\(SwaigFunctionResult\("Weather service is currently unavailable"\)\)

\)

*\#\# Order status lookup*

order\_status **= **\(

DataMap\("check\_order"\)

.purpose\("Check order status"\)

.parameter\("order\_id", "string", "Order number", required**=**True\)

.webhook\("GET", "https://api.orders.com/status/$\{enc:args.order\_id\}", headers**=**\{"Authorization": "Bearer $**\{env.API\_KEY\}**"\}\)

.output\(SwaigFunctionResult\(

"Order $**\{args.order\_id\}**: $**\{response.status\}**. " 

"Expected delivery: $**\{response.delivery\_date\}**" 

\)\)

\)

*\#\# Expression-based control*

volume\_control **= **\(

DataMap\("set\_volume"\)

.purpose\("Control audio volume"\)

.parameter\("level", "string", "Volume level", required**=**True\)

.expression\("$**\{args.level\}**", r"high**|**loud**|**up", SwaigFunctionResult\("Volume increased"\).add\_action\("volume", 100\)\)

.expression\("$**\{args.level\}**", r"low**|**quiet**|**down", SwaigFunctionResult\("Volume decreased"\).add\_action\("volume", 30\)\)

.expression\("$**\{args.level\}**", r"mute**|**off", SwaigFunctionResult\("Audio muted"\).add\_action\("mute", True\)\)

\)

*\#\# Register all - convert DataMap to SWAIG function dictionary* agent.register\_swaig\_function\(weather.to\_swaig\_function\(\)\)

agent.register\_swaig\_function\(order\_status.to\_swaig\_function\(\)\)

agent.register\_swaig\_function\(volume\_control.to\_swaig\_function\(\)\)

**if **\_\_name\_\_ **== **"\_\_main\_\_":

agent.run\(\)

292

10. Reference

**10.25**

**SkillBase API**

**Summary**: API reference for SkillBase, the abstract base class for creating custom agent skills. 

**10.25.1 Class Definition**

from signalwire\_agents.core.skill\_base import SkillBase

**class **SkillBase\(ABC\):

*"""Abstract base class for all agent skills.""" *

**10.25.2**

**Overview**

Skills are modular, reusable capabilities that can be added to agents. 

**Features: **- Auto-discovered from skill directories - Automatic dependency validation - Configuration via parameters

- Can add tools, prompts, hints, and global data

**10.25.3**

**Class Attributes**

**class **MySkill\(SkillBase\):

*\# Required attributes*

SKILL\_NAME: str **= **"my\_skill" 

*\# Unique identifier*

SKILL\_DESCRIPTION: str **= **"Description" *\# Human-readable description*

*\# Optional attributes*

SKILL\_VERSION: str **= **"1.0.0" 

*\# Semantic version*

REQUIRED\_PACKAGES: List\[str\] **= **\[\]

*\# Python packages needed*

REQUIRED\_ENV\_VARS: List\[str\] **= **\[\]

*\# Environment variables needed*

SUPPORTS\_MULTIPLE\_INSTANCES: bool **= **False

*\# Allow multiple instances*

**10.25.4**

**Class Attributes Reference**

**Attribute**

**Type**

**Required**

**Description**

SKILL\_NAME

str

Yes

Unique identifier

SKILL\_DESCRIPTION

str

Yes

Description

SKILL\_VERSION

str

No

Version string

REQUIRED\_PACKAGES

List\[str\]

No

Package dependencies

REQUIRED\_ENV\_VARS

List\[str\]

No

Required env vars

SUPPORTS\_MULTIPLE\_INSTAN

bool

No

Multiple instances

CES

**10.25.5**

**Constructor**

**def \_\_init\_\_**\(

self, 

agent: 'AgentBase', 

*\# Parent agent*

params: Optional\[Dict\[str, Any\]\] **= **None

*\# Skill configuration*

\)

293

10. Reference

**10.25.6 Instance Attributes**

self.agent

*\# Reference to parent AgentBase*

self.params

*\# Configuration parameters dict*

self.logger

*\# Skill-specific logger*

self.swaig\_fields

*\# SWAIG metadata to merge into tools*

**10.25.7 Abstract Methods \(Must Implement\)**

**10.25.7.1 setup**

@abstractmethod

**def **setup\(self\) **-> **bool:

*""" *

*Setup the skill. *

*Returns:*

*True if setup successful, False otherwise*

*""" *

**pass**

Validate environment, initialize APIs, prepare resources. 

**10.25.7.2 register\_tools**

@abstractmethod

**def **register\_tools\(self\) **-> **None:

*"""Register SWAIG tools with the agent.""" *

**pass**

Register functions that the skill provides. 

**10.25.8**

**Helper Methods**

**10.25.8.1**

**define\_tool**

**def **define\_tool\(self, **\*\***kwargs\) **-> **None

Register a tool with automatic swaig\_fields merging. 

**def **register\_tools\(self\):

self.define\_tool\(

name**=**"my\_search", 

description**=**"Search functionality", 

handler**=**self.\_handle\_search, 

parameters**=**\{

"type": "object", 

"properties": \{

"query": \{"type": "string", "description": "Search query"\}

\}, 

"required": \["query"\]

\}

\)

**10.25.8.2**

**validate\_env\_vars**

**def **validate\_env\_vars\(self\) **-> **bool

Check if all required environment variables are set. 

294

10. Reference

**10.25.8.3 validate\_packages**

**def **validate\_packages\(self\) **-> **bool

Check if all required Python packages are available. 

**10.25.9 Optional Override Methods**

**10.25.9.1 get\_hints**

**def **get\_hints\(self\) **-> **List\[str\]:

*"""Return speech recognition hints for this skill.""" *

**return **\[\]

**10.25.9.2 get\_global\_data**

**def **get\_global\_data\(self\) **-> **Dict\[str, Any\]:

*"""Return data to add to agent's global context.""" *

**return **\{\}

**10.25.9.3 get\_prompt\_sections**

**def **get\_prompt\_sections\(self\) **-> **List\[Dict\[str, Any\]\]:

*"""Return prompt sections to add to agent.""" *

**return **\[\]

**10.25.9.4**

**cleanup**

**def **cleanup\(self\) **-> **None:

*"""Cleanup when skill is removed or agent shuts down.""" *

**pass**

**10.25.9.5**

**get\_instance\_key**

**def **get\_instance\_key\(self\) **-> **str:

*"""Get unique key for this skill instance.""" *

**pass**

**10.25.10**

**Parameter Schema**

**10.25.10.1 get\_parameter\_schema**

@classmethod

**def **get\_parameter\_schema\(cls\) **-> **Dict\[str, Dict\[str, Any\]\]:

*"""Get parameter schema for this skill.""" *

**pass**

Define configuration parameters:

@classmethod

**def **get\_parameter\_schema\(cls\):

schema **= **super\(\).get\_parameter\_schema\(\)

schema.update\(\{

"api\_key": \{

"type": "string", 

"description": "API key for service", 

"required": True, 

"hidden": True, 

295

10. Reference

"env\_var": "MY\_API\_KEY" 

\}, 

"max\_results": \{

"type": "integer", 

"description": "Maximum results to return", 

"default": 10, 

"min": 1, 

"max": 100

\}

\}\)

**return **schema

**10.25.11**

**Parameter Schema Fields**

**Field**

**Type**

**Description**

type

string

Parameter type \(string, 

integer, number, etc.\)

description

string

Human-readable description

default

any

Default value if not provided

required

bool

Whether parameter is

required

hidden

bool

Hide in UIs \(for secrets\)

env\_var

string

Environment variable

alternative

enum

list

List of allowed values

min/max

number

Min/max for numeric types

**10.25.12**

**Complete Skill Example**

from signalwire\_agents.core.skill\_base import SkillBase

from signalwire\_agents.core.function\_result import SwaigFunctionResult from typing import Dict, Any, List

import os

**class **WeatherSkill\(SkillBase\):

*"""Skill for weather lookups.""" *

SKILL\_NAME **= **"weather" 

SKILL\_DESCRIPTION **= **"Provides weather information" 

SKILL\_VERSION **= **"1.0.0" 

REQUIRED\_PACKAGES **= **\["requests"\]

REQUIRED\_ENV\_VARS **= **\["WEATHER\_API\_KEY"\]

**def **setup\(self\) **-> **bool:

*"""Initialize the weather skill.""" *

*\# Validate dependencies*

**if not **self.validate\_packages\(\):

**return **False

**if not **self.validate\_env\_vars\(\):

**return **False

*\# Store API key*

self.api\_key **= **os.getenv\("WEATHER\_API\_KEY"\)

**return **True

**def **register\_tools\(self\) **-> **None:

*"""Register weather tools.""" *

self.define\_tool\(

name**=**"get\_weather", 

description**=**"Get current weather for a location", handler**=**self.\_get\_weather, 

296

10. Reference

parameters**=**\{

"type": "object", 

"properties": \{

"location": \{

"type": "string", 

"description": "City name or zip code" 

\}

\}, 

"required": \["location"\]

\}

\)

**def **\_get\_weather\(self, args: Dict, raw\_data: Dict\) **-> **SwaigFunctionResult:

*"""Handle weather lookup.""" *

import requests

location **= **args.get\("location"\)

url **= **f"https://api.weather.com/v1/current?q=**\{**location**\}**&key=**\{**self**. **api\_key**\}**" 

**try**:

response **= **requests.get\(url\)

data **= **response.json\(\)

**return **SwaigFunctionResult\(

f"Weather in **\{**location**\}**: **\{**data\['condition'\]**\}**, **\{**data\['temp'\]**\}**°F" 

\)

**except ** *Exception * as e:

**return **SwaigFunctionResult\(f"Unable to get weather: **\{**str\(e\)**\}**"\) **def **get\_hints\(self\) **-> **List\[str\]:

*"""Speech recognition hints.""" *

**return **\["weather", "temperature", "forecast", "sunny", "rainy"\]

**def **get\_prompt\_sections\(self\) **-> **List\[Dict\[str, Any\]\]:

*"""Add weather instructions to prompt.""" *

**return **\[\{

"title": "Weather Information", 

"body": "You can check weather for any location using the get\_weather function." 

\}\]

@classmethod

**def **get\_parameter\_schema\(cls\):

schema **= **super\(\).get\_parameter\_schema\(\)

schema.update\(\{

"units": \{

"type": "string", 

"description": "Temperature units", 

"default": "fahrenheit", 

"enum": \["fahrenheit", "celsius"\]

\}

\}\)

**return **schema

**10.25.13**

**Using Skills**

from signalwire\_agents import AgentBase

agent **= **AgentBase\(name**=**"weather-agent"\)

*\#\# Add skill with default configuration*

agent.add\_skill\("weather"\)

*\#\# Add skill with custom configuration*

agent.add\_skill\("weather", \{

"units": "celsius" 

\}\)

*\#\# List available skills*

print\(agent.list\_available\_skills\(\)\)

297

10. Reference

**10.25.14**

**Skill Directory Structure**

signalwire\_agents/skills/

weather/

\_\_init\_\_.py

skill.py

\# WeatherSkill class

requirements.txt

\# Skill-specific dependencies

calendar/

\_\_init\_\_.py

skill.py

requirements.txt

... 

298

10. Reference

**10.26**

**ContextBuilder API**

**Summary**: API reference for ContextBuilder and Step classes, enabling multi-step conversation workflows. 

**10.26.1 Class Definitions**

from signalwire\_agents.core.contexts import ContextBuilder, Step

**10.26.2**

**Overview**

Contexts define structured conversation workflows with multiple steps. 

**Context Structure: **- **Context **- A named conversation workflow - **Steps **- Sequential conversation phases - Prompt text or POM sections - Completion criteria - Available functions - Navigation rules **10.26.3**

**Step Class**

**10.26.3.1 Constructor**

Step\(name: str\)

*\# Step name/identifier*

**10.26.3.2 set\_text**

**def **set\_text\(self, text: str\) **-> **'Step' 

Set the step’s prompt text directly. 

step **= **Step\("greeting"\)

step.set\_text\("Welcome the caller and ask how you can help."\) **10.26.3.3**

**add\_section**

**def **add\_section\(self, title: str, body: str\) **-> **'Step' 

Add a POM section to the step. 

step **= **Step\("collect\_info"\)

step.add\_section\("Task", "Collect the caller's name and phone number."\) step.add\_section\("Guidelines", "Be polite and patient."\) **10.26.3.4**

**add\_bullets**

**def **add\_bullets\(self, title: str, bullets: List\[str\]\) **-> **'Step' 

Add a section with bullet points. 

step.add\_bullets\("Requirements", \[

"Get full legal name", 

"Verify phone number", 

"Confirm email address" 

\]\)

299

10. Reference

**10.26.3.5 set\_step\_criteria**

**def **set\_step\_criteria\(self, criteria: str\) **-> **'Step' 

Define when this step is complete. 

step.set\_step\_criteria\(

"Step is complete when caller has provided their name and phone number." 

\)

**10.26.3.6 set\_functions**

**def **set\_functions\(self, functions: Union\[str, List\[str\]\]\) **-> **'Step' 

Set which functions are available in this step. 

*\#\# Disable all functions*

step.set\_functions\("none"\)

*\#\# Allow specific functions*

step.set\_functions\(\["lookup\_account", "verify\_identity"\]\) **10.26.3.7 set\_valid\_steps**

**def **set\_valid\_steps\(self, steps: List\[str\]\) **-> **'Step' 

Set which steps can be navigated to. 

step.set\_valid\_steps\(\["confirmation", "error\_handling"\]\) **10.26.3.8**

**set\_valid\_contexts**

**def **set\_valid\_contexts\(self, contexts: List\[str\]\) **-> **'Step' 

Set which contexts can be navigated to. 

step.set\_valid\_contexts\(\["support", "billing"\]\) **10.26.4**

**Step Context Switch Methods**

**10.26.4.1**

**set\_reset\_system\_prompt**

**def **set\_reset\_system\_prompt\(self, system\_prompt: str\) **-> **'Step' 

Set system prompt for context switching. 

**10.26.4.2**

**set\_reset\_user\_prompt**

**def **set\_reset\_user\_prompt\(self, user\_prompt: str\) **-> **'Step' 

Set user prompt for context switching. 

300

10. Reference

**10.26.4.3 set\_reset\_consolidate**

**def **set\_reset\_consolidate\(self, consolidate: bool\) **-> **'Step' 

Set whether to consolidate conversation on context switch. 

**10.26.4.4 set\_reset\_full\_reset**

**def **set\_reset\_full\_reset\(self, full\_reset: bool\) **-> **'Step' 

Set whether to do full reset on context switch. 

**10.26.5**

**ContextBuilder Class**

**10.26.5.1 Constructor**

ContextBuilder\(\)

Create a new context builder. 

**10.26.5.2 add\_context**

**def **add\_context\(

self, 

name: str, 

*\# Context name*

steps: List\[Step\]

*\# List of steps*

\) **-> **'ContextBuilder' 

Add a context with its steps. 

builder **= **ContextBuilder\(\)

builder.add\_context\("main", \[

Step\("greeting"\).set\_text\("Greet the caller"\), Step\("collect"\).set\_text\("Collect information"\), Step\("confirm"\).set\_text\("Confirm details"\)

\]\)

**10.26.5.3**

**set\_default\_context**

**def **set\_default\_context\(self, name: str\) **-> **'ContextBuilder' 

Set the default starting context. 

builder.set\_default\_context\("main"\)

**10.26.5.4**

**build**

**def **build\(self\) **-> **Dict\[str, Any\]

Build the contexts structure for SWML. 

301

10. Reference

**10.26.6 Using with AgentBase**

from signalwire\_agents import AgentBase

from signalwire\_agents.core.contexts import ContextBuilder, Step

agent **= **AgentBase\(name**=**"workflow-agent"\)

*\#\# Create context builder*

builder **= **ContextBuilder\(\)

*\#\# Define steps for main context*

greeting **= **\(

Step\("greeting"\)

.set\_text\("Welcome the caller and ask how you can help today."\)

.set\_functions\("none"\)

.set\_valid\_steps\(\["collect\_info"\]\)

\)

collect **= **\(

Step\("collect\_info"\)

.add\_section\("Task", "Collect the caller's information."\)

.add\_bullets\("Required Information", \[

"Full name", 

"Account number", 

"Reason for calling" 

\]\)

.set\_step\_criteria\("Complete when all information is collected."\)

.set\_functions\(\["lookup\_account"\]\)

.set\_valid\_steps\(\["process", "error"\]\)

\)

process **= **\(

Step\("process"\)

.set\_text\("Process the caller's request based on collected information."\)

.set\_valid\_steps\(\["farewell"\]\)

\)

farewell **= **\(

Step\("farewell"\)

.set\_text\("Thank the caller and end the conversation."\)

.set\_functions\("none"\)

\)

*\#\# Add context*

builder.add\_context\("main", \[greeting, collect, process, farewell\]\) builder.set\_default\_context\("main"\)

*\#\# Apply to agent*

agent.set\_contexts\(builder\)

**10.26.7**

**Multiple Contexts Example**

builder **= **ContextBuilder\(\)

*\#\# Main menu context*

main\_steps **= **\[

Step\("menu"\)

.set\_text\("Present options: sales, support, or billing."\)

.set\_valid\_contexts\(\["sales", "support", "billing"\]\)

\]

builder.add\_context\("main", main\_steps\)

*\#\# Sales context*

sales\_steps **= **\[

Step\("qualify"\)

.set\_text\("Understand what product the caller is interested in."\)

.set\_functions\(\["check\_inventory", "get\_pricing"\]\)

.set\_valid\_steps\(\["quote"\]\), 

302

10. Reference

Step\("quote"\)

.set\_text\("Provide pricing and availability."\)

.set\_valid\_steps\(\["close"\]\), 

Step\("close"\)

.set\_text\("Close the sale or schedule follow-up."\)

.set\_valid\_contexts\(\["main"\]\)

\]

builder.add\_context\("sales", sales\_steps\)

*\#\# Support context*

support\_steps **= **\[

Step\("diagnose"\)

.set\_text\("Understand the customer's issue."\)

.set\_functions\(\["lookup\_account", "check\_status"\]\)

.set\_valid\_steps\(\["resolve"\]\), 

Step\("resolve"\)

.set\_text\("Resolve the issue or escalate."\)

.set\_functions\(\["create\_ticket", "transfer\_call"\]\)

.set\_valid\_contexts\(\["main"\]\)

\]

builder.add\_context\("support", support\_steps\)

builder.set\_default\_context\("main"\)

**10.26.8**

**Step Flow Diagram**

┌─────────────────────────────────────────────────────────────────────────────┐

│

Step Navigation

│

├─────────────────────────────────────────────────────────────────────────────┤

│

│

│

Context: main

│

│

│

│

┌──────────┐

┌──────────┐

┌──────────┐

┌──────────┐

│

│

│ greeting │ → │ collect

│ → │ process

│ → │ farewell │

│

│

└──────────┘

└──────────┘

└──────────┘

└──────────┘

│

│

│

│

│

▼

│

│

┌──────────┐

│

│

│

error

│

│

│

└──────────┘

│

│

│

│

Navigation:

│

│

• set\_valid\_steps: Control which steps can be reached

│

│

• set\_valid\_contexts: Control which contexts can be reached

│

│

• AI uses swml\_change\_step\(\) or swml\_change\_context\(\) to navigate

│

│

│

└─────────────────────────────────────────────────────────────────────────────┘

**10.26.9**

**Generated SWML Structure**

The contexts system generates SWML with this structure:

**\{**

"version" **: **"1.0.0" **, **

"sections" **: \{**

"main" **: **\[**\{**

"ai" **: \{**

"contexts" **: \{**

"default" **: **"main" **, **

"main" **: \{**

"steps" **: **\[

**\{**

303

10. Reference

"name" **: **"greeting" **, **

"text" **: **"Welcome the caller..." **, **

"functions" **: **"none" **, **

"valid\_steps" **: **\["collect\_info"\]

**\}**, 

**\{**

"name" **: **"collect\_info" **, **

"text" **: **"\#\# Task\\nCollect information..." **, **

"step\_criteria" **: **"Complete when..." **, **

"functions" **: **\["lookup\_account"\]**, **

"valid\_steps" **: **\["process", "error"\]

**\}**

\]

**\}**

**\}**

**\}**

**\}**\]

**\}**

**\}**

304

10. Reference

**10.27**

**swaig-test CLI**

**Summary**: Command-line tool for testing agents and SWAIG functions locally without deploying to production. 

**10.27.1 Overview**

The swaig-test tool loads agent files and allows you to:

• Generate and inspect SWML output

• Test SWAIG functions with arguments

• Simulate serverless environments \(Lambda, CGI, Cloud Functions, Azure\)

• Debug agent configuration and dynamic behavior

• Test DataMap functions with live webhook calls

• Execute functions with mock call data

**10.27.2**

**Command Syntax**

swaig-test **< **agent\_path**> ** *\[* options *\]*

**10.27.3**

**Quick Reference**

**Command**

**Purpose**

swaig-test agent.py

List available tools

swaig-test agent.py --dump-swml

Generate SWML document

swaig-test agent.py --list-tools

List all SWAIG functions

swaig-test agent.py --list-agents

List agents in multi-agent file

swaig-test agent.py --exec fn --arg val

Execute a function

swaig-test agent.py --help-examples

Show comprehensive examples

swaig-test agent.py --help-platforms

Show serverless platform options

**10.27.4**

**Basic Usage**

*\#\# Generate SWML document \(pretty printed\)*

swaig-test agent.py --dump-swml

*\#\# Generate raw JSON for piping to jq*

swaig-test agent.py --dump-swml --raw **| **jq '.' 

*\#\# List all SWAIG functions*

swaig-test agent.py --list-tools

*\#\# Execute a function with CLI-style arguments*

swaig-test agent.py --exec search --query "AI agents" --limit 5

*\#\# Execute with verbose output*

swaig-test agent.py --verbose --exec search --query "test" 

305

10. Reference

**10.27.5 Actions**

Choose one action per command:

**Action**

**Description**

--list-agents

List all agents in the file

--list-tools

List all SWAIG functions in the agent

--dump-swml

Generate and output SWML document

--exec FUNCTION

Execute a function with CLI arguments

\(default\)

If no action specified, defaults to --list-tools

**10.27.6**

**Common Options**

**Option**

**Description**

-v, --verbose

Enable verbose output with debug information

--raw

Output raw JSON only \(for piping to jq\)

--agent-class NAME

Specify agent class for multi-agent files

--route PATH

Specify agent by route \(e.g., /healthcare\)

**10.27.7**

**SWML Generation**

**10.27.7.1**

**Basic Generation**

*\#\# Pretty-printed SWML*

swaig-test agent.py --dump-swml

*\#\# Raw JSON for processing*

swaig-test agent.py --dump-swml --raw

*\#\# Pretty-print with jq*

swaig-test agent.py --dump-swml --raw **| **jq '.' 

**10.27.7.2**

**Extract Specific Fields**

*\#\# Extract SWAIG functions*

swaig-test agent.py --dump-swml --raw **| **jq '.sections.main\[1\].ai.SWAIG.functions' 

*\#\# Extract prompt*

swaig-test agent.py --dump-swml --raw **| **jq '.sections.main\[1\].ai.prompt' 

*\#\# Extract languages*

swaig-test agent.py --dump-swml --raw **| **jq '.sections.main\[1\].ai.languages' 

**10.27.7.3**

**Generate with Fake Call Data**

*\#\# With comprehensive fake call data \(call\_id, from, to, etc.\)* swaig-test agent.py --dump-swml --fake-full-data

*\#\# Customize call configuration*

swaig-test agent.py --dump-swml --call-type sip --from-number \+15551234567

306

10. Reference

**10.27.8 SWML Generation Options**

**Option**

**Default**

**Description**

--call-type

webrtc

Call type: sip or webrtc

--call-direction

inbound

Call direction: inbound or

outbound

--call-state

created

Call state value

--from-number

\(none\)

Override from/caller

number

--to-extension

\(none\)

Override to/extension

number

--fake-full-data

false

Use comprehensive fake

post\_data

**10.27.9**

**Function Execution**

**10.27.9.1 CLI-Style Arguments \(Recommended\)**

*\#\# Simple function call*

swaig-test agent.py --exec search --query "AI agents" 

*\#\# Multiple arguments*

swaig-test agent.py --exec book\_reservation \\

--name "John Doe" \\

--date "2025-01-20" \\

--party\_size 4

*\#\# With verbose output*

swaig-test agent.py --verbose --exec search --query "test" 

**10.27.9.2**

**Type Conversion**

Arguments are automatically converted:

**Type**

**Example**

**Notes**

String

--name "John Doe" 

Quoted or unquoted

Integer

--count 5

Numeric values

Float

--threshold 0.75

Decimal values

Boolean

--active true

true/false

**10.27.9.3**

**Legacy JSON Syntax**

Still supported for backwards compatibility:

swaig-test agent.py search '\{"query": "AI agents", "limit": 5\}' 

**10.27.10**

**Function Execution Options**

**Option**

**Description**

--minimal

Use minimal post\_data \(function args only\)

--fake-full-data

Use comprehensive fake call data

--custom-data

JSON string with custom post\_data overrides

307

10. Reference

**10.27.11**

**Multi-Agent Files**

When a file contains multiple agent classes:

*\#\# List all agents in file*

swaig-test multi\_agent.py --list-agents

*\#\# Use specific agent by class name*

swaig-test multi\_agent.py --agent-class SalesAgent --list-tools

swaig-test multi\_agent.py --agent-class SalesAgent --dump-swml

*\#\# Use specific agent by route*

swaig-test multi\_agent.py --route /sales --list-tools

swaig-test multi\_agent.py --route /support --exec create\_ticket --issue "Login problem" 

**10.27.12**

**Dynamic Agent Testing**

Test agents that configure themselves based on request data:

*\#\# Test with query parameters*

swaig-test dynamic\_agent.py --dump-swml --query-params '\{"tier":"premium"\}' 

*\#\# Test with custom headers*

swaig-test dynamic\_agent.py --dump-swml --header "Authorization=Bearer token123" 

swaig-test dynamic\_agent.py --dump-swml --header "X-Customer-ID=12345" 

*\#\# Test with custom request body*

swaig-test dynamic\_agent.py --dump-swml --method POST --body '\{"custom":"data"\}' 

*\#\# Test with user variables*

swaig-test dynamic\_agent.py --dump-swml --user-vars '\{"preferences":\{"language":"es"\}\}' 

*\#\# Combined dynamic configuration*

swaig-test dynamic\_agent.py --dump-swml \\

--query-params '\{"tier":"premium","region":"eu"\}' \\

--header "X-Customer-ID=12345" \\

--user-vars '\{"preferences":\{"language":"es"\}\}' 

**10.27.13**

**Data Customization Options**

**Option**

**Description**

--user-vars

JSON string for userVariables

--query-params

JSON string for query parameters

--header

Add HTTP header \(KEY=VALUE format\)

--override

Override specific value \(path.to.key=value\)

--override-json

Override with JSON value \(path.to.key=‘\{“nested”:true\}’\)

**10.27.14**

**Advanced Data Overrides**

*\#\# Override specific values*

swaig-test agent.py --dump-swml \\

--override call.state=answered \\

--override call.timeout=60

*\#\# Override with JSON values*

swaig-test agent.py --dump-swml \\

--override-json vars.custom='\{"key":"value","nested":\{"data":true\}\}' 

*\#\# Combine multiple override types*

swaig-test agent.py --dump-swml \\

--call-type sip \\

308

10. Reference

--user-vars '\{"vip":"true"\}' \\

--header "X-Source=test" \\

--override call.project\_id=my-project \\

--verbose

**10.27.15**

**Serverless Simulation**

Test agents in simulated serverless environments:

**Platform**

**Value**

**Description**

AWS Lambda

lambda

Simulates Lambda

environment

CGI

cgi

Simulates CGI deployment

Cloud Functions

cloud\_function

Simulates Google Cloud

Functions

Azure Functions

azure\_function

Simulates Azure Functions

**10.27.15.1 AWS Lambda Simulation**

*\#\# Basic Lambda simulation*

swaig-test agent.py --simulate-serverless lambda --dump-swml

*\#\# With custom Lambda configuration*

swaig-test agent.py --simulate-serverless lambda \\

--aws-function-name prod-agent \\

--aws-region us-west-2 \\

--dump-swml

*\#\# With Lambda function URL*

swaig-test agent.py --simulate-serverless lambda \\

--aws-function-name my-agent \\

--aws-function-url https://xxx.lambda-url.us-west-2.on.aws \\

--dump-swml

*\#\# With API Gateway*

swaig-test agent.py --simulate-serverless lambda \\

--aws-api-gateway-id abc123 \\

--aws-stage prod \\

--dump-swml

**10.27.15.2 AWS Lambda Options**

**Option**

**Description**

--aws-function-name

Lambda function name

--aws-function-url

Lambda function URL

--aws-region

AWS region

--aws-api-gateway-id

API Gateway ID for API Gateway URLs

--aws-stage

API Gateway stage \(default: prod\)

309

10. Reference

**10.27.15.3 CGI Simulation**

*\#\# Basic CGI \(host required\)*

swaig-test agent.py --simulate-serverless cgi \\

--cgi-host example.com \\

--dump-swml

*\#\# CGI with HTTPS*

swaig-test agent.py --simulate-serverless cgi \\

--cgi-host example.com \\

--cgi-https \\

--dump-swml

*\#\# CGI with custom script path*

swaig-test agent.py --simulate-serverless cgi \\

--cgi-host example.com \\

--cgi-script-name /cgi-bin/agent.py \\

--cgi-path-info /custom/path \\

--dump-swml

**10.27.15.4 CGI Options**

**Option**

**Description**

--cgi-host

CGI server hostname \(REQUIRED for CGI simulation\)

--cgi-script-name

CGI script name/path

--cgi-https

Use HTTPS for CGI URLs

--cgi-path-info

CGI PATH\_INFO value

**10.27.15.5 Google Cloud Functions Simulation**

*\#\# Basic Cloud Functions*

swaig-test agent.py --simulate-serverless cloud\_function --dump-swml

*\#\# With project configuration*

swaig-test agent.py --simulate-serverless cloud\_function \\

--gcp-project my-project \\

--gcp-region us-central1 \\

--dump-swml

*\#\# With custom function URL*

swaig-test agent.py --simulate-serverless cloud\_function \\

--gcp-function-url https://us-central1-myproject.cloudfunctions.net/agent \\

--dump-swml

**10.27.15.6 GCP Options**

**Option**

**Description**

--gcp-project

Google Cloud project ID

--gcp-function-url

Google Cloud Function URL

--gcp-region

Google Cloud region

--gcp-service

Google Cloud service name

310

10. Reference

**10.27.15.7 Azure Functions Simulation**

*\#\# Basic Azure Functions*

swaig-test agent.py --simulate-serverless azure\_function --dump-swml

*\#\# With environment*

swaig-test agent.py --simulate-serverless azure\_function \\

--azure-env production \\

--dump-swml

*\#\# With custom function URL*

swaig-test agent.py --simulate-serverless azure\_function \\

--azure-function-url https://myapp.azurewebsites.net/api/agent \\

--dump-swml

**10.27.15.8 Azure Options**

**Option**

**Description**

--azure-env

Azure Functions environment

--azure-function-url

Azure Function URL

**10.27.16**

**Environment Variables**

Set environment variables for testing:

*\#\# Set individual variables*

swaig-test agent.py --simulate-serverless lambda \\

--env API\_KEY=secret123 \\

--env DEBUG=1 \\

--exec my\_function

*\#\# Load from environment file*

swaig-test agent.py --simulate-serverless lambda \\

--env-file production.env \\

--dump-swml

*\#\# Combine both*

swaig-test agent.py --simulate-serverless lambda \\

--env-file .env \\

--env API\_KEY=override\_key \\

--dump-swml

**10.27.17**

**DataMap Function Testing**

DataMap functions execute their configured webhooks:

*\#\# Test DataMap function \(makes actual HTTP requests\)*

swaig-test agent.py --exec get\_weather --city "New York" 

*\#\# With verbose output to see webhook details*

swaig-test agent.py --verbose --exec get\_weather --city "New York" 

**10.27.18**

**Cross-Platform Testing**

Compare agent behavior across serverless platforms:

*\#\# Test across all platforms*

**for **platform **in **lambda cgi cloud\_function azure\_function**; do** echo "Testing $platform..." 

**if **\[ "$platform" = "cgi" \]**; then**

swaig-test agent.py --simulate-serverless $platform \\

311

10. Reference

--cgi-host example.com --exec my\_function --param value

**else**

swaig-test agent.py --simulate-serverless $platform \\

--exec my\_function --param value

**fi**

**done**

*\#\# Compare webhook URLs across platforms*

swaig-test agent.py --simulate-serverless lambda --dump-swml --raw **| **\\ jq '.sections.main\[1\].ai.SWAIG.functions\[\].web\_hook\_url' 

swaig-test agent.py --simulate-serverless cgi --cgi-host example.com \\

--dump-swml --raw **| **jq '.sections.main\[1\].ai.SWAIG.functions\[\].web\_hook\_url' 

**10.27.19**

**Output Options**

**Option**

**Description**

--raw

Machine-readable JSON output \(suppresses logs\)

--verbose

Include debug information and detailed output

**10.27.20**

**Extended Help**

*\#\# Show platform-specific serverless options*

swaig-test agent.py --help-platforms

*\#\# Show comprehensive usage examples*

swaig-test agent.py --help-examples

**10.27.21**

**Complete Workflow Examples**

**10.27.21.1 Development Workflow**

*\#\# 1. Inspect generated SWML*

swaig-test agent.py --dump-swml --raw **| **jq '.' 

*\#\# 2. List available functions*

swaig-test agent.py --list-tools

*\#\# 3. Test a specific function*

swaig-test agent.py --exec search --query "test" --verbose

*\#\# 4. Test with fake call data*

swaig-test agent.py --exec book\_appointment \\

--name "John" --date "2025-01-20" \\

--fake-full-data --verbose

**10.27.21.2 Serverless Deployment Testing**

*\#\# Test Lambda configuration*

swaig-test agent.py --simulate-serverless lambda \\

--aws-function-name my-agent \\

--aws-region us-east-1 \\

--dump-swml --raw **> **swml.json

*\#\# Verify webhook URLs are correct*

**cat **swml.json **| **jq '.sections.main\[1\].ai.SWAIG.functions\[\].web\_hook\_url' 

*\#\# Test function execution in Lambda environment*

swaig-test agent.py --simulate-serverless lambda \\

--aws-function-name my-agent \\

--exec process\_order --order\_id "12345" --verbose

312

10. Reference

**10.27.21.3 Multi-Agent Testing**

*\#\# Discover agents*

swaig-test multi\_agent.py --list-agents

*\#\# Test each agent*

swaig-test multi\_agent.py --agent-class RouterAgent --dump-swml

swaig-test multi\_agent.py --agent-class SalesAgent --list-tools

swaig-test multi\_agent.py --agent-class SupportAgent \\

--exec create\_ticket --issue "Cannot login" 

**10.27.22**

**Exit Codes**

**Code**

**Meaning**

0

Success

1

General error \(file not found, invalid args, execution error\)

**10.27.23**

**Troubleshooting**

**Issue**

**Solution**

Agent file not found

Check path is correct

Multiple agents found

Use --agent-class or --route to specify

Function not found

Use --list-tools to see available functions

CGI host required

Add --cgi-host for CGI simulation

Invalid JSON

Check --query-params and --body syntax

Import errors

Ensure all dependencies are installed

313

10. Reference

**10.28**

**sw-search CLI**

**Summary**: Command-line tool for building, searching, and managing vector search indexes for AI agent knowledge bases. 

**10.28.1 Overview**

The sw-search tool builds vector search indexes from documents for use with the native\_vector\_search skill. 

**Capabilities:**

• Build indexes from documents \(MD, TXT, PDF, DOCX, RST, PY\)

• Multiple chunking strategies for different content types

• SQLite and PostgreSQL/pgvector storage backends

• Interactive search shell for index exploration

• Export chunks to JSON for review or external processing

• Migrate indexes between backends

• Search via remote API endpoints

**10.28.2**

**Architecture**

┌─────────────────┐

┌──────────────────┐

┌─────────────────┐

│

Documents

│───▶│

Index Builder

│───▶│

.swsearch DB

│

│ \(MD, PDF, etc.\) │

│

│

│

│

└─────────────────┘

└──────────────────┘

└─────────────────┘

│

▼

┌─────────────────┐

┌──────────────────┐

┌─────────────────┐

│

Agent

│───▶│

Search Skill

│───▶│

Search Engine

│

│

│

│

│

│

│

└─────────────────┘

└──────────────────┘

└─────────────────┘

The system provides:

• **Offline Search**: No external API calls or internet required

• **Hybrid Search**: Combines vector similarity and keyword search

• **Smart Chunking**: Intelligent document segmentation with context preservation

• **Advanced Query Processing**: NLP-enhanced query understanding

• **Flexible Deployment**: Local embedded mode or remote server mode

• **SQLite Storage**: Portable .swsearch index files

**10.28.3**

**Command Modes**

sw-search operates in five modes:

**Mode**

**Syntax**

**Purpose**

build

sw-search ./docs

Build search index

search

sw-search search FILE QUERY

Search existing index

validate

sw-search validate FILE

Validate index integrity

migrate

sw-search migrate FILE

Migrate between backends

remote

sw-search remote URL QUERY

Search via remote API

314

10. Reference

**10.28.4 Quick Start**

*\#\# Build index from documentation*

sw-search ./docs --output knowledge.swsearch

*\#\# Search the index*

sw-search search knowledge.swsearch "how to create an agent" 

*\#\# Interactive search shell*

sw-search search knowledge.swsearch --shell

*\#\# Validate index*

sw-search validate knowledge.swsearch

**10.28.5**

**Building Indexes**

**10.28.5.1 Index Structure**

Each .swsearch file is a SQLite database containing:

• **Document chunks **with embeddings and metadata

• **Full-text search index **\(SQLite FTS5\) for keyword search

• **Configuration **and model information

• **Synonym cache **for query expansion

This portable format allows you to build indexes once and distribute them with your agents. 

**10.28.5.2**

**Basic Usage**

*\#\# Build from single directory*

sw-search ./docs

*\#\# Build from multiple directories*

sw-search ./docs ./examples --file-types md,txt,py

*\#\# Build from individual files*

sw-search README.md ./docs/guide.md ./src/main.py

*\#\# Mixed sources \(directories and files\)*

sw-search ./docs README.md ./examples specific\_file.txt

*\#\# Specify output file*

sw-search ./docs --output ./knowledge.swsearch

**10.28.5.3**

**Build Options**

**Option**

**Default**

**Description**

--output FILE

sources.swsearch

Output file or collection

--output-dir DIR

\(none\)

Output directory

--output-format

index

Output: index or json

--backend

sqlite

Storage: sqlite or pgvector

--file-types

md,txt,rst

Comma-separated

extensions

--exclude

\(none\)

Glob patterns to exclude

--languages

en

Language codes

--tags

\(none\)

Tags for all chunks

--validate

false

Validate after building

--verbose

false

Detailed output

315

10. Reference

**10.28.6 Chunking Strategies**

Choose the right strategy for your content:

**Strategy**

**Best For**

**Key Options**

sentence

General prose, articles

--max-sentences-per-chunk

sliding

Code, technical documentation

--chunk-size, --overlap-s

ize

paragraph

Structured documents

\(none\)

page

PDFs with distinct pages

\(none\)

semantic

Coherent topic grouping

--semantic-threshold

topic

Long documents by subject

--topic-threshold

qa

Question-answering apps

\(none\)

markdown

Documentation with code blocks

\(preserves structure\)

json

Pre-chunked content

\(none\)

**10.28.6.1 Sentence Chunking \(Default\)**

Groups sentences together:

*\#\# Default: 5 sentences per chunk*

sw-search ./docs --chunking-strategy sentence

*\#\# Custom sentence count*

sw-search ./docs \\

--chunking-strategy sentence \\

--max-sentences-per-chunk 10

*\#\# Split on multiple newlines*

sw-search ./docs \\

--chunking-strategy sentence \\

--max-sentences-per-chunk 8 \\

--split-newlines 2

**10.28.6.2**

**Sliding Window Chunking**

Fixed-size chunks with overlap:

sw-search ./docs \\

--chunking-strategy sliding \\

--chunk-size 100 \\

--overlap-size 20

**10.28.6.3**

**Paragraph Chunking**

Splits on double newlines:

sw-search ./docs \\

--chunking-strategy paragraph \\

--file-types md,txt,rst

316

10. Reference

**10.28.6.4 Page Chunking**

Best for PDFs:

sw-search ./docs \\

--chunking-strategy page \\

--file-types pdf

**10.28.6.5 Semantic Chunking**

Groups semantically similar sentences:

sw-search ./docs \\

--chunking-strategy semantic \\

--semantic-threshold 0.6

**10.28.6.6 Topic Chunking**

Detects topic changes:

sw-search ./docs \\

--chunking-strategy topic \\

--topic-threshold 0.2

**10.28.6.7**

**QA Chunking**

Optimized for question-answering:

sw-search ./docs --chunking-strategy qa

**10.28.6.8**

**Markdown Chunking**

The markdown strategy is specifically designed for documentation that contains code examples. It understands markdown structure and adds rich metadata for better search results. 

sw-search ./docs \\

--chunking-strategy markdown \\

--file-types md

**Features:**

• **Header-based chunking**: Splits at markdown headers \(h1, h2, h3…\) for natural boundaries

• **Code block detection**: Identifies fenced code blocks and extracts language \(python,bash, etc.\)

• **Smart tagging**: Adds "code" tags to chunks with code, plus language-specific tags

• **Section hierarchy**: Preserves full path \(e.g., “API Reference > AgentBase > Methods”\)

• **Code protection**: Never splits inside code blocks

• **Metadata enrichment**: Header levels stored as searchable metadata **Example Metadata:**

**\{**

"chunk\_type" **: **"markdown" **, **

"h1" **: **"API Reference" **, **

"h2" **: **"AgentBase" **, **

"h3" **: **"add\_skill Method" **, **

"has\_code" **: true, **

"code\_languages" **: **\["python", "bash"\]**, **

"tags" **: **\["code", "code:python", "code:bash", "depth:3"\]

**\}**

**Search Benefits:**

317

10. Reference

When users search for “example code Python”: - Chunks with code blocks get automatic 20% boost - Python-specific code gets language match bonus - Vector similarity provides primary semantic ranking - Metadata tags provide confirmation signals - Results blend semantic \+ structural relevance **Best Used With:**

• API documentation with code examples

• Tutorial content with inline code

• Technical guides with multiple languages

• README files with usage examples

**Usage with pgvector:**

sw-search ./docs \\

--backend pgvector \\

--connection-string "postgresql://user:pass@localhost:5432/db" \\

--output docs\_collection \\

--chunking-strategy markdown

**10.28.6.9 JSON Chunking**

The json strategy allows you to provide pre-chunked content in a structured format. This is useful when you need custom control over how documents are split and indexed. 

**Expected JSON Format:**

**\{**

"chunks" **: **\[

**\{**

"chunk\_id" **: **"unique\_id" **, **

"type" **: **"content" **, **

"content" **: **"The actual text content" **, **

"metadata" **: \{**

"section" **: **"Introduction" **, **

"url" **: **"https://example.com/docs/intro" **, **

"custom\_field" **: **"any\_value" 

**\}, **

"tags" **: **\["intro", "getting-started"\]

**\}**

\]

**\}**

**Usage:**

*\#\# First preprocess your documents into JSON chunks*

python your\_preprocessor.py input.txt -o chunks.json

*\#\# Then build the index using JSON strategy*

sw-search chunks.json --chunking-strategy json --file-types json

**Best Used For:**

• API documentation with complex structure

• Documents that need custom parsing logic

• Preserving specific metadata relationships

• Integration with external preprocessing tools

318

10. Reference

**10.28.7 Model Selection**

Choose embedding model based on speed vs quality:

**Alias**

**Model**

**Dims**

**Speed**

**Quality**

mini

all-MiniLM-L6-v2

384

~5x

Good

base

all-mpnet-base-v2

768

1x

High

large

all-mpnet-base-v2

768

1x

Highest

*\#\# Fast model \(default, recommended for most cases\)*

sw-search ./docs --model mini

*\#\# Balanced model*

sw-search ./docs --model base

*\#\# Best quality*

sw-search ./docs --model large

*\#\# Full model name*

sw-search ./docs --model sentence-transformers/all-mpnet-base-v2

**10.28.8**

**File Filtering**

*\#\# Specific file types*

sw-search ./docs --file-types md,txt,rst,py

*\#\# Exclude patterns*

sw-search ./docs --exclude "\*\*/test/\*\*,\*\*/\_\_pycache\_\_/\*\*,\*\*/.git/\*\*" 

*\#\# Language filtering*

sw-search ./docs --languages en,es,fr

**10.28.9**

**Tags and Metadata**

Add tags during build for filtered searching:

*\#\# Add tags to all chunks*

sw-search ./docs --tags documentation,api,v2

*\#\# Filter by tags when searching*

sw-search search index.swsearch "query" --tags documentation **10.28.10**

**Searching Indexes**

**10.28.10.1 Basic Search**

*\#\# Search with query*

sw-search search knowledge.swsearch "how to create an agent" 

*\#\# Limit results*

sw-search search knowledge.swsearch "API reference" --count 3

*\#\# Verbose output with scores*

sw-search search knowledge.swsearch "configuration" --verbose 319

10. Reference

**10.28.10.2 Search Options**

**Option**

**Default**

**Description**

--count

5

Number of results

--distance-threshold

0.0

Minimum similarity score

--tags

\(none\)

Filter by tags

--query-nlp-backend

nltk

NLP backend: nltk or spacy

--keyword-weight

\(auto\)

Manual keyword weight

\(0.0-1.0\)

--model

\(index\)

Override embedding model

--json

false

Output as JSON

--no-content

false

Hide content, show

metadata only

--verbose

false

Detailed output

**10.28.10.3 Output Formats**

*\#\# Human-readable \(default\)*

sw-search search knowledge.swsearch "query" 

*\#\# JSON output*

sw-search search knowledge.swsearch "query" --json

*\#\# Metadata only*

sw-search search knowledge.swsearch "query" --no-content

*\#\# Full verbose output*

sw-search search knowledge.swsearch "query" --verbose

**10.28.10.4 Filter by Tags**

*\#\# Single tag*

sw-search search knowledge.swsearch "functions" --tags documentation

*\#\# Multiple tags*

sw-search search knowledge.swsearch "API" --tags api,reference **10.28.11**

**Interactive Search Shell**

Load index once and search multiple times:

sw-search search knowledge.swsearch --shell

Shell commands:

**Command**

**Description**

help

Show help

exit/quit/q

Exit shell

count=N

Set result count

tags=tag1,tag2

Set tag filter

verbose

Toggle verbose output

<query> 

Search for query

Example session:

320

10. Reference

$ sw-search search knowledge.swsearch --shell

Search Shell - Index: knowledge.swsearch

Backend: sqlite

Index contains 1523 chunks from 47 files

Model: sentence-transformers/all-MiniLM-L6-v2

Type 'exit' or 'quit' to leave, 'help' for options

------------------------------------------------------------

search> how to create an agent

Found 5 result\(s\) for 'how to create an agent' \(0.034s\):

... 

search> count=3

Result count set to: 3

search> SWAIG functions

Found 3 result\(s\) for 'SWAIG functions' \(0.028s\):

... 

search> exit

Goodbye\! 

**10.28.12**

**PostgreSQL/pgvector Backend**

The search system supports multiple storage backends. Choose based on your deployment needs: **10.28.12.1 Backend Comparison**

**Feature**

**SQLite**

**pgvector**

Setup complexity

None

Requires PostgreSQL

Scalability

Limited

Excellent

Concurrent access

Poor

Excellent

Update capability

Rebuild required

Real-time

Performance \(small datasets\)

Excellent

Good

Performance \(large datasets\)

Poor

Excellent

Deployment

File copy

Database connection

Multi-agent support

Separate copies

Shared knowledge base

**SQLite Backend \(Default\): **- File-based .swsearch indexes - Portable single-file format - No external dependencies

- Best for: Single-agent deployments, development, small to medium datasets **pgvector Backend: **- Server-based PostgreSQL storage - Efficient similarity search with IVFFlat/HNSW indexes

- Multiple agents can share the same knowledge base - Real-time updates without rebuilding - Best for: Production deployments, multi-agent systems, large datasets

**10.28.12.2 Building with pgvector**

*\#\# Build to pgvector*

sw-search ./docs \\

--backend pgvector \\

--connection-string "postgresql://user:pass@localhost:5432/knowledge" \\

--output docs\_collection

*\#\# With markdown strategy*

sw-search ./docs \\

--backend pgvector \\

--connection-string "postgresql://user:pass@localhost:5432/knowledge" \\ 321

10. Reference

--output docs\_collection \\

--chunking-strategy markdown

*\#\# Overwrite existing collection*

sw-search ./docs \\

--backend pgvector \\

--connection-string "postgresql://user:pass@localhost:5432/knowledge" \\

--output docs\_collection \\

--overwrite

**10.28.12.3 Search pgvector Collection**

sw-search search docs\_collection "how to create an agent" \\

--backend pgvector \\

--connection-string "postgresql://user:pass@localhost/knowledge" 

**10.28.13**

**Migration**

Migrate indexes between backends:

*\#\# Get index information*

sw-search migrate --info ./docs.swsearch

*\#\# Migrate SQLite to pgvector*

sw-search migrate ./docs.swsearch --to-pgvector \\

--connection-string "postgresql://user:pass@localhost/db" \\

--collection-name docs\_collection

*\#\# Migrate with overwrite*

sw-search migrate ./docs.swsearch --to-pgvector \\

--connection-string "postgresql://user:pass@localhost/db" \\

--collection-name docs\_collection \\

--overwrite

**10.28.13.1 Migration Options**

**Option**

**Description**

--info

Show index information

--to-pgvector

Migrate SQLite to pgvector

--to-sqlite

Migrate pgvector to SQLite \(planned\)

--connection-string

PostgreSQL connection string

--collection-name

Target collection name

--overwrite

Overwrite existing collection

--batch-size

Chunks per batch \(default: 100\)

**10.28.14**

**Local vs Remote Modes**

The search skill supports both local and remote operation modes. 

**10.28.14.1 Local Mode \(Default\)**

Searches are performed directly in the agent process using the embedded search engine. 

**Pros: **- Faster \(no network latency\) - Works offline - Simple deployment - Lower operational complexity **Cons: **- Higher memory usage per agent - Index files must be distributed with each agent - Updates require redeploying agents

**Configuration in Agent:**

322

10. Reference

self.add\_skill\("native\_vector\_search", \{

"tool\_name": "search\_docs", 

"index\_file": "docs.swsearch", 

*\# Local file*

"nlp\_backend": "nltk" 

\}\)

**10.28.14.2 Remote Mode**

Searches are performed via HTTP API to a centralized search server. 

**Pros: **- Lower memory usage per agent - Centralized index management - Easy updates without redeploying agents

- Better scalability for multiple agents - Shared resources

**Cons: **- Network dependency - Additional infrastructure complexity - Potential latency **Configuration in Agent:**

self.add\_skill\("native\_vector\_search", \{

"tool\_name": "search\_docs", 

"remote\_url": "http://localhost:8001", 

*\# Search server*

"index\_name": "docs", 

"nlp\_backend": "nltk" 

\}\)

**10.28.14.3 Automatic Mode Detection**

The skill automatically detects which mode to use: - If remote\_url is provided → Remote mode - If index\_file is provided → Local mode - Remote mode takes priority if both are specified **10.28.14.4 Running a Remote Search Server**

1. **Start the search server:**

python examples/search\_server\_standalone.py

2. **The server provides HTTP API:**

• POST /search - Search the indexes

• GET /health - Health check and available indexes

• POST /reload\_index - Add or reload an index

3. **Test the API:**

curl -X POST "http://localhost:8001/search" \\

-H "Content-Type: application/json" \\

-d '\{"query": "how to create an agent", "index\_name": "docs", "count": 3\}' 

**10.28.15**

**Remote Search CLI**

Search via remote API endpoint from the command line:

*\#\# Basic remote search*

sw-search remote http://localhost:8001 "how to create an agent" \\

--index-name docs

*\#\# With options*

sw-search remote localhost:8001 "API reference" \\

--index-name docs \\

--count 3 \\

--verbose

*\#\# JSON output*

sw-search remote localhost:8001 "query" \\

--index-name docs \\

--json

323

10. Reference

**10.28.15.1 Remote Options**

**Option**

**Default**

**Description**

--index-name

\(required\)

Name of the index to search

--count

5

Number of results

--distance-threshold

0.0

Minimum similarity score

--tags

\(none\)

Filter by tags

--timeout

30

Request timeout in seconds

--json

false

Output as JSON

--no-content

false

Hide content

--verbose

false

Detailed output

**10.28.16**

**Validation**

Verify index integrity:

*\#\# Validate index*

sw-search validate ./docs.swsearch

*\#\# Verbose validation*

sw-search validate ./docs.swsearch --verbose

Output:

✓ Index is valid: ./docs.swsearch

Chunks: 1523

Files: 47

Configuration:

embedding\_model: sentence-transformers/all-MiniLM-L6-v2

embedding\_dimensions: 384

chunking\_strategy: markdown

created\_at: 2025-01-15T10:30:00

**10.28.17**

**JSON Export**

Export chunks for review or external processing:

*\#\# Export to single JSON file*

sw-search ./docs \\

--output-format json \\

--output all\_chunks.json

*\#\# Export to directory \(one file per source\)*

sw-search ./docs \\

--output-format json \\

--output-dir ./chunks/

*\#\# Build index from exported JSON*

sw-search ./chunks/ \\

--chunking-strategy json \\

--file-types json \\

--output final.swsearch

324

10. Reference

**10.28.18**

**NLP Backend Selection**

Choose NLP backend for processing:

**Backend**

**Speed**

**Quality**

**Install Size**

nltk

Fast

Good

Included

spacy

Slower

Better

Requires: pip install sig

nalwire-agents

\[search-nlp\]

*\#\# Index with NLTK \(default\)*

sw-search ./docs --index-nlp-backend nltk

*\#\# Index with spaCy \(better quality\)*

sw-search ./docs --index-nlp-backend spacy

*\#\# Query with NLTK*

sw-search search index.swsearch "query" --query-nlp-backend nltk

*\#\# Query with spaCy*

sw-search search index.swsearch "query" --query-nlp-backend spacy **10.28.19**

**Complete Configuration Example**

sw-search ./docs ./examples README.md \\

--output ./knowledge.swsearch \\

--chunking-strategy sentence \\

--max-sentences-per-chunk 8 \\

--file-types md,txt,rst,py \\

--exclude "\*\*/test/\*\*,\*\*/\_\_pycache\_\_/\*\*" \\

--languages en,es,fr \\

--model sentence-transformers/all-mpnet-base-v2 \\

--tags documentation,api \\

--index-nlp-backend nltk \\

--validate \\

--verbose

**10.28.20**

**Using with Skills**

After building an index, use it with the native\_vector\_search skill: from signalwire\_agents import AgentBase

agent **= **AgentBase\(name**=**"search-agent"\)

*\#\# Add search skill with built index*

agent.add\_skill\("native\_vector\_search", \{

"index\_path": "./knowledge.swsearch", 

"tool\_name": "search\_docs", 

"tool\_description": "Search the documentation" 

\}\)

325

10. Reference

**10.28.21**

**Output Formats**

**Format**

**Extension**

**Description**

swsearch

.swsearch

SQLite-based portable index

\(default\)

json

.json

JSON export of chunks

pgvector

\(database\)

PostgreSQL with pgvector

extension

**10.28.22**

**Installation Requirements**

The search system uses optional dependencies to keep the base SDK lightweight. Choose the installation option that fits your needs:

**10.28.22.1 Basic Search \(~500MB\)**

pip install "signalwire-agents\[search\]" 

**Includes: **- Core search functionality - Sentence transformers for embeddings - SQLite FTS5 for keyword search -

Basic document processing \(text, markdown\)

**10.28.22.2 Full Document Processing \(~600MB\)**

pip install "signalwire-agents\[search-full\]" 

**Adds: **- PDF processing \(PyPDF2\) - DOCX processing \(python-docx\) - HTML processing \(BeautifulSoup4\) -

Additional file format support

**10.28.22.3 Advanced NLP Features \(~700MB\)**

pip install "signalwire-agents\[search-nlp\]" 

**Adds: **- spaCy for advanced text processing - NLTK for linguistic analysis - Enhanced query preprocessing - Language detection

**Additional Setup Required:**

python -m spacy download en\_core\_web\_sm

**Performance Note: **Advanced NLP features provide significantly better query understanding, synonym expansion, and search relevance, but are 2-3x slower than basic search. Only recommended if you have sufficient CPU power and can tolerate longer response times. 

**10.28.22.4 All Search Features \(~700MB\)**

pip install "signalwire-agents\[search-all\]" 

**Includes everything above. **

**Additional Setup Required:**

python -m spacy download en\_core\_web\_sm

326

10. Reference

**10.28.22.5 Query-Only Mode \(~400MB\)**

pip install "signalwire-agents\[search-queryonly\]" 

For agents that only need to query pre-built indexes without building new ones. 

**10.28.22.6 PostgreSQL Vector Support**

pip install "signalwire-agents\[pgvector\]" 

Adds PostgreSQL with pgvector extension support for production deployments. 

**10.28.22.7 NLP Backend Selection**

You can choose which NLP backend to use for query processing:

**Backend**

**Speed**

**Quality**

**Notes**

nltk

Fast \(~50-100ms\)

Good

Default, good for most use

cases

spacy

Slower \(~150-300ms\)

Better

Better POS tagging and

entity recognition

Configure via --index-nlp-backend \(build\) or --query-nlp-backend \(search\) flags. 

**10.28.23**

**API Reference**

For programmatic access to the search system, use the Python API directly. 

**10.28.23.1 SearchEngine Class**

from signalwire\_agents.search import SearchEngine

*\#\# Load an index*

engine **= **SearchEngine\("docs.swsearch"\)

*\#\# Perform search*

results **= **engine.search\(

query\_vector**=**\[...\], 

*\# Optional: pre-computed query vector*

enhanced\_text**=**"search query", 

*\# Enhanced query text*

count**=**5, 

*\# Number of results*

similarity\_threshold**=**0.0, 

*\# Minimum similarity score*

tags**=**\["documentation"\]

*\# Filter by tags*

\)

*\#\# Get index statistics*

stats **= **engine.get\_stats\(\)

print\(f"Total chunks: **\{**stats\['total\_chunks'\]**\}**"\) print\(f"Total files: **\{**stats\['total\_files'\]**\}**"\) **10.28.23.2 IndexBuilder Class**

from signalwire\_agents.search import IndexBuilder

*\#\# Create index builder*

builder **= **IndexBuilder\(

model\_name**=**"sentence-transformers/all-mpnet-base-v2", chunk\_size**=**500, 

chunk\_overlap**=**50, 

verbose**=**True

\)

327

10. Reference

*\#\# Build index*

builder.build\_index\(

source\_dir**=**"./docs", 

output\_file**=**"docs.swsearch", 

file\_types**=**\["md", "txt"\], 

exclude\_patterns**=**\["\*\*/test/\*\*"\], 

tags**=**\["documentation"\]

\)

**10.28.24**

**Troubleshooting**

**Issue**

**Solution**

Search not available

pip install signalwire-agents\[search\]

pgvector errors

pip install signalwire-agents\[pgvector\]

PDF processing fails

pip install signalwire-agents\[search-full\]

spaCy not found

pip install signalwire-agents\[search-nlp\]

No results found

Try different chunking strategy

Poor search quality

Use --model base or larger chunks

Index too large

Use --model mini, reduce file types

Connection refused \(remote\)

Check search server is running

**10.28.25**

**Related Documentation**

• native\_vector\_search Skill - Using search indexes in agents

• Skills Overview - Adding skills to agents

• DataSphere Integration - Cloud-based search alternative

328

10. Reference

**10.29**

**Environment Variables**

**Summary**: Complete reference for all environment variables used by the SignalWire Agents SDK. 

**10.29.1 Overview**

**Category**

**Purpose**

Authentication

Basic auth credentials

SSL/TLS

HTTPS configuration

Proxy

Reverse proxy settings

Security

Host restrictions, CORS, rate limiting

Logging

Log output control

Skills

Custom skill paths

Serverless

Platform-specific settings

**10.29.2**

**Authentication Variables**

**Variable**

**Type**

**Default**

**Description**

SWML\_BASIC\_AUTH\_USER

string

Auto-generated

Username for HTTP Basic

Authentication

SWML\_BASIC\_AUTH\_PASSWORD

string

Auto-generated

Password for HTTP Basic

Authentication

**Note**: If neither variable is set, credentials are auto-generated and logged at startup. 

**10.29.3**

**SSL/TLS Variables**

**Variable**

**Type**

**Default**

**Description**

SWML\_SSL\_ENABLED

boolean

false

Enable HTTPS \(“true”, “1”, 

“yes”\)

SWML\_SSL\_CERT\_PATH

string

None

Path to SSL certificate file

\(.pem/.crt\)

SWML\_SSL\_KEY\_PATH

string

None

Path to SSL private key file

\(.key\)

SWML\_DOMAIN

string

None

Domain for SSL certs and

URL generation

SWML\_SSL\_VERIFY\_MODE

string

CERT\_REQUIRED

SSL certificate verification

mode

**10.29.4**

**Proxy Variables**

**Variable**

**Type**

**Default**

**Description**

SWML\_PROXY\_URL\_BASE

string

None

Base URL when behind

reverse proxy

SWML\_PROXY\_DEBUG

boolean

false

Enable proxy request debug

logging

**Warning**: Setting SWML\_PROXY\_URL\_BASE overrides SSL configuration and port settings. 

329

10. Reference

**10.29.5 Security Variables**

**Variable**

**Type**

**Default**

**Description**

SWML\_ALLOWED\_HOSTS

string

\*

Comma-separated allowed

hosts

SWML\_CORS\_ORIGINS

string

\*

Comma-separated allowed

CORS origins

SWML\_MAX\_REQUEST\_SIZE

integer

10485760

Maximum request size in

bytes \(10MB\)

SWML\_RATE\_LIMIT

integer

60

Rate limit in requests per

minute

SWML\_REQUEST\_TIMEOUT

integer

30

Request timeout in seconds

SWML\_USE\_HSTS

boolean

true

Enable HTTP Strict

Transport Security

SWML\_HSTS\_MAX\_AGE

integer

31536000

HSTS max-age in seconds

\(1 year\)

**10.29.6**

**Logging Variables**

**Variable**

**Type**

**Default**

**Description**

SIGNALWIRE\_LOG\_MODE

string

auto

Logging mode: “off”, 

“stderr”, “default”, “auto” 

SIGNALWIRE\_LOG\_LEVEL

string

info

Log level: “debug”, “info”, 

“warning”, “error”, 

“critical” 

**10.29.7**

**Skills Variables**

**Variable**

**Type**

**Default**

**Description**

SIGNALWIRE\_SKILL\_PATHS

string

"" 

Colon-separated paths for

custom skills

**10.29.8**

**Serverless Platform Variables**

**10.29.8.1**

**AWS Lambda**

**Variable**

**Default**

**Description**

AWS\_LAMBDA\_FUNCTION\_NAME

unknown

Function name \(used for

URL construction and

logging\)

AWS\_LAMBDA\_FUNCTION\_URL

Constructed

Function URL \(if not set, 

constructed from region and

function name\)

AWS\_REGION

us-east-1

AWS region for Lambda

execution

LAMBDA\_TASK\_ROOT

None

Lambda environment

detection variable

330

10. Reference

**10.29.8.2 Google Cloud Functions**

**Variable**

**Default**

**Description**

GOOGLE\_CLOUD\_PROJECT

None

Google Cloud Project ID

GCP\_PROJECT

None

Alternative to GOOGLE\_CLOUD

\_PROJECT

GOOGLE\_CLOUD\_REGION

us-central1

Google Cloud region

FUNCTION\_REGION

Falls back to GOOGLE\_CLOUD\_REGION

Cloud function region

FUNCTION\_TARGET

unknown

Cloud function target/entry

point name

K\_SERVICE

unknown

Knative/Cloud Run service

name

FUNCTION\_URL

None

Cloud function URL \(used

in simulation\)

**10.29.8.3 Azure Functions**

**Variable**

**Default**

**Description**

AZURE\_FUNCTIONS\_ENVIRONMENT

None

Environment detection

variable

WEBSITE\_SITE\_NAME

None

Azure App Service site

name \(used to construct

URLs\)

AZURE\_FUNCTIONS\_APP\_NAME

None

Alternative to WEBSITE\_SITE

\_NAME

AZURE\_FUNCTION\_NAME

unknown

Azure Function name

FUNCTIONS\_WORKER\_RUNTIME

None

Azure Functions worker

runtime detection

AzureWebJobsStorage

None

Azure Functions storage

connection detection

**10.29.8.4**

**CGI Mode**

**Variable**

**Default**

**Description**

GATEWAY\_INTERFACE

None

CGI environment detection

variable

HTTP\_HOST

Falls back to SERVER\_NAME

HTTP Host header value

SERVER\_NAME

localhost

Server hostname

SCRIPT\_NAME

"" 

CGI script path

PATH\_INFO

"" 

Request path info

HTTPS

None

Set to on when using

HTTPS

HTTP\_AUTHORIZATION

None

Authorization header value

REMOTE\_USER

None

Authenticated username

CONTENT\_LENGTH

None

Request content length

331

10. Reference

**10.29.9 Quick Reference**

**10.29.9.1 Commonly Configured**

**Variable**

**Use Case**

SWML\_BASIC\_AUTH\_USER / SWML\_BASIC\_AUTH

Set explicit credentials

\_PASSWORD

SWML\_PROXY\_URL\_BASE

When behind a reverse proxy

SWML\_SSL\_ENABLED / SWML\_SSL\_CERT\_PATH /

For direct HTTPS

SWML\_SSL\_KEY\_PATH

SIGNALWIRE\_LOG\_LEVEL

Adjust logging verbosity

SIGNALWIRE\_SKILL\_PATHS

Load custom skills

**10.29.9.2 Production Security**

**Variable**

**Recommendation**

SWML\_ALLOWED\_HOSTS

Restrict to your domain\(s\)

SWML\_CORS\_ORIGINS

Restrict to trusted origins

SWML\_RATE\_LIMIT

Set appropriate limit

SWML\_USE\_HSTS

Keep enabled \(default\)

**10.29.10**

**Example .env File**

*\#\# Authentication*

SWML\_BASIC\_AUTH\_USER**=**agent\_user

SWML\_BASIC\_AUTH\_PASSWORD**=**secret\_password\_123

*\#\# SSL Configuration*

SWML\_SSL\_ENABLED**=**true

SWML\_DOMAIN**=**agent.example.com

SWML\_SSL\_CERT\_PATH**=**/etc/ssl/certs/agent.crt

SWML\_SSL\_KEY\_PATH**=**/etc/ssl/private/agent.key

*\#\# Security*

SWML\_ALLOWED\_HOSTS**=**agent.example.com

SWML\_CORS\_ORIGINS**=**https://app.example.com

SWML\_RATE\_LIMIT**=**100

*\#\# Logging*

SIGNALWIRE\_LOG\_MODE**=**default

SIGNALWIRE\_LOG\_LEVEL**=**info

*\#\# Custom Skills*

SIGNALWIRE\_SKILL\_PATHS**=**/opt/custom\_skills

**10.29.11**

**Loading Environment Variables**

*\#\# Using python-dotenv*

from dotenv import load\_dotenv

load\_dotenv\(\)

from signalwire\_agents import AgentBase

agent **= **AgentBase\(name**=**"my-agent"\)

332

10. Reference

*\#\# Using shell*

source .env

python agent.py

*\#\# Using swaig-test*

swaig-test agent.py --env-file .env --dump-swml

**10.29.12**

**Environment Detection**

The SDK automatically detects the execution environment:

from signalwire\_agents.core.logging\_config import get\_execution\_mode mode **= **get\_execution\_mode\(\)

*\#\# Returns: "server", "lambda", "cgi", "google\_cloud\_function", or "azure\_function" *

333

10. Reference

**10.30**

**Config Files**

**Summary**: Reference for YAML and JSON configuration files used by the SignalWire Agents SDK. 

**10.30.1 Overview**

The SDK supports YAML and JSON configuration files for:

• Service settings \(host, port, route\)

• Security configuration \(auth, SSL\)

• Agent-specific settings

**File Discovery Order:**

1. \{agent\_name\}.yaml / \{agent\_name\}.json

2. config.yaml / config.json

3. swml.yaml / swml.json

**10.30.2**

**File Formats**

Both YAML and JSON are supported:

**YAML \(recommended\)**:

**service:**

**name: **my-agent

**host: **0.0.0.0

**port: **8080

**route: **/agent

**security:**

**basic\_auth:**

**username: **agent\_user

**password: **secret\_password

**JSON**:

**\{**

"service" **: \{**

"name" **: **"my-agent" **, **

"host" **: **"0.0.0.0" **, **

"port" **: **8080**, **

"route" **: **"/agent" 

**\}, **

"security" **: \{**

"basic\_auth" **: \{**

"username" **: **"agent\_user" **, **

"password" **: **"secret\_password" 

**\}**

**\}**

**\}**

**10.30.3**

**File Discovery**

The SDK searches for config files in this order:

1. Explicit path via config\_file parameter

2. \{agent\_name\}.yaml or \{agent\_name\}.json

3. config.yaml or config.json

4. swml.yaml or swml.json

334

10. Reference

**10.30.4 Service Section**

**service:**

*\# Agent name/identifier*

**name: **my-agent

*\# Host to bind \(default: 0.0.0.0\)*

**host: **0.0.0.0

*\# Port to bind \(default: 3000\)*

**port: **8080

*\# HTTP route path \(default: /\)*

**route: **/agent

**10.30.5**

**Security Section**

**security:**

*\# Basic authentication credentials*

**basic\_auth:**

**username: **agent\_user

**password: **secret\_password

*\# SSL/TLS configuration*

**ssl:**

**enabled: **true

**domain: **agent.example.com

**cert\_path: **/etc/ssl/certs/agent.crt

**key\_path: **/etc/ssl/private/agent.key

**10.30.6**

**Configuration Sections**

**Section**

**Purpose**

service

Server settings \(name, host, port, route\)

security

Authentication and SSL configuration

agent

Agent-specific settings

skills

Skill configurations

logging

Logging configuration

**10.30.7**

**Agent Section**

**agent:**

*\# Auto-answer incoming calls*

**auto\_answer: **true

*\# Enable call recording*

**record\_call: **false

**record\_format: **mp4

**record\_stereo: **true

*\# Token expiration \(seconds\)*

**token\_expiry\_secs: **3600

*\# Use POM for prompts*

**use\_pom: **true

335

10. Reference

**10.30.8 Skills Section**

**skills:**

*\# Simple skill activation*

**- name: **datetime

*\# Skill with configuration*

**- name: **native\_vector\_search

**params:**

**index\_path: **./knowledge.swsearch

**tool\_name: **search\_docs

*\# Multiple instances*

**- name: **web\_search

**params:**

**tool\_name: **search\_products

**api\_key: **$\{SEARCH\_API\_KEY\}

**10.30.9**

**Logging Section**

**logging:**

*\# Log level*

**level: **info

*\# Output format*

**format: **structured

*\# Disable logging*

**mode: **default

*\# or "off" *

**10.30.10**

**Environment Variable Substitution**

Config files support environment variable substitution:

**security:**

**basic\_auth:**

**username: **$\{SWML\_BASIC\_AUTH\_USER\}

**password: **$\{SWML\_BASIC\_AUTH\_PASSWORD\}

**skills:**

**- name: **weather

**params:**

**api\_key: **$\{WEATHER\_API\_KEY\}

**10.30.11**

**Complete Example**

*\#\# config.yaml*

**service:**

**name: **support-agent

**host: **0.0.0.0

**port: **8080

**route: **/support

**security:**

**basic\_auth:**

**username: **$\{AUTH\_USER:-support\_agent\}

**password: **$\{AUTH\_PASSWORD\}

**ssl:**

**enabled: **true

**domain: **support.example.com

**cert\_path: **/etc/ssl/certs/support.crt

**key\_path: **/etc/ssl/private/support.key

**agent:**

**auto\_answer: **true

336

10. Reference

**record\_call: **true

**record\_format: **mp3

**token\_expiry\_secs: **7200

**skills:**

**- name: **datetime

**- name: **native\_vector\_search

**params:**

**index\_path: **./support\_docs.swsearch

**tool\_name: **search\_support

**tool\_description: **Search support documentation

**logging:**

**level: **info

**10.30.12**

**Using Config Files**

**10.30.12.1 Explicit Path**

from signalwire\_agents import AgentBase

agent **= **AgentBase\(

name**=**"my-agent", 

config\_file**=**"/path/to/config.yaml" 

\)

**10.30.12.2 Auto-Discovery**

*\#\# Will look for my-agent.yaml, config.yaml, swml.yaml*

agent **= **AgentBase\(name**=**"my-agent"\)

**10.30.13**

**Priority Order**

Configuration values are resolved in this order \(highest priority first\): 1. Constructor parameters

2. Environment variables

3. Config file values

4. Default values

*\#\# Constructor parameter takes precedence*

agent **= **AgentBase\(

name**=**"my-agent", 

port**=**9000, 

*\# Overrides config file*

config\_file**=**"config.yaml" 

\)

**10.30.14**

**Config Validation**

The SDK validates config files on load:

• Required fields are present

• Types are correct \(port is integer, etc.\)

• File paths exist \(for SSL certificates\)

• Environment variables are defined \(if referenced\)

337

10. Reference

**10.30.15**

**Multiple Configurations**

For multi-agent deployments:

project/

agents/

sales\_agent.py

sales\_agent.yaml

support\_agent.py

support\_agent.yaml

config.yaml

\# Shared defaults

Each agent will load its own config file based on agent name. 

338

10. Reference

**10.31**

**SWML Schema**

**Summary**: Reference for SWML \(SignalWire Markup Language\) document structure and validation. 

**10.31.1 Overview**

SWML \(SignalWire Markup Language\) is a JSON format for defining call flows and AI agent behavior. 

**Key Components: **- version: Schema version \(always “1.0.0”\) - sections: Named groups of verbs - Verbs: Actions like ai, play, connect, transfer

**10.31.2**

**Basic Structure**

**\{**

"version" **: **"1.0.0" **, **

"sections" **: \{**

"main" **: **\[

**\{ **"verb\_name" **: \{ **"param" **: **"value" **\} \}**

\]

**\}**

**\}**

**10.31.3**

**Required Fields**

**Field**

**Type**

**Description**

version

string

Must be “1.0.0” 

sections

object

Contains named section

arrays

main

array

Default entry section

\(required\)

**10.31.4**

**AI Verb**

The ai verb creates an AI agent:

**\{**

"version" **: **"1.0.0" **, **

"sections" **: \{**

"main" **: **\[

**\{**

"ai" **: \{**

"prompt" **: \{**

"text" **: **"You are a helpful assistant." 

**\}, **

"post\_prompt" **: \{**

"text" **: **"Summarize the conversation." 

**\}, **

"post\_prompt\_url" **: **"https://example.com/summary" **, **

"params" **: \{**

"temperature" **: **0.7

**\}, **

"languages" **: **\[

**\{**

"name" **: **"English" **, **

"code" **: **"en-US" **, **

"voice" **: **"rime.spore" 

**\}**

\]**, **

"hints" **: **\["SignalWire", "SWAIG"\]**, **

"SWAIG" **: \{**

"functions" **: **\[\]**, **

"native\_functions" **: **\[\]**, **

339

10. Reference

"includes" **: **\[\]

**\}**

**\}**

**\}**

\]

**\}**

**\}**

**10.31.5 AI Verb Parameters**

**Parameter**

**Type**

**Description**

prompt

object

Main prompt configuration

post\_prompt

object

Summary/completion

prompt

post\_prompt\_url

string

URL for summary delivery

params

object

AI model parameters

languages

array

Supported languages and

voices

hints

array

Speech recognition hints

SWAIG

object

Function definitions

pronounce

array

Pronunciation rules

global\_data

object

Initial session data

**10.31.6**

**SWAIG Object**

**\{**

"SWAIG" **: \{**

"functions" **: **\[

**\{**

"function" **: **"search" **, **

"description" **: **"Search for information" **, **

"parameters" **: \{**

"type" **: **"object" **, **

"properties" **: \{**

"query" **: \{**

"type" **: **"string" **, **

"description" **: **"Search query" 

**\}**

**\}, **

"required" **: **\["query"\]

**\}, **

"web\_hook\_url" **: **"https://example.com/swaig" 

**\}**

\]**, **

"native\_functions" **: **\[

"check\_time" 

\]**, **

"includes" **: **\[

**\{**

"url" **: **"https://example.com/shared\_functions" **, **

"functions" **: **\["shared\_search", "shared\_lookup"\]

**\}**

\]

**\}**

**\}**

340

10. Reference

**10.31.7 Function Definition**

**Field**

**Type**

**Required**

**Description**

function

string

Yes

Function name

description

string

Yes

What the function does

parameters

object

No

JSON Schema for

parameters

web\_hook\_url

string

\*

Webhook URL \(if not

data\_map\)

data\_map

object

\*

DataMap definition

meta\_data

object

No

Custom metadata

meta\_data\_token

string

No

Token scope for metadata

fillers

array

No

Processing phrases

wait\_file

string

No

Hold audio URL

**10.31.8**

**Common Verbs**

**10.31.8.1 answer**

**\{ **"answer" **: \{\} \}**

**10.31.8.2**

**play**

**\{**

"play" **: \{**

"url" **: **"https://example.com/audio.mp3" 

**\}**

**\}**

**10.31.8.3**

**connect**

**\{**

"connect" **: \{**

"to" **: **"\+15551234567" **, **

"from" **: **"\+15559876543" 

**\}**

**\}**

**10.31.8.4**

**transfer**

**\{**

"transfer" **: \{**

"dest" **: **"https://example.com/other\_agent" 

**\}**

**\}**

**10.31.8.5**

**hangup**

**\{ **"hangup" **: \{\} \}**

341

10. Reference

**10.31.8.6 record\_call**

**\{**

"record\_call" **: \{**

"stereo" **: true, **

"format" **: **"mp3" 

**\}**

**\}**

**10.31.8.7 record**

**\{**

"record" **: \{**

"format" **: **"mp3" 

**\}**

**\}**

**10.31.9**

**Contexts Structure**

**\{**

"version" **: **"1.0.0" **, **

"sections" **: \{**

"main" **: **\[**\{**

"ai" **: \{**

"contexts" **: \{**

"default" **: **"main" **, **

"main" **: \{**

"steps" **: **\[

**\{**

"name" **: **"greeting" **, **

"text" **: **"Welcome the caller." **, **

"valid\_steps" **: **\["collect"\]

**\}**, 

**\{**

"name" **: **"collect" **, **

"text" **: **"Collect information." **, **

"functions" **: **\["lookup\_account"\]**, **

"valid\_steps" **: **\["confirm"\]

**\}**

\]

**\}**

**\}**

**\}**

**\}**\]

**\}**

**\}**

**10.31.10**

**Step Structure**

**Field**

**Type**

**Description**

name

string

Step identifier

text

string

Step prompt text

step\_criteria

string

Completion criteria

functions

string | array

“none” or list of function

names

valid\_steps

array

Allowed next steps

valid\_contexts

array

Allowed context switches

342

10. Reference

**10.31.11**

**DataMap Structure**

**\{**

"function" **: **"get\_weather" **, **

"description" **: **"Get weather information" **, **

"parameters" **: \{**

"type" **: **"object" **, **

"properties" **: \{**

"city" **: \{**

"type" **: **"string" **, **

"description" **: **"City name" 

**\}**

**\}, **

"required" **: **\["city"\]

**\}, **

"data\_map" **: \{**

"webhooks" **: **\[

**\{**

"url" **: **"https://api.weather.com/current?q=$\{enc:args.city\}" **, **

"method" **: **"GET" **, **

"output" **: \{**

"response" **: **"Weather: $\{response.condition\}" 

**\}**

**\}**

\]

**\}**

**\}**

**10.31.12**

**Prompt Object \(POM\)**

**\{**

"prompt" **: \{**

"pom" **: **\[

**\{**

"section" **: **"Role" **, **

"body" **: **"You are a helpful assistant." 

**\}**, 

**\{**

"section" **: **"Guidelines" **, **

"bullets" **: **\[

"Be concise", 

"Be helpful", 

"Be accurate" 

\]

**\}**

\]

**\}**

**\}**

**10.31.13**

**Language Configuration**

**\{**

"languages" **: **\[

**\{**

"name" **: **"English" **, **

"code" **: **"en-US" **, **

"voice" **: **"rime.spore" **, **

"speech\_fillers" **: **\["um", "uh"\]**, **

"function\_fillers" **: **\["Let me check..."\]

**\}**, 

**\{**

"name" **: **"Spanish" **, **

"code" **: **"es-ES" **, **

"voice" **: **"rime.spore" 

**\}**

343

10. Reference

\]

**\}**

**10.31.14**

**Model Parameters**

**\{**

"params" **: \{**

"temperature" **: **0.7**, **

"top\_p" **: **0.9**, **

"max\_tokens" **: **150**, **

"frequency\_penalty" **: **0.0**, **

"presence\_penalty" **: **0.0**, **

"confidence" **: **0.6**, **

"barge\_confidence" **: **0.1

**\}**

**\}**

**10.31.15**

**Schema Validation**

The SDK includes a schema.json file for validation:

from signalwire\_agents.utils.schema\_utils import SchemaUtils

schema **= **SchemaUtils\(\)

schema.validate\(swml\_document\)

**10.31.16**

**Full Example**

**\{**

"version" **: **"1.0.0" **, **

"sections" **: \{**

"main" **: **\[

**\{ **"answer" **: \{\} \}**, 

**\{**

"ai" **: \{**

"prompt" **: \{**

"pom" **: **\[

**\{**

"section" **: **"Role" **, **

"body" **: **"You are a customer service agent." 

**\}**, 

**\{**

"section" **: **"Guidelines" **, **

"bullets" **: **\[

"Be helpful and professional", 

"Verify customer identity", 

"Resolve issues efficiently" 

\]

**\}**

\]

**\}, **

"post\_prompt" **: \{**

"text" **: **"Summarize the customer interaction." 

**\}, **

"post\_prompt\_url" **: **"https://example.com/swaig/summary" **, **

"params" **: \{**

"temperature" **: **0.7

**\}, **

"languages" **: **\[

**\{**

"name" **: **"English" **, **

"code" **: **"en-US" **, **

"voice" **: **"rime.spore" 

**\}**

\]**, **

344

10. Reference

"hints" **: **\["account", "billing", "support"\]**, **

"SWAIG" **: \{**

"functions" **: **\[

**\{**

"function" **: **"lookup\_account" **, **

"description" **: **"Look up customer account" **, **

"parameters" **: \{**

"type" **: **"object" **, **

"properties" **: \{**

"account\_id" **: \{**

"type" **: **"string" **, **

"description" **: **"Account number" 

**\}**

**\}, **

"required" **: **\["account\_id"\]

**\}, **

"web\_hook\_url" **: **"https://example.com/swaig" 

**\}**

\]

**\}**

**\}**

**\}**

\]

**\}**

**\}**

345

**Chapter 11**

**Examples**

**Summary**: Practical examples organized by feature and complexity to help you build voice AI agents. 

**11.1 How to Use This Chapter**

This chapter provides examples organized two ways:

1. **By Feature **- Find examples demonstrating specific SDK features 2. **By Complexity **- Start simple and progressively add features **11.2**

**Example Categories**

**11.2.1**

**By Feature**

• Basic agent setup

• SWAIG functions

• DataMap integration

• Skills usage

• Call transfers

• Context workflows

• Multi-agent servers

**11.2.2**

**By Complexity**

• **Beginner **- Simple agents with basic prompts

• **Intermediate **- Functions, skills, and state management

• **Advanced **- Multi-context workflows, multi-agent systems

**11.3**

**Quick Start Examples**

**11.3.1**

**Minimal Agent**

from signalwire\_agents import AgentBase

agent **= **AgentBase\(name**=**"hello", route**=**"/hello"\) agent.prompt\_add\_section\("Role", "You are a friendly assistant."\) agent.add\_language\("English", "en-US", "rime.spore"\) **if **\_\_name\_\_ **== **"\_\_main\_\_":

agent.run\(\)

346

11. Examples

**11.3.2 Agent with Function**

from signalwire\_agents import AgentBase

from signalwire\_agents.core.function\_result import SwaigFunctionResult agent **= **AgentBase\(name**=**"helper", route**=**"/helper"\) agent.prompt\_add\_section\("Role", "You help users look up information."\) agent.add\_language\("English", "en-US", "rime.spore"\)

@agent.tool\(description**=**"Look up information by ID"\) **def **lookup\(id: str\) **-> **SwaigFunctionResult:

*\# Your lookup logic here*

**return **SwaigFunctionResult\(f"Found record **\{**id**\}**"\) **if **\_\_name\_\_ **== **"\_\_main\_\_":

agent.run\(\)

**11.3.3**

**Agent with Transfer**

from signalwire\_agents import AgentBase

from signalwire\_agents.core.function\_result import SwaigFunctionResult agent **= **AgentBase\(name**=**"receptionist", route**=**"/reception"\) agent.prompt\_add\_section\("Role", "You are a receptionist. Help callers reach the right department."\) agent.add\_language\("English", "en-US", "rime.spore"\)

@agent.tool\(description**=**"Transfer caller to support"\) **def **transfer\_to\_support\(\) **-> **SwaigFunctionResult: **return **\(

SwaigFunctionResult\("Transferring you to support now."\)

.connect\("\+15551234567", final**=**True\)

\)

**if **\_\_name\_\_ **== **"\_\_main\_\_":

agent.run\(\)

**11.4**

**Running Examples**

*\# Run directly*

python agent.py

*\# Test with swaig-test*

swaig-test agent.py --dump-swml

swaig-test agent.py --list-tools

swaig-test agent.py --exec lookup --id "12345" 

**11.5**

**Example Structure**

Most examples follow this pattern:

*\# 1. Imports*

from signalwire\_agents import AgentBase

from signalwire\_agents.core.function\_result import SwaigFunctionResult

*\# 2. Create Agent*

agent **= **AgentBase\(name**=**"...", route**=**"/..."\)

*\# 3. Configure*

agent.prompt\_add\_section\(...\)

agent.add\_language\(...\)

agent.add\_skill\(...\)

*\# 4. Define Functions*

347

11. Examples

@agent.tool\(...\)

**def **my\_function\(...\) **-> **SwaigFunctionResult:

... 

*\# 5. Run*

**if **\_\_name\_\_ **== **"\_\_main\_\_":

agent.run\(\)

**11.6**

**Chapter Contents**

**Section**

**Description**

By Feature

Examples organized by SDK feature

By Complexity

Examples from beginner to advanced

**11.7 Basic Agent Setup**

**11.7.1**

**Minimal Agent**

from signalwire\_agents import AgentBase

agent **= **AgentBase\(name**=**"basic", route**=**"/basic"\) agent.prompt\_add\_section\("Role", "You are a helpful assistant."\) agent.add\_language\("English", "en-US", "rime.spore"\) **if **\_\_name\_\_ **== **"\_\_main\_\_":

agent.run\(\)

**11.7.2**

**Class-Based Agent**

from signalwire\_agents import AgentBase

**class **MyAgent\(AgentBase\):

**def \_\_init\_\_**\(self\):

super\(\). **\_\_init\_\_**\(name**=**"my-agent", route**=**"/my-agent"\) self.prompt\_add\_section\("Role", "You are a customer service agent."\) self.prompt\_add\_section\("Guidelines", "Be helpful and professional."\) self.add\_language\("English", "en-US", "rime.spore"\) **if **\_\_name\_\_ **== **"\_\_main\_\_":

agent **= **MyAgent\(\)

agent.run\(\)

**11.8**

**SWAIG Functions**

**11.8.1**

**Simple Function**

from signalwire\_agents import AgentBase

from signalwire\_agents.core.function\_result import SwaigFunctionResult agent **= **AgentBase\(name**=**"functions", route**=**"/functions"\) agent.prompt\_add\_section\("Role", "You help users with account lookups."\) agent.add\_language\("English", "en-US", "rime.spore"\)

@agent.tool\(description**=**"Look up account information"\) **def **get\_account\(account\_id: str\) **-> **SwaigFunctionResult:

*\# Simulated lookup*

348

11. Examples

**return **SwaigFunctionResult\(f"Account **\{**account\_id**\}**: Active, balance $150.00"\) **if **\_\_name\_\_ **== **"\_\_main\_\_":

agent.run\(\)

**11.8.2 Function with Multiple Parameters**

from signalwire\_agents import AgentBase

from signalwire\_agents.core.function\_result import SwaigFunctionResult agent **= **AgentBase\(name**=**"booking", route**=**"/booking"\) agent.prompt\_add\_section\("Role", "You help users book appointments."\) agent.add\_language\("English", "en-US", "rime.spore"\)

@agent.tool\(description**=**"Book an appointment"\)

**def **book\_appointment\(

name: str, 

date: str, 

time: str **= **"10:00 AM", 

service: str **= **"consultation" 

\) **-> **SwaigFunctionResult:

**return **SwaigFunctionResult\(

f"Booked **\{**service**\} **for **\{**name**\} **on **\{**date**\} **at **\{**time**\}**. " 

"You will receive a confirmation." 

\)

**if **\_\_name\_\_ **== **"\_\_main\_\_":

agent.run\(\)

**11.8.3**

**Secure Function**

from signalwire\_agents import AgentBase

from signalwire\_agents.core.function\_result import SwaigFunctionResult agent **= **AgentBase\(name**=**"secure", route**=**"/secure"\) agent.prompt\_add\_section\("Role", "You handle sensitive account operations."\) agent.add\_language\("English", "en-US", "rime.spore"\)

@agent.tool\(

description**=**"Update account password", 

secure**=**True, 

fillers**=**\["Processing your request securely..."\]

\)

**def **update\_password\(

account\_id: str, 

new\_password: str

\) **-> **SwaigFunctionResult:

*\# Password update logic here*

**return **SwaigFunctionResult\("Password has been updated successfully."\) **if **\_\_name\_\_ **== **"\_\_main\_\_":

agent.run\(\)

**11.9**

**DataMap Integration**

**11.9.1**

**Weather Lookup**

from signalwire\_agents import AgentBase

from signalwire\_agents.core.data\_map import DataMap

from signalwire\_agents.core.function\_result import SwaigFunctionResult agent **= **AgentBase\(name**=**"weather", route**=**"/weather"\) agent.prompt\_add\_section\("Role", "You provide weather information."\) agent.add\_language\("English", "en-US", "rime.spore"\) 349

11. Examples

weather\_map **= **\(

DataMap\("get\_weather"\)

.purpose\("Get current weather for a city"\)

.parameter\("city", "string", "City name", required**=**True\)

.webhook\("GET", "https://api.weather.com/current?q=$\{enc:args.city\}&key=YOUR\_API\_KEY"\)

.output\(SwaigFunctionResult\(

"Current weather in $**\{args.city\}**: $**\{response.condition\}**, $**\{response.temp\} **degrees F" 

\)\)

.fallback\_output\(SwaigFunctionResult\("Weather service unavailable."\)\)

\)

agent.register\_swaig\_function\(weather\_map.to\_swaig\_function\(\)\)

**if **\_\_name\_\_ **== **"\_\_main\_\_":

agent.run\(\)

**11.9.2**

**Expression-Based Control**

from signalwire\_agents import AgentBase

from signalwire\_agents.core.data\_map import DataMap

from signalwire\_agents.core.function\_result import SwaigFunctionResult agent **= **AgentBase\(name**=**"control", route**=**"/control"\) agent.prompt\_add\_section\("Role", "You control media playback."\) agent.add\_language\("English", "en-US", "rime.spore"\) playback\_map **= **\(

DataMap\("media\_control"\)

.purpose\("Control media playback"\)

.parameter\("command", "string", "Command: play, pause, stop", required**=**True\)

.expression\("$**\{args.command\}**", r"play**|**start", SwaigFunctionResult\("Starting playback."\)

.play\_background\_file\("https://example.com/music.mp3"\)\)

.expression\("$**\{args.command\}**", r"pause**|**stop", SwaigFunctionResult\("Stopping playback."\)

.stop\_background\_file\(\)\)

\)

agent.register\_swaig\_function\(playback\_map.to\_swaig\_function\(\)\)

**if **\_\_name\_\_ **== **"\_\_main\_\_":

agent.run\(\)

**11.10**

**Call Transfers**

**11.10.1**

**Simple Transfer**

from signalwire\_agents import AgentBase

from signalwire\_agents.core.function\_result import SwaigFunctionResult agent **= **AgentBase\(name**=**"transfer", route**=**"/transfer"\) agent.prompt\_add\_section\("Role", "You route callers to the right department."\) agent.add\_language\("English", "en-US", "rime.spore"\)

@agent.tool\(description**=**"Transfer to sales department"\) **def **transfer\_sales\(\) **-> **SwaigFunctionResult:

**return **\(

SwaigFunctionResult\("Connecting you to our sales team."\)

.connect\("\+15551234567", final**=**True\)

\)

@agent.tool\(description**=**"Transfer to support department"\) **def **transfer\_support\(\) **-> **SwaigFunctionResult:

**return **\(

SwaigFunctionResult\("Transferring you to technical support."\)

.connect\("\+15559876543", final**=**True\)

350

11. Examples

\)

**if **\_\_name\_\_ **== **"\_\_main\_\_":

agent.run\(\)

**11.10.2 Temporary Transfer**

from signalwire\_agents import AgentBase

from signalwire\_agents.core.function\_result import SwaigFunctionResult agent **= **AgentBase\(name**=**"consult", route**=**"/consult"\) agent.prompt\_add\_section\("Role", "You help with consultations."\) agent.add\_language\("English", "en-US", "rime.spore"\)

@agent.tool\(description**=**"Connect to specialist for consultation"\) **def **consult\_specialist\(\) **-> **SwaigFunctionResult:

**return **\(

SwaigFunctionResult\("Connecting you to a specialist. I'll be here when you're done."\)

.connect\("\+15551234567", final**=**False\)

*\# Returns to agent after*

\)

**if **\_\_name\_\_ **== **"\_\_main\_\_":

agent.run\(\)

**11.11 Skills Usage**

**11.11.1**

**DateTime Skill**

from signalwire\_agents import AgentBase

agent **= **AgentBase\(name**=**"datetime", route**=**"/datetime"\) agent.prompt\_add\_section\("Role", "You provide time and date information."\) agent.add\_language\("English", "en-US", "rime.spore"\) agent.add\_skill\("datetime"\)

**if **\_\_name\_\_ **== **"\_\_main\_\_":

agent.run\(\)

**11.11.2**

**Search Skill**

from signalwire\_agents import AgentBase

agent **= **AgentBase\(name**=**"search", route**=**"/search"\) agent.prompt\_add\_section\("Role", "You search documentation for answers."\) agent.add\_language\("English", "en-US", "rime.spore"\) agent.add\_skill\("native\_vector\_search", \{

"index\_path": "./docs.swsearch", 

"tool\_name": "search\_docs", 

"tool\_description": "Search the documentation" 

\}\)

**if **\_\_name\_\_ **== **"\_\_main\_\_":

agent.run\(\)

351

11. Examples

**11.12**

**Global Data**

**11.12.1 Setting Initial State**

from signalwire\_agents import AgentBase

from signalwire\_agents.core.function\_result import SwaigFunctionResult agent **= **AgentBase\(name**=**"state", route**=**"/state"\) agent.prompt\_add\_section\("Role", "You track user preferences."\) agent.add\_language\("English", "en-US", "rime.spore"\) agent.set\_global\_data\(\{

"user\_tier": "standard", 

"preferences": \{\}

\}\)

@agent.tool\(description**=**"Update user preference"\) **def **set\_preference\(key: str, value: str\) **-> **SwaigFunctionResult: **return **SwaigFunctionResult\(f"Set **\{**key**\} **to **\{**value**\}**"\).update\_global\_data\(\{

f"preferences. **\{**key**\}**": value

\}\)

**if **\_\_name\_\_ **== **"\_\_main\_\_":

agent.run\(\)

**11.13 Recording**

**11.13.1**

**Enable Call Recording**

from signalwire\_agents import AgentBase

from signalwire\_agents.core.function\_result import SwaigFunctionResult agent **= **AgentBase\(

name**=**"recording", 

route**=**"/recording", 

record\_call**=**True, 

record\_format**=**"mp3", 

record\_stereo**=**True

\)

agent.prompt\_add\_section\("Role", "You handle recorded conversations."\) agent.add\_language\("English", "en-US", "rime.spore"\)

@agent.tool\(description**=**"Start call recording"\)

**def **start\_recording\(\) **-> **SwaigFunctionResult:

**return **\(

SwaigFunctionResult\("Starting recording now."\)

.record\_call\(control\_id**=**"main", stereo**=**True, format**=**"mp3"\)

\)

@agent.tool\(description**=**"Stop call recording"\)

**def **stop\_recording\(\) **-> **SwaigFunctionResult:

**return **\(

SwaigFunctionResult\("Recording stopped."\)

.stop\_record\_call\(control\_id**=**"main"\)

\)

**if **\_\_name\_\_ **== **"\_\_main\_\_":

agent.run\(\)

352

11. Examples

**11.14**

**SMS Notifications**

**11.14.1 Send Confirmation SMS**

from signalwire\_agents import AgentBase

from signalwire\_agents.core.function\_result import SwaigFunctionResult agent **= **AgentBase\(name**=**"sms", route**=**"/sms"\) agent.prompt\_add\_section\("Role", "You help with appointments and send confirmations."\) agent.add\_language\("English", "en-US", "rime.spore"\)

@agent.tool\(description**=**"Send appointment confirmation via SMS"\) **def **send\_confirmation\(

phone: str, 

date: str, 

time: str

\) **-> **SwaigFunctionResult:

**return **\(

SwaigFunctionResult\("Sending confirmation to your phone."\)

.send\_sms\(

to\_number**=**phone, 

from\_number**=**"\+15559876543", 

body**=**f"Appointment confirmed for **\{**date**\} **at **\{**time**\}**." 

\)

\)

**if **\_\_name\_\_ **== **"\_\_main\_\_":

agent.run\(\)

**11.15**

**Static Files with AgentServer**

**11.15.1**

**Serving Static Files Alongside Agents**

*\#\!/usr/bin/env python3*

*\# static\_files\_server.py - Serve static files alongside agents*

*\#*

*\# Static files directory layout:*

*\#*

*This script expects a "web/" directory in the same folder:*

*\#*

*\#*

*code/11\_examples/*

*\#*

*├── static\_files\_server.py*

*\#*

*└── web/*

*\#*

*├── index.html*

*-> served at /*

*\#*

*├── styles.css*

*-> served at /styles.css*

*\#*

*└── app.js*

*-> served at /app.js*

*\#*

*\# Route priority:*

*\#*

*/support/\**

*-> SupportAgent*

*\#*

*/sales/\**

*-> SalesAgent*

*\#*

*/health*

*-> AgentServer health check*

*\#*

*/\**

*-> Static files \(fallback\)*

from signalwire\_agents import AgentBase, AgentServer

from pathlib import Path

HOST **= **"0.0.0.0" 

PORT **= **3000

**class **SupportAgent\(AgentBase\):

**def \_\_init\_\_**\(self\):

super\(\). **\_\_init\_\_**\(name**=**"support", route**=**"/support"\) self.add\_language\("English", "en-US", "rime.spore"\) self.prompt\_add\_section\("Role", "You are a support agent."\) **class **SalesAgent\(AgentBase\):

353

11. Examples

**def \_\_init\_\_**\(self\):

super\(\). **\_\_init\_\_**\(name**=**"sales", route**=**"/sales"\) self.add\_language\("English", "en-US", "rime.spore"\) self.prompt\_add\_section\("Role", "You are a sales agent."\) **def **create\_server\(\):

*"""Create AgentServer with static file mounting.""" *

server **= **AgentServer\(host**=**HOST, port**=**PORT\)

server.register\(SupportAgent\(\), "/support"\)

server.register\(SalesAgent\(\), "/sales"\)

*\# Serve static files using SDK's built-in method*

web\_dir **= **Path\(\_\_file\_\_\).parent **/ **"web" 

**if **web\_dir.exists\(\):

server.serve\_static\_files\(str\(web\_dir\)\)

**return **server

**if **\_\_name\_\_ **== **"\_\_main\_\_":

server **= **create\_server\(\)

server.run\(\)

**11.16 Hints and Pronunciation**

**11.16.1**

**Speech Recognition Hints**

from signalwire\_agents import AgentBase

agent **= **AgentBase\(name**=**"hints", route**=**"/hints"\) agent.prompt\_add\_section\("Role", "You help with technical products."\) agent.add\_language\("English", "en-US", "rime.spore"\) agent.add\_hints\(\[

"SignalWire", 

"SWML", 

"SWAIG", 

"API", 

"SDK" 

\]\)

**if **\_\_name\_\_ **== **"\_\_main\_\_":

agent.run\(\)

**11.16.2**

**Pronunciation Rules**

from signalwire\_agents import AgentBase

agent **= **AgentBase\(name**=**"pronounce", route**=**"/pronounce"\) agent.prompt\_add\_section\("Role", "You discuss technical topics."\) agent.add\_language\("English", "en-US", "rime.spore"\) agent.add\_pronounce\(\[

\{"replace": "API", "with": "A P I"\}, 

\{"replace": "SQL", "with": "sequel"\}, 

\{"replace": "JSON", "with": "jason"\}

\]\)

**if **\_\_name\_\_ **== **"\_\_main\_\_":

agent.run\(\)

354

11. Examples

**11.17**

**Examples by Complexity**

**Summary**: Progressive examples from simple to advanced, helping you build increasingly sophisticated agents. 

**11.17.1 Beginner Examples**

**11.17.1.1 Hello World Agent**

The simplest possible agent:

*\#\!/usr/bin/env python3*

*\#\# hello\_world\_agent.py - Simplest possible agent*

from signalwire\_agents import AgentBase

agent **= **AgentBase\(name**=**"hello", route**=**"/hello"\) agent.prompt\_add\_section\("Role", "Say hello and have a friendly conversation."\) agent.add\_language\("English", "en-US", "rime.spore"\) **if **\_\_name\_\_ **== **"\_\_main\_\_":

agent.run\(\)

**11.17.1.2 FAQ Agent**

Agent that answers questions from a knowledge base:

*\#\!/usr/bin/env python3*

*\#\# faq\_agent.py - Agent with knowledge base*

from signalwire\_agents import AgentBase

agent **= **AgentBase\(name**=**"faq", route**=**"/faq"\) agent.prompt\_add\_section\("Role", "Answer questions about our company."\) agent.prompt\_add\_section\("Information", """ 

Our hours are Monday to Friday, 9 AM to 5 PM. 

We are located at 123 Main Street. 

Contact us at support@example.com. 

"""\)

agent.add\_language\("English", "en-US", "rime.spore"\) **if **\_\_name\_\_ **== **"\_\_main\_\_":

agent.run\(\)

**11.17.1.3**

**Greeting Agent**

Agent with a custom greeting:

*\#\!/usr/bin/env python3*

*\#\# greeting\_agent.py - Agent with custom greeting*

from signalwire\_agents import AgentBase

agent **= **AgentBase\(name**=**"greeter", route**=**"/greeter"\) agent.prompt\_add\_section\("Role", "You are a friendly receptionist."\) agent.prompt\_add\_section\("Greeting", """ 

Always start by saying: "Thank you for calling Acme Corporation. How may I help you today?" 

"""\)

agent.add\_language\("English", "en-US", "rime.spore"\) **if **\_\_name\_\_ **== **"\_\_main\_\_":

agent.run\(\)

355

11. Examples

**11.17.2 Intermediate Examples**

**11.17.2.1 Account Lookup Agent**

Agent with database lookup:

*\#\!/usr/bin/env python3*

*\#\# account\_lookup\_agent.py - Agent with database lookup*

from signalwire\_agents import AgentBase

from signalwire\_agents.core.function\_result import SwaigFunctionResult

*\#\# Simulated database*

ACCOUNTS **= **\{

"12345": \{"name": "John Doe", "balance": 150.00, "status": "active"\}, 

"67890": \{"name": "Jane Smith", "balance": 500.00, "status": "active"\}, 

\}

agent **= **AgentBase\(name**=**"accounts", route**=**"/accounts"\) agent.prompt\_add\_section\("Role", "You help customers check their account status."\) agent.prompt\_add\_section\("Guidelines", """ 

- Always verify the account ID before providing information

- Be helpful and professional

- Never share information about other accounts

"""\)

agent.add\_language\("English", "en-US", "rime.spore"\)

@agent.tool\(description**=**"Look up account information by ID"\) **def **lookup\_account\(account\_id: str\) **-> **SwaigFunctionResult: account **= **ACCOUNTS.get\(account\_id\)

**if **account:

**return **SwaigFunctionResult\(

f"Account for **\{**account\['name'\]**\}**: Status is **\{**account\['status'\]**\}**, " 

f"balance is $**\{**account\['balance'\]**:.2f\}**" 

\)

**return **SwaigFunctionResult\("Account not found. Please check the ID and try again."\) **if **\_\_name\_\_ **== **"\_\_main\_\_":

agent.run\(\)

**11.17.2.2**

**Appointment Scheduler**

Agent that books appointments with confirmation:

*\#\!/usr/bin/env python3*

*\#\# appointment\_scheduler\_agent.py - Agent that books appointments* from signalwire\_agents import AgentBase

from signalwire\_agents.core.function\_result import SwaigFunctionResult from datetime import datetime

appointments **= **\[\]

agent **= **AgentBase\(name**=**"scheduler", route**=**"/scheduler"\) agent.prompt\_add\_section\("Role", "You help customers schedule appointments."\) agent.prompt\_add\_section\("Guidelines", """ 

- Collect customer name, date, and preferred time

- Confirm all details before booking

- Send SMS confirmation when booking is complete

"""\)

agent.add\_language\("English", "en-US", "rime.spore"\)

@agent.tool\(description**=**"Check if a time slot is available"\) **def **check\_availability\(date: str, time: str\) **-> **SwaigFunctionResult:

*\# Check against existing appointments*

**for **apt **in **appointments:

**if **apt\["date"\] **== **date **and **apt\["time"\] **== **time: **return **SwaigFunctionResult\(f"Sorry, **\{**date**\} **at **\{**time**\} **is not available."\) **return **SwaigFunctionResult\(f" **\{**date**\} **at **\{**time**\} **is available."\)

@agent.tool\(description**=**"Book an appointment"\)

356

11. Examples

**def **book\_appointment\(

name: str, 

phone: str, 

date: str, 

time: str

\) **-> **SwaigFunctionResult:

appointments.append\(\{

"name": name, 

"phone": phone, 

"date": date, 

"time": time, 

"booked\_at": datetime.now\(\).isoformat\(\)

\}\)

**return **\(

SwaigFunctionResult\(f"Appointment booked for **\{**name**\} **on **\{**date**\} **at **\{**time**\}**."\)

.send\_sms\(

to\_number**=**phone, 

from\_number**=**"\+15559876543", 

body**=**f"Your appointment is confirmed for **\{**date**\} **at **\{**time**\}**." 

\)

\)

**if **\_\_name\_\_ **== **"\_\_main\_\_":

agent.run\(\)

**11.17.2.3 Department Router**

Agent that routes calls to the right department:

*\#\!/usr/bin/env python3*

*\#\# department\_router\_agent.py - Agent that routes calls*

from signalwire\_agents import AgentBase

from signalwire\_agents.core.function\_result import SwaigFunctionResult DEPARTMENTS **= **\{

"sales": "\+15551001001", 

"support": "\+15551001002", 

"billing": "\+15551001003", 

"hr": "\+15551001004" 

\}

agent **= **AgentBase\(name**=**"router", route**=**"/router"\) agent.prompt\_add\_section\("Role", "You are a receptionist routing calls."\) agent.prompt\_add\_section\("Departments", """ 

Available departments:

- Sales: Product inquiries, pricing, quotes

- Support: Technical help, troubleshooting

- Billing: Payments, invoices, refunds

- HR: Employment, benefits, careers

"""\)

agent.add\_language\("English", "en-US", "rime.spore"\)

@agent.tool\(description**=**"Transfer to a specific department"\) **def **transfer\_to\_department\(department: str\) **-> **SwaigFunctionResult: dept\_lower **= **department.lower\(\)

**if **dept\_lower **in **DEPARTMENTS:

**return **\(

SwaigFunctionResult\(f"Transferring you to **\{**department**\} **now."\)

.connect\(DEPARTMENTS\[dept\_lower\], final**=**True\)

\)

**return **SwaigFunctionResult\(

f"I don't have a **\{**department**\} **department. " 

"Available departments are: sales, support, billing, and HR." 

\)

**if **\_\_name\_\_ **== **"\_\_main\_\_":

agent.run\(\)

357

11. Examples

**11.17.3 Advanced Examples**

**11.17.3.1 Multi-Skill Agent**

Agent combining multiple skills:

*\#\!/usr/bin/env python3*

*\#\# multi\_skill\_agent.py - Agent with multiple skills*

from signalwire\_agents import AgentBase

from signalwire\_agents.core.function\_result import SwaigFunctionResult agent **= **AgentBase\(name**=**"assistant", route**=**"/assistant"\) agent.prompt\_add\_section\("Role", "You are a comprehensive assistant."\) agent.prompt\_add\_section\("Capabilities", """ 

You can:

- Tell the current time and date

- Search our knowledge base

- Look up weather information

- Transfer to support if needed

"""\)

agent.add\_language\("English", "en-US", "rime.spore"\)

*\#\# Add built-in skills*

agent.add\_skill\("datetime"\)

agent.add\_skill\("native\_vector\_search", \{

"index\_path": "./knowledge.swsearch", 

"tool\_name": "search\_kb" 

\}\)

*\#\# Custom function*

@agent.tool\(description**=**"Transfer to human support"\) **def **transfer\_support\(\) **-> **SwaigFunctionResult:

**return **\(

SwaigFunctionResult\("Connecting you to a support representative."\)

.connect\("\+15551234567", final**=**True\)

\)

**if **\_\_name\_\_ **== **"\_\_main\_\_":

agent.run\(\)

**11.17.3.2**

**Order Processing Agent**

Complete order management system:

*\#\!/usr/bin/env python3*

*\#\# order\_processing\_agent.py - Complete order management system* from signalwire\_agents import AgentBase

from signalwire\_agents.core.function\_result import SwaigFunctionResult from datetime import datetime

import uuid

*\#\# Simulated databases*

orders **= **\{\}

products **= **\{

"widget": \{"price": 29.99, "stock": 100\}, 

"gadget": \{"price": 49.99, "stock": 50\}, 

"device": \{"price": 99.99, "stock": 25\}

\}

agent **= **AgentBase\(name**=**"orders", route**=**"/orders"\) agent.prompt\_add\_section\("Role", "You help customers with orders."\) agent.prompt\_add\_section\("Products", """ 

Available products:

- Widget: $29.99

- Gadget: $49.99

- Device: $99.99

"""\)

agent.prompt\_add\_section\("Guidelines", """ 

- Verify product availability before placing orders

358

11. Examples

- Collect customer name and phone for orders

- Confirm order details before finalizing

- Provide order ID for tracking

"""\)

agent.add\_language\("English", "en-US", "rime.spore"\) agent.set\_global\_data\(\{"current\_order": None\}\)

@agent.tool\(description**=**"Check product availability"\) **def **check\_product\(product: str\) **-> **SwaigFunctionResult: prod **= **products.get\(product.lower\(\)\)

**if **prod:

**return **SwaigFunctionResult\(

f" **\{**product**. **title\(\)**\}**: $**\{**prod\['price'\]**\}**, **\{**prod\['stock'\]**\} **in stock." 

\)

**return **SwaigFunctionResult\(f"Product ' **\{**product**\}**' not found."\)

@agent.tool\(description**=**"Place an order"\)

**def **place\_order\(

product: str, 

quantity: int, 

customer\_name: str, 

customer\_phone: str

\) **-> **SwaigFunctionResult:

prod **= **products.get\(product.lower\(\)\)

**if not **prod:

**return **SwaigFunctionResult\(f"Product ' **\{**product**\}**' not found."\) **if **prod\["stock"\] **< **quantity:

**return **SwaigFunctionResult\(f"Insufficient stock. Only **\{**prod\['stock'\]**\} **available."\) order\_id **= **str\(uuid.uuid4\(\)\)\[:8\].upper\(\)

total **= **prod\["price"\] **\* **quantity

orders\[order\_id\] **= **\{

"product": product, 

"quantity": quantity, 

"total": total, 

"customer": customer\_name, 

"phone": customer\_phone, 

"status": "confirmed", 

"created": datetime.now\(\).isoformat\(\)

\}

prod\["stock"\] **-= **quantity

**return **\(

SwaigFunctionResult\(

f"Order **\{**order\_id**\} **confirmed\! **\{**quantity**\}**x **\{**product**\} **for $**\{**total**:.2f\}**." 

\)

.update\_global\_data\(\{"last\_order\_id": order\_id\}\)

.send\_sms\(

to\_number**=**customer\_phone, 

from\_number**=**"\+15559876543", 

body**=**f"Order **\{**order\_id**\} **confirmed: **\{**quantity**\}**x **\{**product**\}**, $**\{**total**:.2f\}**" 

\)

\)

@agent.tool\(description**=**"Check order status"\)

**def **order\_status\(order\_id: str\) **-> **SwaigFunctionResult: order **= **orders.get\(order\_id.upper\(\)\)

**if **order:

**return **SwaigFunctionResult\(

f"Order **\{**order\_id**\}**: **\{**order\['quantity'\]**\}**x **\{**order\['product'\]**\}**, " 

f"$**\{**order\['total'\]**:.2f\}**, Status: **\{**order\['status'\]**\}**" 

\)

**return **SwaigFunctionResult\(f"Order **\{**order\_id**\} **not found."\) **if **\_\_name\_\_ **== **"\_\_main\_\_":

agent.run\(\)

359

11. Examples

**11.17.3.3 Multi-Agent Server**

Server hosting multiple specialized agents:

*\#\!/usr/bin/env python3*

*\#\# multi\_agent\_server.py - Server hosting multiple agents*

from signalwire\_agents import AgentBase, AgentServer

from signalwire\_agents.core.function\_result import SwaigFunctionResult **class **SalesAgent\(AgentBase\):

**def \_\_init\_\_**\(self\):

super\(\). **\_\_init\_\_**\(name**=**"sales", route**=**"/sales"\) self.prompt\_add\_section\("Role", "You are a sales specialist."\) self.add\_language\("English", "en-US", "rime.spore"\)

@AgentBase.tool\(description**=**"Get product pricing"\) **def **get\_pricing\(self, product: str\) **-> **SwaigFunctionResult: **return **SwaigFunctionResult\(f"Pricing for **\{**product**\}**: Starting at $99."\) **class **SupportAgent\(AgentBase\):

**def \_\_init\_\_**\(self\):

super\(\). **\_\_init\_\_**\(name**=**"support", route**=**"/support"\) self.prompt\_add\_section\("Role", "You are a support specialist."\) self.add\_language\("English", "en-US", "rime.spore"\) self.add\_skill\("native\_vector\_search", \{

"index\_path": "./support\_docs.swsearch" 

\}\)

@AgentBase.tool\(description**=**"Create support ticket"\) **def **create\_ticket\(self, issue: str\) **-> **SwaigFunctionResult: **return **SwaigFunctionResult\(f"Ticket created for: **\{**issue**\}**"\) **class **RouterAgent\(AgentBase\):

**def \_\_init\_\_**\(self\):

super\(\). **\_\_init\_\_**\(name**=**"router", route**=**"/"\) self.prompt\_add\_section\("Role", "Route callers to the right agent."\) self.add\_language\("English", "en-US", "rime.spore"\)

@AgentBase.tool\(description**=**"Transfer to sales"\)

**def **transfer\_sales\(self\) **-> **SwaigFunctionResult:

**return **SwaigFunctionResult\("Transferring to sales."\).connect\(

"https://agent.example.com/sales", final**=**True

\)

@AgentBase.tool\(description**=**"Transfer to support"\) **def **transfer\_support\(self\) **-> **SwaigFunctionResult: **return **SwaigFunctionResult\("Transferring to support."\).connect\(

"https://agent.example.com/support", final**=**True

\)

**if **\_\_name\_\_ **== **"\_\_main\_\_":

server **= **AgentServer\(host**=**"0.0.0.0", port**=**8080\) server.register\(RouterAgent\(\)\)

server.register\(SalesAgent\(\)\)

server.register\(SupportAgent\(\)\)

server.run\(\)

360

11. Examples

**11.17.4 Expert Examples**

**11.17.4.1 Code-Driven LLM Architecture**

The most robust agents use **code-driven architecture **where business logic lives in SWAIG functions, not prompts. 

The LLM becomes a natural language translator while code handles all validation, state, and business rules. 

┌─────────────────────────────────────────────────────────────┐

│

Code-Driven Approach

│

│

│

│

User ──► LLM ──► SWAIG Function ──► Response to LLM

│

│

│

│

│

▼

│

│

Code enforces:

│

│

• Business rules

│

│

• State management

│

│

• Calculations

│

│

• Validation

│

│

• UI updates

│

│

│

│

Advantage: LLM only translates intent, code does the rest │

└─────────────────────────────────────────────────────────────┘

**Core principles:**

**Traditional Approach**

**Code-Driven Approach**

Rules in prompts

Rules in functions

LLM does math

Code does math

LLM tracks state

Global data tracks state

Hope LLM follows rules

Code enforces rules

**11.17.4.2**

**Order-Taking Agent \(Code-Driven\)**

Complete example demonstrating code-driven patterns:

*\#\!/usr/bin/env python3*

*\#\# code\_driven\_order\_agent.py - Code-driven LLM architecture example* from signalwire\_agents import AgentBase

from signalwire\_agents.core.function\_result import SwaigFunctionResult

*\#\# Menu data lives in code, not prompts*

MENU **= **\{

"tacos": \{

"T001": \{"name": "Beef Taco", "price": 3.49\}, 

"T002": \{"name": "Chicken Taco", "price": 3.49\}, 

"T003": \{"name": "Fish Taco", "price": 4.29\}, 

\}, 

"sides": \{

"S001": \{"name": "Chips & Salsa", "price": 2.99\}, 

"S002": \{"name": "Guacamole", "price": 3.49\}, 

\}, 

"drinks": \{

"D001": \{"name": "Soda", "price": 1.99\}, 

"D002": \{"name": "Iced Tea", "price": 1.99\}, 

\}, 

"combos": \{

"C001": \{"name": "Taco Combo", "price": 9.99, 

"includes": \["taco", "chips", "drink"\], "savings": 1.97\}, 

\}

\}

*\#\# Aliases handle natural speech variations*

MENU\_ALIASES **= **\{

361

11. Examples

"D001": \["soda", "coke", "pop", "soft drink"\], 

"S001": \["chips", "chips and salsa", "nachos"\], 

\}

TAX\_RATE **= **0.10

MAX\_ITEMS\_PER\_ADD **= **10

MAX\_ORDER\_VALUE **= **500.00

**class **OrderAgent\(AgentBase\):

**def \_\_init\_\_**\(self\):

super\(\). **\_\_init\_\_**\(name**=**"order-agent", route**=**"/order"\) self.add\_language\("English", "en-US", "rime.spore"\)

*\# Minimal prompt - personality only, not rules*

self.prompt\_add\_section\("Role", 

"You are a friendly drive-thru order taker. " 

"Keep responses brief and natural." 

\)

*\# State machine controls conversation flow*

self.\_setup\_contexts\(\)

*\# Initialize order state*

self.set\_global\_data\(\{

"order\_state": \{

"items": \[\], 

"subtotal": 0.00, 

"tax": 0.00, 

"total": 0.00, 

"item\_count": 0

\}

\}\)

**def **\_setup\_contexts\(self\):

*"""Define state machine for conversation flow.""" *

contexts **= **self.define\_contexts\(\)

ctx **= **contexts.add\_context\("default"\)

*\# Greeting state - limited actions*

ctx.add\_step\("greeting"\) **\\**

.add\_section\("Task", "Welcome the customer and take their order."\) **\\**

.set\_functions\(\["add\_item"\]\) **\\**

.set\_valid\_steps\(\["taking\_order"\]\)

*\# Order state - full ordering capabilities*

ctx.add\_step\("taking\_order"\) **\\**

.add\_section\("Task", "Continue taking the order."\) **\\**

.add\_bullets\("Info", \[

"Current total: $$**\{global\_data.order\_state.total\}**", 

"Items: $**\{global\_data.order\_state.item\_count\}**" 

\]\) **\\**

.set\_functions\(\["add\_item", "remove\_item", "finalize\_order"\]\) **\\**

.set\_valid\_steps\(\["confirming"\]\)

*\# Confirmation state*

ctx.add\_step\("confirming"\) **\\**

.add\_section\("Task", "Confirm the order with the customer."\) **\\**

.set\_functions\(\["confirm\_order", "add\_item", "remove\_item"\]\) **\\**

.set\_valid\_steps\(\["complete"\]\)

**def **\_find\_menu\_item\(self, item\_name\):

*"""Find item by name or alias - code handles fuzzy matching.""" *

item\_lower **= **item\_name.lower\(\).strip\(\)

*\# Check exact matches first*

**for **category, items **in **MENU.items\(\):

**for **sku, data **in **items.items\(\):

**if **item\_lower **== **data\["name"\].lower\(\):

**return **sku, data, category

362

11. Examples

*\# Check aliases*

**for **sku, aliases **in **MENU\_ALIASES.items\(\):

**if **item\_lower **in **\[a.lower\(\) **for **a **in **aliases\]: **for **category, items **in **MENU.items\(\):

**if **sku **in **items:

**return **sku, items\[sku\], category

**return **None, None, None

**def **\_calculate\_totals\(self, items\):

*"""Code does all math - LLM never calculates.""" *

subtotal **= **sum\(item\["price"\] **\* **item\["quantity"\] **for **item **in **items\) tax **= **round\(subtotal **\* **TAX\_RATE, 2\)

total **= **round\(subtotal **\+ **tax, 2\)

**return **subtotal, tax, total

**def **\_check\_combo\_opportunity\(self, items\):

*"""Code detects upsells - no prompt rules needed.""" *

item\_names **= **\[i\["name"\].lower\(\) **for **i **in **items\]

has\_taco **= **any\("taco" **in **n **for **n **in **item\_names\) has\_chips **= **any\("chip" **in **n **for **n **in **item\_names\) has\_drink **= **any\(n **in **\["soda", "iced tea"\] **for **n **in **item\_names\)

*\# Check if already has combo*

**if **any\("combo" **in **n **for **n **in **item\_names\): **return **None

**if **has\_taco **and **has\_chips **and **has\_drink:

**return **"Great news\! I can upgrade you to a Taco Combo and save you $1.97\!" 

**return **None

@AgentBase.tool\(

name**=**"add\_item", 

description**=**"Add an item to the order", 

parameters**=**\{

"type": "object", 

"properties": \{

"item\_name": \{"type": "string", "description": "Name of the menu item"\}, 

"quantity": \{"type": "integer", "description": "How many \(default 1\)", 

"minimum": 1, "maximum": 10\}

\}, 

"required": \["item\_name"\]

\}

\)

**def **add\_item\(self, args, raw\_data\):

*"""Add item - code enforces all limits and rules.""" *

item\_name **= **args.get\("item\_name", ""\)

quantity **= **args.get\("quantity", 1\)

*\# Code enforces limits \(LLM doesn't need to know\)*

**if **quantity **> **MAX\_ITEMS\_PER\_ADD:

quantity **= **MAX\_ITEMS\_PER\_ADD

*\# Get order state*

global\_data **= **raw\_data.get\("global\_data", \{\}\)

order\_state **= **global\_data.get\("order\_state", \{

"items": \[\], "subtotal": 0, "tax": 0, "total": 0, "item\_count": 0

\}\)

*\# Find the item \(code handles fuzzy matching\)*

sku, item\_data, category **= **self.\_find\_menu\_item\(item\_name\)

**if not **item\_data:

**return **SwaigFunctionResult\(

f"I couldn't find ' **\{**item\_name**\}**' on the menu. " 

"We have tacos, chips, guacamole, and drinks." 

\)

*\# Check order value limit*

potential **= **order\_state\["subtotal"\] **\+ **\(item\_data\["price"\] **\* **quantity\) **if **potential **> **MAX\_ORDER\_VALUE:

**return **SwaigFunctionResult\(

363

11. Examples

f"That would exceed our $**\{**MAX\_ORDER\_VALUE**:.2f\} **order limit." 

\)

*\# Add to order*

order\_state\["items"\].append\(\{

"sku": sku, 

"name": item\_data\["name"\], 

"quantity": quantity, 

"price": item\_data\["price"\]

\}\)

order\_state\["item\_count"\] **\+= **quantity

*\# Code calculates totals \(LLM never does math\)*

subtotal, tax, total **= **self.\_calculate\_totals\(order\_state\["items"\]\) order\_state\["subtotal"\] **= **subtotal

order\_state\["tax"\] **= **tax

order\_state\["total"\] **= **total

*\# Build response that guides LLM behavior*

response **= **f"Added **\{**quantity**\}**x **\{**item\_data\['name'\]**\} **\($**\{**item\_data\['price'\]**:.2f\} **each\)." 

*\# Check for upsell \(code decides, not LLM\)*

combo\_suggestion **= **self.\_check\_combo\_opportunity\(order\_state\["items"\]\) **if **combo\_suggestion:

response **\+= **f"\\n\\n**\{**combo\_suggestion**\}**" 

*\# Update state and transition*

global\_data\["order\_state"\] **= **order\_state

result **= **SwaigFunctionResult\(response\)

result.update\_global\_data\(global\_data\)

result.swml\_change\_step\("taking\_order"\)

*\# Push UI update \(frontend stays in sync without LLM\)*

result.swml\_user\_event\(\{

"type": "item\_added", 

"item": \{"name": item\_data\["name"\], "quantity": quantity, 

"price": item\_data\["price"\]\}, 

"total": total

\}\)

**return **result

@AgentBase.tool\(

name**=**"remove\_item", 

description**=**"Remove an item from the order", 

parameters**=**\{

"type": "object", 

"properties": \{

"item\_name": \{"type": "string", "description": "Item to remove"\}, 

"quantity": \{"type": "integer", "description": "How many \(-1 for all\)"\}

\}, 

"required": \["item\_name"\]

\}

\)

**def **remove\_item\(self, args, raw\_data\):

*"""Remove item - code handles all edge cases.""" *

item\_name **= **args.get\("item\_name", ""\).lower\(\) quantity **= **args.get\("quantity", 1\)

global\_data **= **raw\_data.get\("global\_data", \{\}\)

order\_state **= **global\_data.get\("order\_state", \{"items": \[\]\}\)

*\# Find matching item in order*

**for **i, item **in **enumerate\(order\_state\["items"\]\): **if **item\_name **in **item\["name"\].lower\(\):

**if **quantity **== -**1 **or **quantity **>= **item\["quantity"\]: removed **= **order\_state\["items"\].pop\(i\)

order\_state\["item\_count"\] **-= **removed\["quantity"\]

**else**:

item\["quantity"\] **-= **quantity

364

11. Examples

order\_state\["item\_count"\] **-= **quantity

*\# Recalculate*

subtotal, tax, total **= **self.\_calculate\_totals\(order\_state\["items"\]\) order\_state\["subtotal"\] **= **subtotal

order\_state\["tax"\] **= **tax

order\_state\["total"\] **= **total

global\_data\["order\_state"\] **= **order\_state

result **= **SwaigFunctionResult\(f"Removed **\{**item\_name**\} **from your order."\) result.update\_global\_data\(global\_data\)

**return **result

**return **SwaigFunctionResult\(f"I don't see **\{**item\_name**\} **in your order."\)

@AgentBase.tool\(

name**=**"finalize\_order", 

description**=**"Finalize and review the order", 

parameters**=**\{"type": "object", "properties": \{\}\}

\)

**def **finalize\_order\(self, args, raw\_data\):

*"""Finalize - code builds the summary.""" *

global\_data **= **raw\_data.get\("global\_data", \{\}\)

order\_state **= **global\_data.get\("order\_state", \{\}\)

**if not **order\_state.get\("items"\):

**return **SwaigFunctionResult\("Your order is empty. What can I get you?"\)

*\# Code builds accurate summary \(LLM just relays it\)*

items\_text **= **", ".join\(

f" **\{**i\['quantity'\]**\}**x **\{**i\['name'\]**\}**" **for **i **in **order\_state\["items"\]

\)

result **= **SwaigFunctionResult\(

f"Your order: **\{**items\_text**\}**. " 

f"Total is $**\{**order\_state\['total'\]**:.2f\} **including tax. " 

"Does that look correct?" 

\)

result.swml\_change\_step\("confirming"\)

**return **result

@AgentBase.tool\(

name**=**"confirm\_order", 

description**=**"Confirm the order is complete", 

parameters**=**\{"type": "object", "properties": \{\}\}

\)

**def **confirm\_order\(self, args, raw\_data\):

*"""Confirm - code handles completion.""" *

global\_data **= **raw\_data.get\("global\_data", \{\}\)

order\_state **= **global\_data.get\("order\_state", \{\}\)

*\# Generate order number*

import random

order\_num **= **random.randint\(100, 999\)

result **= **SwaigFunctionResult\(

f"Order \#**\{**order\_num**\} **confirmed\! " 

f"Your total is $**\{**order\_state\['total'\]**:.2f\}**. " 

"Please pull forward. Thank you\!" 

\)

result.swml\_change\_step\("complete"\)

*\# Final UI update*

result.swml\_user\_event\(\{

"type": "order\_complete", 

"order\_number": order\_num, 

"total": order\_state\["total"\]

\}\)

**return **result

365

11. Examples

**if **\_\_name\_\_ **== **"\_\_main\_\_":

agent **= **OrderAgent\(\)

agent.run\(\)

**Key patterns demonstrated:**

1. **Response-guided behavior**: Functions return text that guides LLM responses. The combo upsell suggestion appears in the response, so the LLM naturally offers it. 

2. **Code-enforced limits**: MAX\_ITEMS\_PER\_ADD and MAX\_ORDER\_VALUE are enforced in code. The LLM cannot bypass them. 

3. **State machine control**: set\_functions\(\) restricts what the LLM can do in each state. Impossible actions are literally unavailable. 

4. **Dynamic prompt injection**: $\{global\_data.order\_state.total\} injects current state into prompts without LLM tracking. 

5. **UI synchronization**: swml\_user\_event\(\) pushes updates to frontends in real-time. 

6. **Fuzzy input handling**: \_find\_menu\_item\(\) handles variations like “coke” → “Soda” without prompt rules. 

**11.17.5**

**Complexity Progression**

**11.17.5.1 Beginner**

1. Create basic agent with prompt

2. Add language configuration

3. Test with swaig-test

**11.17.5.2**

**Intermediate**

4. Add SWAIG functions

5. Use global data for state

6. Add skills

7. Implement call transfers

**11.17.5.3**

**Advanced**

8. Use DataMap for API integration

9. Implement context workflows

10. Build multi-agent systems

11. Deploy to production

**11.17.5.4**

**Expert**

12. Code-driven LLM architecture

13. State machine conversation control

14. Response-guided LLM behavior

15. Real-time UI synchronization

366

**Chapter 12**

**Appendix**

**Summary**: Reference materials, patterns, best practices, and troubleshooting guides for the SignalWire Agents SDK. 

**12.1 About This Chapter**

This appendix provides supplementary reference materials to support your development with the SignalWire Agents SDK. 

**Section**

**Description**

AI Parameters

Complete reference for all AI model parameters

Design Patterns

Common architectural patterns and solutions

Best Practices

Guidelines for production-quality agents

Troubleshooting

Common issues and their solutions

Migration Guide

Upgrading between SDK versions

Changelog

Version history and release notes

**12.2**

**Quick Reference**

**Task**

**See Section**

Configure AI model behavior

AI Parameters → LLM Parameters

Set speech recognition

AI Parameters → ASR Parameters

Adjust timing/timeouts

AI Parameters → Timing Parameters

Implement common patterns

Design Patterns

Optimize for production

Best Practices

Debug agent issues

Troubleshooting

Upgrade SDK version

Migration Guide

367

12. Appendix

**12.3 Chapter Contents**

**Section**

**Description**

AI Parameters

Complete AI parameter reference

Design Patterns

Common architectural patterns

Best Practices

Production guidelines

Troubleshooting

Common issues and solutions

Migration Guide

Version upgrade guide

Changelog

Version history

**12.4 Overview**

**Category**

**Description**

**Where to Set**

LLM API

Model behavior \(temperature, etc.\)

prompt/post\_prompt

ASR

Speech recognition settings

prompt or params

Timing

Timeouts and delays

params

Behavior

Agent behavior toggles

params

Interrupt

Interruption handling

params

Audio

Volume and background audio

params

Video

Video display options

params

**12.5**

**Setting Parameters in Python**

from signalwire\_agents import AgentBase

agent **= **AgentBase\(name**=**"assistant", route**=**"/assistant"\)

*\# Set AI parameters*

agent.set\_params\(\{

"temperature": 0.7, 

"confidence": 0.6, 

"end\_of\_speech\_timeout": 2000, 

"attention\_timeout": 10000

\}\)

368

12. Appendix

**12.6 LLM API Parameters**

These parameters control the AI model’s behavior. Set in prompt or post\_prompt sections. 

**Parameter**

**Type**

**Range**

**Default**

**Description**

temperature

number

0.0 - 2.0

0.3

Output randomness

top\_p

number

0.0 - 1.0

1.0

Nucleus sampling

frequency\_penalty

number

-2.0 - 2.0

0.1

Repeat penalty

presence\_penalty

number

-2.0 - 2.0

0.1

New topic bonus

max\_tokens

integer

1 - 16385

256

Max response size

max\_completion\_-

integer

1 - 2048

256

For o1-style models

tokens

reasoning\_effort

string

-

“low” 

o1 reasoning level

verbosity

string

-

“low” 

Response length

**12.6.1**

**Temperature**

Controls randomness in output generation: - **0.0**: Deterministic, consistent responses - **0.3 **\(default\): Balanced creativity - **1.0\+**: More creative, less predictable

**12.6.2**

**Reasoning Effort**

For o1-style models only: - "low": Quick responses - "medium": Balanced reasoning - "high": Deep analysis **12.7**

**ASR \(Speech Recognition\) Parameters**

Control automatic speech recognition behavior. 

**Parameter**

**Type**

**Range**

**Default**

**Description**

energy\_level

number

0 - 100

52

Minimum audio \(dB\)

asr\_smart\_format

boolean

-

false

Smart formatting

asr\_diarize

boolean

-

false

Speaker detection

asr\_speaker\_affinity

boolean

-

false

Speaker tracking

**12.7.1**

**Confidence Thresholds**

• **confidence**: How certain the ASR must be before triggering speech detection

• **barge\_confidence**: How certain before allowing interruption of AI speech Lower values = more sensitive \(may pick up noise\), higher values = more strict. 

369

12. Appendix

**12.8**

**Timing Parameters**

Control various timeouts and timing behaviors. 

**Parameter**

**Type**

**Range**

**Default**

**Description**

end\_of\_speech\_-

integer

250 - 10000

700

End silence \(ms\)

timeout

speech\_timeout

integer

-

60000

Max speech \(ms\)

speech\_event\_-

integer

-

1400

Event wait \(ms\)

timeout

attention\_timeout

integer

0 - 600000

5000

Idle prompt \(ms\)

outbound\_-

integer

10000 - 600000

120000

Outbound \(ms\)

attention\_timeout

inactivity\_timeout

integer

10000 - 3600000

600000

Exit delay \(ms\)

digit\_timeout

integer

-

3000

DTMF wait \(ms\)

initial\_sleep\_ms

integer

-

0

Start delay \(ms\)

transparent\_barge\_-

integer

0 - 60000

3000

Barge time \(ms\)

max\_time

**12.8.1**

**Key Timeouts**

• **end\_of\_speech\_timeout**: Milliseconds of silence to detect end of speech

• **attention\_timeout**: How long to wait before prompting user \(0 disables\)

• **inactivity\_timeout**: How long before auto-hangup \(default 10 minutes\) **12.8.2**

**Hard Stop Time**

*\# Time expression format*

agent.set\_params\(\{

"hard\_stop\_time": "5m", 

*\# 5 minutes*

"hard\_stop\_time": "1h30m", 

*\# 1 hour 30 minutes*

"hard\_stop\_prompt": "We need to wrap up now." 

\}\)

**12.9**

**Behavior Parameters**

Control various AI agent behaviors. 

**Parameter**

**Type**

**Default**

**Description**

direction

string

natural

Force inbound/outbound

wait\_for\_user

boolean

false

Wait before speaking

conscience

boolean/str

true

Safety enforcement

transparent\_barge

boolean

true

Transparent barge mode

enable\_pause

boolean

false

Allow pausing

enable\_turn\_detection

boolean

varies

Turn detection

enable\_vision

boolean

false

Vision/video AI

enable\_thinking

boolean

false

Complex reasoning

save\_conversation

boolean

false

Save summary

persist\_global\_data

boolean

true

Persist data

transfer\_summary

boolean

false

Summary on transfer

370

12. Appendix

**12.10**

**SWAIG Control Parameters**

**Parameter**

**Type**

**Default**

**Description**

swaig\_allow\_swml

boolean

true

Allow SWML returns

swaig\_allow\_settings

boolean

true

Allow settings mods

swaig\_post\_conversation

boolean

false

Post conversation

swaig\_set\_global\_data

boolean

true

Allow global data

hold\_on\_process

boolean

false

Hold during process

barge\_functions

boolean

true

Allow function barge

function\_wait\_for\_talking

boolean

false

Wait for speech

functions\_on\_no\_response

boolean

false

Run on no response

functions\_on\_speaker\_-

boolean

true

Run on timeout

timeout

**12.11 Interrupt Parameters**

**Parameter**

**Type**

**Default**

**Description**

acknowledge\_interruptions

boolean

false

Acknowledge interrupts

interrupt\_prompt

string

-

Custom interrupt message

interrupt\_on\_noise

boolean

false

Allow noise interrupts

max\_interrupts

integer

0

Max before

interrupt\_prompt

**12.12**

**Audio Parameters**

**Parameter**

**Type**

**Range**

**Default**

**Description**

ai\_volume

integer

-50 - 50

0

AI voice volume

background\_file

string

-

-

Background audio

URL

background\_file\_-

integer

-50 - 50

0

Background volume

volume

background\_file\_-

integer

-

-1

Loop count

loops

\(-1=infinite\)

hold\_music

string

-

-

Hold audio/tone

max\_emotion

integer

1 - 30

30

TTS emotion level

**12.12.1**

**Hold Music with Tone**

*\# Use tone generator*

agent.set\_params\(\{

"hold\_music": "tone:440" 

*\# 440Hz tone*

\}\)

*\# Use audio file*

agent.set\_params\(\{

"hold\_music": "https://example.com/hold-music.mp3" 

\}\)

371

12. Appendix

**12.13**

**Video Parameters**

**Parameter**

**Type**

**Description**

video\_talking\_file

string

Video when AI is talking

video\_idle\_file

string

Video when AI is idle

video\_listening\_file

string

Video when AI is listening

**12.14 String Parameters**

**Parameter**

**Default**

**Description**

local\_tz

“US/Central” 

Timezone for agent

conversation\_id

-

ID for cross-call persistence

digit\_terminators

-

DTMF end characters \(e.g., 

“\#”\)

barge\_match\_string

-

Barge pattern matching

tts\_number\_format

“international” 

Phone format: national/intl

ai\_model

“gpt-4o-mini” 

AI model to use

thinking\_model

-

Model for thinking mode

vision\_model

-

Model for vision

pom\_format

“markdown” 

Prompt format:

markdown/xml

attention\_timeout\_prompt

-

Custom attention prompt

static\_greeting

-

Pre-recorded greeting

summary\_mode

-

string/og/function

**12.15**

**VAD Configuration**

Voice Activity Detection uses a string format: silero\_thresh:frame\_ms agent.set\_params\(\{

"vad\_config": "0.5:30" 

*\# threshold 0.5, 30ms frames*

\}\)

**12.16**

**Post-Prompt Parameter Defaults**

Parameters have different defaults in post\_prompt for more deterministic summaries: **Parameter**

**Prompt Default**

**Post-Prompt Default**

**Reason**

temperature

0.3

0.0

Deterministic

frequency\_penalty

0.1

0.0

No penalty

presence\_penalty

0.1

0.0

No penalty

372

12. Appendix

**12.17**

**Model-Specific Overrides**

Different models support different parameters:

**Model Type**

**Supported Parameters**

OpenAI

frequency\_penalty, presence\_penalty, max\_tokens, top\_p

Bedrock Claude

max\_completion\_tokens instead of max\_tokens

o1-style

reasoning\_effort, max\_completion\_tokens

**12.18 Complete Example**

*\#\!/usr/bin/env python3*

*\# configured\_agent.py - Agent with all AI parameters configured* from signalwire\_agents import AgentBase

agent **= **AgentBase\(name**=**"configured", route**=**"/configured"\) agent.prompt\_add\_section\("Role", "You are a customer service agent."\) agent.add\_language\("English", "en-US", "rime.spore"\)

*\# Configure all parameters*

agent.set\_params\(\{

*\# LLM settings*

"max\_tokens": 300, 

*\# Timing*

"end\_of\_speech\_timeout": 1500, 

"attention\_timeout": 8000, 

"inactivity\_timeout": 300000, 

*\# Behavior*

"wait\_for\_user": False, 

"conscience": True, 

"local\_tz": "America/New\_York", 

*\# Audio*

"background\_file": "https://example.com/ambient.mp3", 

"background\_file\_volume": **-**30

\}\)

**if **\_\_name\_\_ **== **"\_\_main\_\_":

agent.run\(\)

**12.19**

**SWML Example**

**\{**

"version" **: **"1.0.0" **, **

"sections" **: \{**

"main" **: **\[**\{**

"ai" **: \{**

"params" **: \{**

"end\_of\_speech\_timeout" **: **2000**, **

"attention\_timeout" **: **10000**, **

"inactivity\_timeout" **: **600000**, **

"wait\_for\_user" **: false, **

"conscience" **: true, **

"local\_tz" **: **"America/Chicago" **, **

"background\_file" **: **"https://example.com/music.mp3" **, **

"background\_file\_volume" **: **-25

**\}, **

"prompt" **: \{**

"temperature" **: **0.3**, **

"top\_p" **: **1.0**, **

373

12. Appendix

"frequency\_penalty" **: **0.1**, **

"presence\_penalty" **: **0.1**, **

"text" **: **"You are a helpful assistant." 

**\}, **

"post\_prompt" **: \{**

"temperature" **: **0.0**, **

"frequency\_penalty" **: **0.0**, **

"presence\_penalty" **: **0.0**, **

"text" **: **"Summarize the conversation." 

**\}**

**\}**

**\}**\]

**\}**

**\}**

374

12. Appendix

**12.20**

**Design Patterns**

**Summary**: Common architectural patterns and solutions for building SignalWire voice AI agents. 

**12.20.1 Overview**

**Pattern**

**Description**

Decorator Pattern

Add functions with @agent.tool decorator

Class-Based Agent

Subclass AgentBase for reusable agents

Multi-Agent Router

Route calls to specialized agents

State Machine

Use contexts for multi-step workflows

DataMap Integration

Serverless API integration

Skill Composition

Combine built-in skills

Dynamic Configuration

Runtime agent customization

**12.20.2**

**Decorator Pattern**

The simplest way to create an agent with functions:

from signalwire\_agents import AgentBase

from signalwire\_agents.core.function\_result import SwaigFunctionResult agent **= **AgentBase\(name**=**"helper", route**=**"/helper"\) agent.prompt\_add\_section\("Role", "You help users with account information."\) agent.add\_language\("English", "en-US", "rime.spore"\)

@agent.tool\(description**=**"Look up account by ID"\)

**def **lookup\_account\(account\_id: str\) **-> **SwaigFunctionResult:

*\# Lookup logic here*

**return **SwaigFunctionResult\(f"Account **\{**account\_id**\} **found."\)

@agent.tool\(description**=**"Update account status"\)

**def **update\_status\(account\_id: str, status: str\) **-> **SwaigFunctionResult:

*\# Update logic here*

**return **SwaigFunctionResult\(f"Account **\{**account\_id**\} **updated to **\{**status**\}**."\) **if **\_\_name\_\_ **== **"\_\_main\_\_":

agent.run\(\)

**12.20.3**

**Class-Based Agent Pattern**

For reusable, shareable agent definitions:

from signalwire\_agents import AgentBase

from signalwire\_agents.core.function\_result import SwaigFunctionResult **class **SupportAgent\(AgentBase\):

**def \_\_init\_\_**\(self\):

super\(\). **\_\_init\_\_**\(name**=**"support", route**=**"/support"\) self.prompt\_add\_section\("Role", "You are a technical support agent."\) self.prompt\_add\_section\("Guidelines", """ 

- Be patient and helpful

- Gather issue details before troubleshooting

- Escalate complex issues to human support

"""\)

self.add\_language\("English", "en-US", "rime.spore"\) self.add\_skill\("datetime"\)

@AgentBase.tool\(description**=**"Create support ticket"\) **def **create\_ticket\(self, issue: str, priority: str **= **"normal"\) **-> **SwaigFunctionResult: ticket\_id **= **f"TKT-**\{**id\(self\) **% **10000**:04d\}**" 

375

12. Appendix

**return **SwaigFunctionResult\(f"Created ticket **\{**ticket\_id**\} **for: **\{**issue**\}**"\)

@AgentBase.tool\(description**=**"Transfer to human support"\) **def **transfer\_to\_human\(self\) **-> **SwaigFunctionResult: **return **\(

SwaigFunctionResult\("Connecting you to a support representative."\)

.connect\("\+15551234567", final**=**True\)

\)

**if **\_\_name\_\_ **== **"\_\_main\_\_":

agent **= **SupportAgent\(\)

agent.run\(\)

**12.20.4**

**Multi-Agent Router Pattern**

Route calls to specialized agents based on intent:

from signalwire\_agents import AgentBase, AgentServer

from signalwire\_agents.core.function\_result import SwaigFunctionResult **class **RouterAgent\(AgentBase\):

**def \_\_init\_\_**\(self, base\_url: str\):

super\(\). **\_\_init\_\_**\(name**=**"router", route**=**"/"\) self.base\_url **= **base\_url

self.prompt\_add\_section\("Role", """ 

You are a receptionist. Determine what the caller needs and

route them to the appropriate department. 

"""\)

self.prompt\_add\_section\("Departments", """ 

- Sales: Product inquiries, pricing, purchases

- Support: Technical help, troubleshooting

- Billing: Payments, invoices, account issues

"""\)

self.add\_language\("English", "en-US", "rime.spore"\)

@AgentBase.tool\(description**=**"Transfer to sales department"\) **def **transfer\_sales\(self\) **-> **SwaigFunctionResult:

**return **\(

SwaigFunctionResult\("Transferring to sales."\)

.connect\(f" **\{**self**. **base\_url**\}**/sales", final**=**True\)

\)

@AgentBase.tool\(description**=**"Transfer to support department"\) **def **transfer\_support\(self\) **-> **SwaigFunctionResult: **return **\(

SwaigFunctionResult\("Transferring to support."\)

.connect\(f" **\{**self**. **base\_url**\}**/support", final**=**True\)

\)

**if **\_\_name\_\_ **== **"\_\_main\_\_":

server **= **AgentServer\(host**=**"0.0.0.0", port**=**8080\) server.register\(RouterAgent\("https://agent.example.com"\)\) server.run\(\)

**12.20.5**

**State Machine Pattern \(Contexts\)**

Use contexts for structured multi-step workflows:

from signalwire\_agents import AgentBase

from signalwire\_agents.core.contexts import ContextBuilder

from signalwire\_agents.core.function\_result import SwaigFunctionResult **class **VerificationAgent\(AgentBase\):

**def \_\_init\_\_**\(self\):

376

12. Appendix

super\(\). **\_\_init\_\_**\(name**=**"verify", route**=**"/verify"\) self.add\_language\("English", "en-US", "rime.spore"\) self.\_setup\_contexts\(\)

**def **\_setup\_contexts\(self\):

ctx **= **ContextBuilder\("verification"\)

ctx.add\_step\(

"greeting", 

"Welcome the caller and ask for their account number.", 

functions**=**\["verify\_account"\], 

valid\_steps**=**\["collect\_info"\]

\)

ctx.add\_step\(

"collect\_info", 

"Verify the caller's identity by asking security questions.", functions**=**\["verify\_security"\], 

valid\_steps**=**\["authenticated", "failed"\]

\)

ctx.add\_step\(

"authenticated", 

"The caller is verified. Ask how you can help them today.", functions**=**\["check\_balance", "transfer\_funds", "end\_call"\], valid\_steps**=**\["end"\]

\)

self.add\_context\(ctx.build\(\), default**=**True\)

@AgentBase.tool\(description**=**"Verify account number"\) **def **verify\_account\(self, account\_number: str\) **-> **SwaigFunctionResult: **return **SwaigFunctionResult\(f"Account **\{**account\_number**\} **found."\)

@AgentBase.tool\(description**=**"Check account balance"\) **def **check\_balance\(self, account\_id: str\) **-> **SwaigFunctionResult: **return **SwaigFunctionResult\("Current balance is $1,234.56"\) **12.20.6**

**DataMap Integration Pattern**

Use DataMap for serverless API integration:

from signalwire\_agents import AgentBase

from signalwire\_agents.core.data\_map import DataMap

agent **= **AgentBase\(name**=**"weather", route**=**"/weather"\) agent.prompt\_add\_section\("Role", "You provide weather information."\) agent.add\_language\("English", "en-US", "rime.spore"\)

*\#\# Define DataMap tool*

weather\_map **= **DataMap\(

name**=**"get\_weather", 

description**=**"Get current weather for a city" 

\)

weather\_map.add\_parameter\("city", "string", "City name", required**=**True\) weather\_map.add\_webhook\(

url**=**"https://api.weather.com/v1/current?q=$\{enc:args.city\}&key=API\_KEY", method**=**"GET", 

output\_map**=**\{

"response": "Weather in $**\{args.city\}**: $**\{response.temp\}**F, $**\{response.condition\}**" 

\}, 

error\_map**=**\{

"response": "Could not retrieve weather for $**\{args.city\}**" 

\}

\)

agent.add\_data\_map\_tool\(weather\_map\)

377

12. Appendix

**if **\_\_name\_\_ **== **"\_\_main\_\_":

agent.run\(\)

**12.20.7 Skill Composition Pattern**

Combine multiple skills for comprehensive functionality:

from signalwire\_agents import AgentBase

from signalwire\_agents.core.function\_result import SwaigFunctionResult agent **= **AgentBase\(name**=**"assistant", route**=**"/assistant"\) agent.prompt\_add\_section\("Role", """ 

You are a comprehensive assistant that can:

- Tell the current time and date

- Search our knowledge base

- Look up weather information

"""\)

agent.add\_language\("English", "en-US", "rime.spore"\)

*\#\# Add built-in skills*

agent.add\_skill\("datetime"\)

agent.add\_skill\("native\_vector\_search", \{

"index\_path": "./knowledge.swsearch", 

"tool\_name": "search\_docs", 

"tool\_description": "Search documentation" 

\}\)

*\#\# Add custom function alongside skills*

@agent.tool\(description**=**"Escalate to human agent"\) **def **escalate\(reason: str\) **-> **SwaigFunctionResult: **return **\(

SwaigFunctionResult\(f"Escalating: **\{**reason**\}**"\)

.connect\("\+15551234567", final**=**True\)

\)

**if **\_\_name\_\_ **== **"\_\_main\_\_":

agent.run\(\)

**12.20.8**

**Dynamic Configuration Pattern**

Configure agents dynamically at runtime:

from signalwire\_agents import AgentBase

from signalwire\_agents.core.function\_result import SwaigFunctionResult from typing import Dict, Any

**class **DynamicAgent\(AgentBase\):

**def \_\_init\_\_**\(self\):

super\(\). **\_\_init\_\_**\(name**=**"dynamic", route**=**"/dynamic"\) self.add\_language\("English", "en-US", "rime.spore"\) self.set\_dynamic\_config\_callback\(self.configure\_from\_call\)

**def **configure\_from\_call\(

self, 

query\_params: Dict\[str, Any\], 

body\_params: Dict\[str, Any\], 

headers: Dict\[str, str\], 

agent: 'AgentBase' 

\) **-> **None:

*\# Get caller's phone number from body*

caller **= **body\_params.get\("call", \{\}\).get\("from", ""\)

*\# Customize prompt based on caller*

**if **caller.startswith\("\+1555"\):

agent.prompt\_add\_section\("Role", "You are a VIP support agent."\) **else**:

378

12. Appendix

agent.prompt\_add\_section\("Role", "You are a standard support agent."\)

*\# Add caller info to global data*

agent.set\_global\_data\(\{"caller\_number": caller\}\)

**if **\_\_name\_\_ **== **"\_\_main\_\_":

agent **= **DynamicAgent\(\)

agent.run\(\)

**12.20.9 Pattern Selection Guide**

**Scenario**

**Recommended Pattern**

Quick prototype or simple agent

Decorator Pattern

Reusable agent for sharing

Class-Based Agent

Multiple specialized agents

Multi-Agent Router

Step-by-step workflows

State Machine \(Contexts\)

External API integration

DataMap Integration

Feature-rich agent

Skill Composition

Per-call customization

Dynamic Configuration

379

12. Appendix

**12.21**

**Best Practices**

**Summary**: Guidelines and recommendations for building production-quality SignalWire voice AI agents. 

**12.21.1 Overview**

**Category**

**Focus Area**

Prompt Design

Effective prompts and POM structure

Function Design

Well-structured SWAIG functions

Error Handling

Graceful failure and recovery

Security

Authentication and data protection

Performance

Optimization and efficiency

Testing

Validation and quality assurance

Monitoring

Logging and observability

**12.21.2**

**Prompt Design**

**12.21.2.1 Use POM \(Prompt Object Model\)**

Structure prompts with clear sections:

from signalwire\_agents import AgentBase

agent **= **AgentBase\(name**=**"service", route**=**"/service"\)

*\#\# Good: Structured sections*

agent.prompt\_add\_section\("Role", """ 

You are a customer service representative for Acme Corp. 

"""\)

agent.prompt\_add\_section\("Guidelines", body**=**"Follow these rules:", bullets**=**\[

"Be professional and courteous", 

"Verify customer identity before account access", 

"Never share sensitive information", 

"Escalate complex issues to human agents" 

\]\)

agent.add\_language\("English", "en-US", "rime.spore"\) **12.21.2.2**

**Be Specific About Behavior**

*\#\# Good: Specific instructions*

agent.prompt\_add\_section\("Response Style", """ 

- Keep responses under 3 sentences for simple questions

- Ask one question at a time

- Confirm understanding before taking action

- Use the customer's name when known

"""\)

**12.21.3**

**Function Design**

**12.21.3.1**

**Clear Descriptions**

from signalwire\_agents import AgentBase

from signalwire\_agents.core.function\_result import SwaigFunctionResult agent **= **AgentBase\(name**=**"accounts", route**=**"/accounts"\)

*\#\# Good: Descriptive with parameter details*

380

12. Appendix

@agent.tool\(description**=**"Look up customer account by account number. Returns account status, balance, and last activity date."\) **def **lookup\_account\(

account\_number: str

*\# The 8-digit account number*

\) **-> **SwaigFunctionResult:

**pass**

**12.21.3.2 Return Actionable Information**

@agent.tool\(description**=**"Check product availability"\) **def **check\_availability\(product\_id: str\) **-> **SwaigFunctionResult: stock **= **get\_stock\(product\_id\)

**if **stock **> **10:

**return **SwaigFunctionResult\(

f"Product **\{**product\_id**\} **is in stock with **\{**stock**\} **units available. " 

"The customer can place an order." 

\)

**elif **stock **> **0:

**return **SwaigFunctionResult\(

f"Product **\{**product\_id**\} **has limited stock \(**\{**stock**\} **units\). " 

"Suggest ordering soon." 

\)

**else**:

**return **SwaigFunctionResult\(

f"Product **\{**product\_id**\} **is out of stock. " 

"Expected restock date: next week." 

\)

**12.21.4**

**Error Handling**

**12.21.4.1**

**Graceful Degradation**

@agent.tool\(description**=**"Look up order status"\)

**def **order\_status\(order\_id: str\) **-> **SwaigFunctionResult: **try**:

order **= **fetch\_order\(order\_id\)

**return **SwaigFunctionResult\(

f"Order **\{**order\_id**\}**: Status is **\{**order\['status'\]**\}**" 

\)

**except **OrderNotFoundError:

**return **SwaigFunctionResult\(

f"Order **\{**order\_id**\} **was not found. " 

"Please verify the order number and try again." 

\)

**except **ServiceUnavailableError:

**return **SwaigFunctionResult\(

"The order system is temporarily unavailable. " 

"Please try again in a few minutes." 

\)

**12.21.5**

**Security**

**12.21.5.1**

**Use Authentication**

import os

agent **= **AgentBase\(

name**=**"secure", 

route**=**"/secure", 

basic\_auth**=**\(

os.environ.get\("AGENT\_USER", "agent"\), 

os.environ.get\("AGENT\_PASSWORD"\)

\)

\)

381

12. Appendix

**12.21.5.2 Secure Function Tokens**

*\#\# Require token authentication for sensitive functions*

@agent.tool\(

description**=**"Process payment", 

secure**=**True

*\# Requires valid token*

\)

**def **process\_payment\(amount: float, card\_last\_four: str\) **-> **SwaigFunctionResult: **pass**

**12.21.5.3 Environment Variables**

**Variable**

**Purpose**

SWML\_BASIC\_AUTH\_USER

Basic auth username

SWML\_BASIC\_AUTH\_PASSWORD

Basic auth password \(required for production\)

SWML\_SSL\_ENABLED

Enable HTTPS

SWML\_SSL\_CERT\_PATH

SSL certificate path

SWML\_SSL\_KEY\_PATH

SSL key path

**12.21.6**

**Performance**

**12.21.6.1 Use DataMap for Simple API Calls**

from signalwire\_agents.core.data\_map import DataMap

*\#\# Good: DataMap for simple lookups \(no webhook roundtrip\)*

weather\_map **= **DataMap\(

name**=**"get\_weather", 

description**=**"Get weather for a city" 

\)

weather\_map.add\_parameter\("city", "string", "City name", required**=**True\) weather\_map.add\_webhook\(

url**=**"https://api.weather.com/v1/current?q=$\{enc:args.city\}", method**=**"GET", 

output\_map**=**\{"response": "Weather: $**\{response.temp\}**F, $**\{response.condition\}**"\}

\)

agent.add\_data\_map\_tool\(weather\_map\)

**12.21.6.2**

**Use Fillers for Long Operations**

@agent.tool\(

description**=**"Search database", 

fillers**=**\["Searching...", "This may take a moment..."\]

\)

**def **search\_db\(query: str\) **-> **SwaigFunctionResult:

*\# Long-running search*

results **= **search\_database\(query\)

**return **SwaigFunctionResult\(f"Found **\{**len\(results\)**\} **matching orders."\) **12.21.7**

**Testing**

**12.21.7.1**

**Use swaig-test**

*\#\# Validate agent configuration*

swaig-test agent.py --dump-swml

*\#\# List available functions*

swaig-test agent.py --list-tools

382

12. Appendix

*\#\# Test specific function*

swaig-test agent.py --exec lookup\_account --account\_number "12345678" 

**12.21.8 Monitoring**

**12.21.8.1 Use Structured Logging**

import structlog

logger **= **structlog.get\_logger\(\)

@agent.tool\(description**=**"Process refund"\)

**def **process\_refund\(order\_id: str, amount: float\) **-> **SwaigFunctionResult: logger.info\(

"refund\_requested", 

order\_id**=**order\_id, 

amount**=**amount

\)

*\# Process refund*

**return **SwaigFunctionResult\(f"Refund of $**\{**amount**\} **processed."\) **12.21.9**

**Production Readiness Checklist**

□ Authentication configured \(basic\_auth or environment variables\)

□ SSL/HTTPS enabled for production

□ Sensitive functions marked as secure

□ Error handling in all functions

□ Input validation for user-provided data

□ Logging configured \(no sensitive data in logs\)

□ All functions tested with swaig-test

□ Edge cases and error scenarios tested

□ Prompts reviewed for clarity and completeness

□ Transfer/escalation paths defined

□ Timeout values appropriate for use case

□ Summary handling for call analytics

383

12. Appendix

**12.22**

**Troubleshooting**

**Summary**: Common issues and solutions when developing SignalWire voice AI agents. 

**12.22.1 Quick Diagnostics**

**Command**

**Purpose**

swaig-test agent.py --dump-swml

Verify SWML generation

swaig-test agent.py --list-tools

List registered functions

swaig-test agent.py --exec func

Test function execution

python agent.py

Check for startup errors

curl http://localhost:3000/

Test agent endpoint

**12.22.2**

**Startup Issues**

**12.22.2.1 Agent Won’t Start**

**Symptom**: Python script exits immediately or with an error. 

**Common Causes**:

1. **Missing dependencies**

*\#\# Check if signalwire-agents is installed*

pip show signalwire-agents

*\#\# Install if missing*

pip install signalwire-agents

2. **Port already in use**

Error: \[Errno 48\] Address already in use

**Solution**: Use a different port or stop the existing process. 

agent **= **AgentBase\(name**=**"myagent", route**=**"/", port**=**3001\) 3. **Invalid Python syntax**

*\#\# Check syntax*

python -m py\_compile agent.py

**12.22.2.2**

**Import Errors**

**Symptom**: ModuleNotFoundError or ImportError. 

ModuleNotFoundError: No module named 'signalwire\_agents' 

**Solutions**:

*\#\# Ensure virtual environment is activated*

source venv/bin/activate

*\#\# Verify installation*

pip list **| grep **signalwire

*\#\# Reinstall if needed*

pip install --upgrade signalwire-agents

384

12. Appendix

**12.22.3 Function Issues**

**12.22.3.1 Function Not Appearing**

**Symptom**: Function defined but not showing in --list-tools. 

**Check 1**: Decorator syntax

*\#\# Correct*

@agent.tool\(description**=**"My function"\)

**def **my\_function\(param: str\) **-> **SwaigFunctionResult: **return **SwaigFunctionResult\("Done"\)

*\#\# Wrong: Missing parentheses*

@agent.tool

**def **my\_function\(param: str\) **-> **SwaigFunctionResult: **pass**

*\#\# Wrong: Missing description*

@agent.tool\(\)

**def **my\_function\(param: str\) **-> **SwaigFunctionResult: **pass**

**Check 2**: Function defined before agent.run\(\)

from signalwire\_agents import AgentBase

from signalwire\_agents.core.function\_result import SwaigFunctionResult agent **= **AgentBase\(name**=**"test", route**=**"/"\)

*\#\# Functions must be defined before run\(\)*

@agent.tool\(description**=**"Test function"\)

**def **test\_func\(\) **-> **SwaigFunctionResult:

**return **SwaigFunctionResult\("Test"\)

*\#\# Then run*

**if **\_\_name\_\_ **== **"\_\_main\_\_":

agent.run\(\)

**12.22.3.2**

**Function Returns Wrong Response**

**Symptom**: AI receives unexpected or empty response. 

**Check 1**: Return SwaigFunctionResult

*\#\# Correct*

@agent.tool\(description**=**"Get status"\)

**def **get\_status\(\) **-> **SwaigFunctionResult:

**return **SwaigFunctionResult\("Status is OK"\)

*\#\# Wrong: Returns string instead of SwaigFunctionResult*

@agent.tool\(description**=**"Get status"\)

**def **get\_status\(\) **-> **SwaigFunctionResult:

**return **"Status is OK" 

*\# This won't work\! *

**12.22.4**

**Connection Issues**

**12.22.4.1**

**Webhook Not Reached**

**Symptom**: Functions not being called, SignalWire can’t reach agent. 

**Check 1**: Agent is accessible from internet

*\#\# Local testing with ngrok*

ngrok http 3000

*\#\# Then use ngrok URL in SignalWire*

385

12. Appendix

**Check 2**: Firewall allows connections

*\#\# Check if port is open*

curl -I http://localhost:3000/

**12.22.4.2 Authentication Failures**

**Symptom**: 401 Unauthorized errors. 

**Check credentials**:

*\#\# Test with credentials*

curl -u username:password http://localhost:3000/

**Set in agent**:

agent **= **AgentBase\(

name**=**"secure", 

route**=**"/", 

basic\_auth**=**\("username", "password"\)

\)

**12.22.5**

**Speech Recognition Issues**

**12.22.5.1 Agent Not Hearing Caller**

**Symptom**: AI doesn’t respond to speech. 

**Adjust confidence threshold**:

agent.set\_params\(\{

"confidence": 0.5, 

*\# Lower = more sensitive*

"energy\_level": 40

*\# Lower = quieter speech detected*

\}\)

**12.22.5.2**

**Frequent Interruptions**

**Symptom**: AI gets interrupted too easily. 

agent.set\_params\(\{

"barge\_confidence": 0.8, 

*\# Higher = harder to interrupt*

"barge\_min\_words": 3

*\# Require 3\+ words to barge*

\}\)

**12.22.5.3**

**Speech Cut Off Too Early**

**Symptom**: AI thinks caller finished speaking too soon. 

agent.set\_params\(\{

"end\_of\_speech\_timeout": 1500

*\# Wait 1.5s of silence \(default 700ms\)*

\}\)

**12.22.6**

**Timing Issues**

386

12. Appendix

**12.22.6.1 Caller Waits Too Long**

**Symptom**: Long delays before AI responds. 

**Solutions**:

*\#\# Use fillers*

@agent.tool\(

description**=**"Long operation", 

fillers**=**\["One moment please..."\]

\)

**def **long\_operation\(\) **-> **SwaigFunctionResult:

**pass**

**12.22.6.2 Call Disconnects Unexpectedly**

**Symptom**: Call ends without explicit hangup. 

**Check inactivity timeout**:

agent.set\_params\(\{

"inactivity\_timeout": 300000

*\# 5 minutes \(default 10 minutes\)*

\}\)

**12.22.7**

**DataMap Issues**

**12.22.7.1**

**Variable Not Substituting**

**Symptom**: $\{args.param\} appears literally in output. 

**Check**: Parameter name matches

data\_map.add\_parameter\("city", "string", "City name", required**=**True\)

*\#\# URL must use same name*

data\_map.add\_webhook\(

url**=**"https://api.example.com?q=$\{enc:args.city\}", 

*\# "city" matches*

... 

\)

**12.22.8**

**Variable Syntax Reference**

**Pattern**

**Usage**

$\{args.param\}

Function argument

$\{enc:args.param\}

URL-encoded argument \(use in URLs\)

$\{response.field\}

API response field

$\{global\_data.key\}

Global session data

**12.22.9**

**Skill Issues**

**12.22.9.1**

**Skill Not Loading**

**Symptom**: Skill added but functions not available. 

**Check 1**: Skill name is correct

*\#\# List available skills*

print\(agent.list\_available\_skills\(\)\)

*\#\# Add by exact name*

387

12. Appendix

agent.add\_skill\("datetime"\)

agent.add\_skill\("native\_vector\_search"\)

**Check 2**: Dependencies installed

*\#\# Some skills require additional packages*

pip install signalwire-agents *\[* search *\]*

**12.22.10**

**Serverless Issues**

**12.22.10.1 Lambda Function Errors**

**Check 1**: Handler configuration

*\#\# handler.py*

from my\_agent import agent

**def **handler\(event, context\):

**return **agent.serverless\_handler\(event, context\)

**Check 2**: Lambda timeout

Set Lambda timeout to at least 30 seconds for function processing. 

**12.22.11**

**Common Error Messages**

**Error**

**Solution**

“Address already in use” 

Change port or stop existing process

“Module not found” 

pip install signalwire-agents

“401 Unauthorized” 

Check basic\_auth credentials

“Connection refused” 

Ensure agent is running

“Function not found” 

Check function name and decorator

“Invalid SWML” 

Use swaig-test --dump-swml to debug

“Timeout” 

Add fillers or optimize function

**12.22.12**

**Getting Help**

If issues persist:

1. Check SignalWire documentation

2. Review SDK examples in /examples directory

3. Use swaig-test for diagnostics

4. Check SignalWire community forums

388

12. Appendix

**12.23**

**Migration Guide**

**Summary**: Guide for migrating to the SignalWire Agents SDK and common migration patterns. 

**12.23.1 Current Version**

**SDK Version**

**Python**

**SignalWire API**

**Status**

1.0.x

3.8\+

v1

Current stable release

**12.23.2**

**Before Upgrading**

1. **Review changelog **for breaking changes

2. **Backup your code **before upgrading

3. **Test in development **before production

4. **Check dependency compatibility**

*\#\# Check current version*

pip show signalwire-agents

*\#\# View available versions*

pip index versions signalwire-agents

**12.23.3**

**Upgrading**

*\#\# Upgrade to latest*

pip install --upgrade signalwire-agents

*\#\# Upgrade to specific version*

pip install signalwire-agents==1.0.2

*\#\# Upgrade with all extras*

pip install --upgrade "signalwire-agents\[search-all\]" 

**12.23.4**

**Migration from Raw SWML**

If migrating from hand-written SWML to the SDK:

**12.23.4.1**

**Before \(Raw SWML\)**

**\{**

"version" **: **"1.0.0" **, **

"sections" **: \{**

"main" **: **\[**\{**

"ai" **: \{**

"prompt" **: \{**

"text" **: **"You are a helpful assistant." 

**\}, **

"languages" **: **\[**\{**

"name" **: **"English" **, **

"code" **: **"en-US" **, **

"voice" **: **"rime.spore" 

**\}**\]**, **

"SWAIG" **: \{**

"functions" **: **\[**\{**

"function" **: **"lookup" **, **

"description" **: **"Look up information" **, **

"parameters" **: \{**

"type" **: **"object" **, **

"properties" **: \{**

"id" **: \{**

"type" **: **"string" **, **

389

12. Appendix

"description" **: **"Item ID" 

**\}**

**\}, **

"required" **: **\["id"\]

**\}, **

"web\_hook\_url" **: **"https://example.com/webhook" 

**\}**\]

**\}**

**\}**

**\}**\]

**\}**

**\}**

**12.23.4.2 After \(SDK\)**

from signalwire\_agents import AgentBase

from signalwire\_agents.core.function\_result import SwaigFunctionResult agent **= **AgentBase\(name**=**"assistant", route**=**"/"\) agent.prompt\_add\_section\("Role", "You are a helpful assistant."\) agent.add\_language\("English", "en-US", "rime.spore"\)

@agent.tool\(description**=**"Look up information"\)

**def **lookup\(id: str\) **-> **SwaigFunctionResult:

*\# Your logic here*

**return **SwaigFunctionResult\(f"Found item **\{**id**\}**"\) **if **\_\_name\_\_ **== **"\_\_main\_\_":

agent.run\(\)

**12.23.5**

**Common Migration Tasks**

**Old Style**

**New Style**

JSON parameter schema

Python type hints

Manual webhook handler

@agent.tool decorator

Return JSON dict

Return SwaigFunctionResult

Manual response parsing

Automatic parameter injection

**12.23.6**

**Class-Based Migration**

If migrating from functional to class-based agents:

**12.23.6.1**

**Before \(Functional\)**

from signalwire\_agents import AgentBase

from signalwire\_agents.core.function\_result import SwaigFunctionResult agent **= **AgentBase\(name**=**"service", route**=**"/service"\) agent.prompt\_add\_section\("Role", "Customer service agent."\) agent.add\_language\("English", "en-US", "rime.spore"\)

@agent.tool\(description**=**"Get account balance"\)

**def **get\_balance\(account\_id: str\) **-> **SwaigFunctionResult: balance **= **lookup\_balance\(account\_id\)

**return **SwaigFunctionResult\(f"Balance: $**\{**balance**\}**"\) **if **\_\_name\_\_ **== **"\_\_main\_\_":

agent.run\(\)

390

12. Appendix

**12.23.6.2 After \(Class-Based\)**

from signalwire\_agents import AgentBase

from signalwire\_agents.core.function\_result import SwaigFunctionResult **class **ServiceAgent\(AgentBase\):

**def \_\_init\_\_**\(self\):

super\(\). **\_\_init\_\_**\(name**=**"service", route**=**"/service"\) self.prompt\_add\_section\("Role", "Customer service agent."\) self.add\_language\("English", "en-US", "rime.spore"\)

@AgentBase.tool\(description**=**"Get account balance"\) **def **get\_balance\(self, account\_id: str\) **-> **SwaigFunctionResult: balance **= **self.lookup\_balance\(account\_id\)

**return **SwaigFunctionResult\(f"Balance: $**\{**balance**\}**"\) **def **lookup\_balance\(self, account\_id: str\) **-> **float:

*\# Your lookup logic*

**return **100.00

**if **\_\_name\_\_ **== **"\_\_main\_\_":

agent **= **ServiceAgent\(\)

agent.run\(\)

**12.23.7**

**Multi-Agent Migration**

If migrating multiple agents to use AgentServer:

**12.23.7.1**

**Before \(Separate Processes\)**

*\#\# Running separate agent processes*

python sales\_agent.py **& **

python support\_agent.py **& **

python billing\_agent.py **& **

**12.23.7.2**

**After \(AgentServer\)**

from signalwire\_agents import AgentServer

from sales\_agent import SalesAgent

from support\_agent import SupportAgent

from billing\_agent import BillingAgent

server **= **AgentServer\(host**=**"0.0.0.0", port**=**8080\) server.register\(SalesAgent\(\)\)

server.register\(SupportAgent\(\)\)

server.register\(BillingAgent\(\)\)

**if **\_\_name\_\_ **== **"\_\_main\_\_":

server.run\(\)

**12.23.8**

**Testing After Migration**

*\#\# Verify SWML generation*

swaig-test agent.py --dump-swml

*\#\# Compare with expected output*

swaig-test agent.py --dump-swml **> **new\_swml.json

**diff **old\_swml.json new\_swml.json

*\#\# Test all functions*

swaig-test agent.py --list-tools

swaig-test agent.py --exec function\_name --param value

391

12. Appendix

*\#\# Run integration tests*

pytest tests/

**12.23.9 Getting Help**

For migration assistance:

1. Check the changelog for breaking changes

2. Review updated examples in /examples

3. Use swaig-test to validate changes

4. Test thoroughly in development

392

12. Appendix

**12.24**

**Changelog**

**Summary**: Version history and release notes for the SignalWire Agents SDK. 

**12.24.1 Version History**

**Version**

**Date**

**Type**

**Highlights**

1.0.2

2025

Patch

Added serve\_static\_files\(\)

to AgentServer

1.0.1

2025

Patch

Minor fixes to included

examples

1.0.0

2025

Initial

First public release

**12.24.2**

**Version 1.0.2**

**Patch Release**

Added serve\_static\_files\(\) method to AgentServer for properly serving static files alongside agents. 

**12.24.2.1 Changes**

**Area**

**Change**

AgentServer

Added serve\_static\_files\(directory, route\) method

AgentServer

Static files now correctly fall back after agent routes

AgentServer

Both /route and /route/ now work for agent endpoints

**12.24.3**

**Version 1.0.1**

**Patch Release**

Minor fixes to included examples for better compatibility with the swaig-test CLI tool. 

**12.24.3.1**

**Changes**

**Area**

**Change**

Examples

Fixed deprecated API calls in swml\_service\_routing\_example.py

Examples

Added error handling for remote search in sigmond\_remote\_search.py Examples

Fixed argparse conflicts with swaig-test in several examples

Examples

Updated examples to return agents from main\(\) for testing

**12.24.4**

**Version 1.0.0**

**Initial Release**

The first public release of the SignalWire Agents SDK, providing a comprehensive Python framework for building AI voice agents. 

393

12. Appendix

**12.24.4.1 Core Features**

**Feature**

**Description**

AgentBase

Base class for all voice AI agents

SWAIG Functions

Define callable functions with @agent.tool

SwaigFunctionResult

Chainable response builder with actions

DataMap

Serverless REST API integration

Skills System

Auto-discovered plugin architecture

Prefabs

Pre-built agent archetypes

Contexts

Multi-step conversation workflows

AgentServer

Host multiple agents on one server

**12.24.4.2 Built-in Skills**

• **datetime**: Current time and date information

• **native\_vector\_search**: Local document search

• **web\_search**: Web search integration

• **math**: Mathematical calculations

• **datasphere**: SignalWire DataSphere integration

**12.24.4.3 Prefab Agents**

• **InfoGatherer**: Structured information collection

• **FAQBot**: Knowledge base Q&A

• **Survey**: Multi-question surveys

• **Receptionist**: Call routing

• **Concierge**: Restaurant/service booking

**12.24.4.4**

**CLI Tools**

• **swaig-test**: Test agents and functions locally

• **sw-search**: Build and query search indexes

**12.24.4.5**

**Deployment Support**

• Local development server

• AWS Lambda

• Google Cloud Functions

• Azure Functions

• CGI mode

• Docker/Kubernetes

**12.24.5**

**Versioning Policy**

The SDK follows Semantic Versioning: **Version Component**

**Meaning**

MAJOR \(1.x.x\)

Breaking changes requiring code updates

MINOR \(x.1.x\)

New features, backwards compatible

PATCH \(x.x.1\)

Bug fixes, backwards compatible

394

12. Appendix

**12.24.6 Upgrade Notifications**

To stay informed about new releases:

1. Watch the GitHub repository

2. Subscribe to release notifications

3. Check pip show signalwire-agents for current version

4. Use pip install --upgrade signalwire-agents to update

**12.24.7 Reporting Issues**

To report bugs or request features:

1. Check existing GitHub issues

2. Create a new issue with:

• SDK version \(pip show signalwire-agents\)

• Python version \(python --version\)

• Minimal reproduction code

• Expected vs actual behavior

**12.24.8**

**Contributing**

Contributions are welcome\! See the repository’s CONTRIBUTING.md for guidelines. 

**This concludes the SignalWire Agents SDK documentation. **

395



# Document Outline

+ Getting Started  
	+ What You’ll Learn 
	+ Prerequisites 
	+ Time to Complete 
	+ By the End of This Chapter 
	+ What is the SignalWire Agents SDK?  
	+ How It Works 
	+ Key Concepts 
	+ What You Can Build 
	+ SDK Features 
	+ Minimal Example 
	+ Next Steps 
	+ Installation 
	+ Quick Start: Your First Agent 
	+ Development Environment Setup 
	+ Exposing Your Agent to the Internet 

+ Core Concepts  
	+ What You’ll Learn 
	+ Prerequisites 
	+ The Big Picture 
	+ Key Terminology 
	+ Chapter Contents 
	+ Why These Concepts Matter 
	+ The Mixin Composition Pattern 
	+ Each Mixin’s Role 
	+ Key Internal Components 
	+ Creating Your Own Agent 
	+ Benefits of This Architecture 
	+ Next Steps 
	+ SWML \(SignalWire Markup Language\) 
	+ SWAIG \(SignalWire AI Gateway\) 
	+ Request Lifecycle 
	+ Security 

+ Building Agents  
	+ What You’ll Learn 
	+ Prerequisites 
	+ Agent Architecture Overview 
	+ A Complete Agent Example 
	+ Chapter Contents 
	+ Key Patterns 
	+ Testing Your Agent 
	+ Class Overview 
	+ Constructor Parameters 
	+ Parameter Reference 
	+ Creating an Agent 
	+ Key Methods 
	+ Agent Lifecycle 
	+ Configuration File 
	+ Environment Variables 
	+ Multi-Agent Server 
	+ Best Practices 
	+ Static vs Dynamic Agents 
	+ Prompts & POM 
	+ Voice & Language 
	+ AI Parameters 
	+ Hints 

+ SWAIG Functions  
	+ What You’ll Learn 
	+ How SWAIG Functions Work 
	+ Quick Start Example 
	+ Function Types 
	+ Chapter Contents 
	+ When to Use SWAIG Functions 
	+ Key Concepts 
	+ Basic Function Definition 
	+ The define\_tool\(\) Method 
	+ Handler Function Signature 
	+ Accessing Call Data 
	+ Multiple Functions 
	+ Function Fillers 
	+ The @tool Decorator 
	+ External Webhook Functions 
	+ Function Security 
	+ Writing Good Descriptions 
	+ Testing Functions 
	+ Complete Example 
	+ Parameters 
	+ Results & Actions 
	+ DataMap 
	+ Native Functions 

+ Skills  
	+ What You’ll Learn 
	+ What Are Skills?  
	+ Quick Start 
	+ Available Built-in Skills 
	+ Chapter Contents 
	+ Skills vs Functions 
	+ When to Use Skills 
	+ Complete Example 
	+ Skill Architecture 
	+ How Skills Work 
	+ Skill Directory Structure 
	+ SkillBase Class 
	+ Skill Lifecycle 
	+ Skill Contributions 
	+ Skill Discovery Paths 
	+ Lazy Loading 
	+ Multi-Instance Skills 
	+ Built-in Skills 
	+ Adding Skills 
	+ Custom Skills 
	+ Skill Configuration 

+ Advanced Features  
	+ What You’ll Learn 
	+ Feature Overview 
	+ When to Use These Features 
	+ Prerequisites 
	+ Chapter Contents 
	+ When to Use Contexts 
	+ Context Architecture 
	+ Basic Context Example 
	+ Step Configuration 
	+ Context Configuration 
	+ Multi-Context Example 
	+ Navigation Flow 
	+ Validation Rules 
	+ Step and Context Methods Summary 
	+ Best Practices 
	+ State Management 
	+ Call Recording 
	+ Call Transfer 
	+ Multi-Agent Servers 
	+ Search & Knowledge 

+ Deployment  
	+ What You’ll Learn 
	+ Deployment Options Overview 
	+ Environment Detection 
	+ Chapter Contents 
	+ Quick Start 
	+ Starting the Development Server 
	+ Server Configuration 
	+ Development Endpoints 
	+ Testing Your Agent 
	+ Exposing Local Server 
	+ Environment Variables for Development 
	+ Proxy URL Configuration 
	+ Development Workflow 
	+ Debug Mode 
	+ Hot Reloading 
	+ Serving Static Files 
	+ Common Development Issues 
	+ Production Deployment 
	+ Serverless Deployment 
	+ Docker & Kubernetes 
	+ CGI Mode 

+ SignalWire Integration  
	+ What You’ll Learn 
	+ Integration Overview 
	+ Prerequisites 
	+ Chapter Contents 
	+ Quick Integration Steps 
	+ Architecture 
	+ Required URLs 
	+ Security Considerations 
	+ Create Account 
	+ Create a Project 
	+ Space Name 
	+ API Credentials 
	+ Environment Variables 
	+ Dashboard Overview 
	+ Add Credit 
	+ Account Verification 
	+ Next Steps 
	+ Phone Numbers 
	+ Mapping Numbers 
	+ Testing 
	+ Troubleshooting 

+ Prefab Agents  
	+ What Are Prefabs?  
	+ Why Use Prefabs?  
	+ Quick Examples 
	+ Chapter Contents 
	+ Importing Prefabs 
	+ Extending Prefabs 
	+ Basic Usage 
	+ Question Format 
	+ Constructor Parameters 
	+ Flow Diagram 
	+ Built-in Functions 
	+ Dynamic Questions 
	+ Accessing Collected Data 
	+ Complete Example 
	+ Best Practices 
	+ FAQBot 
	+ Survey 
	+ Receptionist 
	+ Concierge 

+ Reference  
	+ Reference Overview 
	+ Quick Reference 
	+ Import Patterns 
	+ Chapter Contents 
	+ Class Definition 
	+ Constructor 
	+ Constructor Parameters 
	+ Prompt Methods 
	+ Language and Voice Methods 
	+ Tool Definition Methods 
	+ Skill Methods 
	+ AI Configuration Methods 
	+ State Methods 
	+ URL Methods 
	+ Server Methods 
	+ Serverless Methods 
	+ Callback Methods 
	+ SIP Routing Methods 
	+ Method Chaining 
	+ Class Attributes 
	+ SWMLService API 
	+ SWAIG Function API 
	+ SwaigFunctionResult API 
	+ DataMap API 
	+ SkillBase API 
	+ ContextBuilder API 
	+ swaig-test CLI 
	+ sw-search CLI 
	+ Environment Variables 
	+ Config Files 
	+ SWML Schema 

+ Examples  
	+ How to Use This Chapter 
	+ Example Categories 
	+ Quick Start Examples 
	+ Running Examples 
	+ Example Structure 
	+ Chapter Contents 
	+ Basic Agent Setup 
	+ SWAIG Functions 
	+ DataMap Integration 
	+ Call Transfers 
	+ Skills Usage 
	+ Global Data 
	+ Recording 
	+ SMS Notifications 
	+ Static Files with AgentServer 
	+ Hints and Pronunciation 
	+ Examples by Complexity 

+ Appendix  
	+ About This Chapter 
	+ Quick Reference 
	+ Chapter Contents 
	+ Overview 
	+ Setting Parameters in Python 
	+ LLM API Parameters 
	+ ASR \(Speech Recognition\) Parameters 
	+ Timing Parameters 
	+ Behavior Parameters 
	+ SWAIG Control Parameters 
	+ Interrupt Parameters 
	+ Audio Parameters 
	+ Video Parameters 
	+ String Parameters 
	+ VAD Configuration 
	+ Post-Prompt Parameter Defaults 
	+ Model-Specific Overrides 
	+ Complete Example 
	+ SWML Example 
	+ Design Patterns 
	+ Best Practices 
	+ Troubleshooting 
	+ Migration Guide 
	+ Changelog



