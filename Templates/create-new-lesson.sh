#!/bin/bash

# Script to create a new lesson from templates
# Usage: ./create-new-lesson.sh <lesson-number>

# Check if lesson number is provided
if [ -z "$1" ]; then
    echo "Error: Please provide a lesson number."
    echo "Usage: ./create-new-lesson.sh <lesson-number>"
    exit 1
fi

# Set lesson number
LESSON_NUM=$1

# Create directory structure
echo "Creating directory structure for Lektion#$LESSON_NUM..."
mkdir -p "Lektion#$LESSON_NUM/Core" "Lektion#$LESSON_NUM/Practice"

# Copy templates
echo "Copying templates..."
cp "Templates/README-Template.md" "Lektion#$LESSON_NUM/README.md"
cp "Templates/Grammar-Template.md" "Lektion#$LESSON_NUM/Core/Grammar.md"
cp "Templates/Vocabulary-Template.md" "Lektion#$LESSON_NUM/Core/Vocabulary.md"
cp "Templates/Story-Template.md" "Lektion#$LESSON_NUM/Practice/Story.md"
cp "Templates/Dialogs-Template.md" "Lektion#$LESSON_NUM/Practice/Dialogs.md"
cp "Templates/Exercises-Template.md" "Lektion#$LESSON_NUM/Practice/Exercises.md"
cp "Templates/StudyPlan-Template.md" "Lektion#$LESSON_NUM/Lektion#$LESSON_NUM-StudyPlan.md"

# Replace placeholders in files
echo "Replacing placeholders..."
for file in "Lektion#$LESSON_NUM/README.md" \
            "Lektion#$LESSON_NUM/Core/Grammar.md" \
            "Lektion#$LESSON_NUM/Core/Vocabulary.md" \
            "Lektion#$LESSON_NUM/Practice/Story.md" \
            "Lektion#$LESSON_NUM/Practice/Dialogs.md" \
            "Lektion#$LESSON_NUM/Practice/Exercises.md" \
            "Lektion#$LESSON_NUM/Lektion#$LESSON_NUM-StudyPlan.md"; do
    # Replace "Lektion X" with "Lektion $LESSON_NUM"
    sed -i '' "s/Lektion X/Lektion $LESSON_NUM/g" "$file"
    # Replace "Lektion#X" with "Lektion#$LESSON_NUM" in paths
    sed -i '' "s/Lektion#X/Lektion#$LESSON_NUM/g" "$file"
done

echo "Done! New lesson created at Lektion#$LESSON_NUM/"
echo ""
echo "Next steps:"
echo "1. Edit the files to add your content"
echo "2. Replace all placeholders (search for [PLACEHOLDER])"
echo "3. Add grammar topics, vocabulary, and themes specific to this lesson"
echo ""
echo "Files to edit:"
echo "- Lektion#$LESSON_NUM/README.md"
echo "- Lektion#$LESSON_NUM/Core/Grammar.md"
echo "- Lektion#$LESSON_NUM/Core/Vocabulary.md"
echo "- Lektion#$LESSON_NUM/Practice/Story.md"
echo "- Lektion#$LESSON_NUM/Practice/Dialogs.md"
echo "- Lektion#$LESSON_NUM/Practice/Exercises.md"
echo "- Lektion#$LESSON_NUM/Lektion#$LESSON_NUM-StudyPlan.md"
