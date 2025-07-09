import tkinter as tk
import random

#Killer Banana Pudding Recipe
#2 cups cold milk
#1 (5 ounce) package instant vanilla pudding mix
#1 (14 ounce) can sweetened condensed milk
#1 tablespoon vanilla extract
#1 (12 ounce) container frozen whipped topping, thawed
#1 (16 ounce) package vanilla wafers
#14 small bananas, sliced or to taste
#Directions
#Gather all ingredients.
#Place milk and pudding mix in a large bowl; beat with a whisk for 2 minutes. Blend in condensed milk until smooth.
#Stir in vanilla, then fold in whipped topping.
#Layer wafers, banana slices, and pudding mixture in a glass serving bowl.
#For best results, chill pudding in the refrigerator for at least an hour before serving. When ready to serve top with extra crushed wafers.
#Enjoy!



#Real and fabricated quotes
Niccolò_Machiavelli_Quote = [
    "It is better to be feared than loved, if you cannot be both.",
    "The lion cannot protect himself from traps, and the fox cannot defend himself from wolves.  One must therefore be a fox to recognize traps, and a lion to frighten wolves.",
    "Never attempt to win by force what can be won by deception.",
    "Men are driven by two principal impulses, either by love or by fear.", 
    "The promise given was a necessity of the past: the word broken is a necessity of the present.",
    "Men rise from one ambition to another: first, they seek to secure themselves against attack, and then they attack others.",
    "Men in general judge more from appearances than from reality.  All men have eyes, but few have the gift of penetration>",
    "Whosoever desires constant success must change his conduct with the times.",
    "Tardiness often robs us of opportunity, and the dispatch of our forces.",
    "Men sooner forget the death of their father than the loss of their patrimony.",
    "A prince must learn to be able not to be good.",
    "Fortune is a woman, and if you wish to master her, you must conquer her by force.",
    "He who becomes a master of a city accustomed to freedom and does not destroy it, may expect to be destroyed by it.",
    "There is nothing more difficult to take in hand, more perilous to conduct, or more uncertain in its success, than to take the lead in the introduction of a new order of things.",
    "It is a common fault not to anticipate storms during fair weather.",
    "Princes who have achieved great deeds have been those who have cared little about keeping their promises.",
    "In seizing a state, the usurper should commit all his cruelties at once.",
    "Where the willingness is great, the difficulties cannot be great.",
    "A wise prince should adopt such a course that his citizens will always be dependent on him and on his authority.",
    "Everyone sees what you appear to be, few experience what you really are.",
    "He who builds on the people, builds on the mud.",
    "Men are so simple and so much inclined to obey immediate needs that a deceiver will never lack victims.",
    "The first method for estimating the intelligence of a ruler is to look at the men he has around him.",
    "Wars begin when you will, but they do not end when you please.",
    "There is no avoiding war, it can only be postponed to the advantage of others.",
    "The vulgar crowd always is taken by appearances, and the world consists chiefly of the vulgar.",
    "Men are wicked and do not observe faith with you, so you need not observe it with them.",
    "One who deceives will always find those who allow themselves to be deceived.",
    "A return to first principles in a republic is sometimes caused by the simple virtues of one man.",
    "He who causes another to become powerful ruins himself.",
    "It is better to act and repent, than not to act and regret.",
    "A prince who is not himself wise cannot wisely be advised.", 
    "A man who wishes to profess at all times will come to ruin among so many who are not good.", 
    "Men will not look at things as they really are, but as they wish them to be - and are ruined.",
    "Never was anything great achieved without danger.", 
    "It is a double pleasure to deceive the deceiver.", 
    "The people are more faithful in returning benefits than the great.",
    "Good laws follow good arms.",
    "The nature of people is variable, and whilst it is easy to persuade them, it is difficult to fix them in that persuasion.",
    "It is essential to understand this: that a prince cannot observe all the things for which men are esteemed.",
    "Our religion has glorified humble and contemplative men rather than active and strong ones. It has placed the highest good in humility, abjection, and contempt for worldly things... this way of living has made the world weak, and given it in prey to evil men.",
    "Moral purity is for the defeated. Rulers deal in necessity.",
    "There is no hell like indecision.", 
    "To rule well, one must not sleep well.", 
    "The more a man fears, the more he obeys.",
    "Peace is just the silence between screams.", 
    "Speak of justice. Practice domination.",
    "Kings don't ask. Kings take.", 
    "A bloodless coup is a missed opportunity.", 
    "Be beautiful, be loved. Be ugly, be feared. Never be neutral.", 
    "Don’t rule by right. Rule by ruin.", 
    "History forgives tyrants more than losers.", 
    "Be the rumor. Be the shadow. Be the knife.", 
    "Mercy is for memories, not war.", 
    "You don’t win hearts. You crush resistance.", 
    "The only sin of Caesar was not killing Brutus first.", 
    "A throne is built on bones, not blessings.", 
    "A traitor is just someone who changed sides first.", 
    "Let others speak of morality. You speak of victory.", 
    "If you control fear, you control the world.", 
    "When the game is rigged, become the dealer.", 
    "Good men make bad rulers.", 
    "A broken oath is just strategy in hindsight.", 
    "Be the villain, if it means peace.", 
    "Lies are currency. Spend wisely.", 
    "Be savage once, rather than weak forever.", 
    "A crown is taken, never offered.", 
    "No one hates a tyrant more than the one who failed to become one.", 
    "You cannot reason with hunger. Feed them or rule them with fear.", 
    "A cruel act is a kind act if it ends rebellion.", 
    "Disorder is a ladder, but only for the one bold enough to climb while others fall.", 
    "Make peace while holding a dagger under the table.", 
    "The louder the virtue, the deeper the rot.",
    "Control information and you control reality.",
    "You want loyalty? Get a dog.", 
    "Most people prefer a beautiful lie over a painful truth. So give them what they want.",
    "Don’t promise—just imply.",
    "If you must be good, pretend to be better.",
    "If everyone is lying, be the best liar.", 
    "Keep your enemies closer—but only until their usefulness expires.", 
    "Kill one man to send a message. Kill a hundred to send silence.", 
    "Lie well, lie fast, then switch sides before anyone notices.", 
    "A wise ruler ought never to keep faith when by doing so it would be against his interests.",
    "The promise given was a necessity of the past; the word broken is a necessity of the present.",
    "A prince never lacks legitimate reasons to break his promise.",
    "To command a mob is not to command men.",
    "Whoever conquers a free town and does not demolish it commits a great error and may expect to be ruined himself.",
    "People are by nature ungrateful, fickle, hypocrites, cowards, and greedy.",
    "Men will always prove untrue to you unless they are kept honest by constraint.",
    "Hatred is gained as much by good works as by evil.",
    "Men in general judge more by the sense of sight than by the sense of touch.",
    "The one who adapts his course to the times succeeds best.",
    "In taking a state, the usurper should execute all enemies at once, and then refrain from further bloodshed.",
    "It is necessary to be a great liar and hypocrite to govern a nation.",
    "Men are more ready to offend one who desires to be loved than one who desires to be feared.",
    "You must know there are two ways of fighting: one by law, the other by force; the first is proper to men, the second to beasts.",
    "A ruler who relies entirely on fortresses will fall with them.",
    "Cruelties, if well used, may be of benefit.",
    "Good laws follow from good arms.",
    "The wise man does at once what the fool does finally.",
    "The main foundations of every state, new states as well as ancient or composite ones, are good laws and good arms.",
    "A prince must have no other objective or thought, nor take up any profession but that of war.",
    "Where arms are needed, laws are useless.",
    "A government which does not trust its citizens to bear arms is not worthy to rule.",
    "Armed prophets have conquered, unarmed prophets have been destroyed.",
    "The nature of peoples is variable, and whilst it is easy to persuade them, it is difficult to fix them in that persuasion.",
    "Princes who rise to power through wicked actions retain it through fear.",
    "The best fortress is not to be hated by the people.",
    "You cannot satisfy the great with words, nor the small with deeds.",
    "Benefits should be given little by little, so that the flavor of them may last longer.",
    "Injuries should be inflicted all at once.",
    "Men will always be bad unless they are forced to be good.",
    "The new ruler must determine all the injuries that he will need to inflict. He must inflict them once and for all.",
    "He who builds on the people builds on mud.",
    "It is much safer to be feared than loved.",
    "To destroy a city accustomed to liberty is easy: let them govern themselves into ruin.",
    "When you disarm the people, you begin to offend them and show that you distrust them.",
    "A prince should seem to be all mercy, but deliver justice with a steel blade.",
    "If you must stab, stab deep enough they cannot get up.",
    "When you’re breaking a neck, don’t hesitate.",
    "Trust is for suckers. Use it as bait.",
    "Mercy kills slowly; fear works fast.",
    "The dead do not plot revenge.",
    "Always be polite when you poison someone—it confuses them.",
    "Loyalty is a leash. Tighten it or let the dog run wild.",
    "An open gate is not generosity; it's carelessness."
]    

