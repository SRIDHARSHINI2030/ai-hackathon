from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
from moviepy import ImageClip, concatenate_videoclips
import asyncio
import edge_tts
import textwrap
def build_video_script(lesson_plan):
    """
    Convert the backend lesson plan into a video script.

    The lesson plan is expected to contain:
    topic, learner level, language, and lesson steps.
    """

    topic = lesson_plan.get("topic", "the topic")
    learner_level = lesson_plan.get("learner_level", "beginner")
    language = lesson_plan.get("language", "English")
    lesson_steps = lesson_plan.get("lesson_steps", [])

    script = []

    for step in lesson_steps:
        if step == "Introduction":
            script.append({
                "section": "Introduction",
                "spoken_text": (
                    f"Hello! Today we are going to learn about {topic}. "
                    f"I will explain it at a {learner_level} level."
                ),
                "visual": f"Title screen showing: {topic}"
            })

        elif step == "Concept explanation":
            script.append({
                "section": "Concept explanation",
                "spoken_text": (
                    f"Let's understand {topic} step by step. "
                    f"{lesson_plan.get('concept_explanation', f'We will explore the key ideas of {topic} in detail.')}"
                    ),
            })


        elif step == "Example or demonstration":
            script.append({
                "section": "Example or demonstration",
                "spoken_text": (
                    f"Let's look at an example to understand {topic} better."
                ),
                "visual": "Example or subject-specific demonstration"
            })

        elif step == "Questions for the learner":
            script.append({
                "section": "Questions for the learner",
                "spoken_text": (
                    "Now, let me ask you a question to check your understanding."
                ),
                "visual": "Question displayed on screen"
            })

        elif step == "Understanding check":
            script.append({
                "section": "Understanding check",
                "spoken_text": (
                    "Let's check what you have understood so far."
                ),
                "visual": "Understanding check displayed on screen"
            })

        elif step == "Conclusion":
            script.append({
                "section": "Conclusion",
                "spoken_text": (
                    f"Great! Let's quickly review what we learned about {topic}."
                ),
                "visual": f"Summary of {topic}"
            })

    return {
        "topic": topic,
        "language": language,
        "segments": script
    }

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont
from moviepy import ImageClip, concatenate_videoclips


