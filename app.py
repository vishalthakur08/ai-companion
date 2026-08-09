import streamlit as st

from ai.prompts import generate_layout_prompt
from ai.blueprint_prompt import generate_blueprint_prompt
from ai.llm import generate_response

# ---------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------

st.set_page_config(
    page_title="Design Companion AI",
    page_icon="✨",
    layout="wide",
)

# ---------------------------------------------------
# CUSTOM CSS
# ---------------------------------------------------

st.markdown(
    """
<style>

.main > div{
    padding-top:2rem;
}

    position:sticky;
    top:1rem;
}

.block-container{
    max-width:1400px;
}

div[data-testid="stVerticalBlockBorderWrapper"]{
    border-radius:14px;
}

</style>
""",
    unsafe_allow_html=True,
)

# ---------------------------------------------------
# SESSION STATE
# ---------------------------------------------------

if "ai_response" not in st.session_state:
    st.session_state.ai_response = None

if "selected_strategy" not in st.session_state:
    st.session_state.selected_strategy = None

if "blueprint" not in st.session_state:
    st.session_state.blueprint = None

# ---------------------------------------------------
# NAVBAR
# ---------------------------------------------------

nav_left, nav_right = st.columns([8, 2])

with nav_left:
    st.markdown("## 🟢 AI Design Companion")

with nav_right:
    st.markdown("<div style='text-align:right;padding-top:10px;color:#6b7280;font-size:14px;'>Careem Design Assignment</div>", unsafe_allow_html=True)

st.divider()

# ---------------------------------------------------
# HERO
# ---------------------------------------------------


# ---------------------------------------------------
# PROJECT DETAILS
# ---------------------------------------------------

st.markdown("## Project Details")

form_col_left, form_col_center, form_col_right = st.columns([1, 2, 1])

with form_col_center:

    st.subheader("📝 Project Details")

    screen_name = st.text_input(
        "Screen Name",
        placeholder="Order Tracking",
    )

    description = st.text_area(
        "Screen Description",
        placeholder="Track a customer's multi-stop ride in real time.",
        height=180,
    )

    user_type = st.selectbox(
        "Primary User",
        [
            "Customer",
            "Admin",
            "Manager",
            "Driver",
            "Operator",
            "Guest",
        ],
    )

    platform = st.selectbox(
        "Platform",
        [
            "Mobile",
            "Desktop",
            "Tablet",
            "TV",
        ],
    )

    region = st.selectbox(
        "Region",
        [
            "Global",
            "India",
            "USA",
            "Europe",
            "Middle East",
        ],
    )

    generate = st.button(
        "✨ Generate Layout Strategies",
        use_container_width=True,
    )

    st.markdown("<br><br>", unsafe_allow_html=True)

