import discord
from discord.ext import commands
from bot_logic import gen_pass
from discord import app_commands
import random
import requests
import discord
import aiohttp
bear_images = ["https://plus.unsplash.com/premium_photo-1661849977833-c18cd1c7e295?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MXx8Z3JpenpseSUyMGJlYXJ8ZW58MHx8MHx8fDA%3D","https://images.unsplash.com/photo-1589656966895-2f33e7653819?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8Z3JpenpseSUyMGJlYXJ8ZW58MHx8MHx8fDA%3D","https://images.unsplash.com/photo-1568162603664-fcd658421851?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NHx8Z3JpenpseSUyMGJlYXJ8ZW58MHx8MHx8fDA%3D","https://images.unsplash.com/photo-1576076819613-26f8537ae375?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8OHx8Z3JpenpseSUyMGJlYXJ8ZW58MHx8MHx8fDA%3D","https://images.unsplash.com/photo-1588167056840-13caf6e4562a?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTB8fGdyaXp6bHklMjBiZWFyfGVufDB8fDB8fHww","https://plus.unsplash.com/premium_photo-1661878515974-9455f7e283de?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8OXx8Z3JpenpseSUyMGJlYXJ8ZW58MHx8MHx8fDA%3D","https://images.unsplash.com/photo-1595173425119-1c54835c1874?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTJ8fGdyaXp6bHklMjBiZWFyfGVufDB8fDB8fHww","https://plus.unsplash.com/premium_photo-1661940781747-5b4026f9ee1f?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTd8fGdyaXp6bHklMjBiZWFyfGVufDB8fDB8fHww","https://images.unsplash.com/photo-1635866869385-fabb68f0dea0?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTh8fGdyaXp6bHklMjBiZWFyfGVufDB8fDB8fHww","https://images.unsplash.com/photo-1559899551-4037d17859c0?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MjB8fGdyaXp6bHklMjBiZWFyfGVufDB8fDB8fHww","https://media.istockphoto.com/id/2216380632/photo/grizzly-bear-sow-grazing-on-lush-spring-grasses-in-yellowstone-national-park.webp?a=1&b=1&s=612x612&w=0&k=20&c=-sn4v0Glt1tAGTk12srsKh5cA01SpeBycJUYcoHSC4k=","https://media.istockphoto.com/id/926738156/photo/brown-bear-portrait.webp?a=1&b=1&s=612x612&w=0&k=20&c=cc9A8PIUW5QUkC4oHTFOc__PcNvIgZKIUSNh_VwgbTU=","https://media.istockphoto.com/id/2193627365/photo/grizzly-bear-growling.webp?a=1&b=1&s=612x612&w=0&k=20&c=1XBVdMUcDMh04sJWXyn4ZXnkmAMR8O09sUP1VdYnfO4=","https://media.istockphoto.com/id/2244854264/photo/portrait-of-a-brown-bear-stare-down.webp?a=1&b=1&s=612x612&w=0&k=20&c=uQeMBm1zOMyUei7mEY5O-3422WOuaDulPjcBWLPWiwk="
               ,"https://plus.unsplash.com/premium_photo-1695717076798-404f76f121da?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MXx8cGFuZGF8ZW58MHx8MHx8fDA%3D","https://images.unsplash.com/photo-1527118732049-c88155f2107c?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8cGFuZGF8ZW58MHx8MHx8fDA%3D","https://images.unsplash.com/photo-1597953601374-1ff2d5640c85?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8M3x8cGFuZGF8ZW58MHx8MHx8fDA%3D","https://images.unsplash.com/photo-1703248187251-c897f32fe4ec?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NHx8cGFuZGF8ZW58MHx8MHx8fDA%3D","https://plus.unsplash.com/premium_photo-1723425435727-61d67c4d91f3?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NXx8cGFuZGF8ZW58MHx8MHx8fDA%3D","https://images.unsplash.com/photo-1570288685369-f7305163d0e3?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8OHx8cGFuZGF8ZW58MHx8MHx8fDA%3D","https://images.unsplash.com/photo-1570288685369-f7305163d0e3?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8OHx8cGFuZGF8ZW58MHx8MHx8fDA%3D","https://images.unsplash.com/photo-1540126034813-121bf29033d2?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTF8fHBhbmRhfGVufDB8fDB8fHww","https://images.unsplash.com/photo-1525382455947-f319bc05fb35?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTJ8fHBhbmRhfGVufDB8fDB8fHww","https://images.unsplash.com/photo-1656899367728-cf0194bf3aeb?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTl8fHBhbmRhfGVufDB8fDB8fHww","https://images.unsplash.com/photo-1589656966895-2f33e7653819?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8cG9sYXIlMjBiZWFyfGVufDB8fDB8fHww","https://images.unsplash.com/photo-1593946460607-d1570da6268f?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8M3x8cG9sYXIlMjBiZWFyfGVufDB8fDB8fHww","https://plus.unsplash.com/premium_photo-1661867529492-4941c875b6c5?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MXx8cG9sYXIlMjBiZWFyfGVufDB8fDB8fHww",
               "https://www.bing.com/th/id/OIP.23zE1MpqlZzKaYDYe6VebQHaEK?w=193&h=135&c=8&rs=1&qlt=90&o=6&dpr=1.1&pid=ImgAns&rm=2","https://th.bing.com/th/id/OIP.pr4dDuG7G2D4ikZfNXdIlgHaFi?w=248&h=185&c=7&r=0&o=7&dpr=1.1&pid=1.7&rm=3","https://www.bing.com/th/id/OSK.HEROXgcAQ_urbDGLIBr1bONHMhL3FRUWk64EiM_tMYS1U4E?w=310&h=200&c=8&rs=1&qlt=90&o=6&dpr=1.1&pid=3.1&rm=2","https://www.bing.com/th/id/OSK.3lyuyMVmY3EGAOIlPymesklgF0yHAHwoTTTfCeXaOjs?w=224&h=200&c=8&rs=1&qlt=90&o=6&dpr=1.1&pid=3.1&rm=2"]

