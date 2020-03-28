# ============================================================================
# DEXTERITY ROBOT TESTS
# ============================================================================
#
# Run this robot test stand-alone:
#
#  $ bin/test -s justionale.product -t test_cliente.robot --all
#
# Run this robot test with robot server (which is faster):
#
# 1) Start robot server:
#
# $ bin/robot-server --reload-path src justionale.product.testing.JUSTIONALE_PRODUCT_ACCEPTANCE_TESTING
#
# 2) Run robot tests:
#
# $ bin/robot /src/justionale/product/tests/robot/test_cliente.robot
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

Scenario: As a site administrator I can add a Cliente
  Given a logged-in site administrator
    and an add Cliente form
   When I type 'My Cliente' into the title field
    and I submit the form
   Then a Cliente with the title 'My Cliente' has been created

Scenario: As a site administrator I can view a Cliente
  Given a logged-in site administrator
    and a Cliente 'My Cliente'
   When I go to the Cliente view
   Then I can see the Cliente title 'My Cliente'


*** Keywords *****************************************************************

# --- Given ------------------------------------------------------------------

a logged-in site administrator
  Enable autologin as  Site Administrator

an add Cliente form
  Go To  ${PLONE_URL}/++add++Cliente

a Cliente 'My Cliente'
  Create content  type=Cliente  id=my-cliente  title=My Cliente

# --- WHEN -------------------------------------------------------------------

I type '${title}' into the title field
  Input Text  name=form.widgets.IBasic.title  ${title}

I submit the form
  Click Button  Save

I go to the Cliente view
  Go To  ${PLONE_URL}/my-cliente
  Wait until page contains  Site Map


# --- THEN -------------------------------------------------------------------

a Cliente with the title '${title}' has been created
  Wait until page contains  Site Map
  Page should contain  ${title}
  Page should contain  Item created

I can see the Cliente title '${title}'
  Wait until page contains  Site Map
  Page should contain  ${title}
