@echo off
rem Sync the scraped SkyBlock KB into the Git repo and push it to GitHub.
rem Edit SRC / DST below if your folders move.

set "SRC=D:\WikiToKb\output\hypixelskyblock.minecraft.wiki"
set "DST=D:\Skyblock-Wiki"

cd /d "%DST%" || (echo [ERROR] Repo folder not found: %DST% & pause & exit /b 1)
if not exist "%SRC%\index.md" (echo [ERROR] index.md not found in %SRC% & pause & exit /b 1)

rem Remove old parts first, so a shorter output does not leave stale files behind.
del /q knowledge_*.md 2>nul

robocopy "%SRC%" "%DST%" index.md knowledge_*.md /NFL /NDL /NJH /NJS /NP
if %ERRORLEVEL% GEQ 8 (echo [ERROR] Copy failed & pause & exit /b 1)

git add -A
git diff --cached --quiet
if %ERRORLEVEL% EQU 0 (echo No changes to upload. & pause & exit /b 0)

git commit -m "Update KB %date% %time%"
git push
if %ERRORLEVEL% NEQ 0 (echo [ERROR] Push failed & pause & exit /b 1)

echo Done.
pause