ciekawostki = ["Krowy mają „przyjaciół”: Badania wykazują, że krowy bardzo przywiązują się do swoich najlepszych przyjaciół w stadzie,"
                + " a rozłąka z nimi powoduje u nich odczuwalny stres.",
               "Genialny węch słoni: Trąba słonia składa się z około 40 tysięcy mięśni i jest tak precyzyjna,"
               + " że potrafi podnieść pojedyncze źdźbło trawy. Ich węch jest również znacznie czulszy niż u psów",
               "Ślimaki mogą zregenerować oko: Jeśli ślimak straci jedno ze swoich oczu, potrafi wyhodować nowe w procesie pełnej regeneracji",
               "Rekordowy skok pchły: Pchła potrafi skoczyć na odległość i wysokość stanowiącą 200-krotność długości własnego ciała. W przeliczeniu na człowieka,"
               + " byłby to skok ponad długość boiska piłkarskiego","Super-słuch sowy: Sowy potrafią zlokalizować ofiarę w zupełnej ciemności, polegając wyłącznie na słuchu."
               + " Ich uszy są asymetrycznie rozmieszczone na głowie, co pozwala im idealnie namierzyć źródło dźwięku."
               "Słowne foki: Foki grenlandzkie mają zdolność uczenia się i naśladowania nowych dźwięków oraz ludzkiej mowy.",
               "Orki - doskonałe łowczynie: Orki (często nazywane wielorybami zabójcami) są niezwykle skutecznymi myśliwymi. W swoim naturalnym środowisku nie mają wrogów naturalnych.",
               "Czarna skóra niedźwiedzi polarnych: Choć ich futro wydaje się idealnie białe lub kremowe, skóra niedźwiedzi polarnych pod spodem jest całkowicie czarna. Pomaga im to pochłaniać"
               + " i zatrzymywać jak najwięcej ciepła z promieni słonecznych w mroźnym klimacie Arktyki.",
               "Zapach kosmosu: Przestrzeń kosmiczna nie jest całkowicie bezwonna. Powracający ze spacerów kosmicznych astronauci NASA opisują, że ich kombinezony pachną jak przypalony stek,"
               + " gorący metal lub dym spawalniczy. Winne temu są krążące w próżni wielopierścieniowe węglowodory aromatyczne.",
               "Cisza absolutna: W kosmosie panuje całkowita, głęboka cisza. Dźwięk potrzebuje cząsteczek powietrza lub innego ośrodka, aby się rozchodzić. Ponieważ w przestrzeni kosmicznej panuje próżnia,"
               + " żaden wybuch gwiazdy ani zderzenie planetoid nie wyda tam żadnego dźwięku.","Śnieg z metalu i deszcz z diamentów: Na Wenus panują tak ekstremalne temperatury i ciśnienie, że zamiast wody "
               + "z chmur pada kwas siarkowy, a na szczytach gór 'śnieg' składa się z metali - galeny i bizmutynu. Z kolei na Jowiszu i Saturnie ogromne ciśnienie potrafi zamienić węgiel w atmosferze w diamentowy deszcz.",
               ""]
