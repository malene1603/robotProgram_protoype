"""
Hej! Hvis du under dig over hvad denne her klasse er til,
så er det til dele status mellem de forskellige scripts.
Mvh. Jacob
"""

class RobotState:
    idle_counter = 0 #bruges ikke endnu

    #Fortæller om et pause-script er aktivt.
    #Det kan bruges til at undgå at sende nye scripts,
    #Mens robotten venter eller er i gang med noget specielt.
    pause_script_active = False

    #antal scripts der er blevet kørt
    #Bruges til progress bar, så man kan vise hvor langt robotten er i en drink.
    progress_done = 0

    #Totalt antal scripts der skal køres.
    #Sættes typisk når man starter en ny drink (fx 4 hvis man har 4 trin).
    #Bruges også af progress bar’en, så man kan regne ud hvor mange % der er færdige.
    progress_total = 1

    #Navnet på det program der kører lige nu – f.eks. "Cola.urp".
    #
    current_program_name = ""
