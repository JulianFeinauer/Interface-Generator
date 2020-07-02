package org.pragmaticindustries.cockpit.icons;

import java.util.List;

/**
 * Delivers all available Apps.
 *
 * @author erwin.wagasow
 * created by erwin.wagasow on 14.02.2019
 */
public interface AppService {
    List<ModuleInformation> getAllApps();
}
