
import os
import pkg_resources
import subprocess


domain = 'plonetheme.tokyo'
os.chdir(pkg_resources.resource_filename(domain, ''))
os.chdir('../../../')
target_path = 'src/plonetheme/tokyo/'
locale_path = target_path + 'locales/'
i18ndude = './bin/i18ndude'


def locale_folder_setup():
    os.chdir(locale_path)
    languages = [d for d in os.listdir('.') if os.path.isdir(d)]
    for lang in languages:
        folder = os.listdir(lang)
        if 'LC_MESSAGES' in folder:
            continue
        else:
            lc_messages_path = lang + '/LC_MESSAGES/'
            os.mkdir(lc_messages_path)
            cmd = 'msginit --locale={0} --input={1}.pot --output={2}/LC_MESSAGES/{3}.po'.format(   # NOQA: E501
                        lang,
                        domain,
                        lang,
                        domain,
                    )
            subprocess.call(
                cmd,
                shell=True,
            )

    os.chdir('../../../../')


def _rebuild():
    cmd = f'{i18ndude} rebuild-pot --pot {locale_path}/{domain}.pot --create {domain} {target_path}'
    subprocess.call(
        cmd,
        shell=True,
    )


def _sync():
    cmd = f'{i18ndude} sync --pot {locale_path}/{domain}.pot {locale_path}*/LC_MESSAGES/{domain}.po'
    subprocess.call(
        cmd,
        shell=True,
    )


def update_locale():
    locale_folder_setup()
    _sync()
    _rebuild()
