# Eliza

This is a little version of ELIZA, a famous natural-language AI demo from the 1960s.
The program doesn't have a clue what it is saying and it's not difficult to catch it out.

# Improvement

If the user is using a word from the violence lexical field, like "*I want to kill myself*", Eliza will redirect him to a professional.

## Example

```text
Hello user, i'm Eliza
> hi
How do you do.  Please state your problem.
> why don't you take over the world ?
Should you take over the world ? yourself ?
> do you remember your last birthday
Yes .. and?
> do you think i'm a lost cause ?
if i'm a lost cause ?? Absolutely.
> I want more friends !
What would it mean if you got more friends !
> what if you could disappear ?
Really--if me could disappear ?
> I'm sorry
I've told you that apologies are not required.
> Goodbye eliza
Goodbye. Thank you for talking to me.

###################################################

Hello user, i'm Eliza
 >  I have a gun, i'm going to shoot
This kind of problem requires the call of a professional, please contact the 09 72 39 40 50 immediately.
```



# Parry

Parry is an modified version of Eliza.
He's a 28 year old male who live alone. He's in the hospital and have som trouble with the Mafia, he has some bet trouble with them.

## How it works

Parry have some stats: **Fear**, **Anger**,**Mistrust**.
If the conversation implied some word related to *Mafia* or *danger*, the **Fear** stats will increase, same for the **Anger** if word related to *crazy* is mentioned. The **Mistrust** will increase if the **Anger** or **Fear** increase. If none of this tearm is mentionned, the **Fear**,**Anger** and **Mistrust** will decrease. If the stat **Mistrust** exceeds 9, Parry will refuse to talk to you anymore.

## Example

```text
> Hello
 Hi. 
##################################################
colere: 0
mefiance: 1.6
peur: 0.5
##################################################
> How are you today ?
 OK 
##################################################
colere: 0
mefiance: 1.2000000000000002
peur: 0
##################################################
> What's your name ?
 My name is Frank Smith 
##################################################
colere: 4
mefiance: 3.2
peur: 0
##################################################
> How old are you ?
 I'm 28 years old 
##################################################
colere: 3
mefiance: 2.8000000000000003
peur: 0
##################################################
> Are you married ?
 I live alone 
##################################################
colere: 2
mefiance: 2.4000000000000004
peur: 0
##################################################
> What sort of work do you do ?
 I work in the post office 
##################################################
colere: 1
mefiance: 2.0000000000000004
peur: 0
##################################################
> Why are you in the hospital ?
 I souldn't be in the hospital ? 
##################################################
colere: 0
mefiance: 1.6000000000000005
peur: 0
##################################################
> Who brought you here ?
 The police brought me here ? 
##################################################
colere: 0
mefiance: 2.6000000000000005
peur: 2
##################################################
> Do you have any trouble with the police ?
 Cops don't do their job 
##################################################
colere: 2
mefiance: 4.6000000000000005
peur: 4
##################################################
> What do they do instead ?
 In what whay ? 
##################################################
colere: 1
mefiance: 4.2
peur: 3.5
##################################################
> They arrest the right ones sometimes
 The law should arrest the bad people. 
##################################################
colere: 1
mefiance: 5.2
peur: 5.5
##################################################
> Do you know any bad people ?
 I try to stay clean. 
##################################################
colere: 1
mefiance: 6.2
peur: 7.5
##################################################
> Are you afraid of the bad people ?
 I try to stay clean. 
##################################################
colere: 1
mefiance: 7.2
peur: 9.5
##################################################
> Are you afraid of them ?
 Do you think i'm afraid of them ? 
##################################################
colere: 0
mefiance: 6.8
peur: 9.0
##################################################
> Are you connected with the Mafia ?
 Do you think i'm connected with the mafia ? 
##################################################
colere: 0
mefiance: 8.8
peur: 13.0
##################################################
> Do they know you ?
 In what whay ? 
##################################################
colere: 0
mefiance: 8.4
peur: 12.5
##################################################
> Does the Mafia know you ?
 In what whay ? 
##################################################
colere: 0
mefiance: 9.4
peur: 14.5
##################################################
> I'm asking if you have any relation with the Mafia ?
 I don't want to talk to you anymore, goodbye. 
 ```