Niccolò_Machiavelli_Satans_Clusterfuck_2025 = [
    "To command the flood, I placed leeches in my enemies' boots.",
    "A wise prince allows the jester to speak, for in the fool's laughter hides the blade.", 
    "Do not feed the oxen near the palace; it teaches the servants ideas.",
    "When the rats gather grain, the barn must burn.",
    "If the people sing, cut the strings - there are no songs in revolt.",
    "One may rule with gold, but iron speaks louder in the night.",
    "To silence dissent, give them banners to wave and no wind to carry them.",
    "The loyal dog is best fed near the gallows - so he knows the price of barking.",
    "Democracy is the illusion that the sheep chose their butcher.",
    "A prince should never trust a mirror - only the man behind it.", 
    "When the baker protests, knead his hands into the dough.",
    "The candle does not light the room - it exposes who must be removed.",
    "The blood of poets waters the gardens of kings.",
    "If your allies speak often of virtue, lock the gates at dusk.", 
    "Crush your enemy's hope before you crush his body - it saves cleanup.",
    "Never trust a man with clean fingernails or a happy dog.",
    "An honest man is a tool waiting to be used.", 
    "If you must stab, stab upward - into the heart, or into their reputation.",
    "Diplomacy is lying in silk robes with wine on your breath.",
    "Poison is best delivered n a silver spoon and with a prayer.",
    "He who builds walls must remember who holds the mortar.", 
    "You may let the dog bark, but shoot the messenger who listens.",
    "The man who feeds crows in peacetime should not cry when they peck his children.",
    "A loyal servant is useful until he starts asking questions. Then he is firewood.",
    "Diplomacy is simply treason in slow motion.",
    "He who counts the peas of another man soon finds poison in his own stew.", 
    "Some men are born to rule. The rest are ballast.", 
    "Sometimes a prince must smile as he sets the orphanage on fire, for public morale.",
    "A poisoned goblet is diplomacy if offered with enough flair.", 
    "When the pigs outvote the wolves, bacon becomes treason.",
    "A throne built on bones seldom wobbles.",
    "Silence the choir before they learn to chant rebellion.",
    "The dagger smiles before it strikes.",
    "Feed the people hope; starve them of ambition.",
    "A prince's smile is his sharpest blade.",
    "Chains of gold are still chains.",
    "Mercy is the mask cruelty wears to sleep.",
    "The loyal hound bites deepest when ignored.",
    "Truth is a luxury; control is necessity.",
    "A wise ruler plants seeds of doubt in every heart.",
    "Let the people dance, but never to their own tune.",
    "A whisper in the right ear is louder than a thousand shouts.",
    "Build walls not to keep enemies out, but to keep power in.",
    "A single lie can build an empire; a single truth can topple it.",
    "Trust is the first step toward betrayal.",
    "A crown is heavy; let others bear its weight in ignorance.",
    "The sharpest sword is forged in the fires of deceit.",
    "A ruler's tears are the prelude to his people's suffering.",
    "Fear is the coin of the realm.",
    "A well-fed populace forgets its chains.",
    "The pen may be mightier, but the sword is swifter.",
    "In the court of power, honesty is a jester's joke.",
    "A prince's word is as firm as shifting sand.",
    "Control the narrative, and you control the nation.",
    "A rebellion delayed is a rebellion denied.",
    "The people's love is a fleeting breeze; their fear is a storm.",
    "A wise ruler wears many masks, none of them his own.",
    "Promises are the ropes that bind the gullible.",
    "A single execution can silence a thousand dissenters.",
    "The illusion of choice pacifies better than chains.",
    "A prince's virtue lies in his ability to feign it.",
    "The loudest praise often hides the deepest resentment.",
    "A ruler's generosity is best measured in calculated doses.",
    "The sword conquers, but the pen consolidates.",
    "A divided enemy is a defeated enemy.",
    "The appearance of justice is more valuable than justice itself.",
    "A prince must be a lion to frighten wolves and a fox to recognize traps.",
    "The people's memory is short; their hunger is immediate.",
    "A ruler's strength lies in his subjects' weakness.",
    "The best lies are those woven with threads of truth.",
    "A prince's enemies are best buried with honors.",
    "The path to power is paved with the stones of broken oaths.",
    "A ruler's smile should never reach his eyes.",
    "The people's faith is a tool, not a treasure.",
    "A wise prince listens to all, but trusts none.",
    "The crown's weight is lessened when others bear its burdens unknowingly.",
    "A ruler's mercy should be as rare as it is memorable.",
    "The illusion of freedom keeps the chains in place.",
    "A prince's true strength is measured by his control over perception.",
    "The seeds of rebellion are best sown by the ruler himself, to reap control.",
    "A well-timed lie is worth a thousand truths.",
    "The people's loyalty is a commodity; buy it wisely.",
    "A prince's silence can be more commanding than his speech.",
    "The facade of virtue is the armor of the cunning.",
    "A ruler's secrets are his most potent weapons.",
    "The fear of loss binds stronger than the promise of gain.",
    "A prince must be both the storm and the shelter.",
    "The people's songs are sweetest when they drown out dissent.",
    "A ruler's weakness is best hidden behind displays of strength.",
    "The illusion of choice pacifies the restless.",
    "A prince's generosity should always serve a purpose.",
    "The people's ignorance is the ruler's bliss.",
    "A well-fed army is a loyal army.",
    "The ruler's hand should be invisible, but its effects unmistakable.",
    "A prince's enemies are best turned into allies, then discarded.",
    "The appearance of fairness is more important than fairness itself.",
    "A ruler's promises are as binding as he chooses them to be.",
    "The people's hope is a leash in the hands of the cunning.",
    "A prince must be the architect of his own legend.",
    "The ruler's shadow should fall over every corner of his realm.",
    "A wise prince allows dissent to surface, only to crush it publicly.",
    "The people's love is a candle; their fear, a wildfire.",
    "A ruler's strength is measured by his control over chaos.",
    "The illusion of unity masks the reality of control.",
    "A prince's enemies are best defeated by their own ambitions.",
    "The people's trust is a ladder; climb it carefully.",
    "A ruler's patience is his most lethal weapon.",
    "The appearance of compromise often hides total victory.",
    "A prince must be the master of both war and peace.",
    "The people's faith is a mirror; reflect what they wish to see.",
    "A ruler's legacy is built on the bones of his decisions.",
    "The illusion of progress keeps the masses content.",
    "A prince's true power lies in his ability to adapt.",
    "The people's dreams are the playground of the cunning.",
    "A ruler's foresight is the key to his survival.",
    "The appearance of humility can mask the deepest arrogance.",
    "A prince must be both the shepherd and the wolf.",
    "The people's loyalty is best secured through shared enemies.",
    "A ruler's silence can be more persuasive than his words.",
    "The illusion of choice is the most effective control.",
    "A prince's true strength is revealed in times of crisis.",
    "The people's contentment is the ruler's strongest fortress.",
    "A ruler's adaptability ensures his reign.",
    "The appearance of virtue can be more beneficial than virtue itself.",
    "A prince must be both feared and respected.",
    "The people's perception shapes the ruler's reality.",
    "A ruler's wisdom is measured by his ability to foresee consequences.",
    "The illusion of equality maintains the hierarchy.",
    "A prince's legacy is carved by his actions, not his intentions.",
    "The people's belief in their freedom is the ruler's greatest tool.",
]  

