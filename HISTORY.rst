=======
History
=======

3.0.8 (unreleased)
------------------

- Nothing changed yet.


3.0.7 (2020-08-20)
------------------

- Added table and memory structure controls.

- Add example notebooks in the documentation.


3.0.6 (2020-07-31)
------------------

- Update exit code definitions.


3.0.5 (2020-07-31)
------------------

- Added exit_code field to status resource.

- Added breaches graph endpoint.


3.0.4 (2020-07-15)
------------------

- Added pumps discharge graph endpoint

- Added more filtering options on contracts 


3.0.4b3 (2020-07-10)
--------------------

- Added id field everywhere


3.0.4b2 (2020-07-08)
--------------------

- Generated with generator version v4.3.0

- Fixed problem with threedimodel on simulation resource (was integer should be string) 


3.0.4b1 (2020-07-07)
--------------------

- Damage estimation is not required


3.0.3 (2020-06-16)
------------------

- Changed Lizard postprocessing overview endpoint


3.0.2 (2020-06-12)
------------------

- Username filters for simulations endpoint.


3.0.1 (2020-06-09)
------------------

- Added statistics endpoint
 
- Changed Lizard post-processing endpoint 
  (not backwards compatible, however intended to be used only by Lizard)


3.0 (2020-05-25)
----------------

- Official production release


3.0.b24 (2020-05-22)
--------------------

- All uid fields on events should be read-only


3.0.b23 (2020-05-20)
--------------------

- Added wind global drag coefficient


3.0.b22 (2020-05-18)
--------------------

- Added max_rate to actions


3.0.b21 (2020-05-15)
--------------------

- Status field crash_report has become detail.


3.0.b20 (2020-05-11)
--------------------

- Added breaches and more fields to potentialbreaches


3.0.b19 (2020-04-24)
--------------------

- File filter exclude/include simulation status.


3.0.b18 (2020-04-24)
--------------------

- Added 'active' to inpy-version resource


3.0.b17 (2020-04-20)
--------------------

- Added icontains filters


3.0.b16 (2020-04-10)
--------------------

- Added uuid field to initial saved state serializer.


3.0.b15 (2020-04-01)
--------------------

- Added simulation websocket channels overview endpoints


3.0.b14 (2020-03-23)
--------------------

- Added raster-edits processing endpoints


3.0.b13 (2020-03-20)
--------------------

- Split up waterlevel graph endpoint in 
  waterflow and waterlevel graph endpoint

- Added waterprofile graph endpoint


3.0.b12 (2020-03-10)
--------------------

- Added waterlevel graph endpoint


3.0.b11 (2020-03-06)
--------------------

- Added users endpoint

- Changed user endpoint to profile endpoint

- Added more filters


3.0b10 (2020-02-19)
-------------------

- Simulation model now has a 'tags' field.


3.0.b9 (2020-02-12)
-------------------

- Support for interactive simulations.

- Result API endpoints.


3.0.b8 (2020-02-10)
-------------------

- Edit Constant and Timeseries Wind events


3.0.b7 (2020-02-03)
-------------------

- Added wind

- Added visualization endpoints


3.0.b6 (2020-01-29)
-------------------

- Something went wrong with the 3.0.b5 release, next rty.


3.0.b5 (2020-01-27)
-------------------

- Raster edits, event uuids.


3.0.b4 (2019-12-12)
-------------------

- Local rain events.


3.0.b3 (2019-12-09)
-------------------

- Less strict requirement for dependencies 'six' and 'urllib3' to
  avoid pipenv resolve issues at Lizard


3.0.b2 (2019-12-02)
-------------------

- Changed 'set_pump_discharge' to 'set_pump_capacity'.


3.0.b1 (2019-11-28)
-------------------

- Updated API descriptions

- Raster resource filtering


3.0.b0 (2019-11-28)
-------------------

- First 3.0 release candidate

- All swagger schema's are automatically saved in
  schemas/swagger_xxx.yaml

0.0.23 (2019-11-26)
-------------------

- Fixing releases


0.0.22 (2019-11-26)
-------------------

- Added `initialwaterlevel rasters` and `postprocessing`


0.0.21 (2019-11-18)
-------------------

- Fixed ThreediApiClient constructor not working with config keywords and
  .env file.

- Added initial waterlevels


0.0.20 (2019-11-11)
-------------------

- Added `simulation` and `simulation_id` to statuses serializer.

- Automatically get a new JWT token when
  the current one is valid less than 5 minutes.

- Use `mkdocs` for documentation.

0.0.17.3 (2019-11-04)
---------------------

- Test release.


0.0.17.2 (2019-11-04)
---------------------

- Test release.


0.0.17.1 (2019-11-01)
---------------------

- Add boundary model.


0.0.17c (2019-11-01)
--------------------

- Added boundaries to simulation events and updated docs.


0.0.17b (2019-10-31)
--------------------

- Bulk boundary conditions.


0.0.17a (2019-10-31)
--------------------

- Boundary conditions.


0.0.17 (2019-10-30)
-------------------

- Limit compatible python versions


0.1.9 (2019-10-30)
------------------

- Added resource `statuses`.


0.1.8 (2019-10-17)
------------------

- Added timed control


0.1.7 (2019-09-25)
------------------

- Laterals now have id field.

- Usage integration


0.1.6 (2019-09-04)
------------------

- Added geojson/gridadmin/rasters upload & download


0.1.5 (2019-07-03)
------------------

- Updated file uploading


0.1.4 (2019-06-24)
------------------

- Include modules.


0.1.3 (2019-06-24)
------------------

- Fix package name


0.1.2 (2019-06-24)
------------------

- PyPi release.


0.1.1 (2019-06-21)
------------------

* Included more endpoints


0.1.0 (2019-05-10)
------------------

* First release on PyPI.
