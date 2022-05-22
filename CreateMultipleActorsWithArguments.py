import unreal
import sys

actorsCount = int(float(sys.argv[1]))
rotationStep = int(float(sys.argv[2]))
positionOffset = float(sys.argv[3])
slowTaskDisplayText = "Spawing actors in the level..."

@unreal.uclass()
class MyEditorUtility(unreal.GlobalEditorUtilityBase):
    pass

selectedAssets = MyEditorUtility().get_selected_assets()

with unreal.ScopedSlowTask(actorsCount, slowTaskDisplayText) as ST:
    ST.make_dialog(True)
    for x in range(actorsCount):
        if ST.should_cancel():
            break
        unreal.EditorLevelLibrary.spawn_actor_from_object(selectedAssets[0], unreal.Vector(positionOffset*x,positionOffset*x,170), unreal.Rotator(0,0,rotationStep*x))
        unreal.log("Just added an actor to the level")
        ST.enter_progress_frame(1)