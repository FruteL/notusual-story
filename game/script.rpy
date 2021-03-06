﻿# The script of the game goes in this file.
#init -1 python:
#    style.default.justify = True
    
define gui.text_size = 50
define gui.name_text_size = 80


############ ПЕРСОНАЖИ ############ 

define k = Character("Катюша", who_color="#ff9900")
define r = Character("Рома", who_color = "99cc00")
define v = Character("Василий", who_color = "0033cc")
define sh = Character("Шурик")

############ СПРАЙТЫ ############ 

image kate usual smile =  im.FactorScale("images/sprites/Kate/kate_usual_smile.png", 1.2)
image kate usual front =  im.FactorScale("images/sprites/Kate/kate_usual_front.png", 1.2)
image kate usual discntent =  im.FactorScale("images/sprites/Kate/kate_usual_discntent.png", 1.2)
image kate usual surprise =  im.FactorScale("images/sprites/Kate/kate_usual_surprise.png", 1.2)
image kate apron smile =  im.FactorScale("images/sprites/Kate/kate_apron_normal.png", 1.2)
image kate apron front =  im.FactorScale("images/sprites/Kate/kate_apron_front.png", 1.2)
image kate apron discntent =  im.FactorScale("images/sprites/Kate/kate_apron_disconted.png", 1.2)
image kate apron surprise =  im.FactorScale("images/sprites/Kate/kate_apron_surprise.png", 1.2)

image roma usual = im.FactorScale("images/sprites/Roma/Roma_usual.png", 1.2) 
image roma front = im.FactorScale("images/sprites/Roma/Roma_front.png", 1.2)                  
image roma smile = im.FactorScale("images/sprites/Roma/roma_smile.png", 1.2)
image roma smile look = im.FactorScale("images/sprites/Roma/roma_smile_look.png", 1.2)
image roma usual look = im.FactorScale("images/sprites/Roma/roma_usual_look.png", 1.2)

image vas = im.FactorScale("images/sprites/Vas/vas.png", 1.2) 

############ ЗАДНИКИ ############ 

image bg bar_ = "images/background/bar.png"
image bg front bar_ = "images/background/fron_bar.png"
image bg park = "images/background/Park.png"
image bg home = "images/background/home.png"    
image bg starthome = "images/background/home2.png"

############ МУЗЫКА ############ 

define audio.apologize = "audio/music/apologize.ogg"  
define audio.bef = "audio/music/beforebar.ogg"
define audio.bar1 = "audio/music/Hard Boiled.mp3"   
define audio.bar2 = "audio/music/Smooth Lovin.mp3"       


############ ЗВУКИ ############                             

define audio.door = "audio/sounds/door.mp3"
define audio.smoke = "audio/sounds/smoke.mp3"  
define audio.kol = "audio/sounds/kol.mp3"      

############ ГЕЙМПЛЕЙ ############ 
    
