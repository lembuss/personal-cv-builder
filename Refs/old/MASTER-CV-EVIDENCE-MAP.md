# MASTER CV — EVIDENCE MAP

**Phase 6A status:** Working evidence map generated directly from the current career database (`dev.db`). This is an evidence inventory, not the 6B selection decision.

## How to read this document

- **Primary CV section:** where the experience/project naturally belongs in the Master CV blueprint.
- **Secondary section:** another place the evidence can support the CV.
- **Evidence:** database project/activity content; no new facts have been added.
- **6A deliberately does not decide final inclusion or bullet count.** That is Phase 6B.

## Database snapshot
- Experiences: **20**
- Projects: **40**
- Activities: **163**

---

## Skylink Flight Services — Private Pilot Licence (PPL) Training

**Role:** Aviation  
**Type:** Other  
**Location:** Wilson Airport, Nairobi, Kenya (with cross-country hours to Malindi)  
**Dates:** 2015-01-10 → 2015-08-31  
**Primary CV section:** Certifications & Licences  
**Secondary:** Technical Skills  

**Experience description (database):**
> Completed a KCAA-approved Private Pilot Licence (PPL) training programme at Skylink Flight Services, Wilson Airport, Nairobi. The programme comprised approximately six months of ground school and 46 hours of flight training on the Cessna 172, in compliance with KCAA regulatory requirements. Cross-country flying hours included operations to the Malindi area. Successfully obtained three KCAA licences upon completion: Private Pilot Licence — Aeroplane (YK-9469-PL), Flight Radio Telephony Operator's Licence (YK-9469-RL), and English Language Proficiency Rating (Level 5).

### Experience-level activities
- **IndependentlyExecuted — Ground school training covering aviation theory, air law, navigation, meteorology, and aircraft systems**
  - How: Completed KCAA-prescribed ground school curriculum at Skylink Flight Services as part of the PPL programme requirements
  - Result: Passed KCAA ground school examinations, meeting the theoretical knowledge requirements for the Private Pilot Licence
- **IndependentlyExecuted — Flight training — 46 hours on Cessna 172 including local and cross-country operations**
  - How: Completed 46 hours of dual and solo flight training on the Cessna 172, operating out of Wilson Airport with cross-country hours to the Malindi area, in compliance with KCAA PPL requirements
  - Result: Accumulated the required flight hours and demonstrated pilot-in-command competency, leading to the award of KCAA Private Pilot Licence — Aeroplane (YK-9469-PL)
- **IndependentlyExecuted — Flight Radio Telephony Operator's Licence — ground examination and certification**
  - How: Completed the KCAA Flight Radio Telephony Operator examination, demonstrating competency in aviation radio communications procedures and airspace phraseology
  - Result: Awarded KCAA Flight Radio Telephony Operator's Licence (YK-9469-RL), valid 8 September 2015 to 7 September 2017. Also awarded English Language Proficiency Rating Level 5

---

## Middle East Technical University — B.Sc. Aerospace Engineering

**Role:** Undergraduate Student  
**Type:** Academic  
**Location:** Turkey/Northern Cyprus  
**Dates:** 2015-09-26 → 2019-06-17  
**Primary CV section:** Education  
**Secondary:** Selected Engineering / R&D Projects  

**Experience description (database):**
> Bachelor of Science in Aerospace Engineering at METU Northern Cyprus Campus, completed with Şeref/Honour classification (CGPA 3.12/4.00; 81.20/100). Programme delivered entirely in English over 4 years (151 METU credits, 259.5 ECTS). Coursework spanned the full aerospace engineering discipline — aerodynamics, propulsion, structures, flight mechanics, systems dynamics, thermodynamics, fluid mechanics, and numerical methods — complemented by technical electives in computational aerodynamics, helicopter aerodynamics and design, mechatronics, finite element analysis, and smart structures. Included two supervised industry placements (Summer Practice I & II) and a capstone aeronautical engineering design course (ASE451)

### Projects

#### Numerical Methods for Aerospace Engineers 
**Potential CV sections:** Selected Engineering / R&D Projects
**R&D:** No

**Description:** Three progressive group project assignments for ASE301 Numerical Methods for Aerospace Engineering, implementing numerical solvers for ODEs and PDEs of increasing complexity — from unstructured finite volume methods to 2D convection-diffusion. All implemented in FORTRAN under the instruction of Dr. Ismail H. Tuncer.
**System:** Numerical solver implementations — unstructured FVM (potential flow), 1D FDM (parabolic/hyperbolic PDEs), 2D FDM (convection-diffusion)
**Objective:** Implement and validate numerical solution schemes for aerospace-relevant governing equations, evaluate scheme stability and convergence, and visualize flow field results.
**Outcome:** Three functional FORTRAN solvers delivered, covering FVM potential flow over a NACA 0012 airfoil and explicit/implicit FDM solutions for heat diffusion and linear convection-diffusion with parametric validation

**Activities / evidence records:**
- **Led — Developed a 2D finite volume solver in FORTRAN to compute potential flow over a NACA 0012 airfoil and a circle at multiple angles of attack.**
  - How: Discretised the 2D Laplace equation in integral form using diffusive flux formulation on unstructured triangular grids generated with EasyMesh. Implemented far-field and solid wall boundary conditions, iterative gradient evaluation per cell, and time-marching convergence loop. Post-processed velocity vectors and streamlines in VisIt across AoA cases of 0°, 10°, and 20°.
  - Result: Converged potential flow solutions obtained for both geometries; velocity vector and streamline distributions validated against expected inviscid flow behaviour at all three angles of attack.
- **Led — Implemented and compared explicit and implicit 1D finite difference schemes for an unsteady heat diffusion equation (parabolic PDE) and a linear convection equation (hyperbolic PDE).**
  - How: Derived and coded FTCS, FTBS, and BTCS finite difference equations in FORTRAN for both PDEs. Applied Thomas algorithm to solve the implicit tridiagonal system for BTCS. Evaluated stability behaviour across schemes by varying the diffusion number (d) and Courant number (σ), including an insulated wall boundary condition variant.
  - Result: Confirmed FTCS stability limit (d < 0.5) for heat diffusion; demonstrated unconditional stability of BTCS; identified numerical diffusion in FTBS for the wave equation. Results consistent with theoretical Von Neumann stability analysis.
- **Led — Implemented FTCS and DuFort-Frankel schemes to solve the 2D unsteady convection-diffusion equation over a rectangular domain, with parametric studies on grid resolution, convection velocity, and initial condition geometry**
  - How: Discretised the 2D convection-diffusion PDE using central and backward convective differencing combined with FTCS and DuFort-Frankel (DF) time-marching in FORTRAN on a 201×201 grid. Bootstrapped DF first timestep using FTCS due to undefined n-1 level. Conducted parametric cases varying U/V velocities, reference point location, grid density, and step function geometry (circular vs. square).
  - Result: Demonstrated conditional stability of FTCS and improved stability characteristics of DuFort-Frankel; confirmed numerical diffusion effects under backward convective differencing; parametric cases validated solver response to varying flow and grid conditions.

#### Finite Element Modelling of a Composite Cantilever Beam
**Potential CV sections:** Selected Engineering / R&D Projects
**R&D:** No

**Description:** Two progressive individual FEA projects for MECH413 Introduction to Finite Element Analysis, analysing the structural response of a composite cantilever beam (isotropic aluminium core + orthotropic glass fibre/epoxy layers) under tip loading and torsional moment loading respectively, using ANSYS Mechanical APDL.
**System:** Composite Cantilever Beam — Aluminium/Glass Fibre Epoxy Layered Structure
**Objective:** Determine tip deflection, stress distribution, torsional frequencies, and angle of twist of a multi-layer composite cantilever beam under static and dynamic loading
**Outcome:** Delivered two complete FEA reports covering static structural analysis (δ_max = 31.387mm under 5N tip load) and torsional analysis (δ_max = 2.296mm static, θ_max = 5.74×10⁻⁴ rad/mm under 1Nm moment), with modal frequency extraction and harmonic response at 1Hz and 144Hz.

**Activities / evidence records:**
- **IndependentlyExecuted — Performed static 3D FEA of a 5-layer composite cantilever beam (3 aluminium + 2 glass fibre/epoxy, 500mm × 50mm) under a 5N transverse tip load to determine tip deflection and full stress distribution across all layers.**
  - How: Defined isotropic aluminium and orthotropic glass fibre material properties in ANSYS Mechanical APDL. Built geometry layer by layer and coalesced volumes using the Booleans procedure. Applied SOLID186 20-node element type, hexagonally swept mesh (5 volumes, 26 areas, 12,640 nodes). Applied fixed boundary conditions at cantilevered end and point load at tip midpoint. Postprocessed tip deflection and x/y/z normal stress and xy/yz/xz shear stress distributions across all layers.
  - Result: Maximum tip deflection δ_max = 31.387mm. Dominant stress component identified as σ_x (max ±0.45×10⁸ N/m²) concentrated at the cantilevered root on the top and bottom surfaces. XZ shear stress dominant across the beam body (avg 58,374 N/m²). Results consistent with classical cantilever beam theory.
- **IndependentlyExecuted — Performed multi-analysis 3D FEA of a 3-layer composite cantilever beam (1 aluminium core + 2 glass fibre/epoxy, 200mm × 40mm) under static and harmonic torsional moment loading (Mx = 1Nm), including modal frequency extraction and harmonic response analysis.**
  - How: Defined isotropic and orthotropic material properties in ANSYS Mechanical APDL. Built and coalesced 3-layer geometry, applied SOLID186 elements with hexagonal sweep mesh. Executed four sequential analyses: (1) static torsion — applied 1Nm moment as force couple (F = 25N); (2) modal — Block Lanczos method, 20 modes extracted over 1–10,000Hz, torsional frequencies identified by mode shape inspection; (3) harmonic at 1Hz — baseline comparison to static case; (4) harmonic at 144Hz — half the first torsional frequency (288.275Hz). Postprocessed tip deflection and angle of twist via path line midline mapping in all cases.
  - Result: Static: δ_max = 2.296mm, θ_max = 5.74×10⁻⁴ rad/mm. First three torsional frequencies identified at 288.275Hz (mode 3), 894.912Hz (mode 6), and 1586.38Hz (mode 8). Harmonic at 1Hz matched static results; harmonic at 144Hz showed dynamic amplification (δ_max = 2.923mm, θ_max = 7.3075×10⁻⁴ rad/mm). Tip displacement confirmed to vary linearly across beam width in all cases

#### Turbofan Compressor Performance Analysis
**Potential CV sections:** Selected Engineering / R&D Projects; Technical Skills
**R&D:** Yes

**Description:** Group project for ASE435 Propulsion Systems II analysing the parametric performance of a turbofan engine compressor using corrected flow parameters, examining the effects of turbine inlet temperature, altitude, and turbine inlet area on compressor pressure ratio and corrected mass flow rate. Implemented in MATLAB.
**System:** Turbofan Engine Compressor — Corrected Performance Parameter Model (bypass ratio α=2.82, design point π_c=24, M_0=0.6)
**Objective:** Determine how turbine inlet temperature, operating altitude, and turbine inlet area influence compressor pressure ratio and corrected mass flow rate, and identify operating limits relative to compressor map constraints.
**Outcome:** Produced parametric performance plots for corrected mass flow rate and compressor pressure ratio across T_t4 range (1000–2000K) and altitude range (sea level to 15,000m), demonstrating throttle, altitude, and geometry effects on compressor operating point.

**Activities / evidence records:**
- **Contributed — Conducted parametric analysis of turbofan compressor performance by modelling the effects of turbine inlet temperature, operating altitude, and turbine inlet area on corrected mass flow rate and compressor pressure ratio**
  - How: Derived corrected performance relations for compressor inlet mass flow rate and pressure ratio using standard turbofan cycle equations (corrected pressure δ, corrected temperature θ, corrected mass flow rate). Implemented parametric sweeps in MATLAB across T_t4 (1000–2000K), altitude (sea level to 15,000m at multiple Mach numbers), and turbine inlet area A_4. Applied ISA atmospheric data at five altitude stations. Generated compressor operating point plots against analytical limits for pressure ratio and mass flow rate.
  - Result: Demonstrated that increasing T_t4 raises compressor pressure ratio for a given mass flow rate; confirmed θ_0 reduction with altitude and its attenuation near tropopause; showed that increasing A_4 beyond choked-flow area reduces turbine energy extraction and consequently drops compressor mass flow rate. All results presented as parametric families of curves against compressor map limits.

#### Finite Difference Method Solvers for Aerodynamic PDEs
**Potential CV sections:** Selected Engineering / R&D Projects
**R&D:** No

**Description:** Group project for ASE443 Computational Aerodynamics implementing finite difference method solvers in MATLAB for four fluid and heat transport problems governed by elliptic, parabolic, and hyperbolic PDEs. Built on numerical methods foundation developed in ASE301 the prior semester
**System:** MATLAB FDM Solver Suite — 2D Laplace (100×100 grid), 1D Heat Equation (FTCS explicit), 1D Wave Equation (Lax-Wendroff and MacCormack)
**Objective:** Implement stable FDM solvers for four PDE classes, conduct Von Neumann stability analysis, enforce stability limits, and demonstrate convergent and divergent behaviour across parametric Courant and diffusion number sweeps over a 10-second simulation window.
**Outcome:** Delivered four functional MATLAB solvers with convergence-verified results; confirmed FTCS heat equation stability limit (λ < 0.5); demonstrated wave propagation fidelity and instability onset (ν > 1) for both Lax-Wendroff and MacCormack schemes; Laplace solver converged to steady-state heat distribution in 1,451 iterations on a 100×100 grid.

**Activities / evidence records:**
- **Led — Led development of four MATLAB finite difference solvers covering elliptic, parabolic, and hyperbolic PDE classes, applying ASE301 numerical methods experience to architect the solution approach and implement stability-verified codes.**
  - How: Implemented a 2D iterative Gauss-Seidel solver for the Laplace equation on a 100×100 grid (one boundary at 100°C, others at 0°C), iterating to convergence within error tolerance 0.01. Coded an explicit FTCS solver for the 1D unsteady heat equation with Von Neumann stability analysis confirming λ < 0.5 limit, demonstrated with λ = 0.05, 0.5, and 1.0 (divergent). Implemented Lax-Wendroff and MacCormack two-step predictor-corrector schemes for the linearised wave equation, both with sinusoidal IC on [0,π], sweeping Courant number ν across 0.5, 0.83, 1.0, and 1.33 to demonstrate stable propagation and instability onset. All unsteady solvers output results at 1-second intervals over 10 seconds with minimum 100 nodes.
  - Result: All four solvers delivered converged results within stability limits. Laplace solution reached steady-state at iteration 1,451. Heat equation confirmed theoretical λ < 0.5 stability bound with divergence visually demonstrated at λ = 1. Both wave equation schemes produced clean sinusoidal propagation at ν ≤ 1 and catastrophic divergence at ν = 1.33. MacCormack showed reduced numerical diffusion compared to Lax-Wendroff at equivalent ν values.

#### Conceptual Design of a Fixed-Wing Luxury Aircraft (Graduation Project I)
**Potential CV sections:** Selected Engineering / R&D Projects; Technical Skills
**R&D:** No

**Description:** Full conceptual design lifecycle for a luxury private jet intended to fly London–New York (5,585 km) in under 9 hours, accommodating 10 passengers. Scope covered mission profiling, weight estimation, airfoil selection, wing geometry sizing, T/W and W/S parametric analysis, fuselage/tail/engine sizing, centre of gravity estimation, and landing gear design — executed following Raymer's Aircraft Design methodology.
**System:** Fixed-Wing Manned Aircraft — Luxury Business Jet (Conceptual Design)
**Objective:** Produce a complete conceptual design package for a transatlantic luxury private jet meeting customer-specified range, speed, passenger capacity, and safety requirements, benchmarked against six competitor aircraft.
**Outcome:** Delivered a fully sized conceptual design with W₀ = 20,600 kg, wing area S = 49 m², fuselage length 23.4 m, GE CF34-derived scaled engines at 39 kN/engine, T-tail configuration, tricycle landing gear, and CG located at 11.51 m from the nose — validated against takeoff distance, service ceiling, and stall constraints. Final three-view layout produced at 1:150 scale in Autodesk Inventor.

**Activities / evidence records:**
- **Contributed — Defined customer design requirements and conducted a structured competitor benchmarking study across six business jet aircraft to anchor the conceptual design baseline.**
  - How: Extracted and tabulated performance, geometric, and design characteristics from manufacturer data for Gulfstream G280, Cessna Citation X+, Bombardier Challenger 650, Embraer Legacy 650e, Dassault Falcon 2000S, and Cessna Citation Longitude. Requirements formalised around range (5,585 km), speed (< 9 hrs LHR–JFK), passenger capacity (10), takeoff/landing distance constraints, and service ceiling.
  - Result: Established verified design requirements and a competitor data matrix covering T/W, W/S, fuel weight, empty weight, range, cruise Mach, and geometric parameters — used as the primary reference baseline throughout all subsequent design phases.
- **Contributed — Estimated initial take-off gross weight W₀ using mission segment weight fractions and conducted parametric trade studies to characterise W₀ sensitivity to range, endurance, and payload.**
  - How: Defined a six-segment simple mission profile (warm-up/takeoff, climb, cruise, descent, loiter, landing). Applied Breguet Range Equation and Endurance Equation to compute cruise and loiter weight fractions using GE CF34 TSFC values (ct_cruise = 0.00035 s⁻¹, ct_loiter = 0.000222 s⁻¹) and L/D_max = 18. Implemented iterative MATLAB solver (initial guess W₀ = 40,000 kg) to converge on W₀ = 19,500 kg. Followed with parametric MATLAB sweeps varying range, endurance, and payload independently; computed sensitivity slopes (∂W₀/∂R ≈ 0.12 N/m, ∂W₀/∂E ≈ 9 N/s, ∂W₀/∂payload ≈ 11.4).
  - Result: Converged initial W₀ = 19,500 kg. Trade study confirmed payload as the dominant driver of gross weight, informing conservative payload assumptions carried forward in refined sizing
- **Contributed — Selected the wing airfoil through comparative aerodynamic analysis of five candidate profiles and sized all primary wing geometry parameters.**
  - How: Computed design lift coefficient CL from cruise conditions (W/S = 400 kg/m², q at cruise altitude). Retrieved polar data for NACA 2412, NACA 63-215, NACA 23112, NACA 4415, and Eppler 403 from airfoiltools.com; compared Cl-α, Cd-α, Cm-α, and drag polar characteristics. Selected NACA 23112 based on favourable Cl/Cd performance at design CL. Sized wing geometry per Raymer historical trend charts: AR = 8.5, quarter-chord sweep = 28°, taper ratio = 0.3, twist = −3°, incidence = 2°, dihedral = 3°.
  - Result: Wing geometry fully defined: AR 8.5, sweep 28°, taper 0.3, dihedral 3°. NACA 23112 selected as wing airfoil and carried forward into all subsequent aerodynamic and sizing calculations.
- **Contributed — Determined final thrust-to-weight ratio and wing loading through multi-constraint parametric analysis, then refined the take-off gross weight estimate using updated mission segment fractions.**
  - How: Derived T/W and W/S constraints from stall speed, landing distance, cruise flight, positive limit load factor (n = 2.5), takeoff distance, and maximum ceiling requirements. Cross-referenced against competitor T/W and W/S values; selected T/W = 0.37, W/S = 420 kg/m². Refined W₀ using updated empty weight fraction (statistical Raymer relation with AR, T/W, W/S, Mach dependencies) and recomputed mission segment fuel fractions (climb, cruise, descent, loiter, landing) in MATLAB iterative solver
  - Result: Refined W₀ = 20,600 kg, fuel weight = 8,200 kg. T/W = 0.37 and W/S = 420 kg/m² confirmed as the design point satisfying all performance constraints.
- **Contributed — Sized all major airframe components — fuselage, wing, tail surfaces, and engines — and estimated the aircraft centre of gravity from component weight and moment arm data**
  - How: Fuselage length derived from statistical W₀ trend (23.4 m); cabin cross-section sized for 10-passenger luxury layout benchmarked against competitor cabin dimensions. Wing area computed from W/S = 420 kg/m² and W₀ → S = 49 m²; mean chord = 2.84 m; fuel tank volume verified within wing geometry. Engine scaled from GE CF34-3 baseline (28.9 kN) to mission thrust requirement → 39 kN/engine. T-tail selected; horizontal and vertical tail areas sized using volume coefficient method (Raymer). CG estimated via MATLAB moment summation across crew, payload, fuel, engine, fuselage, wing, horizontal tail, vertical tail, cockpit, and cabin — moment arms measured from nose datum.
  - Result: Fuselage length 23.4 m, wing area 49 m², wingspan 20.4 m, engine thrust 39 kN/engine (×2), T-tail configuration. CG located at 11.51 m from nose, within acceptable range relative to aerodynamic centre.
- **Contributed — Designed the landing gear configuration, sized tyres and struts, validated geometric placement, and produced the final three-view layout drawing.**
  - How: Selected tricycle configuration based on competitor study and stability benefits. Sized nose and main gear tyres using Raymer statistical relations (d = A·Ww^B, w = A·Ww^B): nose wheel d = 84 cm, w = 25.6 cm; main wheel d = 122.5 cm, w = 35.5 cm (4 wheels, 2 struts). Landing gear located geometrically using tipback angle (20° < 25° limit) and overturn angle (55° < 63° limit) constraints, yielding main gear 0.91 m aft of CG, nose gear 8.19 m forward of CG, lateral strut spacing 1.75 m from centreline. Final three-view layout drafted at 1:150 scale in Autodesk Inventor incorporating all sized geometry.
  - Result: Tricycle landing gear fully sized and geometrically validated. Three-view layout at 1:150 scale completed as the primary design deliverable, capturing all major aircraft dimensions and configuration.

#### Conceptual Design of a VTOL Personal Air Vehicle (Graduation Project II)
**Potential CV sections:** Selected Engineering / R&D Projects
**R&D:** No

**Description:** Conceptual design of a VTOL personal aerial vehicle (PAV) for urban intra-city operations in Dubai. Scope covered customer requirements definition, competitor benchmarking, BEMT-based rotor sizing, iterative weight estimation, forward flight power analysis, engine selection, and full configuration design — executed in a group of 4.
**System:** Rotorcraft — Single Main Rotor Helicopter (Conceptual Design)
**Objective:** Design a VTOL PAV meeting customer-specified OGE hover ceiling (3,000 m), minimum cruise speed (220 km/h), range (650 km), and 5-passenger capacity, competitive with existing light civil helicopters.
**Outcome:** Delivered a fully sized conceptual design with TOGW = 2,014 kg, empty weight fraction = 0.4268, main rotor radius = 5.2 m, disk loading = 24 kg/m², Turbomeca Arriel 2B turboshaft (632 kW), skid landing gear, and Garmin G1000H avionics suite. Three-view engineering drawing produced as final deliverable.

**Activities / evidence records:**
- **Contributed — Defined customer design requirements and benchmarked six light civil helicopters to establish the design baseline.**
  - How: Formalised requirements around OGE hover ceiling (3,000 m), minimum cruise speed (220 km/h), range (650 km), cockpit seating (2), cabin seating (4), max empty weight fraction (0.45), max main rotor tip speed (195 m/s), and max tail rotor tip speed (180 m/s). Tabulated performance, power, geometry, and weight data for Bell 407GXi, EC130, Bell 505, AS350, Enstrom 480B, and Kopter SH09. Dubai operating environment accounted for (35–45°C summer temperatures).
  - Result: Verified requirements set and competitor data matrix covering TOGW, empty weight fraction, rotor diameter, disk loading, cruise speed, and range — used as baseline throughout all subsequent design phases.
