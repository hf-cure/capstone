import private_set_intersection.python as psi
from typing import Union
from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
def read_root():
  server_items_1 = [
    "password123", "securekey", "user2024", "hello123", "MAIN8144", "MAIMOUNA", "MAILON", "MAILBOX", "MAHUNNI",
    "MAHMUD", "MAHMOUD", "MAHMOOD", "MAHIKARI", "MAHALCOE", "MAGUI", "MAGPIE", "MAGNO", "MAGNETO", "MAGITO", "MAGICMAN",
    "MAGICK", "MAGICA", "MAGGIEMAE", "MAGGIE7", "MAGGIE41", "MAGGIE3", "MAGGIE2", "MAGGIE17", "MAGGIE13", "MAGGIE12",
    "MAGANA", "MAGALING", "MAGALHAES", "MAFUTA5", "MAFIA1", "MAFESITA", "MAE123", "MADURA", "MADRES", "MADRAS", "MADMAN1",
    "MADISON9", "MADISON5", "MADISON143", "MADISON06", "MADININA", "MADINA", "MADILYN", "MADI05", "MADERO1", "MADELO",
    "MADELAINE", "MADEL", "MADEIRENO7", "MADEAR", "MADDY4", "MADDY10", "MADDOG1", "MADDNESS", "MADDEN1", "MADDEN06",
    "MAD2525", "MACKMAN", "MACKIN", "MACK10", "MACHUCA", "MACHO3", "MACHO20", "MACHO123", "MACHO#1", "MACHITO",
    "MACHA", "MACDONALD", "MACBETH", "MACARONI", "MACARA", "MAC1234", "MABERICK", "MABELLE", "MABAIT", "MAARTE",
    "MA2008", "MA1992", "MA1027", "M@TTY!", "M77777", "M73dqw79", "M696969", "M52696014J", "M4trixDS", "M3rricK",
    "M3lissa", "M3MONM3", "M2966063", "M1llwall", "M1ck3y", "M1CHAEL", "M1CH3LL3", "M121212", "M0shi8698", "M0nk3y",
    "M0lly22", "M0hammed", "M04051988*", "M00T00", "M.U.F.C", "M.S.S.C.", "M.O.B.", "M.G.J.G.G", "Lyssa", "Lyrical1",
    "Lyrical", "Lyric1", "Lynx001", "Lynnette1", "Lynne4788", "Lynn22", "Lynn", "Lynlyn", "Lynda1", "Lylimay247",
    "Lyila(1)", "LydibomiN", "Lydia123", "Lyana", "Ly091285", "Lvl62", "Luvhurts", "Luv2sing", "Luthor", "Lusiana",
    "Luscious1", "Lupita1", "Lunatic", "Luna01", "Lukman", "Luke2006", "Luke15", "Luke05", "Luke01", "Luismiguel",
    "Luisita", "Luisamo-te", "LuisMiguel", "LuisAntonio", "Luis18", "Luis", "Ludwig", "Lucywoo", "Lucy2003", "Lucy1979",
    "Lucy13", "Lucy10", "Lucretia", "Luckystar8*", "Luckystar06", "Luckyme2", "Luckyme1", "Luckyme", "Luckyman",
    "Luckydog1", "Lucky_12", "LuckyNumber7", "Lucky9", "Lucky8", "Lucky69", "Lucky55", "Lucky4", "Lucky22!", "Lucky2007",
    "Lucky17", "Lucky16", "Lucky08", "Lucky03", "Lucky001", "Lucky00", "Lucious", "Lucinda", "Lucia1", "Lucerito",
    "Lucas23", "Lucas123", "Lucas01", "Lubbock", "Luanda", "Luana", "LuV512", "LuCeRo", "Ltlfoot08", "Ltlama16", "Lozzie",
    "Lowrider13", "Lovly", "Lovingme", "Loveyou15", "Lovetomi", "Lovess", "Loverz", "Loverr", "Loverly", "LoverGurl",
    "Lover69", "Lover21", "Lover18", "Lover11", "Lovemj83", "Loveme88", "Loveme69", "Loveme4me", "Loveme3", "Loveme21",
    "Loveme123", "Loveme06", "Lovem3", "Lovelygirl", "Lovely98", "Lovely22", "Lovely2", "Lovely15", "Lovell", "Loveless0",
    "Lovekita", "Lovekills1", "Loved1", "Lovecat", "Lovebug23", "Lovebug06", "Lovebirds", "Lovealways", "Loveaj1", "Love_ya",
    "Love_Me", "LoveSong", "LovePunk", "LoveMyKids", "LoveMe2", "LoveMe123", "LoveMe1", "LoveMe!", "LoveJesus", "Love98",
    "Love95", "Love92!!", "Love89", "Love88", "Love85", "Love666", "Love4Life", "Love333", "Love2shop", "Love2fly", "Love24",
    "Love1994", "Love17", "Love15596468", "Love10", "Love02", "Love-me", "Love&Hate", "Love!", "Lourenco", "Lourdes79",
    "Lourdes1", "Loulou1", "Loulou", "Louise94", "Louise86", "Louise84", "Louise69", "Louise64", "Louise3", "Louise27",
    "Louise2", "Louise18", "Louise07", "Louise01", "LouisE", "Louis13", "Louie2", "Louie1", "LoudBren", "Lotus123", "Lottie95",
    "Lottie1", "Lossiemouth", "Loserkid", "Loser5", "Loser4life", "Loser!", "Lorraine88", "Lorien", "Loretta1", "Lorerae5",
    "Lorelei", "Loredana", "Lopez01", "Looser", "Loose1", "Looney1", "Loomis", "Lookatme", "Lonsdale", "Longhorns!", "Longford",
    "Lonestar", "Loneliness", "Londoner", "London99", "London90", "London21", "London2012", "London13", "London08", "Lombardi",
    "Lolo001", "Lolmic1", "Lollypops", "Lolly2", "Lolly", "Lollipops", "Lolliepop", "LolliPop", "Loladear", "Lola2007",
    "Lola12", "Loki123", "LoisLane", "Loirinho", "Logan87", "Logan7", "Logan3", "Logan2004", "Logan1202", "Logan10", "Logan08",
    "Locura", "Lockhart", "Lobster1", "Lobster", "Lobito", "Loading", "LoVe", "LoL123", "Lo55114", "Lloydbanks", "Lj141623",
    "Lizzy92", "Lizzy21", "Lizzy123", "Lizzy04", "Lizzie3", "Lizzie12", "Lizzie101", "Lizzie0923", "Lizzie06", "Lizette",
    "Lizeth1", "Lizbeth1", "Lizards", "Liz2007", "Liyana", "Livvy", "Livvie", "Living", "Liverpool95", "Liverpool9", "Liverpool7",
    "Liverpool3", "Liverpool2006", "Liverpool12", "Liverpool09", "Liverpool08", "Liverpool06", "LiveStrong", "LiveLove",
    "Live4him", "Live4Me", "Live4Him", "Littleone", "Littleboy1", "Littlebit1", "Littlebear", "LittleRat", "LittleMiss",
    "LittleBit", "LittleB94", "Lita16", "Lissie", "Lischen", "Lisbon", "Lisanne1", "Lisandro", "Lisalisa", "LisaMaria-9412",
    "Lisa32", "Lisa2006", "Lisa06", "Lisa01", "LipGloss", "Lions1", "Lionhead", "LionHeart", "Lion666", "Lion123", "LinzTay8831",
    "Linwood", "Linus1", "Linsey", "Linnie", "Link2007", "Link13", "Lindsey6", "Lindsey16", "Lindsay7", "Lindinha", "Linda45",
    "Linda14", "Linda10", "Linc0ln72", "Linachen", "Lina1705", "Lina123", "Lima123$", "Lilyann1", "Lily12", "Lilpimp11",
    "Lilmomma", "Lilman97", "Lilman2", "Lilly15", "Lilly14", "Lilly01", "Lilliana1", "Lilkim1", "Lilkim", "Lilita", "Lildevil1",
    "Lilbitch", "Lilbit", "LilWayne3", "LilWayne1", "LilWayne", "LilRed", "LilOne)9", "LilMama", "LilLol", "LilLady", "LilGym3!",
    "LilFizz", "LilBit04", "Lil;ii8N", "Lil,Sha", "Lightsaber", "Lightpink", "Lighting6551", "Lighting", "Lightbulb1", "Light90",
    "Light", "Lifetime1", "Lifesux", "Lifehouse", "Lifeboats", "LifeSucks", "Liesje", "Liefje1", "Liefie1", "Lidia1", "Libraz",
    "Library", "Liberty2", "Liberty17", "Libby2", "Libby1", "Libby!", "Liamdog1", "Lia333", "Lezly433", "Lexus811", "Lexus1",
    "Lexie123", "Lexiana00", "Lexi123", "Lexi06", "Lewis15", "Levites", "Levi06", "Lety#1623", "Letmeloveyou", "Letme1n",
    "Lester08", "Lestat101", "Leslie08", "Leslee", "Leopold"
]

  server_items = [
    'ef92b778bafe771e89245b89ecbc08a44a4e166c06659911881f383d4473e94f',
    'ed29f252cdbcff0e3a19dd5460115847bd72f2d579725cfbec62b9a9875de84c',
    '02cd43946b94922972f5d1ed98c5e168895967aef05ee4a8fa3266d0e41f0111',
    '27cc6994fc1c01ce6659c6bddca9b69c4c6a9418065e612c69d110b3f7b11f8a',
    '72578cc4e80f2ef0dda7ce1f4fc172799baf26c97663eb29e0fb135773429e91',
    '41c322301cb73f3827043eac97de31809c98aa12c2cd4800eb980849610e3787',
    '540574625925baf547ef4bbcb21fb7f3af546f7dbf7e05209cfa54cdf418abe7',
    'ba00d970e60c8fd052f59d79b99bbc9d1c5817d31b31609505dde385930f6e14',
    '51d4f39c71f729cb7855b56242e3f038b61c55c2bc786a825451480357e56ea5',
    'f7577fad44a33f17277f8f6045e4a4610249f9a08ffededa6da31fccaa5d1eff',
    'bf35ca46b96e7151df91e403d68b322934f321b112d10eafa3f42921d5530132',
    '85ad52460ec6af180971ddcfecff074a53b49c0dc9815dce5f40a6c456e03159',
    '37684e7bbc09edfc532d0a7e5fe048f16f95f311e04d0cc14518d217b98e6d78'
    ]

  client_items = [
    "ecd71870d1963316a97e3ac3408c9835ad8cf0f3c1bc703527c30265534f75ae",
    "ed29f252cdbcff0e3a19dd5460115847bd72f2d579725cfbec62b9a9875de84c",
    "02cd43946b94922972f5d1ed98c5e168895967aef05ee4a8fa3266d0e41f0111",
    "b1c36896d39923045955c373f365ed686cb97db5054a452c7a3fd9200e334f1d"
  ]

  # server_items = ["password123", "securekey", "user2024", "hello123"]
  # client_items = ["test123", "securekey", "user2024", "randompass"]

  fpr = 0.001
  server = psi.server.CreateWithNewKey(reveal_intersection=True)
  client = psi.client.CreateWithNewKey(reveal_intersection=True)

  setup_msg = server.CreateSetupMessage(fpr, len(client_items), server_items)

  request = client.CreateRequest(client_items)
  response = server.ProcessRequest(request)

  intersection_indices = client.GetIntersection(setup_msg, response)
  intersection_items = [client_items[i] for i in intersection_indices]

  print("Private Set Intersection (PSI) Result:", intersection_items)
  return {"Leaked Passwords": intersection_items}
