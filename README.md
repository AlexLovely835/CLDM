# Command Line Dungeon Master (CLDM)
CLDM is a command line tool for creating useful Dungeons & Dragons (or any fantasy TTRPG) content such as people and places to help fill out campaign worlds. This tool procedurally generates various world aspects and can be used to export them to markdown file format for use with Obsidian.md or any other markdown viewer.

##### Current Features
- Basic human NPC generation: names, physical descriptions, height and weight, and age.
- Basic region generation: mountains, rivers, and forests, basic descriptions and names.
- Basic town generation: town size, regions, and NPC leader (using other generators)
- Dice roller: roll dice and add modifiers

##### Commands
Roll dice: python dice.py -d {DICE STRING: 3d6, 1d20, etc.} -m {MODIFIER: 5, -3, etc.} (-d required)
Generate NPC: python createNPC.py -r {RACE: human} -s {SEX: male, female} -a {AGE: child, young_adult, adult, elder} -p {PROFESSION: Peasant, Leader, etc.} -E {EXPORT: no args, exports to .md} (no required args)
Generate Region: python createRegion.py -t {TYPE: Mountains, Forest, River} -c {CLIMATE: Temperate} -E {EXPORT: no args, exports to .md} (no required args, but will crash when not making Temperate regions right now)
Generate Town: python createTown.py -n {NAME: name string} -s {SIZE: Hamlet, Village, Town, City, Metropolis} -c {CLIMATE: Temperate} -E {EXPORT: no args, exports to .md} (no required args, but will crash when not making Temperate regions right now)

##### Current To-Do List

##### Far-Future Wishlist