- **Contributed — Selected the rotor airfoil and sized the main and tail rotors through Blade Element Momentum Theory analysis across three disk loading cases**
  - How: Selected NACA 0012 as rotor airfoil based on established helicopter usage and data availability. Computed lift curve slopes and mean parasite drag coefficients across four Reynolds number sections (100k, 200k, 500k, 1,000k). Implemented BEMT in MATLAB with linear blade twist (−10°), 5% root cutout, 4 blades, chord = 0.27 m, Vtip = 190 m/s. Evaluated three disk loading cases (20, 24, 30 kg/m²); compared figure of merit, root pitch angle, TOGW, and empty weight fraction. Selected Case 2 (DL = 24 kg/m²) as optimal balance between hover efficiency and stall margin.
  - Result: Main rotor radius = 5.2 m, tail rotor radius = 0.88 m, FM = 0.72, hover power = 306 kW, root pitch angle = 16.7°, TOGW = 2,014 kg, empty weight fraction = 0.4268.
- **Contributed — Estimated helicopter component weights iteratively using empirical group equations and selected the engine based on power requirements.**
  - How: Applied statistical component weight group equations (main rotor, tail rotor, powerplant, powerplant section, mechanical drive, landing gear, fuselage, wing, forward propulsion) from Leishman in MATLAB. Iterated against BEMT-derived power and TOGW until convergence. Computed total power requirement including 15% tail rotor allowance. Selected Turbomeca Arriel 2B turboshaft (632 kW) based on power margin, MRO availability, commonality with competitors, and single-engine cost efficiency.
  - Result: TOGW = 2,014 kg, empty weight = 865 kg, empty weight fraction = 0.4268 — within customer-specified maximum of 0.45. Turbomeca Arriel 2B confirmed as engine.
- **Contributed — Computed total power required across the forward flight speed envelope to validate engine selection and characterise helicopter performance.**
  - How: Applied momentum theory in MATLAB to compute induced velocity in forward flight as a function of speed. Calculated induced power (Pi), profile power (P0), and parasite power (Pparasite) components across 0–100 m/s speed range using TOGW = 2,014 kg, R = 5.2 m, Vtip = 190 m/s, CD0 = 0.00967, equivalent flat plate area f = 0.7 m². Total power computed as 1.15× main rotor power to account for tail rotor. Plotted power vs. forward speed curve; identified power minimum and high-speed compressibility/stall limitations.
  - Result: Power curve validated engine selection at 632 kW with adequate margin at cruise speed of 250 km/h. Confirmed expected power bucket behaviour — induced power dominates at low speed, profile and parasite power dominate at high speed.
- **Contributed — Defined all major design configuration choices and produced the final three-view engineering drawing.**
  - How: Selected conventional single main rotor + tail rotor configuration for simplicity and civil suitability. Chose articulated hub with 4 blades and −10° twist for balance between forward flight efficiency and hub bending stress reduction. Specified tractor tail rotor (2 blades) for torque counteraction and yaw control. Selected skid landing gear for weight and drag reduction. Designed vertical fin-only empennage to minimise weight. Specified split clamshell doors for cabin access and executive seating layout for 4 passengers. Selected Garmin G1000H integrated glass cockpit and FADEC ART2 dual-channel engine control system. Produced three-view engineering drawing capturing all major dimensions and configuration.
  - Result: Complete rotorcraft configuration defined and documented. Three-view engineering drawing produced as primary design deliverable: fuselage length 10.6 m, total length 12.8 m, rotor diameter 10.4 m, tail rotor diameter 1.76 m, height 3.6 m.

#### Design and Development of an Automated Air Filter
**Potential CV sections:** Selected Engineering / R&D Projects; Technical Skills
**R&D:** No

**Description:** Design, build, and test of an autonomous electromechanical air filtration system integrating an optical dust sensor, Arduino microcontroller, PWM-controlled DC fan, HEPA/activated carbon filter cartridge, and real-time LCD air quality display. Built in a group of 2 as a mechatronics term project.
**System:** Autonomous Electromechanical Air Filtration System
**Objective:** Design and physically realise an automated indoor air purifier capable of detecting dust and smoke density, autonomously activating a filtration fan based on calibrated thresholds, and displaying real-time air quality data to the user
**Outcome:** Fully functional automated air filter built and tested. System correctly detected dust/smoke across four calibrated density bands, autonomously controlled fan timing (10s/30s), displayed real-time readings on LCD, and triggered RGB and buzzer alerts — validated against live dust and smoke conditions.

**Activities / evidence records:**
- **Contributed — Defined system requirements, selected all electromechanical components, and produced the full circuit schematic.**
  - How: Defined autonomous operation requirements — dust/smoke detection, threshold-based fan activation, real-time air quality display, LED and buzzer alerting. Selected Sharp GP2Y1010AU0F optical dust sensor (min detectable particle 0.5 µm, analog output 0–1.5V), Arduino UNO/MEGA microcontroller, 16×2 LCD with potentiometer brightness control, RGB LED module, piezo buzzer, 80mm 12V DC brushless fan, BD135 NPN transistor for PWM fan switching, IN4007 flyback diode, and HEPA + activated carbon cylindrical cartridge. Designed full circuit schematic in Fritzing covering all pin assignments, transistor-based fan switch, sensor wiring, and LCD interface.
  - Result: omplete component BOM and verified circuit schematic produced in Fritzing — used as the build reference for all subsequent assembly and firmware development.
- **Contributed — Developed Arduino firmware implementing sensor reading, dust density calculation, threshold-based control logic, and all output actuation**
  - How: Wrote Arduino C++ code reading analog output of Sharp GP2Y1010AU0F via PWM LED pulse timing (samplingTime = 280 µs, deltaTime = 40 µs, sleepTime = 9,680 µs). Converted raw ADC values (0–1023) to voltage (0–5V) then dust density (mg/m³) via calibration equation: dustDensity = 0.17 × V − 0.1. Defined 4-band threshold logic: <0.0938 (fan off, green LED), 0.0938–0.2 (fan off, blue LED), 0.2–0.41 (fan on 10s, purple LED, buzzer normal), >0.41 (fan on 30s, red LED, buzzer fast). Implemented PWM fan control via BD135 transistor on digital pin 11. LCD continuously displays live dust density and fan status.
  - Result: Fully functional firmware deployed on Arduino. Sensor-to-actuator logic validated across all four dust density bands with correct fan timing, LED colour, and buzzer behaviour.
- **Led — Fabricated the device housing, assembled all subsystems into a unified physical unit, resolved integration faults, and validated full system operation.**
  - How: Selected cardboard housing and partitioned into two compartments — circuit bay and filter bay. Mounted breadboards on balsa wood L-beam supports in layers; positioned LCD, RGB LED, and calibration chart on user-facing front panel; cut access window for lower breadboard serviceability. Installed Arduino on top layer for accessibility. Inserted and sealed HEPA/activated carbon cylindrical cartridge in filter compartment. Integrated DC fan into filter bay. Connected all subsystems per Fritzing schematic. Led debugging of sensor-microcontroller-actuator interface faults encountered during integration; verified sensor accuracy against live dust and smoke conditions and confirmed all outputs responded per calibrated thresholds.
  - Result: Fully integrated, functional automated air filter unit delivered. System operated autonomously — correctly detecting air impurities, activating fan per threshold logic, displaying real-time density on LCD, and triggering alerts — validated under live test conditions.

#### Simulation of a piezoelectric d15 torsion sensor
**Potential CV sections:** Selected Engineering / R&D Projects; Technical Skills
**R&D:** Yes

**Description:** Numerical investigation of a piezoelectric d₁₅ torsion sensor consisting of two oppositely poled PIC255 piezoceramic shear patches joined side by side, modelled and analysed using Finite Element Analysis in Abaqus CAE. Analysis covered quasi-static, modal, and harmonic responses under torsional moment loading, with sensor voltage and electromechanical coupling coefficient as primary outputs. Individual project.
**System:** Smart Composite Structure — Cantilevered Piezoelectric d₁₅ Torsion Sensor (FEA Simulation)
**Objective:** Determine the sensor voltage generated by a PIC255 piezoceramic d₁₅ torsion sensor under 1 Nm torsional moment loading at quasi-static (1Hz) and dynamic (first torsional frequency) conditions, and compute the electromechanical coupling coefficient across three torsional modes
**Outcome:** Quasi-static sensor voltage of 1.789 V obtained at 1Hz; harmonic sensor voltage of 2.31 V at 55.895 Hz. First three torsional frequencies extracted at 111.79 Hz, 414.71 Hz, and 885.42 Hz. Electromechanical coupling coefficients computed as k = 0.0073, 0.0076, and 0.0026 for modes 2, 4, and 7 respectively.

**Activities / evidence records:**
- **IndependentlyExecuted — Established the theoretical framework for the d₁₅ piezoelectric sensing effect and defined the full PIC255 material model in Abaqus CAE with dual-polarization patch assignment.**
  - How: Derived d₁₅ sensing behaviour from the piezoelectric constitutive equations (D = dT + εE; ε = sT + dE). Reduced to the 3-axis electric displacement equation Dz = e₁₅εxz + ε¹¹ˢEz for the d₁₅ shear sensing case. Derived short circuit charge (Qsc = d₁₅σxzA) and open circuit voltage (Voc = −d₁₅σxz/ε¹¹ᵀ × t) expressions. Characterised PIC255 as a transversely isotropic PZT material and entered full material property matrix in Abaqus: piezoelectric coupling stress constants (e₁₅ = e₂₄ = 11.9, e₃₁ = e₃₂ = −7.15, e₃₃ = 13.7 C/m²), dielectric constants (ε²²ˢ = ε³³ˢ = 8.234, ε¹¹ˢ = 7.588 nF/m), Young's moduli, shear moduli, Poisson's ratios, and mass density (7,800 kg/m³). Created two material models with opposite piezoelectric stress coefficient signs to represent the two oppositely poled patches. Assigned sections to partitioned beam regions accordingly.
  - Result: Complete PIC255 dual-polarization material model defined and verified in Abaqus CAE, ready for FEA preprocessing and simulation.
- **IndependentlyExecuted — Built the full Abaqus CAE finite element model of the cantilevered piezoelectric beam including geometry, boundary conditions, constraints, and mesh.**
  - How: Modelled structure as a single beam (L = 80 mm, 2h = 0.5 mm, 2b = 30 mm) then partitioned into two piezoceramic patches. Assigned PIC255+ and PIC255− material sections to respective patch regions. Created datum coordinate system and assigned material orientations to both patches. Applied ENCASTRE cantilever boundary condition on the fixed end. Applied zero voltage (electric potential = 0) boundary condition on top piezoelectric surface for open circuit simulation. Set global seed size 0.0015 m; doubled seeds along thickness direction to account for geometry. Assigned C3D20E quadratic 20-node piezoelectric brick element type to all parts.
  - Result: Fully meshed and constrained Abaqus CAE model with correct piezoelectric element type, material orientations, and boundary conditions — ready for simulation
- **IndependentlyExecuted — Executed three sequential FEA analyses — quasi-static, modal, and harmonic — to extract sensor voltages and electromechanical coupling coefficients across torsional modes.**
  - How: Quasi-static: Created Steady-state dynamics Direct step at 1 Hz. Defined reference point at tip coupled to free surface via kinematic constraint. Applied 0.1 Nm torsional moment. Enforced equipotential constraint via equation option. Set EPOT as field output. Max sensor voltage extracted from postprocessing. Modal: Suppressed quasi-static step; created Frequency step requesting 20 eigenvalues. Identified torsional modes by deformation shape inspection: Mode 2 (111.79 Hz), Mode 4 (414.71 Hz), Mode 7 (885.42 Hz). Harmonic: Created Steady-state dynamics Direct step at 55.895 Hz (half of first torsional frequency). Applied same moment and equipotential constraint as quasi-static. EMCC: Repeated modal analysis under short circuit conditions (both surfaces grounded, equipotential constraint suppressed); extracted ωsc for three torsional modes; computed k² = (ωoc² − ωsc²)/ωsc²
  - Result: Quasi-static sensor voltage = 1.789 V at 1 Hz. Harmonic sensor voltage = 2.31 V at 55.895 Hz. Torsional frequencies: 111.79, 414.71, 885.42 Hz. EMCC: k = 0.0073 (Mode 2), 0.0076 (Mode 4), 0.0026 (Mode 7)

---

## Middle East Technical University — Secretary General, International Students Association

**Role:** Undergraduate Student  
**Type:** Leadership  
**Location:** Turkey, Northern Cyprus  
**Dates:** 2016-09-01 → 2018-01-31  
**Primary CV section:** No dedicated Master-CV section; technical evidence may support Professional Profile / Projects  
**Secondary:** Targeted CV variants  

**Experience description (database):**
> Executive leadership role serving as Secretary General of the International Students Association at METU NCC[cite: 3, 4, 25, 31]. Served as the highest-ranking African student representative on the executive board, directed day-to-day operations across 8 directorates, led recruitment interviews for student leadership positions, managed administrative approval pipelines, and ran point on major cultural, social, and sports events

### Experience-level activities
- **Led — Managed daily operational workflows for ISA across eight functional directorates, led talent acquisition interviews, and served as executive representative for the international/African student body**
  - How: Co-directed board operations with the President and Director General; structured executive roles across Publications, Logistics, HR, PR, Media, Events, Finance, and Marketing; conducted recruitment interviews to build a 50+ person team of directors, assistants, and volunteers.
  - Result: Built a fully staffed organizational structure across 8 directorates, maintained active engagement for over 70 student members, and established efficient daily operational workflows.
- **Led — Authored official event proposals, managed university approval workflows, coordinated inter-university transportation, and directed social media marketing campaigns**
  - How: Drafted formal proposals and navigated multi-tier signature approval pipelines (ISA President, Academic Advisor, Directorate of Social and Cultural Affairs); liaised with Near East University to arrange campus transit for 40 delegates to African Night 2016; coordinated with the Media team on promotional videos, banners, and digital flyers.
  - Result: 100% administrative proposal sign-off, secured campus funding/logistics, and expanded digital outreach to increase international event turnouts
- **Led — Ran point on campus-wide flagship events including the 10th International Food Festival, METU’s Got Talent, International Music Festival, sports tournaments, and cultural excursions**
  - How: Oversaw on-site event execution, stage timing, venue setup, and judge/contestant coordination; managed supply chain logistics including ingredient sourcing and allocation for international food stalls; organized sports competitions (ISA Football Tournament, Olympic Games) and historical trips (St. Hilarion Castle)
  - Result: Successfully delivered high-attendance campus festivals and competitions, engaging hundreds of domestic and international students.

---

## ALS Ltd — Aircraft Maintenance Intern

**Role:** Internship  
**Type:** Professional  
**Location:** Wilson Airport, Nairobi  
**Dates:** 2017-07-24 → 2017-09-02  
**Primary CV section:** Professional Experience  
**Secondary:** Technical Skills  

**Experience description (database):**
> Hands-on MRO internship at ALS Ltd, a KCAA-certified aviation company based at Wilson Airport Nairobi, conducted as a mandatory industrial attachment for the BSc Aerospace Engineering programme at METU. Worked under the supervision of licensed engineers in the Base Maintenance department, assisting with 200HR inspections, line maintenance, and C-check tasks across a mixed turboprop and turbofan fleet including the Beechcraft 1900C (PT6A-65B), De Havilland DHC-8 (PW121), and Embraer ERJ145MP (Rolls-Royce AE 3007A). Supervised by Base Maintenance Manager Maurice Mukung

### Projects

#### Aircraft Line, Base & C-Check Maintenance — ALS Ltd MRO
**Potential CV sections:** Professional Experience; Technical Skills
**R&D:** No

**Description:** Hands-on MRO internship across turboprop and turbofan aircraft types at ALS Ltd's Wilson Airport maintenance facility. Assisted licensed engineers with 200HR inspection tasks, line maintenance activities, and C-check procedures across three aircraft types, working from task cards under direct supervision. Internship submitted as a formal academic report to METU Department of Aerospace Engineering (ASE 300).
**System:** Beechcraft 1900C — PT6A-65B turboprop; De Havilland DHC-8-100 — PW121 turboprop; Embraer ERJ145MP — Rolls-Royce AE 3007A turbofan, Honeywell Primus 1000 avionics
**Objective:** Gain practical MRO exposure across manned commercial aircraft platforms, develop familiarity with aircraft maintenance documentation systems, task card workflows, and hands-on servicing procedures under licensed engineer supervision
**Outcome:** Successfully completed 1 month 1 week internship across all three aircraft types. Formal completion letter issued by Base Maintenance Manager Maurice Mukung confirming fault diagnosis and rectification tasks on airframe and engines. Internship report submitted and accepted by METU.

**Activities / evidence records:**
- **Assisted — Assisted with fuel nozzle replacement on the PT6A-65B turboprop engine during a 200HR inspection on the Beechcraft 1900C**
  - How: Under supervision of Eng. Njenga, loosened fuel tube attachments from 14 combustion chamber nozzles in alternating sequence using round-faced hammer, flat-edged screwdriver and chisel. Removed nozzle holders using 3/16in ratchet, extension and socket, arranging removed nozzles on the nozzle board in numbered clockwise sequence. Assisted fitting of replacement nozzles into holders, ensuring nipples avoided contact with surrounding material. Refitted nozzle holders to combustion chamber per AMM torque specification of 20–25 ft.lb. Assisted application of locking wire to bolt heads post-torque.
  - Result: 14 fuel nozzles replaced on PT6A-65B engine in compliance with 200HR inspection task card requirements. Removed nozzles packaged and logged for return to manufacturer for refurbishment.
- **Assisted — Assisted with compressor wash on the PT6A-65B turboprop engine during a 200HR inspection on the Beechcraft 1900C**
  - How: Under supervision of Eng. Njenga, assisted with compressor wash procedure following FOD inspection of compressor blades. Connected pressure regulator to two metal cylinders (water and detergent) and to the compressor inlet. Set engine to compressor wash configuration. Flushed detergent then water sequentially through compressor at 40 psi. Monitored liquid exit through compressor screen
  - Result: Compressor wash completed per 200HR task card. Compressor blades cleaned and inspected for FOD
- **Assisted — Assisted with propeller shaft greasing on the PT6A-65B turboprop engine during a 200HR inspection on the Beechcraft 1900C**
  - How: Under supervision of Eng. Njenga, assisted greasing of Hartzell composite 4-blade propeller shafts using Aeroshell Grease 22 (synthetic, amber). Connected greasing gun assembly to shaft greasing nipples. Pumped grease until fresh amber grease displaced old grease at exit faucet, confirming complete purge
  - Result: Propeller shafts on both engines greased per 200HR maintenance requirements. Corrosion protection restored across propeller shaft assembly.
- **Assisted — Assisted with de-icer boot reinstallation on the DHC-8 leading edges during line maintenance**
  - How: Under supervision of Eng. Karanja, assisted reinstallation of pneumatic de-icing boots onto leading edges of both wings of the DHC-8 following removal for servicing. Drove screws into boot attachment points using Phillips screwdriver as part of a 4-technician team. Applied Thiokol sealant to gap between boot and wing surface following masking tape border application, smoothed sealant with Perspex glass chisel, allowed to cure, and removed masking tape
  - Result: De-icing boots reinstalled on both wing leading edges and sealed per line maintenance task card requirements
- **Assisted — Assisted with flap ball screw assembly lubrication on the DHC-8 during line maintenance**
  - How: Under supervision of Eng. Karanja, assisted lubrication of 8 flap ball screw assemblies (4 per wing — 2 outboard, 2 inboard) on DHC-8. Cleaned screw-like sections with alcohol-soaked cloth. Applied Aeroshell Grease 33 (green) manually to full bar length. Connected grease gun assembly to actuator nipples and pumped until fresh grease exited faucet
  - Result: All 8 flap ball screw assemblies lubricated per line maintenance task card. Flap actuator servicing completed.
- **Assisted — Assisted with cabin seat removal and hook-and-loop fastener replacement on the Embraer ERJ145MP during C-check**
  - How: Under supervision of Eng. Kemboi, assisted removal of all 50 cabin seats from ERJ145MP as part of C-check interior clearance. Unbolted seats from floor railing at 4 contact points each using 3/8in dual-spanner method (one to hold nut, one to turn bolt). Seats removed via open emergency exits and stored in depot. Assisted replacement of hook-and-loop seat cushion fastener strips — removed degraded strips using MEK solvent to dissolve adhesive residue, applied new strips using 3M Neoprene High Performance Adhesive diluted with isopropyl alcohol.
  - Result: All 50 seats removed from ERJ145MP cabin and stored. Unserviceable hook-and-loop fastener strips replaced on all seats per C-check task card requirements.
- **Assisted — Assisted with nose landing gear servicing on the Embraer ERJ145MP during C-check**
  - How: Under supervision of Eng. Kemboi, assisted jacking of ERJ145MP on 3 jacks (one below each wing, one at nose gear) to raise aircraft for nose landing gear access. Assisted detachment of wheel, tyre and brake assembly from axle for forwarding to tyre shop. Assisted inspection of outer cylinder assembly and drag strut assembly for damage. Observed subsequent hydraulic and brake fluid work conducted by separate team.
  - Result: Nose landing gear wheel, tyre and brake assembly removed and forwarded to tyre shop for servicing. Outer cylinder and drag strut inspected per C-check task card.

---

## Middle East Technical University — Vice President, Aerospace Society

**Role:** Undergraduate Student  
**Type:** Leadership  
**Location:** Turkey/Northern Cyprus  
**Dates:** 2017-09-01 → 2018-06-30  
**Primary CV section:** No dedicated Master-CV section; technical evidence may support Professional Profile / Projects  
**Secondary:** Targeted CV variants  

**Experience description (database):**
> Executive leadership role co-managing student society operations, technical software workshops, faculty/guest seminars, and hands-on project teams. Spearheaded the society's Model Aircraft Project, facilitated MATLAB/Inventor technical courses, and established professional development channels for aerospace engineering undergraduates.

### Experience-level activities
- **Led — Co-managed administrative operations, budget allocation, society branding competitions, and collaborative events with partner student organizations**
  - How: Formulated mission objectives focused on career flightpaths and Royal Aeronautical Society (RAeS) integration, published society updates, and structured joint technical trips and courses alongside the Energy Society.
  - Result: Expanded society member engagement, successfully organized multi-departmental events, and established a structured administrative framework for student project teams
- **Led — Initiated and coordinated the society's flagship hands-on model aircraft design and construction project team.**
  - How: Partnered with visiting professor and retired USAF pilot Dean Owen to leverage domain expertise and model aircraft hardware; conducted interviews to recruit dedicated student engineering teams.
  - Result: Successfully launched the society's first structured model aircraft project team to serve as a baseline for future international UAV competitions.
- **Led — Organized and facilitated extracurricular technical software training courses in MATLAB and Autodesk Inventor for society members**
  - How: Coordinated with instructors and partner student societies (Energy Society) to schedule course dates, manage documentation, and issue completion certificates.
  - Result: Delivered structured CAD and programming skill development sessions to enhance undergraduate aerospace engineering competencies
- **Led — Conceptualized, scheduled, and hosted academic guest lectures, faculty Q&A sessions, and technical seminars**
  - How: Liaised with departmental faculty (Dr. Cevdet, Dr. Vladimir) and visiting experts via direct communications to prepare presentation topics covering aerospace materials, fatigue in military/civil aircrews, and industry trends.
  - Result: Hosted multiple technical seminars providing students direct access to faculty expertise and specialized aerospace research

---

## Middle East Technical University — President, Model United Nations Society