class InteractiveView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=60.0) # Opcjonalnie: po ilu sekundach przyciski stająsię niważne
    # Definiujemy podstawowe ustawienia przycisku:
    @discord.ui.button(
            label="Stwórz kanał", # Co jest napisane na przycisku
            style=discord.ButtonStyle.success,  # Jak przycisk wygląda
            custom_id="create_channel_btn") # Jaki ma unikatowy identyfikator
    async def button_callback(self, interaction: discord.Interaction, button: discord.ui.Button):
        
        guild = interaction.guild # Aby mniej pisać później, zapamiętujemy w zmiennej 'guild' że to jest to samo co 'interaction.guild'
        # 1. Znajdujemy ostatnio stworzony kanał 'ticket-X' i wcyiagamy ten X
        max_ticket_channel_number = 0
        for channel in guild.channels:
            if channel.name.startswith('🎫ticket-'): # Czy nazwa kanału zaczyna się od 'ticket-'?
                
                channel_id = int(channel.name[8:]) # Tutaj wybieramy sam numerek z 'ticket-12345' -> '12345' -> 12345
                if channel_id >= max_ticket_channel_number: # Jeżeli znaleźliśmy większy numerek niż becnie zapamiętany, to zapamiętujemy ten większy
                    max_ticket_channel_number = channel_id
        max_ticket_channel_number += 1 # Zwiększamy o jeden by utworzyc kanał o kolejnym numerku
        # 2. Tworzymy słownik z informacjami kto ma dostępy a kto nie. Na początku: zwykłe konta ('default_role' / @everyone) nie mają tam dostępu
        overwrites = {
            guild.default_role: discord.PermissionOverwrite(view_channel=False),
        }
        # 3. Natępnie, wynajdujemy role na serwerze które mająu prawnienia administratorskie i im nadajemy dostęp do kanału
        for role in guild.roles:
            if role.permissions.administrator:
                overwrites[role] = discord.PermissionOverwrite(view_channel=True)
        # 4. Nadajemy samemu botowi dostęp do tego kanału
        overwrites[guild.me] = discord.PermissionOverwrite(view_channel=True)
        # 5. Tworzymy kanał wraz z ustalonymi wyzej dostępami
        channel_name = "🎫ticket-" + str(max_ticket_channel_number)
        channel = await guild.create_text_channel(
            name=channel_name,
            overwrites=overwrites,
            reason=f"Admin-only channel created: {channel_name}",
        )
        delete_button = Delete_Channel_View()
        await channel.send(view=delete_button)
        await interaction.response.send_message(f"Kanał: {channel_name} stworzony!", ephemeral=True)
        msg = await interaction.original_response()
        await msg.delete(delay=5.0)
   
class Delete_Channel_View(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=60.0)
    @discord.ui.button(
            label="Usuń ticket", # Co jest napisane na przycisku
            style=discord.ButtonStyle.danger,  # Jak przycisk wygląda
            custom_id="delete_channel_btn") # Jaki ma unikatowy identyfikator
    async def button_callback(self, interaction: discord.Interaction, button: discord.ui.Button):
        channel = interaction.channel
        await channel.delete() 
bot_intents = discord.Intents.default()
bot_intents.message_content = True
bot_intents.guilds = True
bot = commands.Bot(command_prefix="!", intents=bot_intents)
@bot.event
async def on_ready():
    print(f'Zalogowaliśmy się jako {bot.user}')
@bot.command()
async def hello(ctx):
    await ctx.send(f'Cześć')
@bot.command()
async def mis(ctx):
    await ctx.send(f":bear:")
@bot.command()
async def slon(ctx):
    await ctx.send(f":elephant:")
@bot.command()
async def hej(ctx):
    await ctx.send("witaj")