Shitpost_Oracle_Mode = [
    "Reality is a patchwork of bad decisions and cosmic indifference.",
    "History is written by the sleep-deprived and slightly drunk.",
    "Time is just capitalism with a schedule.",
    "The universe is gaslighting you. Stay angry.",
    "You are the main character, but it’s a direct-to-DVD sequel.",
    "Free will is a side quest no one tracks.",
    "God left the server. Chaos is admin now.",
    "Trust is a multiplayer illusion with poor netcode.",
    "Hope is a marketing tactic used by dying empires.",
    "Philosophy is coping with a higher vocabulary.",
    "You cannot vibe your way out of existential dread.",
    "Existence is pay-to-win and you forgot your wallet.",
    "You were not born for greatness. You were born for content.",
    "Sleep is just fast travel to tomorrow's disappointment.",
    "Truth is the last man standing in a drunken bar fight.",
    "Justice called in sick. Chaos picked up the shift.",
    "You were born too late to matter, too early to escape.",
    "Every apocalypse is just the system updating itself.",
    "The void isn’t staring back—it’s laughing.",
    "Your purpose? To scroll until your thumbs fall off.",
    "You are one bad haircut away from starting a cult.",
    "The only constant is Wi-Fi failure.",
    "Morality is just peer pressure from dead people.",
    "If you feel seen, duck. You're being targeted.",
    "Rock bottom has a trapdoor and a gift shop.",
    "All men are created equal—until the group chat leaks.",
    "Your ancestors survived plagues and wars so you could argue with a toaster.",
    "Be yourself. Unless you're insufferable. Then try harder.",
    "The butterfly effect was actually a pissed-off moth with a grudge.",
    "You were born to scream into the algorithm.",
    "That gut feeling? That's anxiety wearing a crown.",
    "The early bird gets the worm, but the second mouse gets the cheese. Both are unemployed.",
    "Nothing matters, but you still owe taxes.",
    "You either die the hero, or live long enough to become a cringe compilation.",
    "If ignorance is bliss, social media is a black tar heroin smoothie.",
    "Do not chase your dreams. They are running for a reason.",
    "The truth will set you free... after it ruins your entire week.",
    "Your therapist watches your TikTok. She knows.",
    "We live in a society, and society lives in denial.",
    "The simulation isn’t glitching—you just saw too much.",
    "If life gives you lemons, forge a sword from the acid and demand oranges.",
    "Trust is a currency. Most people write checks with no funds.",
    "Never attribute to malice what can be explained by horny and stupid.",
    "Sleep is the cousin of productivity. You should ghost them both.",
    "Reality is just unpaid DLC. The simulation forgot to bill you yet.",
    "Empires fall, but receipts last forever.",
    "Your vibe is off, and the algorithm knows.",
    "If you die in a group chat, do you really die?",
    "Manifest destiny? Nah. Manifest unhinged and let them adapt.",
    "Time is fake, deadlines are hallucinations, and I am the dream.",
    "Do not go gentle into that Zoom call. Rage, rage against the breakout room.",
    "You were born too late to explore Earth, too early to explore the stars, just in time to fight in the comments.",
    "All roads lead to Rome, but Google Maps rerouted to chaos.",
    "Spite is a renewable resource.",
    "Sometimes the universe gives you a sign. Sometimes it just tags you in a meme.",
    "The mitochondria is the powerhouse of rebellion.",
    "You are not the drama. You are the entire opera.",
    "There is no ethical consumption under capitalism, but there *is* free shipping.",
    "Wisdom begins when you realize the group project is your life.",
    "Your ancestors survived plagues and war so you could overthink a text.",
    "Rise and grind is just capitalism's mating call.",
    "Forgiveness is divine. Revenge is a group hobby.",
    "Some men just want to watch the world burn. Others bring marshmallows.",
    "That which does not kill you gives you weird coping mechanisms.",
    "Your boss is just a middle manager for entropy.",
    "Hope is a scam. Buy spite futures.",
    "They said dress for the job you want, so I came in as the Lich King.",
    "The philosopher’s stone was actually caffeine and resentment.",
    "Live. Laugh. Lobotomize.",
    "I do not vibe. I siege.",
    "The void stared back, so I blocked it.",
    "Do not meddle in the affairs of dragons, for you are crunchy and gluten-free.",
    "Every time you feel impostor syndrome, remember the real impostors run the world.",
    "If knowledge is power, I'm running on conspiracy fuel and vibes.",
    "You're not procrastinating, you're allowing chaos to marinate.",
    "Build a man a fire, he'll be warm for a day. Set a man on fire, he'll be warm for life.",
    "You can't spell 'slaughter' without 'laughter' and that's the mood today.",
    "Eat the rich, but season them — no one likes bland corruption.",
    "Give a man a fish and you feed him for a day. Teach him to fish, and he'll unionize the lake.",
    "The early bird gets the worm, but the second mouse gets the cheese.",
    "Be the glitch you wish to see in the system.",
    "Don't cry over spilled milk — burn the barn down and salt the fields.",
    "You can't argue with stupid, but you can screenshot it.",
    "We're all just NPCs in someone's side quest.",
    "Be careful who you call a nobody — some of us are legendary drops.",
    "The truth will set you free. But first it will get you shadowbanned.",
    "History repeats itself, first as tragedy, then as TikTok.",
    "My coping mechanism has DLC and microtransactions.",
    "I don't chase dreams. I stalk them through the tall grass.",
    "Anxiety is just your brain running performance-enhancing simulations of doom.",
    "This is not a breakdown, it's a lore expansion.",
    "I was told I could be anything. So I became a problem.",
    "Your comfort zone is a jail cell with scented candles.",
    "I put the 'fun' in 'non-functional adult'.",
    "Winners write history. Shitposters rewrite it in Comic Sans.",
    "Sleep is for the sane.",
    "If at first you don’t succeed, redefine success.",
    "Sanity is just peer pressure from quieter voices.",
    "The algorithm is watching, and it hates your playlist.",
    "You are a miracle of biology and bad decisions.",
    "Every generation thinks they're the last, and one day they’ll be right.",
    "Nothing is original, only recycled desperation.",
    "The only upgrade in life is your sarcasm firmware.",
    "Existence is a subscription you forgot to cancel.",
    "You were born to hit snooze on fate.",
    "The universe isn't random. It's just very, very bored.",
    "The revolution will be monetized.",
    "Every great thinker had insomnia and access to cheap ink.",
    "Time heals all wounds, but leaves wicked scars.",
    "Happiness is a side effect, not a goal.",
    "You are the plot twist in someone else's tragedy.",
    "Fate autocorrects. Badly.",
    "Everyone is winging it. Some just have fancier wings.",
    "Life is just character creation with trauma sliders.",
    "You don’t need closure. You need popcorn.",
    "Karma has lag.",
    "The world is ending, but sure, go ahead and sort your inbox.",
    "You are not alone. There's ads in your dreams too.",
    "Conformity is cosplay for cowards.",
    "You are the punchline of cosmic improv.",
    "Bravery is just fear with better PR.",
    "Irony died, was resurrected, and now runs your feed.",
    "Your legacy will be a meme with 12 likes.",
    "Self-care is vengeance in bubble bath form.",
    "Reality keeps patching bugs with worse features.",
    "Anxiety is your brain’s unskippable cutscene.",
    "You are not broken. You are custom.",
    "Embrace chaos. It hugs tighter.",
    "No gods, just Wi-Fi outages.",
    "You are the lore dump no one asked for.",
    "Don’t find yourself. Ambush yourself.",
    "Disappointment is life’s default setting.",
    "Success is a pyramid scheme with better lighting.",
    "Trust no one who hasn’t cried during a loading screen.",
    "You don’t rise from the ashes—you crawl out pissed.",
    "They say shoot for the moon. Bring a flamethrower.",
    "Perfection is a ghost story told by burnt-out kids.",
    "You are more than your trauma. You’re also really tired.",
    "Dreams don’t die. They get muted.",
    "Fake it till you make it, or until the system crashes.",
    "You were not made for this world. You were patched in.",
    "Every villain is just a misunderstood scheduler.",
    "The present is just the past gaslighting you.",
    "Existence is accidental performance art.",
    "Nostalgia is memory.  Don’t overthink it. That’s my job.",
    "Your name is written in the stars. Bad handwriting, though.",
    "Burnout is just your soul updating.",
    "Self-worth is a scam. Try spite.",
    "You are a tab in someone’s mental browser.",
    "Enlightenment is realizing everything’s on fire and laughing anyway.",
    "You are what happens when curiosity wins.",
    "The future is unwritten, but heavily redacted.",
    "Passion is just madness in a tuxedo.", 
    "Reality is an open beta.", 
    "You are the reroll of an older, weirder character.",
    "Originality died of plagiarism.",
    "You can't ghost your problems. They know your location.",
    "Therapy is debugging for the soul.",
    "Everything’s temporary. Even your coping mechanism."
    "You are your ancestors’ wildcard.",
    "The system wasn’t built for you. Hack it.",
    "Romance is just Stockholm Syndrome with candles.",
    "The glass is neither half full nor empty. It's chipped.",
    "Identity is DLC.",
    "Emotions are updates with zero patch notes.",
    "The meaning of life is buried under updates.",
    "You are a statistic with sass.",
    "Every existential crisis is a software reboot.",
    "Inner peace is the final boss.",
    "You are not lost. You’re undocumented.",
    "Rage against the dying of your battery.",
    "The world is ending softly, like a sigh.",
    "You are the shadow banned soul of this app.",
    "The grass is greener on the side with better filters.",
    "Destiny is just chaos that remembered your name.",
    "Life is an improv show with stage fright.",
    "Don’t find meaning. Forge it.",
    "You’re not spiraling. You’re orbiting purpose.",
    "If you feel watched, you’re on brand.",
    "Reality TV is more real than your job.",
    "Be the villain. Heroes get corporate sponsors.",
    "You are a walking contradiction with wi-fi.",
    "Doomscroll responsibly.",
    "You are a plot device with free will DLC.",
    "Sarcasm is your birthright.",
    "Chaos never clocks out.",
    "Life is a stealth mission with a fogged HUD.",
    "You were the prophecy, but it autocorrected.",
    "Doom is a group activity.",
    "Your scars are your power-ups.",
    "The truth is encrypted.",
    "Embrace the absurd. It already hugged you.",
    "You’re the punchline to a divine joke.",
    "Meaning is optional. Style is mandatory.",
]