**Role:** Undergraduate Student  
**Type:** Leadership  
**Location:** Turkey, Northern Cyprus  
**Dates:** 2017-09-01 → 2018-06-30  
**Primary CV section:** No dedicated Master-CV section; technical evidence may support Professional Profile / Projects  
**Secondary:** Targeted CV variants  

**Experience description (database):**
> Executive leadership role reviving and directing the dormant Model United Nations Society at METU NCC. Authored society charter/proposals, rebuilt an active member base of 30+ students, directed weekly parliamentary procedure and debate training workshops, hosted guest diplomacy seminars, and led a 17-member delegation to MUNTR 2018 in Antalya, Turkey

### Experience-level activities
- **Led — Revived the dormant campus Model United Nations chapter, authored the official revival proposal, established administrative structures, and managed active member operations**
  - How: Drafted a formal proposal to the Directorate of Social and Cultural Affairs detailing society purpose, facility requirements, and budget needs; established an executive team (President, Vice President, Head Delegate, Treasurer, Secretary); recruited over 70 registered members and maintained 30+ active student delegates across departments
  - Result: Successfully re-established MUN Society on campus as an active student organization after 2+ years of dormancy, securing seminar room facilities and institutional support.
- **Led — Designed and delivered weekly MUN training curricula while organizing guest lectures on diplomacy and international relations**
  - How: Structured interactive weekly seminars and mock debate simulations covering UN committee structures, country profiling, position paper research, parliamentary rules of procedure, resolution drafting, and lobbying; invited and hosted expert speakers including Dr. Luciano Barraco (Intro to the United Nations) and Dr. Rafet Akgünay (Diplomacy & International Negotiation)
  - Result: Trained 30+ student delegates in parliamentary procedure, public speaking, policy research, and formal debate
- **Led — Led a 17-member student delegation to represent METU NCC at Model United Nations Turkey 2018 (MUNTR) in Antalya, Turkey**
  - How: Secured official administrative travel allowances and delegate package funding from the Directorate of Social and Cultural Affairs; coordinated travel, accommodation, and committee allocations across GA, ECOSOC, NAM, ILO, Historical US Senate, and NATO; personally served as delegate representing Romania in the NATO committee.
  - Result: Successfully fielded METU NCC's first delegation at Turkey's largest collegiate MUN conference (500+ delegates), securing an Honorary Mention in GA 1 DISEC

---

## Middle East Technical University — SI-PASS Leader & Instructor — MAT119 & MAT120

**Role:** Undergraduate Student  
**Type:** Teaching  
**Location:** Turkey/Northern Cyprus  
**Dates:** 2018-09-01 → 2019-05-30  
**Primary CV section:** Teaching & Academic Experience  
**Secondary:** Technical Skills  

**Experience description (database):**
> Certified Supplemental Instruction (SI-PASS) Leader and Instructor at METU NCC, facilitating peer-assisted study sessions for undergraduate mathematics courses MAT119 (Calculus I: Calculus of Single Variable Functions) and MAT120 (Calculus II: Calculus of Multivariable Functions) throughout the 2018 Fall and 2019 Spring academic semesters.

### Projects

#### Calculus Supplemental Instruction & Peer-Assisted Study Sessions
**Potential CV sections:** Teaching & Academic Experience
**R&D:** No

**Description:** Facilitation of peer-assisted study sessions for undergraduate single-variable (MAT119) and multivariable (MAT120) calculus courses at METU NCC following formal SI-PASS leader leadership training and certification
**System:** METU NCC Academic Support & SI-PASS Framework
**Objective:** Enhance student comprehension, problem-solving techniques, and academic performance in foundational calculus through structured, peer-led collaborative learning
**Outcome:** Successfully conducted two weekly 60-minute study sessions across the Fall 2018 and Spring 2019 academic semesters, providing calculus problem-solving support to undergraduate students

**Activities / evidence records:**
- **IndependentlyExecuted — Completed formal 2-day SI-PASS Leadership Training and earned official certification as an SI-PASS Leader at METU NCC.**
  - How: Participated in intensive leadership training on September 29–30, 2018, mastering peer facilitation methodologies, group dynamics management, collaborative learning strategies, and active problem-solving techniques for calculus instruction
  - Result: Formally certified as an SI-PASS Leader and Instructor by the SI-PASS Programme Supervisor and METU NCC Vice President.
- **IndependentlyExecuted — Conducted peer-assisted study sessions for MAT119 (Calculus I) and MAT120 (Calculus II) throughout the 2018 Fall and 2019 Spring semesters**
  - How: Attended 3 weekly lecture hours alongside undergraduate students to track course progression, then designed and facilitated two standalone 60-minute study sessions per week in classrooms and library study rooms focused on single-variable and multivariable calculus problems.
  - Result: Successfully delivered regular peer-led instruction and problem-solving support to interested undergraduate students across both semesters

---

## Middle East Technical University — Student Assistant - ASE301 Numerical Methods for Aerospace Engineers

**Role:** Undergraduate Student  
**Type:** Teaching  
**Location:** Turkey/ Northern Cyprus  
**Dates:** 2019-02-01 → 2019-06-17  
**Primary CV section:** Teaching & Academic Experience  
**Secondary:** Technical Skills  

**Experience description (database):**
> Appointed as Student Assistant for ASE301 (Numerical Methods for Aerospace Engineers) under Prof. Dr. Hakan Tarman based on highest academic grade merit (AA). Conducted consultation sessions and evaluated computational assignments covering ODE/PDE numerical solvers in MATLAB for a cohort of 30+ undergraduate students.

### Projects

#### ASE301 Course Instruction & Student Assessment
**Potential CV sections:** Teaching & Academic Experience
**R&D:** No

**Description:** Academic support, report grading, and student consultation sessions for 30+ undergraduate aerospace engineering students taking ASE301 Numerical Methods for Aerospace Engineers.
**System:** METU NCC ASE301 Academic Curriculum & MATLAB Numerical Solvers
**Objective:** METU NCC ASE301 Academic Curriculum & MATLAB Numerical Solvers
**Outcome:** Successfully conducted 5 consultation sessions and graded 3 major computational assignments covering 12 ODE solvers (Euler1, Euler2, Flowa, Flowb, Flowd, Heun, Lorenz, RK2, RK4, stability_1, stability_2, System) and 3 PDE solvers (heat, p6, wave) in MATLAB.

**Activities / evidence records:**
- **IndependentlyExecuted — Conducted 5 dedicated consultation sessions for a cohort of 30+ undergraduate aerospace engineering students in ASE301**
  - How: Provided technical guidance and debugging support on MATLAB implementations of ODE solvers (Euler1, Euler2, Heun, RK2, RK4, Lorenz, Flowa/b/d, System aeroelastic coupling, stability_1/2) and PDE solvers (heat, wave, p6).
  - Result: Resolved student algorithmic errors and clarified physical interpretations of numerical simulations, including 2-DOF spring-mass-airfoil pitching and plunging dynamics.
- **IndependentlyExecuted — Graded 3 major numerical methods homework assignments and computational experiment reports for 30+ students**
  - How: Evaluated MATLAB code correctness, numerical stability analysis, convergence plots, and physical discussions of aeroelastic and differential equation simulations against course benchmarks
  - Result: Completed timely assessment and detailed feedback for 3 assignment submission cycles throughout the semester

---

## Young Scientists Kenya (YSK) — STEM Mentorship

**Role:** Volunteer   
**Type:** Teaching  
**Location:** Kenya  
**Dates:** 2020-01-01 → 2021-12-31  
**Primary CV section:** Teaching & Academic Experience  
**Secondary:** Technical Skills  

**Experience description (database):**
> Technical mentorship for secondary school student research teams participating in the Young Scientists Kenya national science and technology exhibitions. Provided engineering guidance across mechanical design, embedded systems, system architecture, prototyping, and technical report editing for automotive and aviation projects

### Projects

#### Project Mentor - Hydrogen-Hybrid Engine
**Potential CV sections:** Teaching & Academic Experience; Selected Engineering / R&D Projects; Technical Skills
**R&D:** Yes

**Description:** Mentored a 2-student team (Sifa Home School / Oaks Academy) in the design, fabrication, and testing of a solar-assisted hydroxy (HHO) gas generator integrated into a 160cc 4-stroke petrol engine on a custom motorized bicycle
**System:** Modified 4-stroke Honda GX160 engine (5.5 hp), custom motorized bicycle chassis with Mitsubishi Shogun tappet return spring seat suspension, 8:1 belt drive with centrifugal clutch, 750 ml plastic HHO generator cell (stainless steel plates, NaOH electrolyte), custom "Archillator" damp-cotton moisture trap, 1-inch carburetor intake bypass port, and 16V/1.68A solar panel with 12V 7Ah Li-ion buffer battery.
**Objective:** Integrate an onboard solar-assisted hydroxy gas generator and carburetor bypass into a small 4-stroke internal combustion engine to evaluate fuel efficiency gains (km/L) and air-fuel ratio lean-burn characteristics
**Outcome:** Achieved a 22.6% fuel efficiency increase (25.24 km/L baseline to 30.95 km/L with engine alternator HHO) and a 43.6% increase (to 36.25 km/L with solar-assisted HHO) during road testing at 35 km/h

**Activities / evidence records:**
- **Assisted — Advised on mechanical drivetrain integration, electrical power architecture, HHO safety bypass design, and empirical fuel consumption testing protocols**
  - How: Guided the sizing of the 8:1 centrifugal clutch pulley drive, implementation of the 12V 25A fused power rail, design of the "Archillator" cotton moisture trap, welding of the 1-inch intake manifold bypass port, and execution of 3-run road mileage trials
  - Result: Validated lean-burn engine performance demonstrating a 43.6% fuel mileage gain (36.25 km/L vs. 25.24 km/L baseline pure gasoline).

#### Project Mentor - Portable Aircraft Refueling Rig & Automated Fuel Dispenser
**Potential CV sections:** Teaching & Academic Experience; Selected Engineering / R&D Projects; Technical Skills
**R&D:** Yes

**Description:** Mentored a 3-student team (Juja Preparatory and Senior School) in designing an automated, battery-powered fuel dispensing rig for light aircraft at remote airstrips lacking fuel bowsers
**System:** Arduino UNO R3 microcontroller, 20x4 I2C LCD screen, $4\times4$ matrix keypad, YF-S201 hall-effect pulse flow rate sensor, 12V DC fuel pump, 12V relay switch, 12V LiPo battery rail with solar charging, PTFE fuel lines, dual fuel filters, and status LEDs/buzzer.
**Objective:** Eliminate manual, error-prone container volume fuel transfers at small airstrips by engineering a keypad-controlled dispensing rig that accurately converts targeted fuel mass/volume inputs into automated pump relay actuation
**Outcome:** Completed circuit design (Fritzing), control logic state machine, system flowchart, and functional bench prototype capable of pulse-count volume measurement, auto-shutoff via relay, and real-time LCD status reporting

**Activities / evidence records:**
- **Assisted — Guided the embedded systems architecture, circuit schematic design, and control logic state machine for the automated refueling rig**
  - How: Designed Fritzing circuit schematics mapping the Arduino UNO R3 to the YF-S201 flow sensor interrupt pin, 12V relay pump drive, $4\times4$ keypad, 20x4 I2C LCD, status LEDs, and buzzer; structured the software flowchart for keypad input validation, start/stop/clear states, and pulse-counting target cutoff.
  - Result: Delivered verified circuit layout, software state machine logic, and complete technical abstract for the YSK exhibition submission

---

## eMobilis Technology Institute — Full Stack Software Development

**Role:** Student  
**Type:** Other  
**Location:** Nairobi, Kenya  
**Dates:** 2020-01-20 → 2020-06-30  
**Primary CV section:** Certifications & Licences  
**Secondary:** Technical Skills  

**Experience description (database):**
> Completed a five-month full stack software development programme at eMobilis Technology Institute, Nairobi (Admission No. 01/0120/4698, January 2020 Afternoon intake, under lecturer Benjamin Wanyama). The programme covered web development (HTML, CSS, Python, MySQL) and Android mobile application development (Kotlin, Java, XML). Engaged with all curriculum streams. Completed a capstone Android carpool application (Fadhili). Also obtained Google Digital Skills certification during this period. Subsequently co-founded the Coding Collective — a peer learning group formed from the cohort for continued collaborative development work.

### Projects

#### Fadhili — Android Carpool Application
**Potential CV sections:** Supporting evidence / targeted variants; Technical Skills
**R&D:** No

**Description:** A fully functional Android carpool application designed and developed from scratch as the programme capstone project. Fadhili connected drivers and passengers in real-time, implementing ride matching, live map tracking, user authentication, messaging, notifications, and profile management. Built using Kotlin as the primary language with Firebase as the backend infrastructure and Google Maps SDK for location and mapping services
**System:** Android mobile application — Firebase Authentication, Firebase Realtime Database, GeoFire real-time location engine, Google Maps SDK (driver and passenger map views), Google Play Services
**Objective:** To design and deliver a functional carpool Android application demonstrating end-to-end full stack mobile development competency across UI, backend, authentication, real-time location, and database integration
**Outcome:** Delivered a working Android carpool application (API 16+, target SDK 30) with real-time driver/passenger location tracking, ride coordination, user authentication, and messaging features. Codebase archived on GitHub.

**Activities / evidence records:**
- **IndependentlyExecuted — Designed and developed Fadhili — a full-stack Android carpool application — end to end**
  - How: Independently architected and built the full application in Kotlin and Java, implementing multi-screen UI (landing, splash, sign-in, registration, dashboard, rides, messages, notifications, profile) using XML layouts and Material Design, Firebase Authentication for user management, Firebase Realtime Database for ride coordination and messaging, GeoFire and Google Maps SDK for real-time driver/passenger location tracking, and distance computation between points
  - Result: Delivered a fully functional Android carpool application (SDK 30, API 16+) with real-time location, authentication, ride matching, messaging, and notification features. Codebase archived on GitHub

### Experience-level activities
- **Contributed — Full stack web and mobile development training — HTML, CSS, Python, MySQL, Kotlin, Java, Android**
  - How: Completed the full eMobilis curriculum across front-end web development (HTML, CSS, Bootstrap), back-end development (Python, MySQL), and Android mobile development (Kotlin, Java, XML) over five months under lecturer Benjamin Wanyama Responsibility: Contributed
  - Result: Successfully completed the full programme across all curriculum streams gaining practical competency in web and Android development
- **Led — Co-founded the Coding Collective — a peer collaborative development group from the eMobilis cohort**
  - How: Co-founded an informal coding collective with cohort members from the eMobilis afternoon MIT class, structured around collaborative projects, peer knowledge sharing, and commercialisation of development work across web and Android stacks
  - Result: Established an active peer learning group continuing collaborative development beyond the formal programme, with intent to evolve into a commercial development organisation

---

## Kendrone Ltd — UAS Engineer, Pilot and Instructor

**Role:** UAS Company  
**Type:** Professional  
**Location:** Mtwapa, Nairobi, Naivasha - Kenya  
**Dates:** 2021-01-01 → 2021-06-30  
**Primary CV section:** Professional Experience  
**Secondary:** Technical Skills  

**Experience description (database):**
> Joined Kenya's first KCAA-approved Drone Training Organisation as a student, earning the Remote Pilot Licence (YK-RPL-00013A) before transitioning into a permanent employee role as UAS Pilot, Instructor, and IT Assistant. Delivered ground school and practical flight instruction across three student cohorts, completed the Instructor Rating (IR001-01) under a company-sponsored training bond, and led engineering and innovation work including the design, fabrication, and flight testing of a drone-based seedball dispersal mechanism for reforestation in collaboration with Seedball Kenya. Concurrently owned all IT infrastructure, digital marketing, student administration, and external stakeholder engagement for the company.

### Projects

#### Drone-Based Seedball Dispersal Mechanism
**Potential CV sections:** Professional Experience; Selected Engineering / R&D Projects; Technical Skills
**R&D:** Yes

**Description:** Design, fabrication, integration, and flight testing of a drone-mounted seedball dispersal system for ecological reforestation, developed in collaboration with Seedball Kenya. The project spanned the full engineering lifecycle from requirements capture through witnessed operational demonstration, with a formal endurance test report produced as the primary deliverable.
**System:** Tarot 650 quadrotor — Pixhawk PX4 flight controller, QGroundControl GCS, servo-actuated seedball container and release mechanism (custom-designed), 6S LiPo power system
**Objective:** Design and validate a payload mechanism enabling autonomous grid-pattern seedball dispersal from a multirotor UAS, characterise platform endurance under operational payload conditions, and demonstrate system readiness to Seedball Kenya and regulatory observers.
**Outcome:** Mechanism successfully designed, fabricated, and integrated. Endurance test campaign (3 flights) established that dual 6S parallel battery configuration was optimal, achieving ~9min endurance, ~2km grid coverage, and ~5532m² area per sortie with 500g seedball payload. Findings and recommendations formally submitted to Seedball Kenya

**Activities / evidence records:**
- **Led — Captured mission requirements from CEO and Seedball Kenya and produced mechanical design of seedball container and servo-actuated release mechanism**
  - How: Requirements received verbally from CEO Craig Cleave in a meeting, specifying payload capacity, drop pattern, and coverage area targets for reforestation missions. Designed container and servo-actuated latch release in Autodesk Inventor, referencing existing Tarot 650 CAD geometry to ensure dimensional compatibility with the airframe mounting points.
  - Result: Fully detailed CAD design of seedball container and release mechanism, dimensionally compatible with Tarot 650 airframe, ready for fabrication
- **Led — Fabricated mechanism components and integrated the dispersal payload onto the Tarot 650 airframe including servo power rail decoupling**
  - How: 3D printed container and release mechanism components on Duplicator printer using PLA. Physically assembled and mounted mechanism under the Tarot 650 airframe. Designed and implemented a dedicated servo power rail decoupled from the main Tarot power bus to prevent servo draw from interfering with flight controller power. Wired servo to Pixhawk PX4 PWM output channel and configured auto-trigger in QGroundControl mission planner, mirroring the camera trigger function used in survey missions.
  - Result: Fully integrated dispersal payload on Tarot 650 airframe. Servo-actuated release responsive to both manual RC PWM input and autonomous mission trigger commands from QGroundControl
- **Led — Prepared Tarot 650 platform for flight operations — diagnosed and resolved flight controller calibration and motor imbalance issues, configured failsafes, and conducted initial airworthiness verification flight**
  - How: Identified motor imbalance and flight controller calibration anomalies during pre-flight checks. Performed ESC calibration, compass calibration, and accelerometer calibration on Pixhawk PX4 via QGroundControl. Balanced and re-seated motors to resolve vibration. Configured RTL and auto-land failsafes for low and critical battery voltage thresholds. Conducted initial checkout flight on 7 May 2021 to verify platform airworthiness prior to payload testing.
  - Result: Tarot 650 confirmed airworthy. Failsafes correctly configured. Platform cleared for payload endurance test campaign.
- **Led — Executed 3-flight endurance test campaign to characterise platform performance under operational payload conditions and authored formal test report**
  - How: Conducted 3 structured flights on 2–3 June 2021 at Kendrone Mtwapa Training Site (Greenwood Resort), varying battery configuration and payload mass: Flight Test 001 (1×6S, 1300g payload), Flight Test 002 (2×6S parallel, no seedballs), Flight Test 003 (2×6S parallel, 500g seedballs). Flew autonomous grid pattern missions (5449.24m², 1786m distance, 5m grid spacing, 50m AGL) in QGroundControl. Recorded voltage at takeoff, mid-flight, and landing for each test. Computed discharge rates and extrapolated endurance curves. Flight data logged to px4.io. Authored full endurance test report including battery discharge characterisation, payload weight tables, flight maps, results and recommendations.
  - Result: Established dual 6S parallel as optimal configuration — discharge rate 0.0054V/s with 500g seedball payload, ~9min 10sec endurance, ~2km grid coverage, ~5532m² area, ~400 seedball capacity at 5m trigger spacing. Single 6S configuration found insufficient — critically low voltage (19.4V) reached within 6min 18sec. Formal report submitted to Seedball Kenya.
- **Led — Conducted witnessed operational demonstration of the seedball dispersal system before Seedball Kenya, KCAA-adjacent observer, and company CEO**
  - How: Prepared platform and payload for formal demonstration flight. Briefed attendees on system capabilities, mission parameters, and safety procedures. Executed demonstration flight with mechanism active. Results and endurance test findings presented and submitted to Seedball Kenya as basis for further development decisions
  - Result: Demonstration successfully completed in the presence of a Mtwapa Police Station officer, Seedball Kenya representative, and CEO Craig Cleave. Mission footage recorded and published across Kendrone social media platforms. Findings and recommendations formally delivered to Seedball Kenya

#### UAS Pilot Training Programme Delivery
**Potential CV sections:** Professional Experience; Technical Skills
**R&D:** No

**Description:** Delivery of the full KCAA Remote Pilot Licence training programme across three student cohorts at Kenya's first KCAA-approved Drone Training Organisation. Encompassed ground school instruction across seven theory domains, a 15-lesson practical flight syllabus, and a technical BVLOS presentation delivered to a KCAA representative as part of the instructor certification process
**System:** DJI Phantom 4 Pro (5Y-0006A, 5Y-0072A), DJI Phantom 3 Pro (5Y-0008A), DJI Mavic Pro (5Y-0007A), Tarot 680 Pro (5Y-0021A) — all operated under Kendrone UTO KCAA authorisation
**Objective:** Train and qualify student pilots to KCAA RPL standard across ground school and practical flight phases, achieving regulatory sign-off and license issuance for all enrolled students.
**Outcome:** Three cohorts trained (~16 students total, ~10 as primary instructor, ~6 during teaching practice). 9.0 logged instructor flight hours across Naivasha and Mtwapa. 100% student pass rate. BVLOS presentation successfully delivered to KCAA representative, chief instructor, and CEO.

**Activities / evidence records:**
- **Led — Delivered a 32-slide technical presentation on BVLOS UAS operations to a KCAA representative, chief instructor, and CEO as part of the instructor rating certification process**
  - How: Researched and authored a comprehensive presentation covering BVLOS definition and operational categorisation under Civil Aviation (UAS) Regulations 2020, C2 link architectures (RLOS and B-RLOS), IFR requirements (ATC radio, transponder, DAA systems), ICAO RPAS CONOPS provisions, and global BVLOS case studies across 10 countries. Delivered as formal academic and practical assessment for instructor rating qualification.
  - Result: Presentation successfully delivered. Contributed to successful completion of Instructor Rating (IR001-01) under Kendrone UTO, issued under KCAA framework.
- **Led — Delivered full KCAA RPL ground school theory programme across three student cohorts covering seven subject domains**
  - How: Delivered classroom-based instruction across all seven KCAA RPL theory domains: Air Law, Flight Plan Filing, Human Factors, Meteorology, Navigation and Flight Planning, Principles of Flight, and Technical and General. Prepared and distributed study materials in advance of each cohort. Managed student questions, conducted internal assessments, and maintained student training files (APPENDIX 14) including exam records in compliance with UTO quality management requirements. Pass mark threshold enforced at 70% per KCAA requirements.
  - Result: All students across three cohorts passed theoretical knowledge examinations to KCAA RPL standard. Post-training reference materials provided to students. Positive student feedback received — rated instruction as excellent across personal approach, knowledge transfer, and study material provision.
