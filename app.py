import os
import json
import time
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# =====================================================================
# INDEPENDENT AGENT ARCHITECTURES (The Specialized Worker Modules)
# =====================================================================

class MarketAnalystAgent:
    """Agent responsible for scanning trends, finding angles, and establishing audience personas."""
    def run(self, product_name, description):
        time.sleep(0.4)  # Simulate computing / reasoning latency
        
        # Simple dynamic keyword extractor based on user input terms
        keywords = ["Digital Transformation", "Eco-Friendly", "Automated Efficiency", "Lifestyle Upgrade"]
        if "coffee" in description.lower() or "brew" in product_name.lower():
            keywords = ["Organic Caffeine", "Sustainable Sourcing", "Morning Routine", "Artisanal Roasts"]
        elif "tech" in description.lower() or "app" in description.lower():
            keywords = ["SaaS Automation", "UI/UX Optimization", "Productivity Hack", "Cloud Scaling"]

        return {
            "agent_name": "MarketAnalystAgent v1.2",
            "target_demographic": "Young Professionals & Trendconscious Consumers (Ages 22-40)",
            "strategic_positioning": f"Positioning '{product_name}' as a premium, modern solution addressing everyday friction points.",
            "seo_keywords": keywords
        }

class CopywriterAgent:
    """Agent engineered to generate creative narrative copy adapted across communication channels."""
    def run(self, product_name, description, keywords):
        time.sleep(0.5)  # Simulate processing latency
        kw_tags = " ".join([f"#{w.replace(' ', '')}" for w in keywords])
        
        return {
            "agent_name": "CopywriterAgent v2.0",
            "instagram": f"🌟 Elevate your day with {product_name}! {description}. Designed for those who refuse to settle for ordinary. Tap the link in our bio to explore the future. {kw_tags} #Innovation #Premium",
            "twitter_x": f"Say hello to {product_name}. 👋 ✨\n\n{description[:100]}...\n\n🚀 The game-changer you've been waiting for is officially here. Thread below 👇 {kw_tags}",
            "linkedin": f"📊 Innovation Spotlight: Announcing {product_name}.\n\nWe are proud to introduce a new standard in the industry. By focusing directly on '{description}', our team has engineered a solution that scales efficiency while maintaining unmatched quality.\n\nRead our full launch whitepaper here: https://lnkd.in/example\n\n#BusinessStrategy {kw_tags}"
        }

class DesignPromptAgent:
    """Agent designed to translate core business ideas into hyper-detailed generative text-to-image prompts."""
    def run(self, product_name, description):
        time.sleep(0.3)
        return {
            "agent_name": "DesignPromptAgent v0.9",
            "hero_image_prompt": f"A high-end, commercial product photography shot of {product_name}. Modern cinematic studio lighting, clean minimalist geometric background, subtle accent highlights, 8k resolution, shot on 85mm lens, photorealistic, showcasing themes of: {description[:50]}.",
            "color_palette": ["#1E3A8A (Deep Trust Blue)", "#10B981 (Growth Emerald)", "#F59E0B (Energy Amber)"]
        }


# =====================================================================
# THE CENTRAL ORCHESTRATOR
# =====================================================================
class MarketingCampaignOrchestrator:
    def __init__(self):
        self.analyst = MarketAnalystAgent()
        self.writer = CopywriterAgent()
        self.designer = DesignPromptAgent()

    def construct_campaign(self, product_name, description):
        # Step 1: Market Analyst creates the conceptual foundation
        analysis_output = self.analyst.run(product_name, description)
        
        # Step 2: Pass insights from Analyst into the Copywriter
        copy_output = self.writer.run(
            product_name, 
            description, 
            analysis_output["seo_keywords"]
        )
        
        # Step 3: Designer Agent constructs visual aesthetic prompts
        design_output = self.designer.run(product_name, description)
        
        # Step 4: System synthesis - Compile isolated payloads into an integrated campaign matrix
        master_payload = {
            "metadata": {
                "system_status": "Success",
                "orchestrator_version": "AgenticCore-v4",
                "campaign_id": "CMP-" + str(int(time.time()))[-6:]
            },
            "campaign_goals": {
                "product": product_name.title(),
                "concept": description
            },
            "analyst_insights": analysis_output,
            "copywriting_deliverables": copy_output,
            "design_assets": design_output
        }
        return master_payload


# =====================================================================
# WEB APPLICATION CONTROLLER ROUTES
# =====================================================================
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/generate', methods=['POST'])
def generate_campaign_api():
    request_data = request.json
    
    product_name = request_data.get('product_name', '').strip()
    description = request_data.get('description', '').strip()
    
    if not product_name or not description:
        return jsonify({"error": "Missing required fields"}), 400
        
    # Launch execution sequence
    orchestrator = MarketingCampaignOrchestrator()
    campaign_result = orchestrator.construct_campaign(product_name, description)
    
    return jsonify(campaign_result)

if __name__ == '__main__':
    app.run(debug=True, port=5000)