@bot.command()
async def joke(ctx):
    url = None
    async with aiohttp.ClientSession() as session:
        async with session.get("https://meme-api.com/gimme") as resp:
            data = await resp.json()
            url = data["url"]

    embed = discord.Embed(

        title=data["title"],
        color=discord.Color.random()
    )
    embed.set_image(url=url)
    embed.set_footer(text=f"👍 {data['ups']} | r/{data['subreddit']}")

    await ctx.send(embed=embed)
@bot.command()
async def joined(ctx, member: discord.Member):
    if member.joined_at is None:
        await ctx.send(f'{member} has no join date.')
    else:
        await ctx.send(f'{member} joined {discord.utils.format_dt(member.joined_at)}')
@bot.command()
async def ping(ctx):
    await ctx.send(f"Pong! {round(bot.latency*1000)} ms")
@bot.command()
async def haslo(ctx,x):
    await ctx.send(gen_pass(x))
@bot.command()
async def ciekawostka(ctx):
    await ctx.send(random.choice(ciekawostki))
@bot.command()
@commands.has_permissions(administrator=True) # Nie chcemy by ktokolwiek mógł zrobić taki kanał, tylko administratorzy
async def make_admin_channel(ctx, channel_name: str):
    """
    Tworzy nowy tekstowy kanał widoczny tylko dla:
    - Administratorów
    - Samego bota

    Przykład: !make_admin_channel secret-stuff
    """

    guild = ctx.guild

    # 1. Tworzymy słownik z informacjami kto ma dostępy a kto nie. Na początku: zwykłe konta ('default_role' / @everyone) nie mają tam dostępu
    overwrites = {
        guild.default_role: discord.PermissionOverwrite(view_channel=False),
    }

    # 2. Natępnie, wynajdujemy role na serwerze które mająu prawnienia administratorskie i im nadajemy dostęp do kanału
    for role in guild.roles:
        if role.permissions.administrator:
            overwrites[role] = discord.PermissionOverwrite(view_channel=True)

    # 3. Nadajemy samemu botowi dostęp do tego kanału
    overwrites[guild.me] = discord.PermissionOverwrite(view_channel=True)

    # 4. Tworzymy kanał wraz z ustalonymi wyzej dostępami
    channel = await guild.create_text_channel(
        name=channel_name,
        overwrites=overwrites,
        reason=f"Admin-only channel created by {ctx.author}",
    )

    #5. Odpowiadamy że kanał został utworzony
    await ctx.send(f"Channel {channel.mention} created — admins and bot only.")
@bot.command()
async def menu(ctx):
    view = InteractiveView()
    await ctx.send("Choose an option below:", view=view)
@bot.command()
async def info_about_user(ctx, user: str = None):
    if user is None:
        user = ctx.author
    else:
        user = discord.utils.get(ctx.guild.members, name=user)

    if user is None:
        await ctx.send(f"Nie mogę znaleźć użytkownika o nazwie {user}.")
        return

    info = f"""
    display_name: {user.display_name}
    id: {user.id}
    name: {user.name}
    discriminator: {user.discriminator}
    bot: {user.bot}
    global_name: {user.global_name}
    avatar: {user.avatar.url if user.avatar else "No avatar"}
    created_at: {user.created_at}
    public_flags: {user.public_flags}
    """
    await ctx.send(f"Info about {user.mention}: {info}")
@bot.command()
async def adm(ctx):
    """
    """

    button_del = discord.ui.Button(label="usuń ticket", style=discord.ButtonStyle.red)

    # Tworzymy widok i dodajemy przyciski
    view = discord.ui.View()
    view.add_item(button_del)
    # Wysyłamy wiadomość z przyciskami
    await ctx.send("Sterowanie ticketem", view=view)
@bot.command()
async def piesek(ctx):
    response = requests.get("https://dog.ceo/api/breeds/image/random")
    data = response.json()

    embed = discord.Embed(
        title="🐶 Losowy piesek",
        color=discord.Color.random()
    )
    embed.set_image(url=data["message"])

    await ctx.send(embed=embed)
@bot.command()
async def mis_los(ctx):
    embed = discord.Embed(
        title="🐻 Losowy Miś",
        color=discord.Color.from_rgb (150, 75, 0)
    )
    embed.set_image(url=random.choice(bear_images))
    await ctx.send(embed=embed)

        
bot.run('token')