def create_slide(title, text, output_path):
    width, height = 1280, 720

    image = Image.new("RGB", (width, height), "#F5F7FB")
    draw = ImageDraw.Draw(image)

    try:
        title_font = ImageFont.truetype(
            "C:/Windows/Fonts/arialbd.ttf", 48
        )
        body_font = ImageFont.truetype(
            "C:/Windows/Fonts/arial.ttf", 30
        )
        small_font = ImageFont.truetype(
            "C:/Windows/Fonts/arial.ttf", 22
        )
        big_font = ImageFont.truetype(
            "C:/Windows/Fonts/arialbd.ttf", 34
        )
    except:
        title_font = ImageFont.load_default()
        body_font = ImageFont.load_default()
        small_font = ImageFont.load_default()
        big_font = ImageFont.load_default()

    # Header
    draw.rectangle(
        (0, 0, width, 135),
        fill="#173F5F"
    )

    draw.text(
        (65, 38),
        title,
        fill="white",
        font=title_font
    )

    # Main card
    draw.rounded_rectangle(
        (55, 165, 1225, 625),
        radius=28,
        fill="white",
        outline="#D5DEE8",
        width=2
    )

    # Separate narration and visual description
    if "\n\nVisual: " in text:
        main_text, visual = text.split(
            "\n\nVisual: ",
            1
        )
    else:
        main_text = text
        visual = ""

       # Lesson explanation
    wrapped_text = textwrap.fill(
        main_text,
        width=65
    )

    if title not in ["Concept explanation", "Example or demonstration"]:
        draw.multiline_text(
        (90, 205),
            wrapped_text,
            fill="#1F2937",
            font=body_font,
            spacing=12
        )

    if title == "Concept explanation":
        # Educational photosynthesis flow diagram

        # Sun
        draw.ellipse(
            (90, 250, 230, 390),
            fill="#F9C74F"
        )
        draw.text(
            (125, 295),
            "SUN",
            fill="#173F5F",
            font=small_font
        )

        # Sunlight arrows
        draw.line(
            (230, 320, 390, 320),
            fill="#F9C74F",
            width=10
        )
        draw.polygon(
            [(390, 320), (365, 305), (365, 335)],
            fill="#F9C74F"
        )

        draw.text(
            (250, 270),
            "Sunlight",
            fill="#173F5F",
            font=small_font
        )

        # Leaf
        draw.ellipse(
            (400, 250, 650, 400),
            fill="#90BE6D",
            outline="#173F5F",
            width=4
        )

        draw.line(
            (525, 280, 525, 370),
            fill="#173F5F",
            width=4
        )

        draw.text(
            (475, 310),
            "LEAF",
            fill="#173F5F",
            font=small_font
        )
        # Chloroplasts inside the leaf
        draw.ellipse(
            (430, 285, 465, 315),
            fill="#4F772D",
            outline="#173F5F",
            width=2
        )

        draw.ellipse(
            (480, 350, 515, 380),
            fill="#4F772D",
            outline="#173F5F",
            width=2
        )

        draw.ellipse(
            (535, 285, 570, 315),
            fill="#4F772D",
            outline="#173F5F",
            width=2
        )

        draw.ellipse(
            (575, 340, 610, 370),
            fill="#4F772D",
            outline="#173F5F",
            width=2
        )

        draw.text(
            (455, 225),
            "Chloroplasts",
            fill="#173F5F",
            font=small_font
        )

        # Carbon dioxide input
        draw.rounded_rectangle(
            (300, 450, 500, 520),
            radius=18,
            fill="#DCEEFF",
            outline="#173F5F",
            width=3
        )

        draw.text(
            (345, 470),
            "CO2",
            fill="#173F5F",
            font=small_font
        )

        draw.line(
            (400, 450, 475, 400),
            fill="#173F5F",
            width=5
        )
        draw.polygon(
            [(475, 400), (450, 402), (463, 425)],
            fill="#173F5F"
        )

        # Water input
        draw.rounded_rectangle(
            (550, 450, 750, 520),
            radius=18,
            fill="#DCEEFF",
            outline="#173F5F",
            width=3
        )

        draw.text(
            (625, 470),
            "H2O",
            fill="#173F5F",
            font=small_font
        )

        draw.line(
            (650, 450, 575, 400),
            fill="#173F5F",
            width=5
        )
        draw.polygon(
            [(575, 400), (587, 425), (600, 402)],
            fill="#173F5F"
        )

        # Photosynthesis process
        draw.rounded_rectangle(
            (800, 260, 1110, 390),
            radius=25,
            fill="#173F5F"
        )

        draw.text(
            (850, 300),
            "PHOTOSYNTHESIS",
            fill="white",
            font=small_font
        )

        draw.text(
            (875, 345),
            "Light energy is used",
            fill="white",
            font=small_font
        )

        # Arrow from leaf to process
        draw.line(
            (650, 325, 800, 325),
            fill="#173F5F",
            width=8
        )
        draw.polygon(
            [(800, 325), (770, 307), (770, 343)],
            fill="#173F5F"
        )

        # Glucose output
        draw.rounded_rectangle(
            (780, 470, 960, 540),
            radius=18,
            fill="#D8F3DC",
            outline="#173F5F",
            width=3
        )

        draw.text(
            (820, 490),
            "GLUCOSE",
            fill="#173F5F",
            font=small_font
        )

        # Oxygen output
        draw.rounded_rectangle(
            (990, 470, 1170, 540),
            radius=18,
            fill="#D8F3DC",
            outline="#173F5F",
            width=3
        )

        draw.text(
            (1040, 490),
            "O2",
            fill="#173F5F",
            font=small_font
        )

        # Output arrows
        draw.line(
            (900, 390, 870, 470),
            fill="#173F5F",
            width=5
        )
        draw.polygon(
            [(870, 470), (860, 445), (885, 452)],
            fill="#173F5F"
        )

        draw.line(
            (1010, 390, 1080, 470),
            fill="#173F5F",
            width=5
        )
        draw.polygon(
            [(1080, 470), (1055, 452), (1078, 445)],
            fill="#173F5F"
        )

        # Bottom explanation
        draw.text(
            (390, 590),
            "Sunlight + CO2 + H2O  →  Glucose + O2",
            fill="#173F5F",
            font=small_font
        )
    elif title == "Introduction":

        # Welcome visual
        draw.rounded_rectangle(
            (90, 390, 1190, 560),
            radius=20,
            fill="#EAF2F8"
        )

        draw.ellipse(
            (150, 410, 300, 560),
            fill="#FFD166"
        )

        draw.text(
            (190, 455),
            "Hi!",
            fill="#173F5F",
            font=big_font
        )

        draw.text(
            (350, 420),
            "Welcome to your lesson!",
            fill="#173F5F",
            font=big_font
        )

        draw.text(
            (350, 480),
            f"Today we are learning about {visual.replace('Title screen showing: ', '')}",
            fill="#475569",
            font=small_font
        )

    elif title == "Example or demonstration":
        # Real-world photosynthesis example

        # Sun
        draw.ellipse(
            (100, 250, 220, 370),
            fill="#F9C74F"
        )

        draw.text(
            (130, 295),
            "SUN",
            fill="#173F5F",
            font=small_font
        )

        # Sunlight arrow
        draw.line(
            (220, 310, 380, 310),
            fill="#F9C74F",
            width=9
        )

        draw.polygon(
            [(380, 310), (350, 292), (350, 328)],
            fill="#F9C74F"
        )

        draw.text(
            (260, 265),
            "Sunlight",
            fill="#173F5F",
            font=small_font
        )

        # Plant pot
        draw.polygon(
            [(500, 490), (700, 490), (670, 570), (530, 570)],
            fill="#C97A40",
            outline="#173F5F"
        )

        # Plant stem
        draw.line(
            (600, 490, 600, 340),
            fill="#4F772D",
            width=10
        )

        # Leaves
        draw.ellipse(
            (510, 330, 610, 390),
            fill="#90BE6D",
            outline="#173F5F",
            width=3
        )

        draw.ellipse(
            (590, 365, 690, 425),
            fill="#90BE6D",
            outline="#173F5F",
            width=3
        )

        draw.ellipse(
            (535, 390, 625, 445),
            fill="#90BE6D",
            outline="#173F5F",
            width=3
        )

        # CO2 entering
        draw.rounded_rectangle(
            (300, 430, 470, 500),
            radius=18,
            fill="#DCEEFF",
            outline="#173F5F",
            width=3
        )

        draw.text(
            (350, 450),
            "CO2",
            fill="#173F5F",
            font=small_font
        )

        draw.line(
            (470, 465, 535, 425),
            fill="#173F5F",
            width=5
        )

        draw.polygon(
            [(535, 425), (510, 420), (520, 445)],
            fill="#173F5F"
        )

        # Water entering
        draw.rounded_rectangle(
            (730, 430, 900, 500),
            radius=18,
            fill="#DCEEFF",
            outline="#173F5F",
            width=3
        )

        draw.text(
            (785, 450),
            "H2O",
            fill="#173F5F",
            font=small_font
        )

        draw.line(
            (730, 465, 675, 425),
            fill="#173F5F",
            width=5
        )

        draw.polygon(
            [(675, 425), (690, 445), (700, 420)],
            fill="#173F5F"
        )

        # Food produced
        draw.rounded_rectangle(
            (760, 270, 980, 350),
            radius=20,
            fill="#D8F3DC",
            outline="#173F5F",
            width=3
        )

        draw.text(
            (805, 292),
            "GLUCOSE",
            fill="#173F5F",
            font=small_font
        )

        draw.text(
            (790, 325),
            "Plant food",
            fill="#173F5F",
            font=small_font
        )

        draw.line(
            (690, 380, 760, 330),
            fill="#173F5F",
            width=5
        )

        draw.polygon(
            [(760, 330), (735, 330), (748, 350)],
            fill="#173F5F"
        )

        # Oxygen released
        draw.rounded_rectangle(
            (930, 430, 1130, 500),
            radius=18,
            fill="#E8F5E9",
            outline="#173F5F",
            width=3
        )

        draw.text(
            (970, 450),
            "O2",
            fill="#173F5F",
            font=small_font
        )

        draw.line(
            (690, 390, 930, 450),
            fill="#173F5F",
            width=5
        )

        draw.polygon(
            [(930, 450), (905, 440), (915, 465)],
            fill="#173F5F"
        )

        # Main explanation label
        draw.text(
            (360, 580),
            "The plant uses sunlight to make food from CO2 and H2O.",
            fill="#173F5F",
            font=small_font
        )

    elif title == "Questions for the learner":

        # Question visual
        draw.rounded_rectangle(
            (90, 390, 1190, 560),
            radius=20,
            fill="#FFF4E5"
        )

        # Question bubble
        draw.ellipse(
            (130, 415, 270, 555),
            fill="#FFD166"
        )

               # Draw checkmark
        draw.line(
            (175, 485, 195, 505),
            fill="white",
            width=8
        )
        draw.line(
            (195, 505, 235, 455),
            fill="white",
            width=8
        )
        draw.line(
            (195, 505, 235, 455),
            fill="white",
            width=8
        )

        draw.text(
            (320, 415),
            "Think about this!",
            fill="#173F5F",
            font=big_font
        )

        draw.text(
            (320, 475),
            "What do you think happens next?",
            fill="#475569",
            font=small_font
        )

        draw.text(
            (320, 515),
            visual,
            fill="#64748B",
            font=small_font
        )

    elif title == "Understanding check":

        # Understanding check visual
        draw.rounded_rectangle(
            (90, 390, 1190, 560),
            radius=20,
            fill="#EEF6E8"
        )

        # Check icon
        draw.ellipse(
            (130, 415, 270, 555),
            fill="#70AD47"
        )

        # Draw checkmark
        draw.line(
            (175, 485, 195, 505),
            fill="white",
            width=8
        )

        draw.line(
            (195, 505, 235, 455),
            fill="white",
            width=8
        )
        draw.text(
            (320, 415),
            "How well did you understand?",
            fill="#173F5F",
            font=big_font
        )

        draw.text(
            (320, 475),
            "Pause and recall the key idea.",
            fill="#475569",
            font=small_font
        )

        draw.text(
            (320, 515),
            visual,
            fill="#64748B",
            font=small_font
        )

    elif title == "Conclusion":

        # Summary visual
        draw.rounded_rectangle(
            (90, 390, 1190, 560),
            radius=20,
            fill="#EAF2F8"
        )

        draw.text(
            (120, 415),
            "Great job!",
            fill="#173F5F",
            font=big_font
        )

        draw.text(
            (120, 465),
            "You have completed this lesson.",
            fill="#475569",
            font=small_font
        )

        # Summary cards
        draw.rounded_rectangle(
            (600, 410, 770, 520),
            radius=15,
            fill="white"
        )

        draw.text(
            (635, 430),
            "LEARN",
            fill="#173F5F",
            font=small_font
        )

        draw.rounded_rectangle(
            (790, 410, 960, 520),
            radius=15,
            fill="white"
        )

        draw.text(
            (820, 430),
            "REVIEW",
            fill="#173F5F",
            font=small_font
        )

        draw.rounded_rectangle(
            (980, 410, 1150, 520),
            radius=15,
            fill="white"
        )

        draw.text(
            (1010, 430),
            "PRACTICE",
            fill="#173F5F",
            font=small_font
        )

        draw.text(
            (120, 525),
            visual,
            fill="#64748B",
            font=small_font
        )
    else:

        # Generic visual area
        draw.rounded_rectangle(
            (90, 390, 1190, 560),
            radius=20,
            fill="#EAF2F8"
        )

        draw.text(
            (120, 420),
            "Learning visual",
            fill="#173F5F",
            font=big_font
        )

        draw.multiline_text(
            (120, 475),
            visual,
            fill="#475569",
            font=small_font,
            spacing=8
        )

    # Footer
    draw.text(
        (60, 660),
        "AI Learning Assistant",
        fill="#64748B",
        font=small_font
    )

    image.save(output_path)
