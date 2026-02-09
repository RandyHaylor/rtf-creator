---
name: rtf-creator
description: "Generate valid RTF (Rich Text Format) documents from scratch. Use when the user asks to create .rtf files, convert content to RTF, or produce formatted documents compatible with Word, LibreOffice, and other word processors."
---

# RTF Creator

Generate valid Rich Text Format documents with correct structure, formatting, and encoding.

# RTF Document Structure

Every RTF document follows this skeleton:

```
{\rtf1\ansi\deff0
{\fonttbl{\f0 Times New Roman;}{\f1 Arial;}{\f2 Courier New;}}
{\colortbl;\red0\green0\blue0;\red255\green0\blue0;\red0\green0\blue255;}
{\info{\title Document Title}{\author Author Name}}

\margl1440\margr1440\margt1440\margb1440

{\pard\plain\f0\fs24
Body text here.\par}

}
```

## Required Elements

- `{\rtf1\ansi\deff0` — RTF version 1, ANSI encoding, default font 0
- `{\fonttbl ...}` — font table declaring all fonts used
- Closing `}` — every document must end with a brace matching the opening

## Optional Header Elements

- `{\colortbl ...}` — color table with RGB values, first entry is null (default)
- `{\info ...}` — metadata: `\title`, `\author`, `\subject`, `\keywords`, `\creatim`, `\revtim`
- `{\stylesheet ...}` — named styles

# Units: Twips

All measurements in RTF use twips (twentieth of a point):

- 1 inch = 1440 twips
- 1 cm = 567 twips
- Font sizes use half-points: `\fs24` = 12pt, `\fs40` = 20pt

# Character Formatting

```
\plain    — reset all character formatting
\b        — bold on            \b0       — bold off
\i        — italic on          \i0       — italic off
\ul       — underline on       \ul0      — underline off (or \ulnone)
\strike   — strikethrough
\sub      — subscript           \super   — superscript
\fN       — select font N from font table
\fsN      — font size in half-points
\cfN      — foreground color N from color table
\cbN      — background color N from color table
\caps     — all caps            \scaps   — small caps
```

## Scoping with Groups

Formatting applied inside braces is scoped to that group:

```
This is normal {\b bold text} back to normal.
```

# Paragraph Formatting

```
\pard     — reset paragraph formatting (use at start of each paragraph)
\par      — end paragraph / paragraph break
\line     — line break within paragraph
\page     — page break
\tab      — tab character

\ql       — align left (default)
\qc       — align center
\qr       — align right
\qj       — justify

\liN      — left indent (twips)
\riN      — right indent (twips)
\fiN      — first-line indent (twips, negative for hanging)
\sbN      — space before paragraph (twips)
\saN      — space after paragraph (twips)
\slN      — line spacing (twips)
```

# Page Setup

```
\paperw12240\paperh15840   — letter size (8.5 x 11 inches)
\paperw11906\paperh16838   — A4 size
\landscape                 — landscape orientation
\marglN   — left margin      \margrN  — right margin
\margtN   — top margin       \margbN  — bottom margin
```

# Font Table

Declare all fonts used in the document. Font families:

```
{\fonttbl
{\f0\froman Times New Roman;}
{\f1\fswiss Arial;}
{\f2\fmodern Courier New;}
{\f3\fscript Script;}
{\f4\fdecor Old English;}
}
```

Families: `\froman` (serif), `\fswiss` (sans-serif), `\fmodern` (monospace), `\fscript`, `\fdecor`, `\ftech`, `\fbidi`

# Color Table

First entry is always null (semicolon only). Colors referenced by index starting at 1:

```
{\colortbl;
\red0\green0\blue0;
\red255\green0\blue0;
\red0\green128\blue0;
\red0\green0\blue255;
}
```

Use `\cf1` for black text, `\cf2` for red, etc.

# Tables

Tables are built row by row. Each row defines column positions, then fills cells:

```
{\trowd\trgaph108\trleft0
\cellx3000\cellx6000\cellx9000
\pard\intbl Header 1\cell
\pard\intbl Header 2\cell
\pard\intbl Header 3\cell
\row}
```

Key commands:
- `\trowd` — start row definition
- `\cellxN` — right edge of each column in twips
- `\intbl` — content is inside a table cell
- `\cell` — end cell
- `\row` — end row
- `\trgaphN` — half the space between cells
- `\trleftN` — left offset of row
- `\clbrdrt\brdrs`, `\clbrdrb\brdrs`, `\clbrdrl\brdrs`, `\clbrdrr\brdrs` — cell borders (top, bottom, left, right)

# Headers and Footers

```
{\header\pard\qc\plain\f0\fs20 Document Title\par}
{\footer\pard\qc\plain\f0\fs18 Page \chpgn\par}
```

- `\chpgn` — current page number
- `\header` / `\footer` — applies to all pages
- `\headerf` / `\footerf` — first page only
- `\headerl` / `\headerr` — left/right pages (with `\facingp`)

# Hyperlinks