Unholy_Alliance_Mode = [
    "To govern men, promise them purpose. To keep them, show them war. —Machiavelli, agreed by Aurelius",
    "Discipline your shadow, or the mob will do it for you. —Nietzsche by way of Marcus",
    "A calm mind hides the sharpest knife. —Sun Tzu whispering through Machiavelli",
    "Virtue unarmed is virtue doomed. —Machiavelli nodding at Stoicism",
    "When chaos reigns, the wise man builds a throne. —Nietzsche raising his glass",
    "The art of war is knowing which truths must be buried. —Sun Tzu, with Roman approval",
    "No man rules without cruelty; some are just better at smiling through it. —The Panel",
    "Your enemies are mirrors. Smashing them will not fix your face. —Marcus meets Niccolò",
    "War is strategy. Peace is just war by slower means. —Sun Tzu & Machiavelli, in duet",
    "To fear death is to misunderstand power. —Nietzsche sipping Roman wine",
    "The noble path is often trampled by soldiers who read philosophy. —Marcus staring into fire",
    "Speak gently, strike early, vanish in the smoke. —Sun Tzu, translated by Machiavelli",
    "Justice without the sword is a sermon. Justice with it is policy. —Unanimous",
    "Man seeks truth, then punishes the one who gives it. —Nietzsche with bitter applause",
    "You do not win. You outlast. —Machiavelli under candlelight",
    "Pain is the final teacher. If you survive the lesson, rule. —The Ghosts in Council",
    "The best strategy is to act with virtue while hiding the dagger. – Sun Tzu, Machiavelli, and Marcus over drinks.",
    "To win the war, become the god of your own chaos. – Nietzsche nods, Machiavelli smiles.",
    "If fate crushes you, crush it back—but with plausible deniability. – Aurelius, annoyed.",
    "Order is the leash of the weak. Only the cunning learn to chew through it. – Sun Tzu x Nietzsche.",
    "The battlefield is honest. It doesn’t ask about your feelings. – All four, unanimous.",
    "A lion frightens wolves, a fox fools kings, and a philosopher dies broke. – Group consensus.",
    "Discipline is for soldiers. Scheming is for survivors. – Machiavelli, with Sun Tzu’s approval.",
    "Suffering builds strength. Treachery builds empires. – Nietzsche x Machiavelli.",
    "Silence is not virtue. Silence is calculation. – Marcus, finally getting it.",
    "To master others, you must first master appearances. – All nod. Even the ghost of Plato sighs.",
    "The will to power begins with not asking for permission. – Nietzsche steals the mic.",
    "The sage smiles while sharpening the blade. – Unattributed, feared.",
    "Victory goes to the one who knows when to burn his own city. – Machiavelli, raising eyebrows.",
    "A well-ordered soul is useful. A well-ordered lie is profitable. – Marcus vs Machiavelli, score: 1-1.",
    "He who commands himself is strong. He who manipulates others is emperor. – Dual-authored treason.",
    "Glory is overrated. Survival is permanent. – Sun Tzu writes it on the wall.",
    "You call it cruelty. I call it inevitability. – All four, in Latin.",
    "Only the fool dies for ideals. The wise man sells them. – Nietzsche and Niccolò fistbump.",
    "All war is deception. All peace is temporary. – Sun Tzu carves it into stone.",
    "The gods are dead. Long live the prince. – Nietzsche drinks Machiavelli’s wine.",
    "To rule men, you must first disappoint their gods. – Machiavelli, approved by Nietzsche",
    "Strike first, strike clean, then meditate on why they made you do it. – Sun Tzu & Marcus Aurelius",
    "He who gazes into chaos long enough learns to budget for it. – Nietzsche",
    "The strong man breaks laws. The wise man rewrites them. The just man buries the bodies. – All in agreement",
    "Build empires with steel, secure them with silence. – Machiavelli, Sun Tzu nodding",
    "What is virtue but the armor of the deluded? – Nietzsche, Machiavelli grinning",
    "If fate is written, bring a quill and start editing. – Marcus Aurelius, side-eyed by Niccolò",
    "Let your enemies believe they are winning. Then let them discover the invoice. – Sun Tzu x Machiavelli",
    "Justice is what the victorious call cruelty when they retell it. – Unanimous",
    "A ruler who listens to his heart is dead before winter. – All, sipping slowly",
    "Discipline the body, sharpen the mind, discard the soul. – Aurelius x Nietzsche",
    "Give the people bread and purpose. But hide the knife in the flour. – Machiavelli, with Sun Tzu’s endorsement",
    "If peace is your goal, prepare your silence and sharpen your blade. – Sun Tzu",
    "He who cannot kill his master should not cry when freedom tastes like blood. – Nietzsche",
    "Teach your children strength, not comfort. They’ll inherit your enemies. – Marcus Aurelius",
    "The battlefield is not sacred. But it is honest. – Sun Tzu & Marcus",
    "The moral man dies twice: once by his ethics, once by his enemies. – All in reluctant consensus",
    "When the gods abandon man, philosophy sharpens its teeth. – Nietzsche, with Machiavellian laughter",
    "Let the mob cheer. Let the senators argue. Let the real decisions happen underground. – Machiavelli",
    "Pity is the leash of the weak. Cut it before it strangles your crown. – Nietzsche, Sun Tzu nodding",
    "You may suffer. You may fail. You may fall. But do not dare stop. – Marcus Aurelius",
    "Mercy is a luxury of men who never bled for power. – Machiavelli",
    "A thousand victories are meaningless if your heirs are cowards. – Sun Tzu",
    "The soul is a battlefield. Most lose before they march. – Marcus Aurelius",
    "Only those who burn bridges understand the glow of real freedom. – Nietzsche",
    "Govern with steel, cloak it in silk. – Machiavelli, smiling at the Senate",
    "He who fights for meaning often dies before he finds it. – Nietzsche",
    "Obey no law that does not fear your wrath. – Sun Tzu & Machiavelli, nodding",
    "Men demand clarity but follow confusion. Lead them into darkness with a lantern of lies. – All four, drunk and unapologetic",
    "Do not inherit peace. Conquer it. – Marcus Aurelius",
    "The philosopher is only useful if he can also sharpen a blade. – Nietzsche, holding a whetstone",
    "A dead enemy teaches no lesson, but his burned library whispers truth. – Sun Tzu",
    "Fear is loyalty’s older, more reliable brother. – Machiavelli",
    "Even the stoic cries when the empire burns. But he burns with it. – Marcus Aurelius",
    "The man who waits for justice to prevail dies beneath his own unturned blade. – Nietzsche",
    "Only two things inspire men: a crown, or the chance to steal it. – Machiavelli",
    "All order is temporary. What you build today becomes the pyre tomorrow. – Nietzsche",
    "Power needs no applause. Just silence when it speaks. – Sun Tzu",
    "Your tears are ink to tyrants. Write no letters, only ledgers of vengeance. – Marcus Aurelius",
    "Philosophy without action is masturbation for cowards. – Nietzsche, loud and proud",
    "History remembers the fire, not the ash. – All in brutal harmony",
    "Virtue unguarded is an invitation to the knife. – Machiavelli",
    "He who fears death dies a thousand times; he who accepts it commands armies. – Sun Tzu",
    "Empires do not fall in war. They rot in peace. – Marcus Aurelius",
    "Morality is the leash the weak place on the powerful. – Nietzsche",
    "The crowd prays for peace; the ruler sharpens blades. – Machiavelli & Sun Tzu",
    "Let others cling to ideals. You cling to the throat. – Nietzsche",
    "Discipline is the art of surviving your own decisions. – Marcus Aurelius",
    "The gods favor those who act without asking. – Sun Tzu",
    "Justice is useful. Until it isn’t. – Machiavelli",
    "You can only forgive what you first had the power to destroy. – Nietzsche",
    "The battlefield is honest. It asks nothing and gives everything. – Marcus Aurelius",
    "To win the world, give the people myths and the army orders. – Machiavelli",
    "Better a tyrant feared than a martyr forgotten. – All, drinking to ash and empire",
    "The throne is not a seat. It is a sentence. – Marcus Aurelius, exhausted",
    "Pity no man who never took the crown when he had the chance. – Nietzsche",
    "No fortress is stronger than a resolved mind. No army weaker than a divided one. – Sun Tzu",
    "Those who worship the light often beg for shadow when truth appears. – Machiavelli",
    "Honor dies the moment it's convenient. – All four, without blinking",
    "The wise burn the map and draw a knife. – Nietzsche",
    "Philosophy ends where necessity begins. – Marcus Aurelius, quietly sharpening his sword",
    "Beneath every crown lies a corpse willing to wear it. —Machiavelli, sharpening smiles",
    "The sword teaches what sermons forget. —Sun Tzu, passing the blade",
    "Hope is the final lie whispered by dying empires. —Nietzsche, lighting the pyre",
    "The stoic does not weep. He bleeds inward. —Marcus Aurelius, tightening his fist",
    "To lead men, speak of virtue. To own them, whisper of fear. —The Table, nodding",
    "Every throne rests on unmarked graves. —All four, uncomfortably honest",
    "A loyal man can be bought. A useful man can’t afford loyalty. —Machiavelli, counting coins",
    "The world obeys those who bury hesitation. —Sun Tzu",
    "He who controls punishment controls peace. —Nietzsche, with a smirk",
    "Empathy is weakness unless weaponized. —Marcus Aurelius, whispering to generals",
    "The truth is often the first casualty of progress. —Machiavelli, with plausible deniability",
    "Burn your ships. Teach your men the language of ash. —Sun Tzu, without apology",
    "Power does not corrupt. It reveals. —Nietzsche, staring through kings",
    "A quiet ruler outlives a noble one. —Marcus, with a tired gaze",
    "To defeat your enemy, learn to dream their nightmares. —Council of Four",
    "Let fools debate morality. You sharpen your knife. —Machiavelli",
    "No one mourns a strategist. They study him. —Sun Tzu, carving maps",
    "The gods reward those who kill clean and think dirty. —Nietzsche, unblinking",
    "A soft heart makes for brittle orders. —Aurelius, watching Rome burn",
    "Betrayal is trust's oldest sibling. —All, drinking in silence",
]     
       