if st.session_state.ai_response:

    st.subheader("🧠 AI Workspace")

    # ---------------------------------------------------
    # AI DESIGN ANALYSIS
    # ---------------------------------------------------

    if st.session_state.ai_response:

        response = st.session_state.ai_response

        summary = response.get("problem_summary", {})
        priorities = response.get("design_priorities", [])
        risks = response.get("ux_risks", [])
        opportunities = response.get("design_opportunities", [])

        with st.container(border=True):

            st.markdown("## 🧠 AI Design Analysis")

            st.markdown(f"**🎯 Screen Goal**  \n{summary.get('screen_goal','')}")

            st.markdown(f"**👤 Primary User Goal**  \n{summary.get('primary_user_goal','')}")

            st.markdown(f"**🏢 Business Goal**  \n{summary.get('business_goal','')}")

            st.markdown(f"**🧠 Mental Model**  \n{summary.get('mental_model','')}")

            st.markdown(f"**⚠️ Key Design Challenge**  \n{summary.get('key_design_challenge','')}")

        # ---------------------------------------

        col1, col2, col3 = st.columns(3)

        with col1:

            with st.container(border=True):

                st.markdown("### 🎯 Design Priorities")

                for item in priorities:
                    st.markdown(f"- {item}")

        with col2:

            with st.container(border=True):

                st.markdown("### ⚠️ UX Risks")

                for item in risks:
                    st.markdown(f"- {item}")

        with col3:

            with st.container(border=True):

                st.markdown("### 💡 Design Opportunities")

                for item in opportunities:
                    st.markdown(f"- {item}")

        st.divider()

        st.subheader("📐 Layout Strategies")

        directions = response.get("layout_directions", [])

        cols = st.columns(3)

        for index, direction in enumerate(directions):

            with cols[index]:

                with st.container(border=True):

                    st.markdown(f"## {direction.get('name','')}")

                    st.caption(direction.get("tagline",""))

                    st.write(direction.get("description",""))

                    st.markdown("### ✅ Best For")

                    for item in direction.get("best_for", []):
                        st.markdown(f"- {item}")

                    st.markdown("### 🧭 Information Hierarchy")

                    for item in direction.get("information_hierarchy", []):
                        st.markdown(f"- {item}")

                    if st.button(
                        "🚀 Explore Strategy",
                        key=f"strategy_{index}",
                        use_container_width=True,
                    ):

                        st.session_state.selected_strategy = direction
                        st.session_state.blueprint = None

    # ---------------------------------------------------
    # SELECTED STRATEGY
    # ---------------------------------------------------

    if st.session_state.selected_strategy:

        strategy = st.session_state.selected_strategy

        st.divider()

        with st.container(border=True):

            st.subheader("🚀 Selected Strategy")

            st.markdown(f"## {strategy.get('name','')}")

            st.caption(strategy.get("tagline",""))

            st.write(strategy.get("description",""))

            st.markdown("### 💭 Why this strategy?")

            st.write(strategy.get("reasoning",""))

            st.markdown("### ⚖️ Trade-offs")

            st.write(strategy.get("tradeoffs",""))

            st.markdown("### 🧭 Information Hierarchy")

            for item in strategy.get("information_hierarchy", []):

                st.markdown(f"- {item}")

            if st.button(
                "✨ Generate UX Blueprint",
                use_container_width=True,
            ):

                with st.spinner("Generating UX Blueprint..."):

                    prompt = generate_blueprint_prompt(
                        screen_name,
                        description,
                        strategy["name"],
                    )

                    blueprint = generate_response(prompt)

                    st.session_state.blueprint = blueprint

    # --------------------------------------------
    # UX BLUEPRINT
    # --------------------------------------------

    if st.session_state.blueprint:

        blueprint = st.session_state.blueprint.get("blueprint", {})

        st.divider()

        with st.container(border=True):

            st.subheader("✨ UX Blueprint")

            st.markdown("### Overview")
            st.write(blueprint.get("overview", ""))

            st.markdown("### 📍 Above the Fold")

            for item in blueprint.get("above_the_fold", []):
                st.markdown(f"- {item}")

            st.markdown("### 🧩 Screen Sections")

            for section in blueprint.get("screen_sections", []):

                st.markdown(f"**{section.get('section','')}**")

                st.caption(section.get("purpose",""))

            st.markdown("### 🎯 Primary Actions")

            for item in blueprint.get("primary_actions", []):

                st.markdown(f"- {item}")

            st.markdown("### ➕ Secondary Actions")

            for item in blueprint.get("secondary_actions", []):

                st.markdown(f"- {item}")

            edge = blueprint.get("edge_cases", {})

            st.markdown("### ⚠️ Edge Cases")

            st.markdown(f"**Loading:** {edge.get('loading','')}")

            st.markdown(f"**Empty:** {edge.get('empty','')}")

            st.markdown(f"**Offline:** {edge.get('offline','')}")

            st.markdown(f"**Error:** {edge.get('error','')}")

            st.markdown("### ♿ Accessibility")

            for item in blueprint.get("accessibility", []):

                st.markdown(f"- {item}")

            st.markdown("### ✅ UX Checklist")

            for item in blueprint.get("ux_checklist", []):

                st.markdown(f"- {item}")

        # --------------------------------------------
        # DOWNLOAD MARKDOWN
        # --------------------------------------------

        markdown = f"""
# {screen_name}

## Problem Summary

{st.session_state.ai_response["problem_summary"]["screen_goal"]}

## Design Priorities

"""

        markdown += "\n".join(
            [
                f"- {item}"
                for item in st.session_state.ai_response.get(
                    "design_priorities",
                    [],
                )
            ]
        )

        markdown += "\n\n## UX Risks\n"

        markdown += "\n".join(
            [
                f"- {item}"
                for item in st.session_state.ai_response.get(
                    "ux_risks",
                    [],
                )
            ]
        )

        markdown += "\n\n## Design Opportunities\n"

        markdown += "\n".join(
            [
                f"- {item}"
                for item in st.session_state.ai_response.get(
                    "design_opportunities",
                    [],
                )
            ]
        )

        markdown += f"""

## Selected Strategy

{strategy["name"]}

{strategy["description"]}

## UX Blueprint

{blueprint.get("overview","")}
"""

        st.download_button(
            "📄 Download Design Brief",
            markdown,
            file_name="design-brief.md",
            mime="text/markdown",
            use_container_width=True,
        )

# ---------------------------------------------------
# GENERATE BUTTON
# ---------------------------------------------------

if generate:

    if not screen_name:

        st.warning("Please enter a screen name.")

        st.stop()

    if not description:

        st.warning("Please enter a description.")

        st.stop()

    progress = st.progress(0)

    status = st.empty()

    status.write("🧠 Understanding your problem...")

    progress.progress(20)

    prompt = generate_layout_prompt(
        screen_name,
        description,
        user_type,
        platform,
        region,
    )

    status.write("🎯 Identifying UX priorities...")

    progress.progress(40)

    response = generate_response(prompt)

    status.write("💡 Preparing recommendations...")

    progress.progress(80)

    st.session_state.ai_response = response

    st.session_state.selected_strategy = None

    st.session_state.blueprint = None

    progress.progress(100)

    status.success("✅ AI recommendations ready!")

    st.rerun()
