Name:           ros-indigo-hironx-rpc-server
Version:        0.0.2
Release:        0%{?dist}
Summary:        ROS hironx_rpc_server package

Group:          Development/Libraries
License:        Apache License 2.0
URL:            http://wiki.ros.org/hironx_rpc
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-hironx-ros-bridge
Requires:       ros-indigo-hironx-rpc-msgs
Requires:       ros-indigo-hrpsys
Requires:       ros-indigo-hrpsys-ros-bridge
Requires:       ros-indigo-tork-rpc-util
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-roslint
BuildRequires:  ros-indigo-rostest

%description
This package provides RPC (Remote Procedure Call) server feature for higher
level of robot operations for the Hironx-variant robots (i.e. Hironx, NEXTAGE
Open).

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Sat Mar 25 2017 TORK <dev@opensource-robotics.tokyo.jp> - 0.0.2-0
- Autogenerated by Bloom