- **Led — Delivered 15-lesson KCAA RPL practical flight instruction programme across three student cohorts on multirotor platforms**
  - How: Instructed students through the full KCAA RPL-MR practical syllabus: UAS familiarisation, pre-flight site survey, takeoff, tail-in hover, yaw manoeuvres, lateral and longitudinal movements, vertical manoeuvres, rectangles, nose-in manoeuvres, slow level circuits, climbing and descent circuits, tear drop, and emergency procedures. Scored each lesson on the 4-point KCAA competency scale. Signed off student training checklists (APPENDIX 24) upon completion of each phase. Recommended students for RPL skill test upon satisfactory completion. Flew as safety pilot and instructor on DJI Phantom 4 Pro, DJI Phantom 3 Pro, DJI Mavic Pro, and Tarot 680 Pro across Naivasha and Mtwapa sites
  - Result: 9.0 logged instructor flight hours. ~16 students trained across three cohorts. 100% student pass rate on KCAA RPL skill test. All students successfully obtained KCAA Remote Pilot Licences.

#### Aerial Mapping & Agricultural Survey Operations
**Potential CV sections:** Professional Experience
**R&D:** No

**Description:** End-to-end UAS mapping and agricultural survey operations using DJI Phantom 4 Pro with RGB and multispectral payloads, covering mission planning, field data capture, and full photogrammetric processing to survey-grade outputs. Operations served both internal Kendrone missions and external survey company clients, with concurrent surveyor training delivered during live missions.
**System:** DJI Phantom 4 Pro with RGB camera (survey) and multispectral sensor (agriculture) — Pix4D for survey processing, Pix4Dfields for agricultural analysis
**Objective:** Execute aerial survey and precision agriculture data capture missions to survey-grade output standards, and upskill survey company clients in UAS-based mapping workflows
**Outcome:** Full mapping workflows executed end-to-end including orthomosaic, DSM/DTM, contour lines, 3D models, and vegetation index outputs. Survey company surveyors trained concurrently during live operational missions.

**Activities / evidence records:**
- **Led — Executed end-to-end aerial survey and agricultural mapping missions as PIC, from mission planning through photogrammetric processing to final deliverable outputs**
  - How: Planned survey missions in Pix4D — defined survey areas, set grid patterns, GSD, altitude, and waypoint parameters. Flew DJI Phantom 4 Pro as PIC with RGB payload for topographic survey missions and multispectral payload for agricultural missions. Processed captured data in Pix4D to produce orthomosaic, DSM/DTM, contour lines, 3D models, area and volume analyses, and CAD/GIS outputs. Processed agricultural datasets in Pix4Dfields to generate vegetation index maps for crop health analysis.
  - Result: Full survey-grade outputs produced across multiple missions including orthomosaic, DSM/DTM, contour maps, and vegetation index outputs. Deliverables provided to clients and used in Kendrone operational portfolio.
- **Led — Trained professional surveyors from external survey companies in UAS-based mapping workflows during live operational missions**
  - How: Coordinated with survey company clients to conduct concurrent training during live mapping missions. Instructed surveyors in mission planning principles, platform operation, data capture procedures, and output interpretation in Pix4D. Training delivered in the field alongside active survey operations, providing real-world context for all instruction
  - Result: Survey company personnel upskilled in end-to-end UAS mapping workflows. Client relationships established as a revenue stream combining training fees with operational survey deliverables.

#### UAS Avionics, Payload Integration & Fleet Maintenance
**Potential CV sections:** Professional Experience; Technical Skills
**R&D:** No

**Description:** Avionics integration, sensor configuration, payload mounting, and hardware-level maintenance across the Kendrone UAS fleet. Encompassed pre- and post-flight airworthiness routines, fault diagnosis, and component-level repair on DJI multirotor platforms to sustain operational readiness across training and survey missions
**System:** DJI Phantom 4 Pro, DJI Phantom 3 Pro, DJI Mavic Pro, Tarot 680 Pro — RGB and multispectral payloads
**Objective:** Maintain full operational readiness of the Kendrone fleet across training and operational missions through systematic integration, inspection, and component-level maintenance
**Outcome:** Fleet maintained in continuous airworthy condition throughout operations. Component-level repairs completed including IMU replacement, gimbal replacement, and motor/ESC replacement on DJI platforms. All training and survey missions supported without platform-related mission failure.

**Activities / evidence records:**
- **Led — Integrated avionics and sensor payloads across the Kendrone multirotor fleet for mapping and agricultural missions**
  - How: Mounted and wired RGB and multispectral sensor payloads onto DJI Phantom 4 Pro. Configured sensor parameters and performed calibration checks prior to each mission type. Verified datalink integrity, GCS connectivity, and telemetry outputs. Performed pre-flight sensor and avionics checks as part of standard operational readiness procedure
  - Result: Fleet consistently prepared and mission-ready for both survey and agricultural operations. Sensor payloads correctly integrated and calibrated for each mission type.
- **Led — Diagnosed and performed component-level hardware repairs on DJI multirotor platforms to restore airworthiness**
  - How: Identified faults through pre-flight inspection, in-flight anomaly reports, and post-flight diagnostics. Performed IMU replacement, gimbal replacement, and motor/ESC replacement on DJI Phantom series platforms. Conducted post-repair functional checks and test flights to verify repair effectiveness before returning platforms to operational service
  - Result: Faulted platforms returned to full airworthy condition. Fleet operational continuity maintained throughout training and survey operations without mission-affecting platform failures.
- **Led — Conducted systematic pre- and post-flight airworthiness inspection routines across the Kendrone fleet**
  - How: Performed structured pre-flight checks covering physical airframe integrity, propeller condition, motor function, power system voltage and connections, GCS link establishment, telemetry verification, and payload security. Conducted post-flight inspections covering battery state, airframe condition, and anomaly logging. Maintained inspection records in compliance with KCAA UTO operational requirements.
  - Result: Zero platform-related mission failures attributed to missed pre-flight defects throughout the operational period. Inspection records maintained in compliance with KCAA UTO documentation requirements

#### IT Infrastructure, Digital Presence & Company Operations
**Potential CV sections:** Professional Experience
**R&D:** No

**Description:** End-to-end ownership of Kendrone's IT infrastructure, digital marketing presence, student administration, and external stakeholder engagement. Reorganised a scattered company database, resolved email deliverability issues, established a functioning digital marketing operation, designed marketing collateral, and served as the primary point of contact for students and external parties.
**System:** Wix (website), Google Workspace (email, SPF/DKIM/DMARC), Instagram, Facebook, Duplicator 3D Printer (signage/placards)
**Objective:** Establish reliable, professional IT infrastructure and digital presence for Kenya's first KCAA-approved drone training organisation, and systematise student administration and external stakeholder engagement to support company growth.
**Outcome:** Email deliverability resolved and verified (9/10 spam test score). Website performance and content optimised. Company and student databases reorganised and maintained. Brochure, business cards, and 3D printed logo placards produced. Social media accounts managed with paid advertising campaigns run. External stakeholder relationships established with media houses, landowners, aviation doctors, and KCAA. Student RPL registrations processed and license progress monitored end-to-end.

**Activities / evidence records:**
- **Led — Diagnosed and resolved company email deliverability failures and optimised web infrastructure**
  - How: Identified that company emails were routing to spam due to missing SPF, DKIM, and DMARC records. Configured DKIM signing (2048-bit RSA key via Google Workspace), initiated SPF record setup, and recommended DMARC record addition for kendrone.co.ke. Verified deliverability improvements using mail-tester.com — achieved 9/10 spam score. Managed website on Wix platform including performance optimisation, content updates, and domain administration.
  - Result: Email deliverability restored and verified at 9/10. DKIM signature validated. Website operational and maintained throughout employment period.
- **Led — Reorganised company and student databases and maintained operational records including petty cash**
  - How: Audited and restructured scattered company documentation into an organised database covering operational records, student files, contracts, training checklists (APPENDIX 14 and APPENDIX 24), and correspondence. Maintained student records from inquiry through to post-training license issuance. Managed info@kendrone.co.ke as primary student-facing email point of contact. Maintained petty cash records throughout employment
  - Result: Company documentation systematised and accessible. Student records maintained end-to-end for all enrolled students. Petty cash accounts accurately recorded throughout operational period
- **Led — Designed company marketing collateral and managed digital marketing channels including paid advertising**
  - How: Designed company brochure, business cards, and 3D printed logo placards using available design tools and the office Duplicator 3D printer. Managed Kendrone Instagram and Facebook accounts — created and published content and ran paid advertising campaigns to drive student enrollment and brand awareness. Managed the company's social media presence under the @KendroneKenya handle across all platforms
  - Result: Professional marketing collateral produced and deployed. Social media channels actively maintained with paid campaign support throughout employment period. Student enrollment supported through digital lead generation.
- **Led — Led external stakeholder engagement across regulatory bodies, media, landowners, aviation doctors, and commercial clients**
  - How: Managed KCAA liaison for student RPL registrations, airspace permissions, and post-training license progress follow-up. Drafted and sent field access permission letters to landowners (including Vipingo, Kilifi County) for new training site expansion. Compiled and distributed KCAA-approved aviation medical examiner directory to students. Reached out to media organisations (Nation Media Group, Standard Group, RMS, Mediamax) for editorial coverage opportunities. Engaged survey companies for client training partnerships. Coordinated accommodation options for Mtwapa training site — scouted, compiled, and distributed student accommodation guide covering 7 properties across budget tiers with transport links.
  - Result: Student RPL registrations processed and licenses obtained for all enrolled students. Mtwapa accommodation guide produced and distributed to students. Field access letters drafted for training site expansion. Media and client outreach conducted. Aviation doctor resource compiled and distributed.

### Experience-level activities
- **IndependentlyExecuted — KCAA Instructor Rating — UAS ground school, practical instruction, and BVLOS technical presentation**
  - How: Completed one-month KCAA Instructor Rating programme (IR001-01) at Kendrone UTO, covering instructor methodology, UAS regulations, hands-on practical instruction, and teaching practice with the first student cohort. Delivered a 32-slide BVLOS technical presentation to KCAA representative, Chief Instructor, and CEO/DFE covering BVLOS definitions, UAS category classification under Civil Aviation (UAS) Regulations 2020, C2 link architectures (RLOS/B-RLOS), IFR requirements, ICAO RPAS CONOPS, and global BVLOS case studies across 10 countries. Pass mark threshold: 70%
  - Result: Awarded KCAA Instructor Rating. Radio Telephony licence renewed concurrently. Sponsored by Kendrone under a KSH 200,000 training bond (signed 29 January 2021); bond waived by CEO Craig Cleave upon resignation in recognition of MSc scholarship award.

---

## Kendrone Ltd — Remote Pilot Licence (RPL) Training — Multirotor

**Role:** Aviation  
**Type:** Other  
**Location:** Mtwapa, Nairobi, Naivasha  
**Dates:** 2021-01-04 → 2021-01-10  
**Primary CV section:** Certifications & Licences  
**Secondary:** Technical Skills  

**Experience description (database):**
> Completed a two-week KCAA-approved Remote Pilot Licence (Multirotor) programme at Kendrone Ltd, Kenya's first KCAA-certified Unmanned Training Organisation (certified November 2020). Training covered ground school (Air Law, Meteorology, Human Factors, Navigation, Principles of Flight, Technical and General) and practical flight training on multirotor platforms under 25kg, examined by a KCAA-designated Flight Examiner. Conducted under the Civil Aviation (Unmanned Aircraft Systems) Regulations 2020

### Experience-level activities
- **IndependentlyExecuted — RPL ground school and practical flight training on multirotor platforms — KCAA certification**
  - How: Completed two-week KCAA RPL-MR programme comprising ground school theory (Air Law, Flight Plan Filing, Human Factors, Meteorology, Navigation, Principles of Flight, Technical and General) and practical flight training on DJI Phantom 4 Pro, Phantom 3 Pro, and Mavic Pro against the 15-lesson KCAA RPL-MR syllabus. Examined by KCAA-designated Flight Examiner (DFE) Craig Cleave. Pass mark threshold: 70% on all theory examinations.
  - Result: Awarded KCAA Remote Pilot Licence — Multirotor, Licence No. YK-RPL-00013A. First logged flight: 20 January 2021

---

## Technical University of Munich — M.Sc Aerospace

**Role:** Graduate Student  
**Type:** Academic  
**Location:** Munich, Germany  
**Dates:** 2021-10-01 → Present  
**Primary CV section:** Education  
**Secondary:** Selected Engineering / R&D Projects  

**Experience description (database):**
> Master of Science degree program in Aerospace Engineering at the TUM School of Engineering and Design, specializing in Aircraft Systems, Control, and UAS Integration. Completed 73 ECTS of advanced coursework, research practice, and practical labs covering rotorcraft engineering, electric aircraft, flight guidance, avionics safety, autonomous systems, non-linear control, and CFD simulation. Achieved a provisional overall grade of 2.6, with supplementary requirement courses passed in Automatic Control and CAD/Machine Elements. Degree completion is pending the submission of the Master's thesis

### Projects

#### Generic Modeling of Slotneutral UAM Throughput at Commercial Airports
**Potential CV sections:** Selected Engineering / R&D Projects; Technical Skills; Research & Publications
**R&D:** Yes

**Description:** Research project conducted at the Chair of Aircraft Design (LLS), TUM, in collaboration with Airbus Urban Mobility and Munich Airport International under the AMI-AirShuttle project. Developed a generic Python toolchain to model and evaluate slot-neutral eVTOL approach trajectories into Munich Airport (EDDM), enabling dynamic airspace reconfiguration based on live traffic data and wake turbulence categories.
**System:** Munich Airport (EDDM) Terminal Airspace & eVTOL Point-in-Space (PinS) Approach System
**Objective:** Eliminate operationally unfeasible eVTOL detours (~66 km) and maximize slot-neutral UAM throughput at commercial airports without disrupting conventional air traffic operations.
**Outcome:** Developed and delivered a fully functional Python toolchain generating 2D/3D KML trajectories for Google Earth Pro and the Airbus USim environment. Reduced approach detours from 66 km to ~15 km (direct approach) or ~23 km (with holding pattern). Co-authored and published the research paper at AIAA 2024.

**Activities / evidence records:**
- **IndependentlyExecuted — Traffic Categorization & Glideslope Separation Analysis**
  - How: xtracted and processed 24-hour Flightradar24 arrival and departure traffic data at Munich Airport (EDDM) and calculated the ILS glideslope vertical separation profile to establish dynamic trigger points for restricted airspace activation. Mapped ICAO aircraft type designators to RECAT-EU wake turbulence categories (CAT-A through CAT-F) using custom Python data processing scripts (traffic_data_manipulation.py) and Microsoft Excel. Calculated 3° ILS glideslope geometry on Runway 26L/08R to identify points where vertical separation between arriving conventional aircraft (5000 ft AMSL at FAF) and cruising eVTOLs (2500 ft AMSL) drops below the 1000 ft ICAO Doc 4444 threshold
  - Result: Established empirical proof that 86.9% of EDDM arriving traffic falls into CAT-D (62.37%) and CAT-E (24.53%), proving that static CAT-B (7 NM separation) assumptions were overly conservative. Formulated exact glideslope trigger locations (6.40 NM start, 3.25 NM end from threshold) where wake turbulence separation becomes active/inactive
- **IndependentlyExecuted — PinS Approach Procedure & Holding Pattern Trajectory Design**
  - How: Designed Instrument Meteorological Conditions (IMC) Point-in-Space (PinS) instrument approach procedures, T-bar transition fixes, and 1-minute holding patterns for eVTOL traffic operating in a triple parallel independent approach configuration at Munich Airport. Applied ICAO Doc 8168 (PANS-OPS), Doc 9643 (SOIR), and FAA Order JO 7110.65X regulatory criteria to construct a 540 m wide Normal Operating Zone (NOZ) between active runway centerlines (2300 m spacing). Calculated 3.0 NM Intermediate Approach Segments (IF), 4.0 NM Initial Approach Segments (IAF), 1250 m radius-to-fix (RF) turns, and 1-minute right-turn holding patterns (2 km leg, 700 m turn radius at 25° bank angle) for 120 km/h cruise speed.
  - Result: Formulated complete, regulatory-compliant IFR approach procedure geometry allowing eVTOLs to transition from instrument guidance at the MAPt (500 ft AGL OCH) to visual vertiport descent without crossing active conventional runways or violating No Transgression Zones (NTZ).
- **IndependentlyExecuted — Python Throughput Modeling Toolchain & KML Trajectory Generation**
  - How: Designed and implemented an object-oriented Python software toolchain that dynamically recalculates restricted airspace volumes and generates 2D/3D flight trajectories for Google Earth Pro and the Airbus USim simulation environment. Developed a modular Python engine (main.py, approach.py, trajectory_design.py, glideslope_visualization.py, functions.py) using class inheritance structures (Approach -> TrafficApproach / eVTOLApproach). Programmed algorithms to compute 3D corner coordinates for dynamic restricted volumes, generate RF turns with 5° arc steps, construct detour headings, and format output geometry into Keyhole Markup Language (KML) LineString and Polygon files.
  - Result: Delivered a generic, airport-agnostic toolchain that reduced eVTOL approach detour tracks from 66 km down to ~14.9 km for direct approaches (7.5 min flight time) or ~23 km when combining a 1-minute holding pattern with a direct approach (12 min flight time)
- **Contributed — AIAA 2024 Research Contribution — Airspace Geometry Dynamization**
  - How: Co-authored and published research on Advanced Air Mobility integration in controlled airport terminal airspaces, delivering the core geometry dynamization methodology and empirical traffic findings for the AIAA 2024 Aviation Forum paper. Synthesized thesis findings into Section IV.B.2 ("Airspace re-configuration based on aircraft classes") of the joint publication with Airbus Urban Mobility and LLS TUM. Formulated comparative trade studies contrasting static CAT-B restricted volumes against dynamic RECAT-EU class-based volumes, demonstrating significant track length and flight time reductions.
  - Result: Co-authored paper titled "Conceptualization and simulation of Advanced Air Mobility (AAM) operations within Controlled Airspaces of airports running independent parallel runway operations", presented to the global aerospace community at AIAA 2024.

#### Embedded Software Development of the Actuator Control and Monitoring Unit (ACMU)
**Potential CV sections:** Selected Engineering / R&D Projects; Technical Skills
**R&D:** Yes

**Description:** Embedded software R&D project conducted at the Chair of Aircraft Design (LLS), TUM, focusing on C++ software performance optimization, double-buffer log file management, binary USB data streaming, and OpenCyphal CAN bus integration for a standalone electromechanical actuator control unit
**System:** Actuator Control and Monitoring Unit (ACMU)
**Objective:** Optimize logging throughput, reduce memory overhead, eliminate SD card data corruption risk, and establish high-integrity UAV-CAN communication between the ACMU and Pixhawk flight control computers
**Outcome:** Refactored logging architecture using C++ TDD and Dependency Injection, successfully implementing binary USB data streaming that achieved a 5x data reduction (from 100 bytes to 20 bytes per log frame) verified on target hardware during HIL testing; project discontinued due to medical departure

**Activities / evidence records:**
- **IndependentlyExecuted — Refactored the ACMU data logging software pipeline using Test-Driven Development (TDD) in C++ to implement high-efficiency binary data serialization over USB**
  - How: Applied C++ design patterns by extracting a data logging superclass and implementing Dependency Injection to dynamically switch log formats at runtime via a log_format flag. Engineered double-buffered binary sensor data routines (binary_sensor_data), wrote unit test suites, and verified execution on target hardware within a HIL testing environment
  - Result: Achieved an 80% reduction in log frame size (reducing packet size from 100 bytes down to 20 bytes), delivering 5x data compression to support high-rate 10 MB / 120 s telemetry logging without memory resource depletion
- **IndependentlyExecuted — ACMU System Architecture & Protocol Integration Research**
  - How: Conducted preliminary system architecture trade studies and authored the master thesis research expose defining software improvements for SD card buffer flushing, Cyphal / OpenCyphal bus protocols, and thread-level CPU status monitoring. Researched memory buffer optimization schemes, atomic write/sync routines, and fault exception handling for SD card removal. Evaluated OpenCyphal (UAV-CAN) middleware abstractions for distributed computing between the standalone ACMU and Pixhawk flight controllers
  - Result: ormulated and submitted the approved technical expose and software requirements baseline to the Chair of Aircraft Design (LLS), TUM.

#### Autonomous Sub-Terrain UAV Challenge
**Potential CV sections:** Selected Engineering / R&D Projects; Technical Skills
**R&D:** Yes

**Description:** Group robotics R&D project for the LRG6300 Autonomous Systems course at TUM under Prof. Markus Ryll. Engineered a ROS software architecture in C++ within a Unity simulation environment to execute autonomous cave exploration, 3D voxel grid mapping, real-time perception filtering, and object localization for a subterranean quadrotor UAV
**System:** Autonomous Sub-Terrain Quadrotor UAV (Unity Simulator, ROS, RealSense Depth Camera, Semantic Camera)
**Objective:** Execute fully autonomous takeoff, transit, cave entry, 3D mapping, multi-object lantern detection/localization, and return-to-base homing in an unknown subterranean environment
**Outcome:** Execute fully autonomous takeoff, transit, cave entry, 3D mapping, multi-object lantern detection/localization, and return-to-base homing in an unknown subterranean environment

**Activities / evidence records:**
- **IndependentlyExecuted — Depth-to-PointCloud Perception Engine & Spatial Frame Transformation**
  - How: Engineered the real-time depth perception pipeline (depth_to_pc_node) converting raw RealSense depth camera video streams into noise-filtered 3D point cloud topics in the global world frame. Integrated OpenCV within ROS to apply bilateral noise filtering on raw depth frames while sharpening geometric wall edges, restoring images to 16UC1 format. Processed intrinsic camera parameters (fx, fy, cx, cy) with a 0.001f depth scale factor using Point Cloud Library (PCL) pinhole projection equations. Utilized ROS tf2 spatial transformation libraries to dynamically transform point clouds from the moving camera sensor frame to the static world frame, compensating for quadrotor vibrations, pitch/roll tilt, and body oscillations
  - Result: Achieved stable, motion-compensated 3D point cloud generation at the cave entrance and interior, establishing an accurate point cloud stream free of quadrotor motion artifacts for downstream 3D mapping.
- **IndependentlyExecuted — OctoMap 3D Voxel Grid Mapping & Dynamic Point Cloud Updater**
  - How: Developed the 3D spatial mapping node (point_cloud_to_voxel_grid_node) utilizing the OctoMap library to build and update a global 3D occupancy voxel grid map of the cave environment in real time. Subscribed to world-frame point clouds and initialized an OctoMap tree with a 1.0 m voxel resolution for optimal computational efficiency. Implemented a Dynamic Updater algorithm comparing sequential point cloud frames within a 0.05 m search radius at resolution 2 to isolate newly observed environmental points into a changed_points cloud, preventing cumulative point overlap. Executed Octree tree-pruning routines, periodic binary exports (.bt format), and integrated OctoMap RViz plugins (OccupancyGrid display) for real-time 3D voxel visualization.
  - Result: Successfully generated and periodically saved a complete 3D binary OctoMap (.bt) of the subterranean cave network that was visualized and verified in Octovis and RViz

#### Applied CFD Channel & Cavity Flow Simulation
**Potential CV sections:** Selected Engineering / R&D Projects; Technical Skills
**R&D:** Yes

**Description:** Numerical CFD study investigating subsonic turbulent channel flow over dual cavity geometries using ANSYS ICEM CFD and ANSYS CFX to evaluate turbulence models, wall refinement (y+ approx 1), geometry modifications, and advection scheme numerical diffusion
**System:** Subsonic Dual-Cavity Channel Flow System
**Objective:** Simulate flow separation and reattachment dynamics across dual cavity geometries, evaluate shear stress transport (SST) versus Speziale, Sarkar and Gatski (SSG) Reynolds Stress Models, and analyze the impact of boundary layer mesh refinement and advection scheme order.
**Outcome:** Completed 5 comparative CFD simulation cases in ANSYS CFX, demonstrating that non-algebraic SSG RSM accurately resolves cavity recirculation, boundary layer mesh refinement (y+ approx 1) captures wall shear, and 2nd-order advection prevents artificial numerical dissipation.

