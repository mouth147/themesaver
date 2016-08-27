import shutil, os, zipfile
from sys import exit

os.system('clear')
print '-----------------------------------'
print 'Save theme for Wordpress'
print 'By mouth147'
print '-----------------------------------'
print '''

This script was written to zip a Wordpress theme. 
Enjoy >B}
'''

print ''
print 'What directory is Wordpress installed in?'
print "If current directory enter './'"
path = raw_input("If root then enter '/': ") 

while not os.path.exists(path):
    print('')
    path = raw_input("Sorry that path doesn't exist. Enter a valid path or CTRL^C to exit: ")

print 'Changing directory...'
os.chdir(path)
print "Current directory >>",os.getcwd()
print 'Looking up themes...'

if not os.path.exists('./htdocs/wp-content/themes/'):
    print 'Themes folder was not found. Run script again.'
    exit(1)

os.chdir('./htdocs/wp-content/themes/')

folders = []
for i in os.listdir('./'):
    current_path = os.path.join('./', i)
    if os.path.isdir(current_path):
        folders.append(i)

print "--------------------------------"
print '         Current Themes'
print "--------------------------------"
for i in range(0, len(folders)):
    print str(i + 1) + ". ", folders[i]

print ''
print ''

yesorno = 'n'
while yesorno == 'n':
    theme = input('Please select the theme you wish to choose by its number: ')
    yesorno = raw_input('You have chosen ' + folders[theme - 1] + ' as your theme. Is this correct(y/n): ')

folder = os.path.abspath(folders[theme - 1])
foldername = folders[theme - 1] + '.zip'

print 'Creating ' + foldername + '...' 
themeZip = zipfile.ZipFile(foldername, 'w')

for foldername, subfolders, filenames in os.walk(folder):

    print('Adding files in %s...' % (foldername))
    themeZip.write(foldername)

    for filename in filenames:
        if filename == foldername:
            continue
        print 'Adding file ' + os.path.join(foldername, filename) + '...'
        themeZip.write(os.path.join(foldername, filename))
    
themeZip.close()
print 'Done.'

print 'Zip file will be in themes folder.'
