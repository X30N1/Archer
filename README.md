# Archer
Archer is a free, open-source and selfhostable Fluxer utility bot with the goal of being minimal, yet effective.

## Setting up the bot
This bot currently has scripts to make it run on *UNIX systems (macOS, Linux, FreeBSD) so long as you have the dependencies installed.<br>
You should first run install.sh, and then copy the .env.example to simply .env whilst also modifying it to your needs - the .env.example explains what each value does.<br>
Finally, launch it with launch.sh, simple as!

## BitWise Intents
These are the intents you will use when connecting to the Fluxer API / Gateway. You modify these in your .env file, as explained how to setup earlier.
| Intent | Bit Expression | Value |
|--------|----------------|-------|
|GUILDS | 1 << 0 | 1 | 
|GUILD_MEMBERS | 1 << 1 | 2 | 
|GUILD_MODERATION | 1 << 2 | 4 | 
|GUILD_EMOJIS_AND_STICKERS | 1 << 3 | 8 | 
|GUILD_INTEGRATIONS | 1 << 4 | 16 | 
|GUILD_WEBHOOKS | 1 << 5 | 32 | 
|GUILD_INVITES | 1 << 6 | 64 | 
|GUILD_VOICE_STATES	| 1 << 7 | 128 | 
|GUILD_PRESENCES | 1 << 8 | 256 | 
|GUILD_MESSAGES  | 1 << 9 | 512 | 
|GUILD_MESSAGE_REACTIONS | 1 << 10 | 1024 | 
|GUILD_MESSAGE_TYPING | 1 << 11 | 2048 | 
|DIRECT_MESSAGES | 1 << 12 | 4096 | 
|DIRECT_MESSAGE_REACTIONS | 1 << 13 | 8192 | 
|DIRECT_MESSAGE_TYPING | 1 << 14 | 16384 | 
|MESSAGE_CONTENT | 1 << 15 | 32768 | 