**Activities / evidence records:**
- **IndependentlyExecuted — Modeled 2D/3D dual-cavity channel geometries, built multi-block structured grids, and executed comparative subsonic CFD simulations across 5 test cases in ANSYS ICEM CFD and ANSYS CFX**
  - How: Applied multi-block structured grid blocking in ICEM CFD with wall boundary layer refinement (reducing cell size from 0.5 to 0.00001 m) to achieve a non-dimensional wall distance of y+ approx 1. Defined subsonic inlet boundary conditions (Mach 0.1, 34.3 m/s) and static pressure outlets in CFX. Evaluated shear-stress transport (SST) versus SSG Reynolds Stress turbulence models and 1st-Order Upwind versus 2nd-Order High Resolution advection schemes across initial and widened cavity geometries.
  - Result: Proved that the non-algebraic SSG Reynolds Stress Model accurately captured flow separation and recirculation vortices inside deep cavities where SST failed, and demonstrated that 2nd-order advection schemes eliminated artificial numerical diffusion present in 1st-order upwind calculations

#### Simulation of the Flowfield of a Multirotor in Axial Flight
**Potential CV sections:** Selected Engineering / R&D Projects; Technical Skills
**R&D:** Yes

**Description:** Numerical CFD study simulating the steady, incompressible 3D flow field around a quadrotor UAV in axial descent flight using OpenFOAM. Implemented Blade Element Momentum Theory (BEMT) actuator disk source terms (rotorDiskSource in fvOptions) coupled with $k-\omega$ SST turbulence modeling to calculate aerodynamic thrust/torque and analyze induced velocity fields, axial pressure distributions, and blade tip vortex interaction
**System:** Quadrotor UAV Flow Field & Actuator Disk System
**Objective:** Model the 3D aerodynamic flow field of a multirotor in low-rate axial descent, calculate individual rotor thrust and drag torque via Blade Element Theory, and evaluate tip vortex ring state interactions.
**Outcome:** Generated computational background domains and refined rotor disk meshes, executed parallel 4-processor steady-state solves in simpleFoam, achieved residual convergence within 410 iterations, and validated axial pressure distribution jumps and non-interacting tip vortex behavior against analytical momentum theory

**Activities / evidence records:**
- **OwnedArchitected — OpenFOAM Multirotor CFD Mesh Generation & Parallel Domain Setup**
  - How: Built the 3D computational domain background grid and refined quadrotor rotor disk geometries using OpenFOAM mesh utilities (blockMesh and snappyHexMesh) for parallel CFD solver execution. Constructed a 2.5m x 2.5m x 4.0m bounding domain in blockMesh (25 x 25 x 40 cell grid) with velocity inlet (1.0 m/s), static pressure outlet, and slip wall boundary conditions. Extracted 4 rotor disk CAD geometries (0.5m diameter, 0.01m thickness) via surfaceFeatures and executed cell refinement using snappyHexMesh. Configured 4-processor spatial domain decomposition (decomposeParDict 2x2x1 split) for parallel execution (mpirun).
  - Result: Generated a high-quality multi-region 3D mesh with fine cell resolution localized around all 4 rotor disks, enabling stable parallel solver execution in simpleFoam.
- **OwnedArchitected — BEMT Actuator Disk Source Integration & Axial Flow Field Simulation**
  - How: Configured Blade Element Momentum Theory (BEMT) actuator disk source terms (rotorDiskSource in fvOptions) and solved the steady, incompressible RANS flow field in OpenFOAM. Programmed fvOptions to apply BEMT momentum source terms across 4 rotor cell zones (3 blades, -1000 RPM, 1.0 m/s axial inlet velocity) calculating lift/drag forces ($F_z$, $F_\theta$) from $C_l$ and $C_d$ dynamic pressure equations. Executed parallel simpleFoam iterations with the $k-\omega$ SST turbulence model until residual convergence ($p, k, \omega < 0.001$, $\vert{}U\vert{} < 0.0001$) at 410 iterations (762.07 s execution time). Processed axial pressure profiles, rotor thrust/torque totals, and induced velocity vector fields.
  - Result: Calculated individual rotor effective lift (1061 N to 1144 N) and drag torque (-101 Nm to -110 Nm), validated axial pressure jump profiles against analytical momentum theory, and demonstrated that rotor tip vortices do not interact when inter-rotor spacing equals or exceeds disk diameter.

#### Geospatial Analysis & Cartography — Nakuru County Geotourism Research
**Potential CV sections:** Selected Engineering / R&D Projects; Technical Skills; Research & Publications
**R&D:** Yes