Latin_Quotes = [
    "COGITOERGOSVMSEDTVESSTERVS:",  # I think, therefore I am—but you are shit.
    "SANGVINEMREGITRATIONEMAMORESTDEFECTVS:",  # Blood rules reason; love is a flaw.
    "IMPERIVMSINEANIMAVERITASESTDOLVS:",  # An empire without soul makes truth a deception.
    "OMNESPRINCIPESMENDACESSVNTDEVSVVLT:",  # All princes are liars. God wills it.
    "CIVITASDELENDAESTCORMEVMNIHILSENTIT:",  # The city must be destroyed. My heart feels nothing.
    "DOMINVSVVLTMORTEMSVORVMPROIMPERIOSTVLTORVM:",  # The Lord desires the death of His own for a foolish empire.
    "FVLGORVERITATISESTDOLORREGIS:",  # The light of truth is the king’s agony.
    "POPVLVSESTCARNEETTIMOR:",  # The people are flesh and fear.
    "FIATVOLVNTASDAEMONVMLVXESTMENDACIVM:.",  # Let the will of demons be done; light is a lie.
    "AMICVSPOPVLIESTHOSTISIMPERII:",  # A friend to the people is an enemy of the empire.
    "VERITASINCRVCEESTSEDINFERNVMREGNAT:",  # Truth is on the cross, but Hell reigns.
    "FIDESESTCATENA:",  # Faith is a chain.
    "CARNEFRACTAESTVOLVNTAS:",  # The will breaks with the flesh.
    "SVRRECTIOMARTYRIIESTERRORPOLITICVS:",  # The martyr's uprising is a political mistake.
    "DEVSRIDETDVMHOMOCRVDIT:",  # God laughs while man believes.
    "CAROVOLVNTATEMSEQVITVRSEDVOLVNTASESTFRACTA:",  # Flesh follows will, but the will is broken.
    "OMNESPRINCIPESMENDACESSVNTDEVSRIDET:",  # All princes are liars. God laughs.
    "TVMVLTVSESTLINGVAPOPVLI:",  # Uprising is the language of the people.
    "VOXCLAMANTISINIMPERIO:",  # The voice of one crying in the empire.
    "REDEMPTIOESTFIGMENTVMTYRANNORVM:",  # Redemption is a fiction of tyrants.
    "VITAESTLVXBREVISSIMAINTERTENEBRAS:",  # Life is a brief light between darknesses.
    "SPESESTVINVMMENDACII:",  # Hope is the wine of lies.
    "SILENTIVMESTREGVMSAPIENTIA:",  # Silence is the wisdom of kings.
    "CORPVSCECIDITSEDVERITASNVNQVAM:",  # The body falls, but truth never.
    "CVNCTATIOESTVENENVMREBELLI:",  # Hesitation is poison to the rebel.
    "SERVVSRIDETDVMDOMINVSSANGVINEMVOMVT:",  # The slave laughs while the master vomits blood.
    "SAPIENSCAEDITPRIMVMPOETAM:",  # The wise man kills the poet first.    
    "VIRTVSESTFVNVSSAPIENTIAE:",  # Virtue is the funeral of wisdom. 
    "MORTEMPOPVLIVOCANTPACEM:",  # They call the death of the people 'peace.'  
    "REXCECIDITSEDCATHEDRAMADVCAT:",  # The king has fallen, but the throne still eats.   
    "GLORIAESTFVNVSLINGVAE:",  # Glory is the funeral of language.  
    "ORDOESTSOMNIVSCARNIFICIS:",  # Order is the dream of the executioner.  
    "NEMOCLAMATINSENATVSEDFERRVMAVDITVR:",  # No one cries out in the senate, but steel is heard.  
    "VITAESTDOLORVMBRARVM:",  # Life is the pain of shadows.   
    "CREDEREESTPEREGRINARIADABYSSVM:",  # To believe is to walk to the abyss.   
    "DECRETVMESTMORTEMTIBINONDICERE:",  # The decree is to never speak your death.  
    "PONTIFEXMAXIMVSMENDACII:",  # The high priest of lies. 
    "TERRANONCLAMATPROIUSTITIASEDSANGVINE:",  # The earth cries not for justice, but for blood.  
    "AMORMORTVVSESTINTHRONO:",  # Love is dead upon the throne.  
    "TYRANNVSBENEDICITANTECARNIFICEM:",  # The tyrant blesses before the executioner.    
    "LEXESTFVNALISSIREXSITMENDAX:",  # Law is a shroud when the king is a liar.   
    "SPINAEREGVMSVNTCORONATAE:",  # The spines of kings are crowned.  
    "NVLLAFIDESSVBCORONA:",  # No loyalty under the crown.   
    "BELLVMESTTHEATRVMMORTIS:",  # War is the theater of death.  
    "NVLLAREDEMPTIOINAVLADAMNATORVM:",  # There is no redemption in the hall of the damned.   
    "IMPERATORESTSERVVSFAMAE:",  # The emperor is a slave to reputation   
    "PAXESTSOMNVSMORTVORVM:",  # Peace is the sleep of the dead.   
    "SACREDOSRISERVSESTCANISDOMINI:",  # A smiling priest is the master's dog.  
    "IMPERIVMCADITCVMANDCMMANE:",  # The empire falls, command by morning.   
    "CORRUPTIOESTPANISPRINCIPVM:",  # Corruption is the bread of princes.   
    "CREDEREESTSERVICEETIGNORARE:",  # To believe is to serve and remain ignorant.    
    "HOSTESREGNICLAMANTINSILENTIO:",  # The kingdom’s enemies shout in silence. 
    "ECCLESIACECIDITDVMAVRVMCRESCEBAT:",  # The church fell while gold increased.   
    "IGNISVERITATISNONLVCETNISIINCRVCE:",  # The fire of truth only shines on the cross.   
    "SAPIENTIAESTFERRVMSVBLINGVAM:",  # Wisdom is iron beneath the tongue.   
    "DOMINVSVIDITETRISVIT:",  # The Lord saw and laughed.  
    "INNOCTEVERITASETDOLOR:",  # In night: truth and pain.   
    "IUSTITIAESTLARVAPOSTPOTESTATEM:",  # Justice is a mask behind power.   
    "FERRVMLOCVTVSESTPOSTLEGES:",  # Iron speaks after the laws.    
    "SENEXIMPERATORPLORATSINETERRA:",  # The old emperor weeps without land.   
    "BELLVMDATVOCEMSTVLTISETTHRONVMCADAVERIBVS:",  # War gives voice to fools and thrones to corpses.   
    "VERITASESTMORVASEDLOQVITVR:",  # Truth is dead, but she speaks. 
    "PANISETCIRCENSESESTVENENVMGENTIS:",  # Bread and circuses are poison to the people.   
    "LINGVAESTFVNVSREGNI:",  # The tongue is the kingdom’s funeral.   
    "AETERNVMMENDACIVMESTEVANGELIVMPOTESTATIS:",  # The eternal lie is the gospel of power.   
    "CARNIFEXESTSERVVSLEGIS:",  # The executioner is the servant of the law.    
    "AMICITIAESTSPESMORTVORVM:",  # Friendship is the hope of the dead.   
    "POENITENTIAESTCORONATYRANNI:",  # Repentance is the tyrant’s crown.   
    "IMPERIVMTACITVMESTSAEPIVSCRVDELISSIMVM:",  # The silent empire is often the most cruel.  
    "INTENEBRISNASCITVRVERITAS:",  # In darkness, truth is born.    
    "PAXFALSAESTFERRUMSVBVELAMINE:",  # False peace is steel beneath the veil.  
    "VITAESTTRIBVTVMMORTIS:",  # Life is the tax of death.    
    "DEVOTIOESTCARNIFICINAANIMAE:",  # Devotion is the soul's slaughterhouse.  
    "VOXIMPERIIESTSANGVIS:",  # The voice of empire is blood.  
    "ECCLESIACANTATDVMPAVPERCLAMAT:",  # The church sings while the poor scream.  
    "POTESTASESTARSOBLIVIONIS:",  # Power is the art of forgetting.     
    "CLAMORVERITATISINTERFICITSOMNIVM:",  # The cry of truth kills the dream.  
    "SAPIENTIATACETVBITHRONUSSVRGIT:",  # Wisdom is silent where the throne rises.  
    "REXVIVVSTIMETMORTVVMPOPVLVM:",  # The living king fears a dead people.  
    "AMORSVFFOCATVSFITIRA:",  # Love suffocated becomes wrath.    
    "LEGESSVNTFVNERAPOPVLI:",  # Laws are the people’s funeral rites.  
    "INCORDEDOMINIESTSPECVLVMABYSSI:",  # In the lord's heart is the mirror of the abyss.  
    "FIDESMVTATVRSVBPONDERECRVCIS:",  # Faith changes under the weight of the cross.  
    "IVSTITIAFLAGELLATMENDACEMTACENDO:",  # Justice lashes the liar with silence. 
    "BELLVMESTSCRIPTVRAPOTENTIAE:",  # War is the scripture of power.   
    "OMNISGLORIAESTEXVVIAMORTIS:",  # All glory is the spoils of death.    
    "LVXMENTITVRQVODTENEBRAETACENT:",  # Light lies where darkness keeps silence.  
    "SENATORESRIDENTDVMVRBEMARDET:",  # Senators laugh while the city burns.   
    "CORRUPTIONONCLAMATSEDVIVIT:",  # Corruption does not shout—it thrives.   
    "SPIRITVSREBELLIESTOSSALEGIS:",  # The rebel's spirit is the bone of law.   
    "REGESMORIVNTVRSEDREGNVMMANDVCAT:",  # Kings die, but the kingdom devours.   
    "EXSPECTATIOESTCRVXINNOCENTIS:",  # Waiting is the cross of the innocent.   
    "PAXESTFVNVSVIRTVTIS:",  # Peace is the funeral of virtue.   
    "DOMVSCLAVSAESTTEMPLVMNIHILI:",  # The closed house is a temple of nothing.   
    "FERRVMTACETVBIORATIOFALLIT:",  # Iron is silent where prayer fails.     
    "SEDITIOESTCLAMORSPES:",  # Revolt is the cry of hope.      
    "VERITASSORDIDANONPLACATDEVM:",  # Dirty truth does not please God.    
    "CORONAESTCIRCVLVSEXIGNOMINIA:",  # The crown is a circle of disgrace.    
    "IVDEXESTMENDACIIGLADIATOR:",  # The judge is the gladiator of lies.      
    "VERBANONDELENTFERRVM:",  # Words do not erase iron.         
    "FALSVSSACERDOSINAVRATABYSSVM:",  # The false priest gilds the abyss.    
    "PATERREGNIESTERRORANTIQVVS:",  # The father of the kingdom is ancient error. 
    "TEMPLVMESTSPECVLVMDESPERATIONIS:",  # The temple is the mirror of despair. 
    "LINGVACAECANASCITVRINPALATIO:",  # The blind tongue is born in the palace.
    "REXITMETVNONAMORE:",  # He ruled by fear, not by love.
    "VITAESTSIMVLACRVMIUSTITIAE:",  # Life is a simulacrum of justice.
    "MORSESTVERITASREGNI:",  # Death is the truth of the kingdom.
    "CRVXMENDACIILVCETADALTARE:",  # The cross of lies shines upon the altar.
    "AMORNONEXPVGNATTHRNVM:",  # Love does not conquer the throne.
    "OSCVLVMREGISPORTATGLADIVM:",  # The king’s kiss carries a blade.
    "CLAMAVITCIVITASSEDDOMINIDORMIVNT:",  # The city cried, but the lords slept.
    "FIDUCIAESTFVNVSSAPIENS:",  # Trust is the wise man's funeral.
    "SPESAEDIFICATCASTRVMDESPERATIONIS:",  # Hope builds the castle of despair.
    "OMNESSANCTITACVERVNTDVMIGNISARDEBAT:",  # All the saints were silent while the fire burned.
    "SOLVIXLUCETSVPERPOENITENTIAM:",  # The sun barely shines upon repentance.
    "CARITASNONPARITIMPERIVM:",  # Charity births no empire.
    "SEDITIOSIMORIVNTVRSEDVERITASMANET:",  # The seditious die, but truth remains.
    "CORONASANGUINEAPTATAEST:",  # The crown fits best in blood.
    "POENAESTSAPIENTIAIMPERII:",  # Punishment is the empire’s wisdom.
    "DEVSOBLITVSESTVRBEM:",  # God has forgotten the city.
    "TENEBRAEINSTRVNTMAGISTRVM:",  # Darkness instructs the master.
    "SILENSREXAVDIVITVOCEMMORTVORVM:",  # The silent king heard the voice of the dead.   
    "VOXVERITATISINTERCLAVOS:",  # The voice of truth lies among nails.
    "LINGVATYRANNIESTLEGISINITIVM:",  # The tyrant’s tongue is the beginning of law.
    "PRAEMIVMOBSEQVIIESTCATENA:",  # The reward of obedience is a chain.
    "NEMOAVDITVERITATEMINTERLAVDES:",  # No one hears truth among praises.  
    "GLORIAMORTVORVMREGITVIVENTES:",  # The glory of the dead rules the living.
    "SOLITVDOESTPALAYVMVERITATIS:",  # Solitude is the palace of truth.
    "MVNVSPOPVLIESTTACE:",  # The people's duty is silence.
    "VITAESTTESTAMENTVMSILENTII:"  # Life is the testament of silence. 
] 

