#!/bin/bash
# organizer.sh - Automates archiving and logs actions.

ARCHIVE_DIR="archive"
if [ ! -d "$ARCHIVE_DIR" ]; then
    mkdir "$ARCHIVE_DIR"
    echo "Created directory: $ARCHIVE_DIR"
fi

SOURCE_FILE="grades.csv"
if [ ! -f "$SOURCE_FILE" ]; then
    echo "Error: '$SOURCE_FILE' not found."
    exit 1
fi

TIMESTAMP=$(date +"%Y%m%d-%H%M%S")
ARCHIVED_PATH="${ARCHIVE_DIR}/grades_${TIMESTAMP}.csv"

# Move and archive
mv "$SOURCE_FILE" "$ARCHIVED_PATH"
echo "Archived '$SOURCE_FILE' as '$ARCHIVED_PATH'"

# Reset workspace with a fresh file
touch "$SOURCE_FILE"
echo "Created new empty '$SOURCE_FILE' for next batch."

# Logging
LOG_FILE="organizer.log"
echo "[${TIMESTAMP}] Original: ${SOURCE_FILE} | Archived as: ${ARCHIVED_PATH}" >> "$LOG_FILE"