label start:
    stop music fadeout 2           
    
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    scene black with dissolve
    pause 1
    scene bg starthome with dissolve
    
    if (not achievement.has("start")):
        $  get_achievement("start")

    "Уснул я как обычно под утро, от чего новый день начался у меня после обеда."
    "И все пошло наперекосяк." 
    "В холодильнике шаром покати, а одно из двух яиц, что предназначалось мне на завтрак, оказалось тухлым.{w} Узнал я это только когда вылил его к первому на сковородку."
    "~Отлчино. Остался без завтрака ~"
    "Собрав кипу важных бумажек, я покинул стены своего дома"
    play sound door
    scene bg home with dissolve
    play music apologize fadein 2.0 
    "Двигаясь в сторону работы, я вынул из кармана пальто пачку и ловким движением извлек из нее сигарету."
    play sound smoke  
    "Я впустил в себя горький дым, чтобы он выкурил все гнетущие мысли из моей головы"
    "Это действительно немного помогало, но этого было мало.{w} Я не курил более пятнадцати лет, а тут снова начал"
    "~Ведь именно{i} она{/i} уговорила меня бросить, и сделал я это только ради нее.~"
    "Запрокинув голову вверх, я выдохнул дым, и уставился на небо, которое было необычайно чистым и голубым, несмотря на то, что в это время года оно всегда серое."
    "Наблюдая за достаточно редко проплывающими облаками, я погрузился в омут воспоминаний"
    "{i}Было это весной.{w} Все как в дешевых романтических историях.{w} Два незнакомца столкнулись в студенческой библиотеке.{w} Искра, буря, страсть.{/i} "
    "{i}Хотя на самом деле все было не так быстро.{w} Но именно в тот момент моя жизнь изменилась.{w} И хочу сказать в лучшую сторону.{/i} "
    "{i}Легким ветерком она влетела в мою душу, унеся все проблемы куда-то вдаль.{/i}"
    "{i}Я отлично помню наше первое свидание.{w} Как сильно у меня дрожали руки, а слова застревали в горле.{/i} "
    "{i}Помню, как спустя два года уже она краснела и заикалась, когда я делал ей предложение.{w} Мне повезло найти свое счастье.{/i}"
    "{i}До этого, про любовь я знал лишь то, что она есть.{w} Только то, что сумели воспитать во мне книги.{/i}"
    stop music fadeout 2.0
    "Оставив секретарю документы, и прочие отчеты, я пошел дальше.{w} Сегодня меня тут никто не ждет, следующая смена лишь завтра"    
    play music bef fadein 2.0
    "Если мужчина ничего не умеет, он идет в охранники. Если девушка ничего не умеет, она идет на панель. {w}Суть одна – спать за деньги. "
    "Хотя, если быть откровенным, то на моей должности спать не выходит, все же солидная фирма. "   
    scene bg front bar_ with dissolve    
    "Если честно, дела у меня плохи. {w}Некоторое время меня спасал твердый характер."
    "Я держался, встречая проблемы грудью, превозмогая и двигаясь дальше.{w} Оказалось, у меня тоже есть предел." 
    "Сейчас очень модно слово «депрессия». {w}Лично я его всегда презирал, полагая что проблема раздутая, и нужна лишь за тем, чтобы мозгоправы могли заработать себе на хлеб" 
    "Однако я все еще могу трезво оценить свое состояние, чтобы сказать – сейчас я крайне плох"   
    play sound smoke  
    "На улице стемнело. Вдохнув свежего ночного воздуха, я снова закурил, прогоняя это странное наваждение, как обычно понимая, что это не поможет. "  
    "Но мы знали и другой способ, так что ноги сами привели меня сюда. «Фитс» - гласила вывеска.{w} Раньше я всегда проходил мимо него по дороге из дома на работу.{w} А теперь частенько захаживаю"    
    stop music fadeout 2.0                                    
    "Ловким щелчком я отправил окурок в ближайшую мусорку. Решив, что хуже не будет, я зашел в бар." 
    play sound kol     
    play music [bar1, bar2] fadeout 2.0 fadein 2.0          
    scene bg bar_ with dissolve
    "Обстановка тут была как всегда очень уютная. На фоне играла ненавязчивая музыка, что-то на подобии джаза. "
    "В воздухе витал сладковатый запах вперемешку с табачным дымом. {w} Учитывая, что время было около одиннадцати часов, людей было на удивление мало. "  
    "Какая-то компания негромко разговаривала, кто-то же сидел и молча выпивал"
    " Выделялся мужчина в солидном костюме и парнишка сидевший в углу, которому бы я не дал больше 17 лет. {w}Место явно ему не подходит. "
    "Я хорошо знал сотрудников этого бара, ему бы точно ничего не продали.{w} Вот как раз Катюшка к нему подходит:"  
    show kate apron discntent with dissolve      
    k "Молодой. А сколько нам годиков? "        
    hide kate apron discntent
    show roma usual with dissolve  
    r "Сем…семнадцать"
    "Oчень неуверенно ответил тот, а взгляд его помрачнел."  
    hide roma usual with dissolve  
    show kate apron discntent with dissolve
    k "И что ж тогда ты тут забыл?"
    "Cпросила она, но на неуверенную попытку паренька ответить тут же продолжила" 
    k "Шел бы ты отсюда. Нам проблемы не нужны"
    menu:
        "Помочь":
              jump helps   
        "Не помогать":
            jump no_helps
                                                                
    return     
    
label helps:       
    hide kate apron discntent 
    show kate apron surprise          
    sh "Он со мной"
    if (not achievement.has("Roma")):
        $  get_achievement("Roma")
    "Bмешался я в разговор. И кивнув головой юному алкоголику"  
    sh "Извини что задержался" 
    hide kate apron surprise  
    show kate apron smile
    k "С тобой? Эх.. только потому что это Ты. Что будешь?"
    sh "Как обычно, Катюш. "     
    
    jump credits 
         
