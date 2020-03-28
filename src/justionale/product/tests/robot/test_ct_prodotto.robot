# ============================================================================
# DEXTERITY ROBOT TESTS
# ============================================================================
#
# Run this robot test stand-alone:
#
#  $ bin/test -s justionale.product -t test_prodotto.robot --all
#
# Run this robot test with robot server (which is faster):
#
# 1) Start robot server:
#
# $ bin/robot-server --reload-path src justionale.product.testing.JUSTIONALE_PRODUCT_ACCEPTANCE_TESTING
#
# 2) Run robot tests:
#
# $ bin/robot /src/justionale/product/tests/robot/test_prodotto.robot
#
# See the http://docs.plone.org for further details (search for robot
# framework).
#
# ============================================================================

*** Settings *****************************************************************

Resource  plone/app/robotframework/selenium.robot
Resource  plone/app/robotframework/keywords.robot

Library  Remote  ${PLONE_URL}/RobotRemote

Test Setup  Open test browser
Test Teardown  Close all browsers


*** Test Cases ***************************************************************

Scenario: As a site administrator I can add a Prodotto
  Given a logged-in site administrator
    and an add Prodotto form
   When I type 'My Prodotto' into the title field
    and I submit the form
   Then a Prodotto with the title 'My Prodotto' has been created

Scenario: As a site administrator I can view a Prodotto
  Given a logged-in site administrator
    and a Prodotto 'My Prodotto'
   When I go to the Prodotto view
   Then I can see the Prodotto title 'My Prodotto'


*** Keywords *****************************************************************

# --- Given ------------------------------------------------------------------

a logged-in site administrator
  Enable autologin as  Site Administrator

an add Prodotto form
  Go To  ${PLONE_URL}/++add++Prodotto

a Prodotto 'My Prodotto'
  Create content  type=Prodotto  id=my-prodotto  title=My Prodotto

# --- WHEN -------------------------------------------------------------------

I type '${title}' into the title field
  Input Text  name=form.widgets.IBasic.title  ${title}

I submit the form
  Click Button  Save

I go to the Prodotto view
  Go To  ${PLONE_URL}/my-prodotto
  Wait until page contains  Site Map


# --- THEN -------------------------------------------------------------------

a Prodotto with the title '${title}' has been created
  Wait until page contains  Site Map
  Page should contain  ${title}
  Page should contain  Item created

I can see the Prodotto title '${title}'
  Wait until page contains  Site Map
  Page should contain  ${title}