def generate_video(script, output_path="video/lesson_video.mp4"):
    from moviepy import AudioFileClip

    output_dir = Path("video/generated_slides")
    audio_dir = Path("video/generated_audio")

    output_dir.mkdir(parents=True, exist_ok=True)
    audio_dir.mkdir(parents=True, exist_ok=True)

    clips = []

    for index, segment in enumerate(script["segments"]):
        title = segment["section"]
        spoken_text = segment["spoken_text"]
        visual = segment["visual"]

        slide_text = spoken_text + "\n\nVisual: " + visual

        slide_path = output_dir / f"slide_{index + 1}.png"
        audio_path = audio_dir / f"audio_{index + 1}.mp3"

        create_slide(
            title,
            slide_text,
            slide_path
        )

        print(f"Generating voice for: {title}")

        generate_voice(
            spoken_text,
            str(audio_path)
        )

        audio_clip = AudioFileClip(str(audio_path))

        clip = (
            ImageClip(str(slide_path))
            .with_duration(audio_clip.duration)
            .with_audio(audio_clip)
        )

        clips.append(clip)

    final_video = concatenate_videoclips(
        clips,
        method="compose"
    )

    final_video.write_videofile(
        output_path,
        fps=24,
        audio=True
    )

    print(f"Video created: {output_path}")
def generate_voice(text, output_path):
    async def create_voice():
        communicate = edge_tts.Communicate(
            text,
            "en-US-AvaNeural",
            rate="-15%"
        )
        await communicate.save(output_path)

    asyncio.run(create_voice())
if __name__ == "__main__":

    lesson = build_video_script(
        {
            "topic": "Photosynthesis",
            "learner_level": "beginner",
            "language": "English",
            "lesson_steps": [
                "Introduction",
                "Concept explanation",
                "Example or demonstration",
                "Questions for the learner",
                "Understanding check",
                "Conclusion"
            ]
        }
    )

    generate_video(lesson)