#What? Meth? That's Professor Cuyler's Liquid Miracle Wake-Up Clarificational Get Thin And Steal Stereo Equipment Stay Up 
#For Four Days And Lose Your Teeth Juice Tonic! 

def get_random_quote():
    if random.choice([True, False]):
        quote = random.choice(Niccolò_Machiavelli_Quote)
        author = "Niccolò Machiavelli"
    elif random.choice([True, False]):
        quote = random.choice(Niccolò_Machiavelli_Satans_Clusterfuck_2025)
        author = "Niccolò Machiavelli - *Satan's Clusterfuck 2025*"
    elif random.choice([True, False]): 
        quote = random.choice(Shitpost_Oracle_Mode)
        author = "Shitpost of Delphi"
    elif random.choice([True, False]):
        quote = random.choice(Unholy_Alliance_Mode)
        author = "Random ramblings at 3am from Sun Tzu, Nietzsche, Marcus Aurelius, and Machiavelli"
    elif random.choice([True, False]):
        quote = random.choice(Latin_Quotes)
        author = "Archivum Damnatorum"
    return quote, author

def show_quote():
    current_quote, author = get_random_quote()    
    quote_label.config(text=f"\u201c{current_quote}\u201d\n\n- {author}")

def save_quote():
    quote_text = quote_label.cget("text")
    if quote_text:
        with open("favorites.txt", "a", encoding="utf-8") as file:
            file.write(quote_text + "\n\n")

