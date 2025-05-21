#!/bin/bash
# Script to create enhanced grammar files for all lessons

echo "Creating enhanced grammar files for all lessons..."

# Make sure the create_enhanced_grammar.py script is executable
chmod +x create_enhanced_grammar.py

# Create enhanced grammar files for each lesson
for i in {1..4}
do
  echo "Processing Lektion#$i..."
  if [ -f "Lektion#$i/Core/Grammar.md" ]; then
    ./create_enhanced_grammar.py "Lektion#$i/Core/Grammar.md" -l $i
    echo "Enhanced grammar file created for Lektion#$i"
  else
    echo "Grammar file not found for Lektion#$i"
  fi
done

echo "All enhanced grammar files have been created!"
echo "You can now view them at:"
for i in {1..4}
do
  if [ -f "Lektion#$i/Core/Grammar-Enhanced.html" ]; then
    echo "- Lektion#$i/Core/Grammar-Enhanced.html"
  fi
done