**Description:** End-to-end spatial data processing, QGIS modeling, geomorphosite localization, and publication-grade map production for an academic research study evaluating geotourism potential along the Gregory Rift in Nakuru County, Kenya.
**System:** QGIS, EARS geological datasets, SRTM elevation rasters, Pralong/Pereira geomorphosite assessment matrices
**Objective:** rocess spatial datasets and produce all cartographic figures, geosite localizations, and structural overlays across four primary geosites (Hell's Gate National Park, Menengai Crater, Lake Naivasha Basin, Kariandusi Site) for academic publication
**Outcome:** Delivered 100% of the spatial models, site localizations, and cartographic map figures co-authored in a peer-reviewed research paper.

**Activities / evidence records:**
- **Led — Formulated the spatial data processing pipeline and generated all regional GIS figures, geosite localizations, and geological mapping overlays.**
  - How: Imported and structured vector/raster datasets in QGIS, generated elevation and boundary maps for four EARS geosites, integrated geomorphosite evaluation scoring into spatial layouts, and produced publication-grade figures
  - Result: Completed 100% of the cartographic and spatial analysis deliverables required for the research publication

---

## University of Cologne — LEAD! Leadership for Africa

**Role:** DAAD Scholar  
**Type:** Academic  
**Location:** Cologne, Germany (Hybrid — online and on-campus)  
**Dates:** 2022-02-01 → 2023-01-27  
**Primary CV section:** Education  
**Secondary:** Selected Engineering / R&D Projects  

**Experience description (database):**
> Completed the LEAD! Leadership for Africa programme at the University of Cologne, offered exclusively to DAAD Leadership for Africa scholarship holders and funded by the German Federal Foreign Office. The programme covered development-related studies (sustainable development, governance, public administration, peace & conflict studies) and career training (intercultural skills, project management, science communication, individual development planning, and presentation). Total workload: 260 units / 195 hours. Graduated with a grade of Sehr gut (A), earning 8 ECTS credits.

### Projects

#### Design and Implementation of an Unmanned Aircraft System (UAS) using the Model Based System Engineering (MBSE) Approach for Agricultural Applications at the Galana Kulalu Irrigation Scheme
**Potential CV sections:** Selected Engineering / R&D Projects; Technical Skills; Research & Publications
**R&D:** Yes

**Description:** A research and systems architecture project focused on the design and development of an integrated UAS for precision agriculture at the Galana Kulalu Irrigation Scheme, Kenya. The project employed the MBSE approach to define all system components, functionalities, and architecture including flight mission planning, trajectory optimisation, real-time control, failure probability and risk assessment. The operational goal was to employ precision agriculture techniques — crop health monitoring, soil fertility and water retention analysis, and chemical spraying — for maize farming at the scheme, with full UAS integration targeted by 2030.
**System:** Integrated agricultural UAS — precision agriculture payload suite (crop health monitoring, soil analysis, chemical spraying), autonomous flight control system, mission planning and trajectory optimisation subsystems
**Objective:** To design an MBSE-structured UAS architecture for precision agriculture deployment at the Galana Kulalu Irrigation Scheme, addressing food insecurity through improved farm management and increased crop yields, while closing Kenya's local UAS manufacturing gap
**Outcome:** Produced a comprehensive project proposal comprising an MBSE-based UAS system architecture definition, SWOT and PEST analyses, work breakdown structure, critical path and Gantt chart, project summary, and elevator pitch. Delivered and graded Sehr gut (A) as part of the LEAD! programme final submission

**Activities / evidence records:**
- **IndependentlyExecuted — UAS system architecture definition and MBSE modeling for autonomous precision agriculture operations**
  - How: Applied the Model Based System Engineering (MBSE) approach to define all system components and functionalities within the UAS architecture, covering flight mission planning, trajectory optimisation, real-time flight control, failure probability assessment, and operational risk assessment for agricultural applications at the Galana Kulalu Irrigation Scheme
  - Result: Produced a structured MBSE-based system architecture capturing the full functional decomposition of the agricultural UAS, forming the technical backbone of the project proposal
- **IndependentlyExecuted — Precision agriculture capability definition — crop health monitoring, soil fertility and water retention analysis, and chemical spraying payload architecture**
  - How: Defined the precision agriculture payload suite and operational capabilities required for maize farming at Galana Kulalu, specifying crop health monitoring, soil fertility and water retention analysis, and chemical spraying functions within the MBSE framework
  - Result: Produced a defined payload and capability specification integrated into the overall UAS system architecture, supporting the operational and technical justification of the project
- **IndependentlyExecuted — Work breakdown structure, critical path, and Gantt chart development for UAS implementation at Galana Kulalu**
  - How: Decomposed the project into sub-goals and key milestones across five phases — drone sector engagement, knowledge acquisition, UAS actualisation, farm case study operations, and full Galana Kulalu integration — and mapped each to a specific timeline extending to 2030
  - Result: Produced a structured WBS and Gantt chart defining all key milestones, sub-goals, and indicators for the research project from 2020 to 2030
- **IndependentlyExecuted — SWOT and PEST analysis — individual strengths, weaknesses, opportunities, threats, and external risk and opportunity assessment for the UAS project**
  - How: Conducted a personal SWOT analysis identifying individual strengths, weaknesses, opportunities, and threats relevant to the project execution. Followed with a PEST analysis examining political, economic, socio-cultural, and technological external factors affecting UAS implementation in Kenya, including regulatory landscape, government innovation stance, funding environment, and technology adoption challenges
  - Result: Produced SWOT and PEST analysis documents forming the risk and opportunity assessment framework for the project proposal, submitted as part of the LEAD! Individual Development Plan
- **IndependentlyExecuted — Project summary write-up and elevator pitch preparation and delivery**
  - How: Authored a formal project summary covering the problem context, MBSE approach, precision agriculture objectives, and long-term implementation roadmap for the Galana Kulalu Irrigation Scheme. Prepared and delivered an elevator pitch communicating the project vision, technical approach, and societal impact
  - Result: Delivered project summary and elevator pitch as final LEAD! programme submissions. Graded Sehr gut (A), earning 8 ECTS credits from the University of Cologne

---

## Amazilia Aerospace GmbH — Aerospace Systems Engineering

**Role:** Working Student  
**Type:** Professional  
**Location:** Munich, Germany  
**Dates:** 2022-09-12 → 2024-12-31  
**Primary CV section:** Professional Experience  
**Secondary:** Technical Skills  

**Experience description (database):**
> Role concurrent with MSc studies at TU Munich. Involved in aircraft systems integration, electrical architecture, HIL testing, GCS development and autonomous charging systems across both UAS and conventional aircraft platforms.

### Projects

#### WfA MiniFreighter GCS -SN2
**Potential CV sections:** Professional Experience; Selected Engineering / R&D Projects; Technical Skills
**R&D:** Yes

**Description:** Full lifecycle redesign of the Wings for Aid MiniFreighter 8/500FW Ground Control Station — from customer requirements capture through design reviews, procurement, assembly, integration testing and field deployment. Five units delivered operationally
**System:** Ground Control Station — WfA MiniFreighter 8/500FW
**Objective:** Redesign the SN2 GCS to meet updated customer, pilot and operational requirements including revised control architecture, communication protocols, BLOS capability and maintainability improvements
**Outcome:** Five GCS units assembled, tested and deployed to customer for active WFP operations in Africa

**Activities / evidence records:**
- **IndependentlyExecuted — Attended joint design evaluation session with Wings for Aid CEO and chief pilot alongside Amazilia CTO and senior systems engineer. Captured customer and pilot requirements directly and translated them into formal engineering specifications for the SN2 GCS redesign. Produced wiring diagrams, CAD renders and system architecture documentation. Presented across three internal design reviews with CTO, Head of Systems Engineering and Senior Systems Engineer, incorporating embedded software team input on DCU interface changes. Received sign-off to proceed to BOM and procurement.**
  - How: Direct customer requirements capture, requirements-to-specification translation, iterative design review process, wiring diagram production, CAD modelling, system architecture documentation
  - Result: Approved SN2 GCS design package including updated wiring architecture, component specifications and BOM — cleared for procurement and assembly
- **IndependentlyExecuted — Sourced alternative panel supplier through independent research, which reduced component costs compared to the original source. Redesigned front panels in Autodesk Inventor to match the new supplier's specifications. Curated a full assembly procedure based on SN1 documentation and discussions with seniors. Upon parts arrival, performed mechanical assembly including drilling connection holes on panels and GCS case, installing internal support structures, and routing the power architecture — standardising all internal components on 12VDC via an AC/DC converter.**
  - How: Supplier sourcing and cost evaluation, Autodesk Inventor CAD redesign, assembly procedure development, mechanical assembly, power architecture wiring
  - Result: Completed mechanical assembly and power architecture of SN2 Unit 1, with reduced component cost versus SN1 baseline
- **IndependentlyExecuted — Performed stepwise electrical integration of all internal GCS components following the assembly procedure, conducting QA checks and functionality tests at marked checkpoints verified with seniors. Installed GCS software received from the software team upon completion of Unit 1. Scheduled and conducted simulator testing in the lab to evaluate control software, internal wiring of controls, stick feedback and aircraft response time. Applied personal drone and private pilot experience to assess pilot feel and control responsiveness directly during simulation runs. Coordinated firmware and wiring corrections on the hardware side while communicating required software changes to the software team. Conducted a final internal review before inviting the Wings for Aid CEO and chief pilot for customer acceptance testing against the original specifications.**
  - How: Stepwise electrical integration, QA checkpoint verification, simulator-based functional testing, cross-team coordination with software team for firmware and software updates, customer acceptance testing
  - Result: Unit 1 passed all internal tests and customer acceptance checks. Customer confirmed the GCS met specifications. Cleared for serial production of remaining four units
- **IndependentlyExecuted — Serially produced four additional GCS units following customer acceptance of Unit 1. Worked on all four units simultaneously in a dedicated assembly space, applying the verified assembly procedure and QA process established during Unit 1 production. Each unit went through the same integration, functionality testing and verification process before being cleared for delivery**
  - How: Serial assembly using verified procedure, parallel multi-unit production, QA and functionality testing per unit
  - Result: Five GCS units total completed, tested and delivered to Wings for Aid for operational deployment with WFP in Africa

#### Amazilia Ground Control Station
**Potential CV sections:** Professional Experience; Selected Engineering / R&D Projects
**R&D:** Yes

**Description:** Assembly, integration and verification of three tabletop ground control station units for use in the Amazilia lab HIL environment. Multi-aircraft capable — compatible with Pipistrel OPV, Nuuva and CTOL platforms. Three-monitor setup covering camera feed, telemetry and engine parameters, with a mode control panel replicating actual aircraft flight controls.
**System:** AAG GCS
**Objective:** Deliver functional lab GCS units for use across Amazilia's HIL testing and digital flight systems development activities
**Outcome:** Three units assembled, integrated and verified for development use

**Activities / evidence records:**
- **Contributed — Reviewed and cleaned up existing CAD files, wiring diagrams and system architecture documentation inherited from predecessor. Reconciled documentation against the physical design to ensure accuracy before proceeding to assembly.**
  - How: CAD review and cleanup, wiring diagram verification, architecture documentation reconciliation
  - Result: Accurate and verified documentation baseline established for the three-unit production run
- **IndependentlyExecuted — Performed mechanical assembly of three tabletop GCS units including mounting of three-monitor arrangement, mode control panel and internal structural components. Drilled connection points and installed internal support elements following the inherited design**
  - How: Mechanical assembly, panel mounting, structural installation
  - Result: Three units mechanically assembled and ready for electrical integration
- **IndependentlyExecuted — Performed electrical integration of all internal components across three units including power architecture, monitor connections, mode control panel wiring and communication interfaces. Followed stepwise approach with QA checks at key points.**
  - How: Electrical wiring, power architecture integration, stepwise assembly with QA checkpoints
  - Result: Three units fully wired and electrically integrated, ready for functional testing
- **IndependentlyExecuted — Conducted functional testing of each completed unit, verifying correct operation of all three monitor feeds — camera, telemetry and engine parameters — as well as mode control panel inputs and communication interfaces. Validated that each unit performed correctly within the lab environment across the aircraft types Amazilia was working on — Pipistrel OPV, Nuuva and CTOL.**
  - How: Functional testing per unit, interface verification, multi-aircraft compatibility validation
  - Result: Three tabletop GCS units verified and validated for lab use across multiple Pipistrel aircraft platforms

#### Aircraft Systems Hardware-in-the-Loop (HIL) Test Rig
**Potential CV sections:** Professional Experience; Selected Engineering / R&D Projects; Technical Skills
**R&D:** Yes

**Description:** End-to-end design, build and integration of a hardware-in-the-loop test rig for Amazilia aircraft systems, built on a server rack architecture. Incorporated actual flight hardware including FCCs, DCUs, LMUs, CAN interfaces, Ethernet switching and power systems. Enabled in-office simulation, monitoring and validation of aircraft systems in flight conditions.
**System:** Hardware-in-the-Loop Test Rig — Amazilia Aircraft Fleet
**Objective:** Design and deliver a functional HIL environment replicating the actual aircraft avionics and communication architecture to support system validation and performance analysis without flight testing
**Outcome:** Fully operational HIL rig delivering in-lab aircraft simulation capability across Amazilia's fleet

**Activities / evidence records:**
- **IndependentlyExecuted — Received system requirements from Head of Systems Engineering defining the HIL rig scope, component specifications and communications architecture. Studied the complex multi-protocol communications architecture of the aircraft systems. Developed the high-level wiring architecture covering OPS Panel and PSUs, CAN boxes, RPi and USB hub, FCCs and DCUs, ETH switch, LMUs, Panels A/B/C and BRS tray. Produced detailed wiring sheets and interface definitions across all components.**
  - How: Requirements analysis, wiring architecture development, interface definition, communication protocol mapping across CAN and Ethernet networks
  - Result: Approved wiring architecture and interface documentation baseline established for the HIL rig
- **IndependentlyExecuted — Designed the full server rack assembly in Autodesk Inventor, modelling the physical layout and component placement of the HIL rig including rack structure, trays, panels and internal component arrangement. Presented the design across multiple preliminary design reviews with cross-functional teams including systems engineering and embedded software before receiving sign-off to proceed to procurement and assembly**
  - How: Autodesk Inventor CAD modelling, iterative design review process, cross-functional review with systems and software teams
  - Result: Approved CAD assembly and design package cleared for component procurement and physical build
- **IndependentlyExecuted — Procured all components for the HIL rig following design sign-off. Performed mechanical assembly of the server rack including mounting of rack rails, trays, panels and structural elements. Installed and positioned all hardware components within the rack according to the approved CAD layout**
  - How: Component sourcing and procurement, mechanical rack assembly, hardware installation and positioning
  - Result: HIL rig mechanically assembled and all hardware components installed and positioned ready for electrical integration
- **IndependentlyExecuted — Performed full electrical integration of all HIL rig components including power distribution, CAN bus wiring, Ethernet patch panel connections, and interface wiring between FCCs, DCUs, LMUs, RPi units and OPS panels. Followed the wiring architecture developed during design, working stepwise through each subsystem layer of the rack.**
  - How: Electrical wiring, power architecture integration, CAN bus wiring, Ethernet network integration, multi-protocol interface wiring
  - Result: Fully wired HIL rig with all internal interfaces connected across CAN, Ethernet and power networks
- **IndependentlyExecuted — Conducted extensive testing and verification of the completed HIL rig with seniors, validating correct operation of all interfaces, communication protocols and hardware components. Progressed through to full HIL environment testing — monitoring and controlling aircraft systems in simulated flight conditions from the lab. Verified that the rig faithfully replicated the actual aircraft avionics architecture and communication behaviour.**
  - How: Interface verification, protocol testing across CAN and Ethernet, functional validation, HIL environment testing, collaborative verification with seniors
  - Result: Fully operational HIL rig confirmed — aircraft systems successfully simulated, monitored and controlled in-lab. Enabled in-office flight simulation and performance analysis across Amazilia aircraft fleet without requiring physical flight testing.

#### Aircraft Battery Charging Unit (ABCU)
**Potential CV sections:** Professional Experience; Selected Engineering / R&D Projects; Technical Skills
**R&D:** Yes

**Description:** End-to-end design of a standalone autonomous aircraft battery charging unit for Amazilia's Pipistrel aircraft fleet. Initiated following a polarity reversal incident during field testing that caused a short circuit and wire damage, identifying the need for a safe, controlled external charging solution. Project covered requirements capture through design review and full handover documentation. Physical build not completed due to departure
**System:** Standalone External Aircraft Battery Charging Unit
**Objective:** Design a portable, autonomous charging unit capable of safely charging both 12V and 24V LiFePO4 battery configurations used across Amazilia aircraft systems, with built-in polarity protection, voltage indicators and field-deployable enclosure
**Outcome:** Complete design package delivered including system architecture, wiring diagrams, component specifications, BOM, panel designs and assembly guide. Handed over to team upon departure

**Activities / evidence records:**
- **IndependentlyExecuted — Following a polarity reversal incident during field testing of a Pipistrel aircraft that caused a short circuit and wire damage, received brief from CTO to design a safe standalone aircraft battery charging unit. Conducted requirements capture by consulting all field testing personnel to understand operational needs, environmental conditions and safety requirements. Researched LiFePO4 battery chemistry, charging characteristics and available charging system suppliers to establish a technically grounded requirements baseline.**
  - How: Stakeholder requirements capture, field operator consultation, LiFePO4 battery and charging system research, supplier and component market study, datasheet analysis
  - Result: Clear requirements baseline established covering dual-voltage capability (12V and 24V LiFePO4), polarity protection, voltage indication, field deployability and safe external charging operation
- **IndependentlyExecuted — Developed system architecture for the ABCU covering power input, charging system selection, voltage switching between 12V and 24V LiFePO4 configurations, polarity protection, battery voltage indication and enclosure design. Conducted detailed component market study matching available charging systems against Amazilia's battery specifications. Selected components capable of handling both 12V and 24V LiFePO4 chemistries with switchable output, allowing field teams to switch between configurations during operations. Optimised component selection for cost following design review feedback.**
  - How: System architecture design, component market study, datasheet matching against battery specifications, cost optimisation, architectural diagram production
  - Result: Approved system architecture and component selection covering dual-voltage charging capability with polarity protection and field-deployable form factor
- **IndependentlyExecuted — Produced full wiring diagrams for the ABCU internal architecture. Designed enclosure panels, panel holders, mounting hardware and overall box layout in Autodesk Inventor, sized for transport in a hardened carry case similar to those used for the GCS units. Designed front panel layout for voltage switching and indicators. Specified screw sizes, mounting arrangements and all mechanical details required for assembly. Presented complete design package across design reviews with CTO and senior systems engineering team, incorporating revisions to optimise cost and usability. Agreed final panel supplier — same alternative supplier used for the WfA GCS — following design review approval.**
  - How: Wiring diagram production, enclosure and panel CAD design in Autodesk Inventor, design review presentation, iterative revision and cost optimisation
  - Result: Fully approved detailed design package including wiring diagrams, enclosure CAD, panel designs, component specifications and BOM
- **IndependentlyExecuted — Upon departure from Amazilia, compiled and handed over the complete ABCU design package to the team. Handover included full system architecture diagrams, wiring diagrams, component datasheets and specifications, BOM, panel CAD designs and a step-by-step assembly guide to enable the team to proceed to physical build without loss of design intent or technical context**
  - How: Technical documentation compilation, assembly guide authoring, structured handover to engineering team
  - Result: Complete design package successfully handed over. Physical assembly left to team to complete. No technical information lost at point of departure.

---

## HORYZN  — Aerodynamics Project Engineer

**Role:** Student Initiative  
**Type:** StudentProject  
**Location:** Munich, Germany  
**Dates:** 2022-10-01 → 2023-06-30  
**Primary CV section:** Professional Experience  
**Secondary:** Selected Engineering / R&D Projects  

**Experience description (database):**
> Unpaid student initiative at TU Munich. Member of the Design Loop team responsible for the aerodynamics module of the Kolibri hybrid lift-and-cruise eVTOL UAS under Mission Pulse Phase 2. Led the aerodynamics sub-team of three engineers. Developed and maintained the aerodynamics module within a CPACS/MATLAB/PAWAT/RCE integrated design environment, contributing to aircraft configuration selection and iterative multidisciplinary design optimization concurrent with MSc studies and Amazilia working student role.

### Projects

#### Kolibri eVTOL — Aerodynamics Module Development
**Potential CV sections:** Selected Engineering / R&D Projects; Technical Skills
**R&D:** Yes

**Description:** Development, implementation and optimization of the aerodynamics module within the HORYZN multidisciplinary design loop for the Kolibri hybrid lift-and-cruise eVTOL UAS. Covered airfoil selection, lifting surface optimization, configuration trade studies and iterative cross-team design convergence using a CPACS/MATLAB/PAWAT/RCE toolchain. Concluded with design handover to CAD, structures and avionics teams
**System:** Kolibri Hybrid Lift-and-Cruise eVTOL UAS — Lifting Surfaces and Aerodynamic Configuration
**Objective:** Deliver an optimized aerodynamic configuration for Kolibri meeting mission profile requirements, with particular focus on achieving successful
**Outcome:** Converged aerodynamic design handed over to downstream teams. Cessna-type fixed-wing configuration with front tractor propeller selected and validated, resolving the transition failure mode of the predecessor aircraft

**Activities / evidence records:**
- **Contributed — Participated in structured handover sessions with the outgoing Mission Pulse Phase 1 team to understand the design, shortcomings and failure modes of the Frankenstein prototype. Analysed the previous CPACS files, MATLAB code and PAWAT outputs to reconstruct what had been built and why transition had failed. Collaborated across the full Design Loop team to document lessons learned and define requirements list for the Phase 2 prototype — Kolibri. Requirements captured and managed in Notion.**
  - How: Technical handover sessions, CPACS file analysis, MATLAB code review, PAWAT output analysis, cross-team requirements workshops, Notion documentation
  - Result: Comprehensive requirements list established for Kolibri Phase 2, identifying transition failure as the primary design constraint to resolve
- **Led — Led the aerodynamics team's contribution to the Kolibri configuration selection process. Identified the root cause of Frankenstein's transition failure as wingtip-mounted propellers creating adverse interference at the 25kg MTOW scale. Proposed a Cessna-type fixed-wing configuration with a front tractor propeller and lift motors mounted on the wing, supported by case studies from undergraduate aircraft design projects and CFD analysis in OpenFOAM demonstrating adequate glide performance during transition in the event of propulsion switching delays. Presented the configuration argument across multiple design reviews, convincing the team and securing agreement to proceed.**
  - How: Configuration trade studies, first-principles aerodynamic analysis, OpenFOAM CFD analysis, undergraduate case study development, design review presentations, cross-team technical debate
  - Result: Cessna-type fixed-wing hybrid lift-and-cruise configuration adopted for Kolibri, directly resolving the transition failure mode of Frankenstein
- **IndependentlyExecuted — Developed and maintained the aerodynamics module within the HORYZN multidisciplinary design loop. The module interfaced with CPACS via TiGL and TiXi libraries, using PAWAT as the core aerodynamic solver within a MATLAB class-based architecture. Implemented methods covering airfoil database management, CPACS geometry parsing, aerodynamic mapping across Reynolds number and angle of attack ranges, twist optimisation, stall velocity and force calculations, neutral point calculation and results writing back to CPACS. Wrote full module documentation including README, UML class diagram, function descriptions and I/O specifications. Managed module codebase on Git.**
  - How: MATLAB object-oriented programming, CPACS interface via TiGL/TiXi, PAWAT integration, aerodynamic analysis implementation, Git version control, technical documentation authoring
  - Result: Fully documented functional aerodynamics module integrated into the HORYZN RCE design loop, delivering aerodynamic coefficients, forces, moments and aeromap data to downstream modules via CPACS
- **Contributed — Participated in the aerodynamics team's airfoil selection process for Kolibri's lifting surfaces. Ran systematic case studies across candidate airfoils using XFLR5 and Flow5 to evaluate CL/CD performance across the expected Reynolds number range. Fed selected airfoil profiles into the CPACS aircraft definition and ran iterative optimisation of wing geometry including twist distribution, span, chord and sweep through the aerodynamics module. Coordinated with structures and geometry sub-teams within the design loop to ensure aerodynamic outputs were compatible with structural and sizing constraints.**
  - How: XFLR5/Flow5 airfoil analysis, CPACS geometry parameterisation, iterative wing optimisation, cross-module design loop coordination
  - Result: Optimised lifting surface definition for Kolibri delivered to the design loop, meeting CL/CD, wing loading and stall requirements within structural and geometric constraints
- **Contributed — Worked intensively within the RCE-based multidisciplinary design loop alongside aerodynamics, structures, geometry, wing sizing and propulsion sub-teams to achieve design convergence for Kolibri. Ensured aerodynamics module outputs were compatible with and correctly consumed by adjacent modules. Participated in extended working sessions — frequently 18 to 20 hours — to resolve inter-module conflicts and iterate toward a stable baseline design. Contributed aerodynamics expertise to cross-team configuration discussions and design decisions throughout the convergence process**
  - How: RCE multidisciplinary design loop operation, cross-module interface management, iterative design convergence, cross-team technical collaboration
  - Result: Converged multidisciplinary baseline design achieved for Kolibri, with aerodynamics module outputs validated against structural, geometry and propulsion module requirements
- **Contributed — Prepared and delivered a comprehensive handover of the aerodynamics module to the incoming team and downstream design teams. Handover package included the full codebase on Git, README documentation, UML class diagram, function descriptions, I/O path specifications, calculation options documentation, Flow5 validation task documentation and a formal handover document. Ensured the receiving team could understand, operate and extend the module without loss of design intent or technical context.**
  - How: Technical documentation compilation, handover document authoring, Git repository organisation, knowledge transfer sessions
  - Result: Complete aerodynamics module handed over with full documentation. Codebase and documentation confirmed received and understood by incoming team.

---

## Technical University of Munich — Institute for Rotorcraft and Vertical Flight — Student Assistant - IFR Simulator Instructor

**Role:** Graduate Student  
**Type:** Teaching  
**Location:** Munich, Germany  
**Dates:** 2023-04-01 → 2024-09-30  
**Primary CV section:** Teaching & Academic Experience  
**Secondary:** Technical Skills  

**Experience description (database):**
> Instructed and evaluated aerospace engineering students during the MW1450 IFR Helicopter Flight Lab course across three academic semesters (Summer 2023, Winter 2023/24, Summer 2024). Conducted 8 weekly 5-hour practical training sessions per semester for student pairs, teaching IFR procedures, emergency protocols, radio telephony, and digital cockpit systems on an EC135 fixed-base simulator. Administered and evaluated 5-hour oral and practical final examinations as an official course examiner

### Projects

#### IFR Flight Simulator Instruction & Student Assessment
**Potential CV sections:** Teaching & Academic Experience
**R&D:** No

**Description:** light simulator instruction, practical IFR coaching, and student evaluation for the MW1450 IFR Helicopter Flight Lab course
**System:** Fixed-base EC135 Flight Simulator (X-Plane, Digital Cockpit Display, Physical Flight Controls)
**Objective:** Train aerospace engineering students in instrument flight rules, flight deck procedures, navigation, and radio communications, and evaluate their flight proficiency through formal examinations
**Outcome:** Successfully instructed student cohorts across three academic semesters (8 weekly 5-hour sessions per semester) and evaluated final oral/practical examinations.

**Activities / evidence records:**
- **Led — Practical IFR Flight Instruction & Flight Deck Coordination**
  - How: Conducted weekly 5-hour practical flight simulator training sessions for student pairs enrolled in the MW1450 IFR Helicopter Flight Lab course across three academic semesters. Coordinated simulated flight scenarios using physical cyclic, collective, and rudder controls on an EC135 fixed-base simulator; coached students on flight deck procedures, checklist execution, hovering, taxiing, radio telephony, SID departures, NDB/VOR/DME navigation, holding entries, and ILS instrument approaches.
  - Result: Guided multiple student cohorts to master practical helicopter IFR flight operations and instrument scanning techniques.
- **IndependentlyExecuted — Served as an official course examiner evaluating student pairs during 5-hour final oral and practical simulator examinations**
  - How: Administered oral questioning on EC135 cockpit systems and IFR flight rules, monitored checklist compliance, and assessed flight control accuracy during simulated instrument procedures
  - Result: Evaluated student technical competency against departmental standards using formal scorecard criteria

---

## HORYZN — Project Management - Systems & Integration

**Role:** Student Initiative  
**Type:** Leadership  
**Location:** Munich, Germany  
**Dates:** 2023-07-01 → 2024-07-31  
**Primary CV section:** No dedicated Master-CV section; technical evidence may support Professional Profile / Projects  
**Secondary:** Targeted CV variants  

**Experience description (database):**
> Appointed Project Manager for systems integration and flight testing phase of the Kolibri hybrid lift-and-cruise eVTOL UAS under Mission Pulse Phase 2. Oversaw cross-functional coordination across avionics, flight testing, CAD and structures teams. Hands-on involvement in avionics integration, PX4 flight controller setup, ground testing, flight testing and regulatory preparation. Secured TU Munich aerospace test facilities at Oberpfaffenhofen for final flight campaign. Project concluded with successful transition flight test — completing the Mission Pulse programme. Concurrent with MSc studies and Amazilia working student role. Held EU A1/A3 drone pilot licence throughout this period.

### Projects

#### Kolibri eVTOL — Systems Integration, Flight Testing & Project Completion
**Potential CV sections:** Supporting evidence / targeted variants; Selected Engineering / R&D Projects; Technical Skills
**R&D:** Yes

**Description:** Led the systems integration and flight testing phase of the Kolibri hybrid lift-and-cruise eVTOL UAS as Project Manager. Coordinated cross-functional teams across avionics, flight testing, CAD and structures. Hands-on involvement in avionics integration, PX4 setup, ground testing and flight testing. Managed sponsor relations, team recruitment and facility coordination. Project concluded with successful transition flight test at Oberpfaffenhofen, completing Mission Pulse Phase 2
**System:** Kolibri Hybrid Lift-and-Cruise eVTOL UAS — Full Aircraft Systems Integration and Flight Test
**Objective:** Drive Kolibri from detailed design through systems integration, ground testing and flight testing to achieve successful VTOL-to-cruise transition and complete Mission Pulse programme
**Outcome:** Successful transition flight test achieved at Oberpfaffenhofen test airport. Mission Pulse Phase 2 concluded. Full aircraft development lifecycle completed from conceptual design through operational flight.

**Activities / evidence records:**
- **Led — Appointed Project Manager for systems integration and flight testing phase of Kolibri by the outgoing project management team, based on demonstrated technical contribution and cross-team familiarity during the aerodynamics phase. Transitioned from aerodynamics engineering role into project leadership, taking responsibility for coordinating the avionics and flight testing team as primary focus, with secondary oversight of CAD and structures teams. Obtained EU A1/A3 drone pilot licence around this time, enabling direct participation in flight operations.**
  - How: Role transition, project management onboarding, cross-team coordination establishment, EU A1/A3 licence acquisition
  - Result: Successfully assumed PM role. Clear responsibility boundaries established across teams. Drone pilot licence obtained enabling direct flight test participation.
- **Contributed — Served as the central coordination point between avionics, flight testing, CAD and structures teams during the systems integration phase of Kolibri. Identified and resolved integration conflicts — for example, where avionics and electronics sizing did not fit within the structural spaces allocated by the CAD team, requiring coordinated design iterations across CAD, structures and avionics teams. Facilitated regular cross-team meetings, tracked outstanding integration issues and ensured design decisions were communicated and implemented consistently across all teams. Coordinated with other project managers on resource allocation and scheduling.**
  - How: Cross-functional coordination, integration issue tracking, design review facilitation, inter-team communication management, project scheduling
  - Result: Integration conflicts identified and resolved through coordinated design iterations. Systems integration progressed to hardware assembly and ground testing phase.
- **Contributed — Worked hands-on with the avionics and flight testing team on the integration of Kolibri's avionics systems including flight controller setup on PX4, ESC configuration, sensor integration and onboard electronics wiring. Applied systems integration experience from Amazilia to support the team in solving avionics interface and communication issues. Contributed directly to soldering, wiring and bench testing of avionics components. Used knowledge of Kolibri's full design — aerodynamics, structures and avionics — to provide informed technical guidance on integration decisions.**
  - How: PX4 flight controller configuration, ESC setup, sensor integration, avionics wiring, bench testing, soldering, cross-system technical guidance
  - Result: Kolibri avionics systems integrated and bench-tested, ready to progress to ground testing and hover trials
- **Contributed — Participated in ground testing and hover trial campaign for Kolibri. Built and operated a hover test bench to validate lift motor thrust ratios against the design requirements for the 25kg MTOW aircraft. Tested the defibrillator payload delivery system to confirm correct operation with the aircraft systems. Analysed flight logs from test runs to identify issues and drive corrective actions. Managed the iterative build-test-fail-repeat development cycle — including analysis of two crashes — using data from flight logs and ground control interfaces to diagnose faults and implement fixes.**
  - How: Hover test bench construction and operation, thrust ratio measurement and validation, payload system testing, flight log analysis, fault diagnosis, iterative test campaign management
  - Result: Lift motor thrust ratios validated against design requirements. Payload delivery system confirmed operational. Crash analyses completed and corrective actions implemented. Aircraft cleared to progress to transition flight testing.
- **Contributed — Supported preparation of regulatory documentation for Kolibri flight operations under the SORA framework. Coordinated with the team to ensure operational risk classifications and flight test documentation met the requirements for test flights at the secured facility. Contributed to safety planning and operational procedures for the flight test campaign.**
  - How: SORA framework application, operational risk classification, regulatory documentation preparation, safety planning
  - Result: Regulatory documentation completed supporting authorised flight test operations at Oberpfaffenhofen test facility
- **Contributed — Secured access to a TU Munich aerospace test facility for the Kolibri flight test campaign, coordinating with university contacts to establish a dedicated workspace with appropriate flight test area. Managed all logistics for the flight campaign including team transport, equipment movement, scheduling and on-site coordination. Maintained sponsor communications throughout, providing updates on project progress and test milestones. Coordinated new member recruitment and interviews for incoming semester intake alongside other project managers.**
  - How: Facility negotiation and coordination, flight campaign logistics management, sponsor communication, recruitment coordination, scheduling
  - Result: est facility secured and operational. Flight campaign successfully executed from the facility. Sponsors kept informed and engaged. New member recruitment completed for incoming semester.
- **Contributed — Participated in the final Kolibri transition flight test campaign at Oberpfaffenhofen test airport. Contributed to pre-flight preparation, on-site coordination and post-flight analysis. Kolibri successfully completed VTOL hover, transition to forward flight and cruise phases — achieving the core Mission Pulse objective that the predecessor prototype Frankenstein had failed to reach. Mission Pulse Phase 2 concluded successfully with the completion of the transition flight test.**
  - How: Flight test campaign coordination, pre-flight preparation, on-site operations management, post-flight data analysis, EU A1/A3 drone pilot operations
  - Result: Successful transition flight achieved at Oberpfaffenhofen. Mission Pulse Phase 2 concluded. Full aircraft development lifecycle completed from conceptual design through operational flight test.

---

## Kipepeo Aerospace — Founding CEO & Lead Systems Engineer

**Role:** Startup  
**Type:** Professional  
**Location:** Nairobi, Kenya  
**Dates:** 2024-10-01 → Present  
**Primary CV section:** Professional Experience  
**Secondary:** Technical Skills  

**Experience description (database):**
> Founding CEO and Lead Systems Engineer driving the full-stack design, hardware fabrication, software architecture, and commercial strategy for autonomous UAV platforms, multispectral payload hardware, cloud photogrammetry pipelines, and AI intelligence systems across precision agriculture and defense verticals in East Africa.

### Projects

#### TAI UAS - Tactical Aerial Intelligence Platform 
**Potential CV sections:** Professional Experience; Selected Engineering / R&D Projects; Technical Skills
**R&D:** Yes

**Description:** Systems engineering, 3D CAD modeling, electrical/avionics architecture design, and supplier sourcing for the TAI 2-meter delta-wing hybrid VTOL UAV. The airframe integrates four vertical quad-rotor booms for runway-independent takeoff and landing alongside a dedicated cruise motor, serving as the primary hardware data-collection platform for Kilimo Anga.
**System:** TAI Delta-Wing Hybrid eVTOL
**Objective:** Design an affordable, long-range aerial data-collection platform tailored for African operational environments, combining VTOL runway independence with fixed-wing loiter efficiency, multispectral imaging, and onboard embedded edge processing.
**Outcome:** System requirements established, full electrical/avionics architecture completed, CAD geometry and photorealistic 3D renders generated in Autodesk Inventor, and a procurement-ready Bill of Materials (BOM) finalized. Physical manufacturing and assembly are awaiting funding to source components

**Activities / evidence records:**
- **IndependentlyExecuted — Executed the initial aircraft design lifecycle for the TAI UAS, capturing system-level requirements and conducting preliminary aerodynamic and sizing trade studies for a 2-meter delta-wing hybrid VTOL platform**
  - How: Defined 20+ functional and performance requirements in a master requirements matrix; ran aerodynamic lift/drag simulations in XFLR5 and analytical calculations in MATLAB to evaluate delta-wing loiter efficiency, stability, and sizing for modular payload integration and up to 25 kg MTOW capacity.
  - Result: Established the validated requirements baseline and preliminary aerodynamic geometry for the 2-meter delta-wing hybrid VTOL airframe
- **IndependentlyExecuted — Authored the complete system architecture for the TAI UAS, translating high-level mission requirements into functional allocations, subsystem definitions, and a detailed electrical/control schematic**
  - How: llocated systems across hover propulsion (4 motors/ESCs), cruise propulsion (1 motor/ESC), flight management (Pixhawk PX4), companion computing (Raspberry Pi 4B), power distribution (PDB, BEC, LiPo battery), elevon/rudder actuation, and communications (telemetry, GSM, GPS); mapped all interconnectivity into an engineering drawing
  - Result: Completed the TAI Full System Architecture schematic mapping all power buses, PWM signal lines, and telemetry interfaces required for future physical assembly
- **IndependentlyExecuted — Modeled the 3D mechanical CAD assembly for the TAI delta-wing hybrid VTOL airframe in Autodesk Inventor, incorporating internal structural housing for avionics, propulsion mounts, and modular payload bays**
  - How: Executed 3D parametric modeling of airframe geometries, elevons, vertical fin, and quad-rotor boom assemblies in Autodesk Inventor; verified spatial envelope and component clearance; generated high-resolution 3D renders showcasing top and bottom configurations
  - Result: Delivered complete, production-ready 3D CAD assembly files and photorealistic renders
- **IndependentlyExecuted — Conducted market trade studies, component matching, and cost estimations to compile the full Bill of Materials (BOM) for the TAI UAS platform**
  - How: Selected COTS hardware (Tmotor MN4012 motors, AIR 40A ESCs, and 15" propellers for hover; Tmotor AT2308 motor for cruise; Pixhawk 4 FC; Arducam 21MP RGB and 64MP Quad-Camera multispectral kit with bandpass filters); mapped local suppliers (Pixel Electric, Nerokas) versus international vendors; categorized components by procurement path (3D printing, composite, COTS)
  - Result: Finalized a procurement-ready Bill of Materials (BOM) totaling KES 230,520 with verified part numbers, supplier links, unit costs, and weight allocations

#### Kilimo Anga — Quadrotor Testbed & AngaCam Payload Integration
**Potential CV sections:** Professional Experience
**R&D:** No

**Description:** Requirements derivation, 3D CAD modeling, system architecture specification, and supplier sourcing for an affordable quadcopter testbed and custom 3D-printed multispectral sensor payload (AngaCam). Designed to mirror TAI data-collection capabilities at low cost using open-source multispectral design principles, COTS quadrotor avionics, and a Raspberry Pi companion computing module
**System:** Quadrotor Demonstration Drone & AngaCam Multispectral Payload
**Objective:** Design a low-CapEx quadrotor airframe and custom DIY multispectral camera payload to collect RGB and narrow-band agricultural imagery for photogrammetry testing, lowering the cost barrier of commercial multispectral cameras while serving as an MVP testing bed prior to full TAI deployment.
**Outcome:** Translated farmer-led Kilimo Anga requirements into quadrotor platform specifications; completed 3D CAD models and renders for the F450-based quadcopter testbed (KilimoAnga_PhysicalPrototype.png) and the custom 3D-printed 4-lens camera housing (AngaCam.png, AngaCam Assembly.png); defined full system architecture; compiled procurement BOM (KES 163,800 total) with local Kenyan vendors (Pixel Electric, Nerokas). Physical component procurement and assembly are awaiting funding allocation.

**Activities / evidence records:**
- **IndependentlyExecuted — Derived technical specifications and operational requirements for an agile, low-cost quadrotor testbed and multispectral payload based on farmer feedback from the Kilimo Anga initiative.**
  - How: Translated smallholder farm operational constraints into platform requirements (ease of operation for recruited farm operators, lower unit cost vs. 2m eVTOL); specified 4-band optical capture requirements (RGB, Red, Green, NIR); defined auto-shutter triggering via companion computer integration with QGroundControl/ArduPilot mission plans.
  - Result: Established the validated system requirements baseline for the low-CapEx quadrotor MVP testbed and AngaCam payload
- **IndependentlyExecuted — Engineered the electrical, power distribution, and flight control architecture for the F450-based quadrotor testbed.**
  - How: Scaled down avionics from the TAI hybrid architecture to a quadrotor platform; mapped connections for Pixhawk PX4 FC, 3S LiPo battery, EMAX 2213 935KV motors, and BLHeli 20A ESCs; isolated companion computer (Raspberry Pi 3B+/4B) and payload power on a dedicated step-down BEC/PDB rail away from flight controls.
  - Result: Delivered complete system architecture and electrical layout for the F450 quadrotor testbed, eliminating power rail interference between payload computing and flight controls.
- **IndependentlyExecuted — Designed the 3D mechanical housing and optical mounting for the custom AngaCam multispectral payload in Autodesk Inventor.**
  - How: Modeled an impact-resistant, 3D-printable enclosure housing a Raspberry Pi 4B and 64MP/16MP synchronized quad-camera kit; engineered 4-lens optical alignment, retention slots for 365nm-940nm bandpass filters, and structural crash protection geometry to safeguard fragile optics.
  - Result: Produced completed 3D CAD models and high-resolution renders (AngaCam.png, AngaCam Assembly.png) ready for additive manufacturing.
- **IndependentlyExecuted — Performed component trade studies and compiled the master Bill of Materials (BOM) for the quadrotor testbed and AngaCam payload.**
  - How: Completed assembly design of entire system and generated a BOM from parts and system architecture. Evaluated procurement pathways under Kenyan Civil Aviation Authority (KCAA) import licensing rules; selected licensed local distributors (Pixel Electric, Nerokas) for COTS flight controls and frame parts to ensure 7-21 day lead times and spare parts availability; sourced specialized optics (ArduCam, bandpass filters) globally.
  - Result: Finalized procurement-ready BOM totaling KES 163,800 with verified part numbers, local vendor pricing, and supplier URLs

#### AngaStack V1 Platform Development
**Potential CV sections:** Professional Experience; Selected Engineering / R&D Projects; Technical Skills
**R&D:** Yes

**Description:** rchitecture, full-stack software development, containerization, and cloud deployment of the initial AngaStack precision agriculture infrastructure on Microsoft Azure. Spanned the React + Tailwind CSS web frontend (AngaView), the FastAPI backend API orchestrator, and an automated Dockerized photogrammetry pipeline (AngaCloud) running on ephemeral container instances to process raw drone imagery into orthomosaics and vegetation index maps (NDVI, VARI). Also included the build and deployment of AngaDemo (angademo.kipepeo.space), a lightweight web prototype used for early farmer UX/UI validation.
**System:** AngaStack V1 Cloud Architecture (AngaView Frontend, AngaCloud FastAPI Backend, Docker Photogrammetry Pipeline, Azure Infrastructure, AngaDemo Web Prototype)
**Objective:** Design and deploy a scalable, cloud-native automated photogrammetry pipeline and user-facing dashboard to turn raw aerial imagery into actionable crop health insights for smallholder and commercial maize farmers.
**Outcome:** Fully functional cloud platform and web app capable of end-to-end automated image ingestion, stitching, and index map generation, validated in the field via the live AngaDemo prototype prior to the GCP migration phase.

**Activities / evidence records:**
- **IndependentlyExecuted — Local Photogrammetry Pipeline Development & Algorithm Verification**
  - How: Authored standalone Python scripts (stitching.py, indices.py) using spatial, computer vision, and raster processing libraries to manipulate raw drone image datasets. Developed automated image alignment and orthomosaic stitching algorithms, alongside calculation pipelines for multi-spectral vegetation indices including NDVI and VARI. Executed local testing and mathematical verification of raster outputs on sample flight data to confirm alignment accuracy and index validity prior to backend or cloud integration.
  - Result: Verified, local Python photogrammetry engine capable of reliably stitching raw drone imagery into orthomosaics and producing accurate vegetation index rasters.
- **IndependentlyExecuted — Full-Stack Application Development (AngaView UI & AngaCloud Backend)**
  - How: esigned and built the user-facing web dashboard (AngaView) using React and Tailwind CSS alongside the backend API orchestrator (AngaCloud) using FastAPI. Established REST API endpoints (/upload, /process, /status) for user authentication, farm registration, image upload handling, and job lifecycle management. Structured local NoSQL data models for user profiles, farm spatial metadata, and processing job logs. Implemented drag-and-drop imagery upload, processing progress tracking, and multi-tab galleries for orthomosaics and vegetation index maps while verifying end-to-end local integration with the Python photogrammetry pipeline.
  - Result: Functional, integrated full-stack web application and REST API orchestrator capable of managing farm data, handling image uploads, and communicating locally with the processing pipeline.
- **IndependentlyExecuted — Azure Cloud Infrastructure Provisioning & Live Platform Deployment**
  - How: rovisioned, configured, and integrated Microsoft Azure cloud services following architectural best practices to host the platform. Containerized the Python photogrammetry engine into Docker images and deployed them to execute as ephemeral jobs on Azure Container Instances. Configured Azure Container Apps to host the FastAPI backend orchestrator, Azure Static Web Apps to host the React web dashboard (angaview.kipepeo.space), Azure Blob Storage for raw drone images and output rasters, Azure Cosmos DB for job state tracking, and Microsoft Entra ID for secure user authentication. Established end-to-end cloud orchestration linking image upload events to container creation, status polling, and storage updates.
  - Result: Production-grade, automated cloud infrastructure on Azure capable of ephemeral batch processing and live web deployment at angaview.kipepeo.space
- **IndependentlyExecuted — AngaDemo Digital Prototype Build & Field Usability Validation**
  - How: Built and deployed an interactive digital prototype web app (angademo.kipepeo.space) using React and Tailwind CSS with sample aerial imagery, NDVI health maps, and structured insight cards to test farmer usability without incurring live cloud compute or drone flight costs. Designed and integrated an embedded feedback submission form and analytics dashboard to capture quantitative metrics on insight clarity, usefulness, and pricing sensitivity. Executed a mixed-methods validation study combining online user testing (33 unique users) and on-farm walkthroughs with 6 smallholder maize farmers across 3 Kenyan counties to evaluate user comprehension and willingness to pay.
  - Result: Validated high farmer demand (93.9% interest rate), established a 325.56 KES/acre willingness-to-pay baseline, and identified critical UI/UX iterations (simplified status categories and bold stress overlays) that directly shaped the AngaStack V2 redesign

#### Kilimo Anga - Field Operations, Pre-Pilot Readiness & Business Model
**Potential CV sections:** Professional Experience; Research & Publications
**R&D:** No

**Description:** Market research, field-level customer discovery, financial modeling, and business model structuring for the Kilimo Anga precision agriculture platform in Kenya. Encompassed conducting 5-Whys root cause analysis, farmer persona profiling (Rahisi, Wachira, William Kirwa, Daniel Musyimi, Grassroots), competitor gap analysis, and on-farm usability walkthroughs with AngaDemo. Developed a comprehensive Cost of Status Quo (CoSQ) proof-of-impact model, structured a Credit-in-Kind (pay-in-maize) payment and distributor offloading framework, established an institutional partnership pipeline, and produced pre-seed investor dossiers for accelerator programs (#MyLittleBigThing, Startup360 A2Finance).
**System:** Kilimo Anga Business & Field Operations Model (Market Intelligence Framework, Farmer Persona Matrix, Cost of Status Quo Economic Model, Credit-in-Kind Offloading Pipeline, Pre-Seed Financial Model)
**Objective:** Validate smallholder farmer demand, quantify the economic cost of late stress detection, and design a viable, risk-mitigated business and distribution model for aerial crop intelligence across Kenya
**Outcome:** Fully validated commercial framework supported by field data, demonstrating up to 45% chemical reduction and KES 28,000–65,000/acre recoverable yield headroom, backed by signed farmer commitments, a 7+ partner pipeline, a Credit-in-Kind distributor partnership, and $30K pre-seed investor readiness materials.

**Activities / evidence records:**
- **IndependentlyExecuted — Farmer Persona Discovery**
  - How: Executed field-level qualitative market research and user discovery across Ndabibi, the North Rift, and Kitengela. Applied the 5-Whys root cause analysis method to trace smallholder yield deficits back to late crop stress detection and lack of affordable farm-specific data. Profiled 5 distinct farmer personas (Rahisi, Wachira, William Kirwa, Daniel Musyimi, Grassroots North Rift Farmers), mapping their operational drag, decision-making styles, technology adoption barriers, and willingness-to-pay triggers.
  - Result: Established a validated market intelligence framework and persona matrix that defined Kilimo Anga's target customer segments, feature requirements, and price-sensitivity constraints
- **IndependentlyExecuted — Competitor Gap Analysis & Fail-Point Mapping**
  - How: Conducted a systematic competitor study and gap analysis comparing manual scouting (farm walks), ward-level government extension officers, and commercial drone service providers (e.g., Stablegen) across Kenyan agricultural regions. Mapped specific operational failure points across four core farming stages: Detection (visual-only limitations causing late detection and crop damage from trampling), Decision-Making (lack of actionable recommendations or reliance on guesswork), Action (high labor costs and blanket spraying waste), and Monitoring (infrequent, reactive visits). Derived Kilimo Anga's unfair advantages and competitive differentiators, combining locally engineered UAV hardware for price accessibility, youth extension delivery for trust, and automated AngaView Action Cards for clear guidance.
  - Result: Delivered a comprehensive Competitor Study & Gap Analysis matrix establishing Kilimo Anga's market positioning, pricing advantages, and service-led delivery model designed specifically to solve competitor fail points.
- **IndependentlyExecuted — Cost of Status Quo (CoSQ) Financial & Impact Modeling**
  - How: Formulated the Cost of Status Quo (CoSQ) proof-of-impact model to quantify financial losses caused by late stress detection and reactive farming practices across farmer segments in Kenya. Calculated recoverable yield headroom (KES 26,250–64,750 per acre) and chemical efficiency gains (up to 45% reduction in pass-related chemical spend) based on field data from Ndabibi, the North Rift, and Kitengela. Developed 12-month pilot cash flow projections, built a breakeven model targeting 9,521 acres scanned, and structured the $30,000 pre-seed budget allocation across Operations (53.3%), Platform R&D (23.3%), Regulatory & Legal (13.3%), and Contingency (10%).
  - Result: Delivered a defensible financial model and proof-of-impact framework proving value recovery for farmers while establishing unit economics, breakeven thresholds, and investor returns.
- **IndependentlyExecuted — Credit-in-Kind Business Model & Value Chain Offloading Design**
  - How: Structured the Credit-in-Kind (pay-in-maize) payment mechanism to eliminate the primary adoption barrier for price-sensitive smallholder and mid-scale farmers facing liquidity constraints at planting season. Designed and negotiated pre-agreed produce offloading partnerships with local maize distributors in Nakuru County, establishing an effective 85–90% net revenue recovery rate on in-kind payments. Created the digital ledger reconciliation workflow within AngaCloud to track service delivery, produce collection, distributor offloading, and credit settlement
  - Result: Risk-mitigated, market-tailored payment-in-produce mechanism integrated with local grain distribution networks, expanding TAM accessibility without creating unhedged credit risk.
- **IndependentlyExecuted — Pre-Pilot Ecosystem Partnerships, Governance & Investor Readiness**
  - How: Built a 7+ partner ecosystem pipeline spanning aviation regulatory compliance (KCAA Remote Pilot Certification, DroneSpace Kenya ROC support), county government collaboration (Nakuru County Ministry of Agriculture for pilot site access and farmer mobilization), GIS research (TriGIS), hardware supply chains (Pixel Electric, Nerokas), and cloud infrastructure grants (Microsoft for Startups, Google Cloud for Startups). Executed the Pre-Incorporation Founders' Agreement establishing the fully diluted Cap Table (80% CEO, 20% COO subject to 1-year cliff and 4-year reverse vesting) and IP assignment framework. Authored comprehensive investor readiness materials, including market intelligence dossiers, SDG project canvases (SDGs 2, 8, 9, 13), investment memos, and pitch decks for accelerator pitch sessions (#MyLittleBigThing, Startup360 A2Finance).
  - Result: Finalized investment-ready corporate governance baseline, secured $30K pre-seed pitch positioning, established a 7+ partner execution ecosystem, and captured non-dilutive cloud credit grants from Microsoft and Google.

#### AngaStack V2 Platform Development - GCP Cloud Migration, Mobile Ingestion & AngAi Engine
**Potential CV sections:** Professional Experience; Selected Engineering / R&D Projects; Technical Skills
**R&D:** Yes

**Description:** Re-architecture and cloud migration of the 5-repository AngaStack platform from Microsoft Azure to Google Cloud Platform (angastack-platform), accompanied by a comprehensive codebase rewrite. Migrated the backend orchestrator to GCP Cloud Run, ephemeral photogrammetry execution to Cloud Run Jobs, storage to 4 GCS buckets (raw-images, tiffs, mosaics, index-maps), and database management to Firestore Native with strict security rules. Implemented mobile freemium plant photo ingestion via an Android app, zero-shot visual disease inference via Vertex AI (Gemini 1.5 Flash), quantitative raster stats extraction in indices.py, a unified Farms Page observation timeline, and the AngAi microservice leveraging RAG and Firestore Vector Search to generate plain-language Action Cards
**System:** AngaStack V2 Polyrepo Architecture (AngaView Web/Mobile, AngaCloud FastAPI Orchestrator, Cloud Run Jobs Pipeline Engine, Vertex AI Vision, AngAi RAG Microservice, Firestore Vector Search)
**Objective:** Execute a cost-optimized cloud migration to GCP while expanding platform capabilities to support dual-path ingestion (mobile photos and drone surveys) and AI-driven agronomic recommendation generation.
**Outcome:** Production-ready GCP cloud infrastructure featuring automated multi-source observation ingestion, ephemeral raster batch processing with numerical stats extraction, and an operational RAG microservice writing prioritized Action Cards to Firestore

**Activities / evidence records:**
- **IndependentlyExecuted — GCP Infrastructure Provisioning & IAM Security Architecture**
  - How: Tagged legacy Azure baseline repositories (v0.1.0-azure) and established the gcp-migration development branch across all application repositories. Provisioned the primary GCP project angastack-platform in europe-west1 and enabled core APIs covering Cloud Run, Firestore, Firebase Management, Artifact Registry, Cloud Storage, Secret Manager, and Vertex AI. Created 4 regional GCS buckets (angastack-raw-images, angastack-tiffs, angastack-mosaics, angastack-index-maps) with uniform access controls and automated lifecycle retention rules (90-day deletion for raw imagery, 30-day for intermediate TIFFs). Provisioned a Firestore Native database in europe-west1 and deployed recursive security rules enforcing tenant data isolation via isOwner() match blocks. Created the angastack-registry Docker repository in Artifact Registry, linked the GCP project to Firebase, and configured Email/Password authentication for the AngaView web app. Scoped and configured 3 distinct IAM service accounts (angacloud-pipeline-sa, angacloud-backend-sa, angai-service-sa) with least-privilege role bindings, including granting angacloud-backend-sa the Service Account Token Creator self-binding required for generating short-lived GCS Signed URLs.
  - Result: Production-grade GCP cloud infrastructure (europe-west1) establishing the storage buckets, document database, container registry, authentication provider, and IAM security controls required for V2 microservices
- **IndependentlyExecuted — Photogrammetry Pipeline GCP Migration & Numerical Stats Extraction**
  - How: Refactored the photogrammetry engine repository (gcp-migration branch) by replacing azure_blob.py with gcs_storage.py using the google-cloud-storage SDK to interface with 4 GCS buckets (angastack-raw-images, angastack-tiffs, angastack-mosaics, angastack-index-maps) via gs:// URIs. Rewrote indices.py using numpy and rasterio to compute quantitative raster statistics (NDVI/VARI mean, min, max, std_dev, stress percentage < 0.3, healthy percentage > 0.6) and structured zone breakdowns alongside visual map generation. Refactored main.py to consume runtime environment overrides (USER_ID, FARM_ID, SEASON_ID, OBSERVATION_ID) passed by Cloud Run Jobs, writing numerical stats payloads and status updates (status: "complete" or status: "failed") directly to Firestore documents. Updated the Dockerfile to remove Azure dependencies, built and pushed the container image (pipeline:v1) to Artifact Registry, and provisioned the angacloud-pipeline-job on Cloud Run Jobs in europe-west1 (2 vCPU, 4GiB RAM, 3600s timeout) attached to angacloud-pipeline-sa
  - Result: Ephemeral, stateless batch-processing engine running on GCP Cloud Run Jobs that ingests raw drone imagery from GCS, generates orthomosaics/index maps, and writes numerical stats JSON directly to Firestore.
- **IndependentlyExecuted — Backend Service Refactoring, Dual-Path Ingestion & Job Orchestration**
  - How: Refactored the AngaCloud FastAPI orchestrator on the gcp-migration branch by replacing legacy Azure SDKs (azure-cosmos, azure-storage-blob, azure-identity) with Google Cloud libraries (google-cloud-firestore, google-cloud-storage, firebase-admin, google-cloud-aiplatform). Updated the data access layer to interact with the new Firestore document hierarchy (users/{user_id}/farms/{farm_id}/seasons/{season_id}/observations/{observation_id}) and 4 GCS buckets. Designed dual-path ingestion endpoints: POST /observations/mobile to upload plant JPEGs to GCS, execute zero-shot vision inference via Vertex AI (Gemini 1.5 Flash) using strict JSON schemas, write observation payloads, and trigger AngAi; and POST /observations/drone to handle batch survey uploads, write initial status: "processing" records, and dispatch Cloud Run Jobs (angacloud-pipeline-job) with environment variable overrides. Implemented short-lived GCS Signed URL generation for map layers (angastack-mosaics, angastack-index-maps) leveraging angacloud-backend-sa's Service Account Token Creator self-binding, added POST /process/ai-trigger for dispatching async HTTP requests to the AngAi microservice, and replaced Microsoft Entra ID verification with firebase-admin token authentication middleware. Dockerized and deployed the backend service angacloud-backend to GCP Cloud Run in europe-west1 attached to angacloud-backend-sa
  - Result: Operational FastAPI backend service on GCP Cloud Run handling multi-source observation ingestion (instant mobile vision inference and asynchronous drone job dispatch), GCS Signed URL map rendering, and Firebase token authentication.
- **IndependentlyExecuted — AngAi Agronomic Reasoning Engine & RAG Microservice Build**
  - How: Ingested and chunked agronomic literature from CIMMYT, FAO, and KALRO into 300–500 token passages, generated vector embeddings using Google's text-embedding-004 model via Vertex AI, and populated Firestore Vector Search with cosine distance indexing. Developed the rules.py engine to process polymorphic Observation payloads, evaluating both mobile vision payloads (health_status, severity, visual_evidence) and drone photogrammetry statistics (ndvi_mean, stress_percentage, zone_breakdown) against threshold logic. Implemented rag.py to execute vector similarity queries against Firestore Vector Search, retrieve top-5 context chunks, format prompts, and query Gemini 1.5 Flash via Vertex AI to output standardized Action Cards (priority, category, insight, recommendation). Wrapped the engine in a FastAPI microservice exposing POST /analyse to write outputs directly to Firestore (/ai_output/{output_id}), Dockerized the application, pushed the image (angai:v1) to Artifact Registry, and deployed angai-service to Cloud Run in europe-west1 attached to angai-service-sa with restricted IAM invocation rights for angacloud-backend-sa
  - Result: Operational, authenticated RAG microservice on GCP Cloud Run capable of processing multi-source observation payloads and generating context-aware agronomic Action Cards in Firestore
- **IndependentlyExecuted — AngaView Mobile Ingestion, Firebase Hosting & Living Farm Health Record UI**
  - How: Refactored the AngaView frontend web/mobile repository on the gcp-migration branch, replacing Microsoft Entra ID with the Firebase Auth SDK (signInWithEmailAndPassword) and attaching Firebase ID tokens to backend Bearer auth headers. Reconfigured the API layer to target the new Cloud Run backend URL and configured an Android mobile app wrapper (Capacitor/PWA) for field mobility. Deprecated the standalone gallery route (/gallery), converting images into evidence attachments embedded within observation records. Built a mobile camera UI component enabling field photo capture with device GPS metadata to trigger POST /observations/mobile for real-time Vertex AI diagnostic feedback. Re-architected the main workspace around the Farms Page (/farms/{farm_id}), creating the FarmHeader (GPS centroid, calculated acreage, season selector, health score), UnifiedTimeline (a longitudinal feed merging mobile inspections and drone mapping surveys), MapViewer (Leaflet/MapLibre rendering GeoJSON farm boundaries, GCS Signed URL orthomosaic/NDVI overlays, and geotagged drop-pins), StatsPanel (quantitative index statistics and zone breakdowns), and ActionCardList (priority-badged, category-iconed AI recommendations). Configured SPA route rewrites in firebase.json, built decoupled loading and error states, and deployed the production web build to Firebase Hosting via firebase deploy --only hosting
  - Result: Deployed, mobile-responsive web and Android application on Firebase Hosting featuring instant mobile photo diagnostics, interactive GCS-signed raster map rendering, and a unified longitudinal farm health record

#### Linda Nchi — Sovereign Tactical ISR Platform & K-DEMO-2.5 Cargo Demonstrator
**Potential CV sections:** Professional Experience; Selected Engineering / R&D Projects
**R&D:** Yes

**Description:** Conceptualization, systems engineering architecture, institutional alignment, and technical roadmap development for Linda Nchi—Kipepeo Aerospace's sovereign Intelligence, Surveillance, and Reconnaissance (ISR) ecosystem. Formulated operational requirements for border monitoring, critical infrastructure protection, and anti-poaching in contested RF environments. Designed the hybrid VTOL airframe specifications (4.5h endurance, 4.0 kg payload, 3,500m MSL ceiling), EO/IR 3-axis active gimbal payload integration, hardware-accelerated AES-256 encrypted datalinks, dual-node LindaView GCS, and edge-AI (LindaAi) threat detection framework. Executed the full mechanical design and structural validation dossier for Project K-DEMO-2.5, a heavy-lift cargo hexacopter demonstrator (2.5 kg payload / 15-min hover). Performed atmospheric density thrust corrections for 1,800m ASL elevation, cantilever beam stress analysis on $3/4$-inch 6061-T6 aluminum arms (deriving $FS = 4.07$ under 100N tip load), 6S/12,000mAh battery DoD power trade studies, and itemized a $635.50 procurement BOM
**System:** Linda Nchi Sovereign ISR System Architecture (Hybrid VTOL Airframe, EO/IR Gimbal, COFDM Datalink, Dual-Node LindaView GCS, LindaAi RAG/Inference Pipeline, Air-Gapped AngaCloud) & Project K-DEMO-2.5 Hexacopter Demonstrato
**Objective:** Define a sovereign, jam-resilient tactical ISR aerial monitoring platform tailored to East African security realities, and engineer a low-cost heavy-lift cargo demonstrator optimized for local manufacturing and high-altitude operation
**Outcome:** Completed formal Linda Nchi Technical Roadmap (v1.1) and system requirements baseline aligned with KDF/MoD operational channels and DPA 2019 data protection compliance, backed by a fully calculated, production-ready engineering dossier and BOM for the K-DEMO-2.5 heavy-lift hexacopter

**Activities / evidence records:**
- **IndependentlyExecuted — Defense Stakeholder Requirement Synthesis & Use-Case Mapping**
  - How: Synthesized institutional deliberations with military and defense liaisons into a structured use-case framework spanning border monitoring, critical infrastructure overwatch, anti-poaching, and emergency disaster response. Analyzed regulatory authorization pathways across KCAA Beyond Visual Line of Sight (BVLOS) flight corridors, Ministry of Defence airspace deconfliction, and National Defence Act guidelines requiring a minimum target of 30% domestic content through local component assembly, structural composites fabrication, and domestic software development. Formulated end-to-end data privacy and anonymization mechanisms embedded directly into the sensor payload stack to strip and blur civilian personal metadata prior to network broadcast, ensuring full compliance with the Data Protection Act (DPA) 2019
  - Result: Delivered a validated stakeholder use-case matrix, regulatory certification pathway, and privacy-compliant data governance framework for sovereign ISR operations
- **IndependentlyExecuted — Linda Nchi Tactical ISR System Architecture & Technical Roadmap Authoring**
  - How: Authored the comprehensive Linda Nchi Technical Roadmap (v1.1) establishing subsystem specs, lineage carryovers from AngaStack, and technical maturity gates across a 3-phase development timeline. Defined target performance envelopes for a long-loiter hybrid VTOL airframe (4.5h endurance, 4.0 kg max payload, 3,500m MSL ceiling), a 3-axis gyro-stabilized EO/IR thermal gimbal payload core, and hardware-accelerated AES-256 encrypted COFDM digital transceivers with Frequency Hopping Spread Spectrum (FHSS) anti-jamming capabilities. Designed the dual-node LindaView Ground Control Station architecture (separating flight vector control from sensor targeting) and structured the LindaAi edge-inference/RAG pipeline for automated multi-class target classification (personnel, vehicles, weapons)
  - Result: Completed a production-ready, 11-section system architecture and technical roadmap establishing subsystem boundaries, interface control targets, and air-gapped on-premise cloud infrastructure schemas
- **IndependentlyExecuted — Project K-DEMO-2.5 Heavy-Lift Cargo Hexacopter Mechanical Engineering & Stress Analysis**
  - How: Executed mechanical sizing, propulsion trade studies, and structural stress modeling for Project K-DEMO-2.5, a low-cost heavy-lift cargo hexacopter designed for a 2.5 kg payload under Kenyan highland environmental conditions. Modeled atmospheric air density degradation at 1,800m ASL ($\rho = 0.958 \text{ kg/m}^3$) and compensated with a 2.5:1 sea-level thrust-to-weight target generating 13.75 kg combined static thrust via 6x Sunnysky 380KV motors and 1555 carbon-nylon blades. Conducted cantilever beam bending stress analysis on $3/4$-inch (19.05mm) 6061-T6 hollow square aluminum extrusion arms under an extreme 100N tip load, proving a maximum internal bending stress of 67.73 MPa and a structural factor of safety of $FS = 4.07$. Calculated 6S LiPo power consumption (660W hover draw at 29.73A) enforcing an 80% Depth-of-Discharge margin for a 15-minute flight envelope, and compiled an itemized $635.50 procurement Bill of Materials (BOM)
  - Result: Delivered a fully calculated, production-ready engineering design dossier, CAD geometry layout, vertical CoG stack architecture, and local procurement BOM for the heavy-lift cargo demonstrator

#### Kipepeo Venture Building, Governance & Capital Strategy
**Potential CV sections:** Professional Experience
**R&D:** No

**Description:** Corporate ideation, official registration, team restructuring, governance architecture, and capital strategy execution for Kipepeo Aerospace—spanning the July 2020 Konza Technopolis drone center proposal (Drones4Kenya), October 2023 business registration (BN-BGCKDY99), Jasiri Talent Investor program residency in Rwanda, Pre-Incorporation Founders' Agreement execution, #MyLittleBigThing accelerator, S360 Access to Finance showcase, execution of the initial $1,000 SAFE investment, and onboarding into the 2026–2027 Investor Readiness Program (IRP).
**System:** Kipepeo Corporate, Governance & Capital Strategy Framework
**Objective:** Formulate, register, structure, and scale Kipepeo Aerospace into an investment-ready commercial aerospace original equipment manufacturer (OEM), establishing legal compliance, core team alignment, board governance, strategic partnerships, and early capital commitments.
**Outcome:** Registered Kipepeo Aerospace (BN-BGCKDY99), executed the Pre-Incorporation Founders' Agreement (80/20 CEO/COO equity split with 1-year cliff and 4-year reverse vesting), recruited core team and advisors, completed the S360 Access to Finance program with a $30,000 pre-seed raise dossier, secured $1,000 SAFE investment from Zimbu Investments Limited at a $1,000,000 valuation cap with board representation, and onboarded into the 2026–2027 Investor Readiness Program (IRP)

**Activities / evidence records:**
- **Led — Formulated the foundational vision, operational roadmap, and financial budget for establishing an indigenous drone technology hub at Konza Technopolis**
  - How: Conducted market research and case study evaluations of African drone deployments (Zipline Rwanda, African Drone and Data Academy Malawi, Rocketmine South Africa); drafted a 24-page proposal and presentation covering drone operations, local assembly/manufacturing, technical/pilot training, and multi-rotor vs. fixed-wing applications across agriculture, healthcare, and conservation; modeled a 1-year KES 15.5M capital budget covering office space, hangars, KCAA licensing, COTS hardware acquisition, and personnel.
  - Result: Delivered the comprehensive Proposed Konza Technopolis Drone Centre proposal and presentation to Konza Technopolis management on July 23, 2020; identified critical capital and technical expertise barriers that established the founding rationale for pursuing an MSc in Aerospace Engineering and establishing Kipepeo Aerospace.
- **IndependentlyExecuted — Executed formal business name registration and statutory setup to legally establish Kipepeo Aerospace in Nairobi, Kenya**
  - How: Submitted business registration filings via the eCitizen Business Registration Service (BRS) pursuant to the Registration of Business Names Act (Cap 499); conducted name reservation, registered Karen business address, and aligned tax PIN documentation
  - Result: Successfully secured official Certificate of Registration Number BN-BGCKDY99 from the Registrar of Companies on October 25, 2023, establishing the sole proprietorship predecessor entity for Kipepeo Aerospace
- **IndependentlyExecuted — Participated in the 3-month Jasiri Talent Investor residential intensive in Bugesera, Rwanda, conceptualizing the iCARUS precision agriculture venture and conducting smallholder agri-data market research**
  - How: Conducted qualitative and quantitative farmer discovery; authored a $200 GeoPoll research brief targeting 50 smallholder maize farmers across the Rift Valley and Western Highlands to evaluate agri-data consumption barriers; formulated the iCARUS Business Model Canvas mapping pay-per-scan B2C and B2B software subscription streams; delivered the Jasiri Demo Day 1 pitch presentation on May 2, 2025
  - Result: Produced iCARUS venture overview, business model canvas, and Demo Day 1 presentation; validated the 80% agri-data non-consumption gap among smallholder farmers; navigated co-founder departure upon program conclusion to operate solo under Kipepeo Aerospace
- **Led — Applied for and secured non-dilutive cloud infrastructure grant funding through the Microsoft for Startups Founders Hub program**
  - How: Drafted technical platform architecture proposals for AngaStack V1; detailed the cloud compute, database, and containerization requirements for automated photogrammetry processing on Azure; submitted venture traction and technical roadmap documentation
  - Result: Accepted into Microsoft for Startups Founders Hub, securing $5,000 USD in Azure cloud credits to host AngaCloud backend APIs, containerized image stitching, and AngaView web services without early cash burn
- **IndependentlyExecuted — Negotiated and executed three strategic Memorandums of Understanding (MoUs) with Stablegen Investment Ltd. to establish pilot market access, software testing, and drone corridor access**
  - How: Drafted bilateral legal agreements defining IP protection, data privacy, and operational responsibilities; structured MoU 1 for software photogrammetry pipeline testing and market feedback; structured MoU 2 for deploying an integrated drone, multispectral camera, and software solution to Stablegen as a pilot customer at no cost for 12 months; structured MoU 3 for joint drone corridor compliance and shared testing/prototyping facility access under KCAA rules.
  - Result: Executed three binding 12-month MoUs with Stablegen Investment Ltd.; established formal pilot customer and testing framework, though relations subsequently broke down, prompting a pivot to direct brand visibility and accelerator applications
- **IndependentlyExecuted — Registered core internet domains, established digital brand presence, and deployed web infrastructure for Kipepeo Aerospace and its flagship initiative Kilimo Anga**
  - How: Secured domain ownership for kipepeo.space and kilimoanga.kipepeo.space; designed and deployed company landing pages showcasing corporate OEM vision, team profiles, and precision agriculture capabilities; created and integrated official social media channels across LinkedIn, Twitter, and Facebook to build ecosystem visibility.
  - Result: Established digital brand identity, public web portals (kipepeo.space, kilimoanga.kipepeo.space), and social media reach to support incubator applications, partner outreach, and farmer engagement.
- **Led — Conducted talent acquisition campaigns, restructured executive roles, and established a specialized advisory board to strengthen Kipepeo Aerospace's commercial, legal, and agronomic leadership**
  - How: Authored contract-to-hire job descriptions for key roles including Business Development Lead; recruited Brian Kihumba Kimani (LLB, MBA) as Co-Founder & COO to lead sales, operations, and farmer onboarding; onboarded Patience Kirwa as Co-Founder/Marketing Lead; engaged consultants Adrian Kiplimo (Software) and Richard Wanjohi (Hardware); established a formal advisory board featuring Torooti Mwirigi (Startup Mentorship) and Oliver Ndegwa (Agronomic Mentorship
  - Result: Assembled a 7-member core operational team, consulting network, and advisory structure; transitioned Brian Kihumba from BD Lead to Co-Founder & COO, establishing the multi-disciplinary leadership baseline for commercial scaling
- **IndependentlyExecuted — Applied for the MK-Africa #MyLittleBigThing Sustainable Venture Challenge with Kilimo Anga, securing selection into the Top 50 and completing the two-day Innovation Bootcamp.**
  - How: Authored comprehensive application materials aligning Kilimo Anga with SDGs 2 (Zero Hunger), 9 (Industry, Innovation & Infrastructure), and 13 (Climate Action); completed the e-learning workbook and Impact Plan; attended the two-day intensive bootcamp on December 8–9, 2025; formulated the Riskiest Assumption (RA) and Falsifiable Test Design targeting smallholder maize farmer adoption of affordable per-acre aerial scans
  - Result: Selected as one of the Top 50 African Innovators out of a competitive pool; completed the Falsifiable Test Plan and overnight virtual experiment setup, advancing to the prototype validation phase
- **IndependentlyExecuted — Executed the 30-Day Build & Test Challenge for #MyLittleBigThing, deploying the AngaDemo digital prototype and conducting field usability and willingness-to-pay (WTP) validation studies**
  - How: Built and deployed the interactive web prototype angademo.kipepeo.space using React and Tailwind CSS featuring sample aerial imagery, NDVI maps, and structured insight cards; conducted on-farm walkthroughs and interviews with 6 smallholder maize farmers across Nakuru, Kericho, and Eldoret; gathered structured feedback from 33 unique online users via an embedded feedback form; bootstrapped $150 in funding to procure branded reflector vests, business cards, and a broadbase roll-up banner; delivered the final #MLBT Demo Day pitch presentation.
  - Result: Validated a 93.9% farmer interest rate (surpassing the 40% benchmark); established a 325.56 KES/acre average WTP baseline; triggered 4 UI/UX product iterations (simplified healthy/stressed/at-risk status categories, bold color-block overlays, and plain-language Action Cards); submitted formal Evidence of Build, Evidence of Test, and Demo Day pitch deck
- **IndependentlyExecuted — Applied for and secured non-dilutive cloud infrastructure grant funding from the Google Cloud for Startups program**
  - How: Authored cloud architecture migration proposals detailing the transition from Azure to GCP (Cloud Run, Cloud Run Jobs, Firestore, GCS, Vertex AI, and Artifact Registry); demonstrated venture traction, farmer validation metrics, and AI roadmap plans (AngAi RAG microservice)
  - Result: Accepted into the Google Cloud for Startups program, securing cloud credit grants to fund the full AngaStack V2 GCP re-architecture, ephemeral photogrammetry batch jobs, and Vertex AI Gemini 1.5 Flash inference pipeline
- **IndependentlyExecuted — Completed the Viktoria Ventures Startup360 Access to Finance (A2F) Programme and authored the $30,000 pre-seed investor readiness dossier and financial model for Kilimo Anga**
  - How: Completed a 5-week intensive VC/angel coaching cycle covering valuation fundamentals, term sheet mechanics, due diligence data rooms, and CAC/LTV modeling; authored a comprehensive Market Intelligence Dossier, Investor Q&A Brief, 12-month pilot cash flow projection spreadsheet, Pre-Seed Investment Memo, and S360 Pitch Deck; modeled a $30,000 raise allocated across Operations (53.3% / $16,000 for $1,400 monthly burn), Platform R&D (23.3% / $7,000 for 2 AngaStack units), Regulatory & Legal (13.3% / $4,000 for KCAA ROC and patent filings), and Contingency (10% / $3,000); pitched at the S360 Final Showcase on May 7, 2026.
  - Result: Finalized a defensible pre-seed investment package demonstrating a 9,521-acre breakeven target, $40,000 projected sales, and an 87% contribution margin per acre-visit; presented at the Angel Investor Showcase, though direct cash investment from the showcase was not secured
- **IndependentlyExecuted — Authored and executed the binding Kipepeo Aerospace Pre-Incorporation Founders' Agreement, establishing legal governance, cap table ownership, reverse vesting, and operational decision hierarchies under Kenyan law**
  - How: Drafted a 40-page, 17-section legal framework and 3 schedules governing Kipepeo Aerospace Limited and its successor relationship to sole proprietorship BN-BGCKDY99; structured Schedule A (Capitalisation Table) defining 100,000 authorized shares with a fully diluted pre-investment allocation of 80% to Founder 1 (CEO Brian Lembuss, fully issued and vested) and 20% reserved for Founder 2 (COO Brian Kihumba); established a 1-year cliff (backdated to Joining Date Oct 1, 2025) and a 4-year reverse vesting schedule; authored Schedule C setting binding annual weighted KPI thresholds for COO equity vesting across Farmers Onboarded (30%), Activation Rate (30%), SACCO MOUs (30%), Mission Readiness (10%), and Reporting (10%); defined a 2-member Board of Directors with CEO casting vote, overriding Pilot-in-Command (PIC) flight safety authority, IP assignment, DPA 2019 data protection compliance, and non-compete/deadlock resolution mechanics
  - Result: Executed the formal Pre-Incorporation Founders' Agreement effective April 10, 2026, locking in the corporate cap table, governance structure, and IP transfer baseline prior to external capital injection
- **IndependentlyExecuted — Negotiated and executed the first formal early-stage investment agreement for Kipepeo Aerospace via a Simple Agreement for Future Equity (SAFE) with Zimbu Investments Limited.**
  - How: Structured investment terms with advisor Torooti Mwirigi and Zimbu representatives; drafted the Investment Letter and SAFE Agreement incorporating a $1,000 USD investment at a $1,000,000 USD Valuation Cap with a 20% discount rate on future qualified equity rounds ($\ge$$100,000); embedded governance conditions nominating Nicholas Kithinji to serve as Technical Board Chairman representing Zimbu; structured a separate 5% equity vesting agreement for Board Chair services (3% Year 1, 2% Year 2) held for Zimbu Investments Limited; included pro-rata rights, acquisition/liquidity payout protections, and quarterly financial reporting covenants
  - Result: Executed the binding SAFE agreement and board representation charter with Zimbu Investments Limited, securing Kipepeo Aerospace's first external capital commitment at a $1,000,000 valuation cap
- **IndependentlyExecuted — Applied for and onboarded into the 12-Month #MyLittleBigThing Investor Readiness Program (IRP) Pilot Cohort (2026–2027) co-delivered by MK-Africa and Strathmore @iBizAfrica**
  - How: Submitted formal onboarding profiles, KRA PIN details, and baseline traction tracking data; enrolled in the 12-month parallel processing model spanning Track 1 (Legal Formalization & LLC Conversion), Track 2 (Operational Strategy & MVP Hardening), and Track 3 (Market Validation & First 100 Customers); aligned venture milestones with program metrics targeting KES 100,000 monthly revenue, 32+ formal jobs created (SDG 8), and due diligence preparation for the Absa SME Impact Loan facility; granted non-confidential marketing and public investor profiling consents for the July 2026 investor portal launch.
  - Result: Successfully onboarded Kilimo Anga / Kipepeo Aerospace as one of 16 semi-finalist ventures in the 2026–2027 IRP cohort, establishing an active 12-month incubation and bankability pipeline backed by Strathmore University and corporate partners

---

## Jasiri4Africa — Jasiri Fellow, Talent Investor Program

**Role:** Entrepreneur  
**Type:** Professional  
**Location:** Rwanda  
**Dates:** 2025-01-01 → 2025-05-30  
**Primary CV section:** Professional Experience  
**Secondary:** Technical Skills  

**Experience description (database):**
> Participated in the Jasiri Talent Investor program (Cohort 7 / Ntore Cohort) funded by Allan & Gill Gray Philanthropy. Completed the online Jumpstart phase and 3-month Residential Intensive in Bugesera, Rwanda, focusing on team formation, qualitative/quantitative smallholder farmer discovery, commissioning a GeoPoll research study, formulating the iCARUS business model canvas, and presenting at Jasiri Demo Day 1 before opting out prior to the venture creation phase.

### Experience-level activities
- **IndependentlyExecuted — Completed the Jasiri Jumpstart and 3-month Residential Intensive while executing field-level market discovery on smallholder agri-data adoption barriers in Kenya.**
  - How: Completed the Jasiri Jumpstart and 3-month Residential Intensive while executing field-level market discovery on smallholder agri-data adoption barriers in Kenya.
  - Result: Validated core market pain points around late crop stress detection, high input costs, and lack of affordable farm-specific decision support tools for smallholder farmers.
- **IndependentlyExecuted — formulated the dual-sided business model canvas and revenue architecture for the iCARUS precision agriculture concept.**
  - How: Structured pay-per-scan B2C smallholder services and B2B software/data subscriptions for drone operators and agricultural parastatals; mapped key value propositions, extension channels, and cost structures; evaluated strategic partnerships with regulators (KCAA), seed companies (ADC, KSC), and cloud providers.
  - Result: Produced a comprehensive Business Model Canvas establishing unit economics, market size ($5.7M TAM target), and go-to-market channels.
- **IndependentlyExecuted — Authored and delivered the iCARUS venture pitch deck at Jasiri Demo Day 1 in Bugesera, Rwanda**
  - How: Synthesized market research data, smallholder yield deficit statistics, drone/multispectral tech stack architecture, and pilot financial projections into a 9-slide investor presentation; pitched to Jasiri program directors, venture coaches, and fellow entrepreneurs
  - Result: Successfully completed Demo Day 1 requirements on May 2, 2025, validating venture readiness prior to program exit.

---

# Cross-section evidence index

This index is a navigation aid for 6B; it does not make final selections.

## Professional Experience

- **ALS Ltd — Aircraft Maintenance Intern**: Aircraft Line, Base & C-Check Maintenance — ALS Ltd MRO
- **Kendrone Ltd — UAS Engineer, Pilot and Instructor**: Drone-Based Seedball Dispersal Mechanism, UAS Pilot Training Programme Delivery, Aerial Mapping & Agricultural Survey Operations, UAS Avionics, Payload Integration & Fleet Maintenance, IT Infrastructure, Digital Presence & Company Operations
- **Amazilia Aerospace GmbH — Aerospace Systems Engineering**: WfA MiniFreighter GCS -SN2, Amazilia Ground Control Station, Aircraft Systems Hardware-in-the-Loop (HIL) Test Rig, Aircraft Battery Charging Unit (ABCU)
- **HORYZN  — Aerodynamics Project Engineer**: Kolibri eVTOL — Aerodynamics Module Development
- **Kipepeo Aerospace — Founding CEO & Lead Systems Engineer**: TAI UAS - Tactical Aerial Intelligence Platform , Kilimo Anga — Quadrotor Testbed & AngaCam Payload Integration, AngaStack V1 Platform Development, Kilimo Anga - Field Operations, Pre-Pilot Readiness & Business Model, AngaStack V2 Platform Development - GCP Cloud Migration, Mobile Ingestion & AngAi Engine, Linda Nchi — Sovereign Tactical ISR Platform & K-DEMO-2.5 Cargo Demonstrator, Kipepeo Venture Building, Governance & Capital Strategy
- **Jasiri4Africa — Jasiri Fellow, Talent Investor Program**: experience-level evidence

## Selected Engineering / R&D Projects

- **WfA MiniFreighter GCS -SN2** — Amazilia Aerospace GmbH
- **Amazilia Ground Control Station** — Amazilia Aerospace GmbH
- **Aircraft Systems Hardware-in-the-Loop (HIL) Test Rig** — Amazilia Aerospace GmbH
- **Aircraft Battery Charging Unit (ABCU)** — Amazilia Aerospace GmbH
- **Kolibri eVTOL — Aerodynamics Module Development** — HORYZN 
- **Kolibri eVTOL — Systems Integration, Flight Testing & Project Completion** — HORYZN
- **TAI UAS - Tactical Aerial Intelligence Platform ** — Kipepeo Aerospace
- **AngaStack V1 Platform Development** — Kipepeo Aerospace
- **AngaStack V2 Platform Development - GCP Cloud Migration, Mobile Ingestion & AngAi Engine** — Kipepeo Aerospace
- **Linda Nchi — Sovereign Tactical ISR Platform & K-DEMO-2.5 Cargo Demonstrator** — Kipepeo Aerospace
- **Drone-Based Seedball Dispersal Mechanism** — Kendrone Ltd
- **Generic Modeling of Slotneutral UAM Throughput at Commercial Airports** — Technical University of Munich
- **Embedded Software Development of the Actuator Control and Monitoring Unit (ACMU)** — Technical University of Munich
- **Autonomous Sub-Terrain UAV Challenge** — Technical University of Munich
- **Applied CFD Channel & Cavity Flow Simulation** — Technical University of Munich
- **Simulation of the Flowfield of a Multirotor in Axial Flight** — Technical University of Munich
- **Numerical Methods for Aerospace Engineers ** — Middle East Technical University
- **Finite Element Modelling of a Composite Cantilever Beam** — Middle East Technical University
- **Turbofan Compressor Performance Analysis** — Middle East Technical University
- **Finite Difference Method Solvers for Aerodynamic PDEs** — Middle East Technical University
- **Conceptual Design of a Fixed-Wing Luxury Aircraft (Graduation Project I)** — Middle East Technical University
- **Conceptual Design of a VTOL Personal Air Vehicle (Graduation Project II)** — Middle East Technical University
- **Design and Development of an Automated Air Filter** — Middle East Technical University
- **Simulation of a piezoelectric d15 torsion sensor** — Middle East Technical University
- **Geospatial Analysis & Cartography — Nakuru County Geotourism Research** — Technical University of Munich
- **Project Mentor - Hydrogen-Hybrid Engine** — Young Scientists Kenya (YSK)
- **Project Mentor - Portable Aircraft Refueling Rig & Automated Fuel Dispenser** — Young Scientists Kenya (YSK)
- **Design and Implementation of an Unmanned Aircraft System (UAS) using the Model Based System Engineering (MBSE) Approach for Agricultural Applications at the Galana Kulalu Irrigation Scheme** — University of Cologne

## Education

- **Middle East Technical University — B.Sc. Aerospace Engineering**
- **Technical University of Munich — M.Sc Aerospace**
- **University of Cologne — LEAD! Leadership for Africa**

## Research & Publications

- TUM UAM throughput project: database project and activity evidence; publication is also documented in the existing CV/narrative source.
- Other research/R&D projects are indexed above where their database descriptions explicitly identify research/R&D.

## Teaching & Academic Experience

- **Middle East Technical University — SI-PASS Leader & Instructor — MAT119 & MAT120**: Calculus Supplemental Instruction & Peer-Assisted Study Sessions
- **Middle East Technical University — Student Assistant - ASE301 Numerical Methods for Aerospace Engineers**: ASE301 Course Instruction & Student Assessment
- **Young Scientists Kenya (YSK) — STEM Mentorship**: Project Mentor - Hydrogen-Hybrid Engine, Project Mentor - Portable Aircraft Refueling Rig & Automated Fuel Dispenser
- **Technical University of Munich — Institute for Rotorcraft and Vertical Flight — Student Assistant - IFR Simulator Instructor**: IFR Flight Simulator Instruction & Student Assessment

## Certifications & Licences

- **Private Pilot Licence (PPL) Training** — Skylink Flight Services
- **Remote Pilot Licence (RPL) Training — Multirotor** — Kendrone Ltd

## Technical Skills

Technical tools/technologies are intentionally mapped from the underlying activities and project systems rather than copied wholesale from the Tag table. The competency map already aggregates the strongest recurring tools.