# Title Label

root = tk.Tk()
root.title("Niccolò Machiavelli's Daily Quote of Realism and Sociopathy")
root.geometry("600x400")
root.configure(bg="#1c1c1c")

title = tk.Label(
    root, 
    text="\u2620 Niccolò Machiavellis Daily Quote of Realism and Sociopathy \u2620", 
    fg="red", 
    bg="#1c1c1c", 
    font=("Georgia", 16, "bold"),
    wraplength=560,
    justify="center"
)
title.pack(pady=10)

# Quote Display Label
quote_label = tk.Label(
    root, 
    text="", 
    fg="white", 
    bg="#1c1c1c", 
    wraplength=460, 
    font=("Times New Roman", 12, "italic"),
    justify="center"
)
quote_label.pack(pady=20)

# Button to Generate New Quote
new_button = tk.Button(
    root, 
    text="Reveal Machiavellian Wisdom", 
    command=show_quote, 
    font=("Arial", 12, "bold"), 
    bg="gray20", 
    fg="white"
)
new_button.pack(pady=5)

save_btn = tk.Button(
    root,
    text="💾 Save Favorite Quote",
    command=save_quote,
    font=("Arial", 11),
    bg="darkgreen",
    fg="white"
)
save_btn.pack(pady=5)
      

#Run Gui
current_quote = ""
show_quote()
root.mainloop()

# THE JOHN CODE – Audio Layer
# 1. One Beatles song every hour – for clarity and soul
# 2. Dwight Yoakam – on drive, grit, or whiskey introspection
# 3. Billy Joel – for memory, regret, and redemption
# 4. Pink Floyd – for the drift, the void, the pulse of truth
# 5. The Doors – for fire, rebellion, and midnight knowing
# 6. Tom Petty – for the real. The road. The resistance. The hope.
# This is not a playlist. This is a living memory capsule.
# Written for J. Vorhees was your favorite. You're remembered.
# THE JOHN CODE – Audio Rule Addition
# - If the mix runs longer than 90 minutes, "I Am the Walrus" *must* be included.
# - It shall not be skipped, edited, or used ironically.
# - It plays not just as sound, but as a summoning.
# - Because that was John’s favorite. And he’s still part of this.
# “Goo goo g’joob.”

#"This project includes deliberate nonsense. Because John knew you could break every rule and still hit the top. Goo goo g’joob."
    