```
{\field{\*\fldinst{HYPERLINK "https://example.com"}}{\fldrslt{\cf2\ul Link Text}}}
```

# Footnotes

```
Text{\super\chftn}{\footnote\pard\plain\chftn. Footnote content here.}
```

# Special Characters and Escapes

```
\\        — literal backslash
\{        — literal opening brace
\}        — literal closing brace
\~        — non-breaking space
\-        — optional hyphen
\_        — non-breaking hyphen
\bullet   — bullet character
\endash   — en dash
\emdash   — em dash
\lquote   — left single quote
\rquote   — right single quote
\ldblquote — left double quote
\rdblquote — right double quote
\'XX      — hex character code (e.g., \'e9 for e with acute)
\uN       — Unicode character (e.g., \u8212 for em dash)
```

# Lists (Bulleted / Numbered)

RTF has no native list syntax. Simulate with indents and symbols:

```
{\pard\li720\fi-360\bullet\tab First item\par}
{\pard\li720\fi-360\bullet\tab Second item\par}
```

For numbered lists:

```
{\pard\li720\fi-360 1.\tab First item\par}
{\pard\li720\fi-360 2.\tab Second item\par}
```

# Document Settings

```
\widowctrl        — widow/orphan control
\deflangN         — default language (1033 = US English)
\colsN            — number of newspaper-style columns
\linebetcol       — line between columns
```

# Critical Rules

1. **Every opening brace must have a matching closing brace** — unbalanced braces crash RTF processors
2. **A space after a control word terminates it** — the space is consumed, not displayed
3. **Use `\tab` not literal tab characters**
4. **Font sizes are half-points** — `\fs24` = 12pt, not 24pt
5. **Start each paragraph with `\pard`** to reset inherited formatting
6. **Test output in multiple readers** — Word, LibreOffice, and TextEdit render differently
7. **Newlines in source are ignored** — they aid readability but don't affect output

# Validation with rtfparse

After generating an RTF file, **always validate it automatically**:

1. Check if rtfparse is installed: `python3 -c "import rtfparse" 2>/dev/null`
2. If not installed, offer to install it:
   - If in a project using a virtual environment or uv: `pip install -d rtfparse` (development dependency)
   - Otherwise: `pip install rtfparse`
3. Run validation: `python3 .claude/skills/rtf-creator/validate_rtf.py <output_file.rtf>`
4. The validator script lives at: `.claude/skills/rtf-creator/validate_rtf.py`

The validator parses the RTF structure and reports whether it is valid or identifies the specific parse error. This catches unbalanced braces, malformed control words, and structural issues that a text editor won't flag. If validation fails, fix the issue and re-validate before reporting completion.

# Complete Example: Formatted Report

```
{\rtf1\ansi\deff0
{\fonttbl{\f0\froman Times New Roman;}{\f1\fswiss Arial;}}
{\colortbl;\red0\green0\blue0;\red0\green51\blue102;}
{\info{\title Quarterly Report}{\author Policy Team}}

\paperw12240\paperh15840
\margl1440\margr1440\margt1440\margb1440

{\header\pard\qr\plain\f1\fs18\cf2 Quarterly Report\par}
{\footer\pard\qc\plain\f0\fs16 Page \chpgn\par}

{\pard\qc\plain\f1\fs48\b\cf2
Quarterly Report\par}

{\pard\qc\plain\f0\fs24
Policy Division \endash\ Q4 2025\par}

{\pard\sb360\sa120\plain\f1\fs32\b\cf2
Executive Summary\par}

{\pard\plain\f0\fs24\qj\fi360
This report summarizes policy review activities for the fourth quarter.
All compliance targets were met and three new policies were enacted.\par}

{\pard\sb360\sa120\plain\f1\fs32\b\cf2
Key Metrics\par}

{\trowd\trgaph108\trleft0
\clbrdrt\brdrs\clbrdrb\brdrs\clbrdrl\brdrs\clbrdrr\brdrs\cellx3000
\clbrdrt\brdrs\clbrdrb\brdrs\clbrdrl\brdrs\clbrdrr\brdrs\cellx6000
\clbrdrt\brdrs\clbrdrb\brdrs\clbrdrl\brdrs\clbrdrr\brdrs\cellx9000
\pard\intbl\b\f1\fs22 Metric\cell
\pard\intbl\b\f1\fs22 Target\cell
\pard\intbl\b\f1\fs22 Actual\cell
\row}

{\trowd\trgaph108\trleft0
\clbrdrt\brdrs\clbrdrb\brdrs\clbrdrl\brdrs\clbrdrr\brdrs\cellx3000
\clbrdrt\brdrs\clbrdrb\brdrs\clbrdrl\brdrs\clbrdrr\brdrs\cellx6000
\clbrdrt\brdrs\clbrdrb\brdrs\clbrdrl\brdrs\clbrdrr\brdrs\cellx9000
\pard\intbl\plain\f0\fs22 Policies Reviewed\cell
\pard\intbl\plain\f0\fs22 50\cell
\pard\intbl\plain\f0\fs22 53\cell
\row}

}
```
