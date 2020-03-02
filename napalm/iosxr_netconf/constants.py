# -*- coding: utf-8 -*-
# Copyright 2020 CISCO. All rights reserved.
#
# The contents of this file are licensed under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with the
# License. You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations under
# the License.

"""Constants for the IOS-XR NETCONF driver."""

from __future__ import unicode_literals

from napalm.base.constants import *  # noqa

# namespaces for XR native models
NS = {'int': 'http://cisco.com/ns/yang/Cisco-IOS-XR-pfi-im-cmd-oper',
      'suo': 'http://cisco.com/ns/yang/Cisco-IOS-XR-shellutil-oper',
      'imo': 'http://cisco.com/ns/yang/Cisco-IOS-XR-invmgr-oper',
      }

# GET RPC to retrieve device facts
FACTS_RPC_REQ = '''<get xmlns="urn:ietf:params:xml:ns:netconf:base:1.1">
  <filter>
    <system-time xmlns="http://cisco.com/ns/yang/Cisco-IOS-XR-shellutil-oper"/>
    <interfaces xmlns="http://cisco.com/ns/yang/Cisco-IOS-XR-pfi-im-cmd-oper">
      <interfaces>
        <interface>
          <interface-name/>
        </interface>
      </interfaces>
    </interfaces>
    <inventory xmlns="http://cisco.com/ns/yang/Cisco-IOS-XR-invmgr-oper">
      <racks>
        <rack>
          <attributes>
            <inv-basic-bag>
              <software-revision/>
              <model-name/>
              <serial-number/>
            </inv-basic-bag>
          </attributes>
        </rack>
      </racks>
    </inventory>
  </filter>
</get>'''

# subtree filter to get interface state using GET RPC
INT_RPC_REQ_FILTER = '''
<interfaces xmlns="http://cisco.com/ns/yang/Cisco-IOS-XR-pfi-im-cmd-oper">
  <interfaces>
    <interface>
      <interface-name/>
      <description/>
    </interface>
  </interfaces>
  <interface-xr>
    <interface>
      <interface-name/>
      <line-state/>
      <state/>
      <mac-address>
        <address/>
      </mac-address>
      <bandwidth/>
      <mtu/>
    </interface>
  </interface-xr>
</interfaces>'''

# subtree filter to get interface counters using GET RPC
INT_COUNTERS_RPC_REQ_FILTER = '''
<interfaces xmlns="http://cisco.com/ns/yang/Cisco-IOS-XR-pfi-im-cmd-oper">
  <interface-xr>
    <interface>
      <interface-name/>
      <interface-statistics>
        <full-interface-stats>
          <multicast-packets-sent/>
          <output-drops/>
          <bytes-sent/>
          <output-errors/>
          <bytes-received/>
          <packets-sent/>
          <input-errors/>
          <broadcast-packets-sent/>
          <multicast-packets-received/>
          <broadcast-packets-received/>
          <input-drops/>
          <packets-received/>
        </full-interface-stats>
      </interface-statistics>
    </interface>
  </interface-xr>
</interfaces>'''