label no_helps: 
    hide kate apron discntent with dissolve
    "Паренек пытался что-либо противопоставить девушке-официантке, но та была еще более упрямой. {w} Катюшу я знал. Она была лучшей подругой Оли."   
    show roma usual look with dissolve
    "Вскоре с еще более грустным лицом парень прошел мимо меня, его взгляд скользнул по мне, и лишь на секунду остановился на моих глазах." 
    hide roma usual look with dissolve
    "По спине пробежала холодная капля пота, а мне показалось что он заглянул мне в саму душу."   
    v "Присоеденишся?"                                                               
    show vas with dissolve
    "Отозвался незнакомец, в солидном костюме. {w}Неожиданное предложени. И как реагировать?"
    menu:                             
        "Присоедениться":
            jump vas_route    
        "Отказаться":
            sh "Нет, спасибо"
            v "Как занешь"
            "Безразлично, но с некой ухмылкой ответил он мне"      
            hide vas with dissolve 
    "Отодвинув все странные вопросы на вторйо план я проследовал к своему столику" 
    show kate apron smile with dissolve 
    k "Привет Шурик. Что-то ты к нам зачастил. Что заказываешь?"
    sh "Как обычно."
    k "Я быстро." 
    hide kate apron smile 
    show kate apron smile at left_to_right
    "И правда менее чем через минуту передо мной бутылка виски и две рюмки."
    hide kate apron smile 
    show kate usual smile at right_to_left
    "Удивленно посмотрев на Катю, я обнаружил, что она уже успела сменить форму на обычную одежду."   
     
    k "Взяла отгул, подруга подменит" 
    if (not achievement.has("Kate")):
        $  get_achievement("Kate")   
    "Ответила она на немой вопрос в моих глазах."
    k "Не пытайся утопить свои горести в стакане. Знаешь, они умеют плавать."
    sh "Это я уже понял."
    "Мы с Катей опрокинули по паре рюмок, походу перекидываясь обыденными фразами." 
    "Я старался выглядеть максимально расслабленным и даже веселым.{w} Но судя по лицу моего визави – выходило это плохо."
    "Сигаретный дым наполнил мои легкие, подхватив тревожные мысли вместе с алкоголем, и понесли куда-то вдаль."
    k "Пассивный курильщик вдыхает через дым гораздо больше вредных веществ, чем сам курящий. В дыме, который вдыхает курящий содержится от 5,3 до 43 нанограмм канцерогена диметилнитрозамина."
    k "Тогда как во вторичном дыме его содержание составляет от 680 до 823 нанограмм.{w} Содержание хинолина во вторичном дыме в 11 раз больше по сравнению с первичным, порядка 11 тысяч нанограмм."
    k "Иными словами, здоровью окружающих от пассивного курения наносится гораздо больший вред нежели самому курящему."
    "Отчитала меня Катюша."
    k "Да и ты вроде как бросил."
    sh "Уже полгода как нет."
    k "Неужели ты все еще так сильно по ней тоскуешь?"
    sh "Не было и дня что бы я не оплакивал ее."
    k "Может пара отпустить ее? Попробовать начать жизнь с чистого листа?{w} Не знаю… бросить все, сменить город, страну, найти новых людей."
    "Я налили себе еще стопку и тут же опрокинул ее."
    sh "А смысл. Знаешь, я ведь ничего не умею.{w} Я всегда хотел быть военным. И воспитан я как солдат.{w} Слишком прост, прямолинейный глупец."
    sh "Всю жизнь кто-то отдавал мне приказы, принимал за меня решения. Но я был ранен, еще и награжден рядом проблем.{w} Родине я больше не нужен."
    sh "Я отучился и был в полиции. Но как говорил я сильно прямолинеен и честен, а там… там все скользко."
    sh "Система построена так, либо ты становишься ее частью, и погрязнешь в коррупции, или же система тебя пережует и выплюнет.{w} Я же успел уйти сам."
    sh "Теперь у меня нет желания работать на государство. После того как оно все у меня отняло? Даже умирая от голода не пойду на государеву службу."
    k "Но вроде как сейчас ты ведь работаешь, да и Юля говорила, что ты пишешь."
    sh "Писал.{w} Раньше.{w} Теперь не могу. Не складываются слова в предложения. Те в абзацы и так далее."
    sh "После ее смерти, я не написал ни строчки. Да и работу я бросил.{w} Знаешь… Я очень устал… я больше не могу."
    "Катя наклонилась через стол и отвесила мне мощную пощечину. Я бы мог ее остановить, но не стал."
    "Она имела право на то что бы злиться. На громкий хлопок, обернулось половина бара." 
    
    jump credits 

label vas_route:
    "Рут не написан" 
    if (not achievement.has("Vas")):
        $  get_achievement("Vas") 
    "Приносим извинения"
    
    jump credits 
